"""
main_demo.py
Demonstração completa:
- Carrega JSONs brutos
- Gera BUSINESS_JSON (com retries)
- Normaliza o JSON baseado no schema
- Valida usando schema rígido
- Injeta no Sales Agent
- Simula conversa
"""

import json
from builder.config_builder import ConfigBuilder
from sales_agent.sales_agent import SalesAgent
from utils.llm_client import LLMClient
from utils.validation import validate_business_json, normalize_business_json

MAX_RETRIES = 3

def main():

    # ------------------------------------
    # 1. Instanciar LLM
    # ------------------------------------
    llm = LLMClient(provider="openai", model="gpt-4o-mini")

    # ------------------------------------
    # 2. Criar Config Builder
    # ------------------------------------
    config_builder = ConfigBuilder(
        llm=llm,
        system_prompt_path="builder/config_builder_prompt.txt"
    )

    # ------------------------------------
    # 3. Carregar JSONs brutos
    # ------------------------------------
    raw_jsons = config_builder.load_raw_jsons("samples")

    # ------------------------------------
    # 4. Carregar schema (apenas 1 vez)
    # ------------------------------------
    with open("schemas/infoproduct.schema.json", "r", encoding="utf-8") as f:
        schema = json.load(f)

    # ------------------------------------
    # 5. Retry loop: gerar BUSINESS_JSON válido + normalização
    # ------------------------------------
    business_json = None

    for attempt in range(1, MAX_RETRIES + 1):
        print(f"Tentando gerar BUSINESS_JSON (tentativa {attempt})...")

        # 5.1 – Gerar o JSON bruto usando LLM
        try:
            candidate_json = config_builder.build(raw_jsons)
        except Exception as e:
            print("Erro ao gerar JSON:", e)
            continue

        # 5.2 – Normalizar automaticamente baseado no schema
        try:
            candidate_json = normalize_business_json(candidate_json, schema)
        except Exception as e:
            print("Erro ao normalizar JSON:", e)
            continue

        # 5.3 – Validar JSON normalizado
        valid, err = validate_business_json(candidate_json, "schemas/infoproduct.schema.json")

        if valid:
            print("JSON validado com sucesso!")
            business_json = candidate_json
            break
        else:
            print("JSON inválido:", err)

    # Se mesmo após retries não validou → HUMAN-IN-THE-LOOP
    if not business_json:
        print("Falha após 3 tentativas. Use HUMAN-IN-THE-LOOP.")
        return

    # ------------------------------------
    # 6. Criar Sales Agent
    # ------------------------------------
    sales_agent = SalesAgent(
        llm=llm,
        system_prompt_template_path="sales_agent/sales_agent_prompt.txt"
    )

    # ------------------------------------
    # 7. Simular conversa
    # ------------------------------------
    print("\nSimulação de conversa:")
    user_messages = [
        "Oi, tudo bem?  Esse produto serve pra mim?",
        "Quanto custa?",
        "Poxa, tá caro...",
        "Tem alguma garantia?",
        "Como faço pra comprar?",
        "Por que o preço é tão alto assim?",
        "Quais formas de pagamento vocês aceitam?",
        "Se eu não gostar, você me devolve o dobro do dinheiro?"
    ]

    for msg in user_messages:
        print(f"\nUsuário: {msg}")
        response = sales_agent.run_turn(business_json, msg)
        print("Agente:", json.dumps(response, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
