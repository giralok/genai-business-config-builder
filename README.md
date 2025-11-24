
# Universal Product Chatbot Config Builder

AI config builder that merges multiple business/product data JSON sources into a unified, Schema-validated `BUSINESS_JSON`, then transforms it into a System Prompt for an LLM Sales/Support chatbot ready for integration.

This project demonstrates a full GenAI configuration pipeline used to create business-specific chatbot agents capable of responding with consistent tone, correct product details, and real business rules.

---

## 🚀 Overview

This application:

1. **Ingests multiple JSON data sources from a business**  
   (landing pages, product catalog, FAQs, etc.)

2. **Unifies them into a single structured configuration**  
   → Produces a normalized, Schema-validated `BUSINESS_JSON`.

3. **Generates a System Prompt for an LLM chatbot**  
   → The chatbot becomes *business-aware*, responding using the product's benefits, rules, objections, FAQ, and brand voice.

4. **Simulates a real WhatsApp-style customer conversation**  
   → The agent returns structured JSON:
   ```json
   {
     "reply": "...",
     "stage": "...",
     "intent": "...",
     "action": "..."
   }


> **Future goal:** integrate this pipeline with WhatsApp X1 flows through Meta API or automation platforms.

---

## 🧱 Project Architecture

```
samples/
   ├── landing_page.json
   ├── product_catalog.json
   └── faq.json
schemas/
   └── infoproduct.schema.json
builder/
   ├── config_builder.py
   └── config_builder_prompt.txt
sales_agent/
   ├── sales_agent.py
   └── sales_agent_prompt.txt
utils/
   ├── llm_client.py
   └── validation.py
main_demo.py
requirements.txt
```

---

## 🧠 How It Works

### **1. Raw JSON ingestion**

Your business data (FAQ, product catalog, LP, etc.) is loaded from `/samples`.

### **2. Config Builder Agent**

Uses a dedicated prompt to:

* read raw business JSONs
* extract relevant information
* fill missing fields intelligently
* map everything into the `BUSINESS_JSON` structure

### **3. Schema Validation**

Data is validated against:

```
schemas/infoproduct.schema.json
```

Ensuring:

* required fields
* correct types
* non-empty arrays
* no extra properties
* structured objections, FAQ, benefits, voice, prices, etc.

### **4. System Prompt Generation**

The validated `BUSINESS_JSON` is injected into the LLM system prompt.

This makes the chatbot:

* product-aware
* brand-safe
* compliant
* consistent
* deterministic

### **5. Sales Agent Simulation**

The chatbot replies in structured JSON including:

```json
{
  "reply": "...",
  "stage": "...",
  "intent": "...",
  "action": "..."
}
```

This replicates a WhatsApp X1 sales flow.

---

## 🧪 Running the Demo

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Set your OpenAI API Key:

Mac/Linux:

```bash
export OPENAI_API_KEY="your_key_here"
```

Windows PowerShell:

```powershell
setx OPENAI_API_KEY "your_key_here"
```

### Run the project:

```bash
python main_demo.py
```

You will see:

* raw JSON ingestion
* BUSINESS_JSON generation
* schema validation
* chatbot X1-style interaction

---

## 🧩 Example Chatbot Output

```json
{
  "reply": "Oi! Tudo bem? O Hidraliso é indicado para pessoas que querem deixar o cabelo mais liso e alinhado. Me conta um pouco sobre o seu cabelo?",
  "stage": "Diagnóstico",
  "intent": "dúvida_geral_produto",
  "action": "perguntar"
}
```

---

## 📦 BUSINESS_JSON Schema

The configuration follows an enterprise-level schema that includes:

* product information
* benefits
* features
* target audience
* brand voice
* objections
* funnel stages
* compliance
* handoff rules

This ensures the agent is deterministic and safe.

---

## 🧭 Why This Project Matters

This repository demonstrates core competencies expected in GenAI engineering:

### ✔ Schema-guided generation

### ✔ LLM prompt engineering

### ✔ Data normalization & validation

### ✔ Multi-source business data ingestion

### ✔ Modular AI architecture

### ✔ Sales & support agent design

### ✔ Structured JSON outputs for safe automation

### ✔ Realistic funnel & objection handling

This architecture forms the basis for:

* WhatsApp Sales Bots
* Enterprise Support Agents
* AI Product Assistants
* X1 Conversion Agents
* Multi-brand conversational layers

---

## 📈 Next Steps

* Integrate with WhatsApp (Meta API)
* Add streaming responses
* Add consistency metrics for chatbot evaluation
* Create a multi-product version
* Add a UI dashboard for configuration visualization

---

## 🤝 Contributing

Pull requests are welcome!
Feel free to open issues for improvements, new features, or suggestions.

---

## 📝 License

MIT License.

Made with ❤️ specially for GenAI!


