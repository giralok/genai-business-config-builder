"""
config_builder.py
Responsável por:
1. Carregar JSONs brutos (LP, produto, FAQ)
2. Enviar tudo para o Config Builder LLM
3. Receber o BUSINESS_JSON (canônico)
"""

import json
from utils.llm_client import LLMClient

class ConfigBuilder:
    def __init__(self, llm: LLMClient, system_prompt_path: str):
        self.llm = llm

        with open(system_prompt_path, "r", encoding="utf-8") as f:
            self.system_prompt = f.read()

    def load_raw_jsons(self, folder_path: str) -> list[dict]:
        """
        Carrega todos os JSONs da pasta samples/.
        """
        import os
        data = []
        for file in os.listdir(folder_path):
            if file.endswith(".json"):
                with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                    data.append(json.load(f))
        return data

    def build(self, raw_jsons: list[dict]) -> dict:
        """
        Usa a LLM para gerar o BUSINESS_JSON.
        """
        user_prompt = (
            "Aqui estão os JSONs brutos da empresa:\n\n"
            + "\n\n".join(json.dumps(j, indent=2, ensure_ascii=False) for j in raw_jsons)
            + "\n\nGere o BUSINESS_JSON seguindo exatamente o formato canônico."
        )

        response_text = self.llm.generate(
            system_prompt=self.system_prompt,
            user_prompt=user_prompt
        )

        # Tentar converter resposta em JSON
        try:
            return json.loads(response_text)
        except:
            raise ValueError("A LLM devolveu algo que não é JSON válido.")
