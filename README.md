# 🚀 BCG X: Generative AI & Financial Chatbot (GFC)

**Author:** Sushant Kumar Yadav  
**Domain:** Generative AI, Financial Analytics, Python Engineering & NLP Foundation  
**Certification:** BCG X GenAI Job Simulation (Completed April 2026)  

## 📑 Executive Summary
Financial analysts spend countless hours manually extracting, comparing, and calculating metrics from dense 10-K and 10-Q financial documents. This project, developed in simulation for **Global Finance Corp (GFC)** under the **BCG X** framework, addresses this inefficiency by architecting the foundational logic for an AI-powered Financial Chatbot.

The objective was to bridge the gap between complex financial data and user-friendly accessibility. I designed an end-to-end data pipeline—from manual SEC EDGAR extraction to feature engineering in Pandas—and built an advanced rule-based Natural Language Processing (NLP) chatbot prototype. This system dynamically interprets queries, calculates financial ratios on-the-fly, and executes multi-company comparisons without relying on static, hardcoded responses.

---

## 💼 Business Scenario & Role Context
As a Junior Data Scientist within the BCG X GenAI consulting team, my mandate was split into two critical phases:
1. **Data Extraction & Initial Analysis:** Extracting key financial indicators (Revenue, Net Income, Assets, Liabilities, Operating Cash Flow) for tech giants (Apple, Microsoft, Tesla) across FY2023–FY2025.
2. **AI Chatbot Development:** Establishing the core "Rule-based logic", state management, and error handling required for the chatbot to accurately understand financial intents before handing the architecture off to specialized ML and NLP teams for neural network integration.

---

## 🛠️ Key Capabilities & Chatbot Intelligence
The `Chatbot.py` engine is powered by custom Python algorithms utilizing Regular Expressions (`re`) and Pandas to deliver real-time financial intelligence:

* **Dynamic Multi-Entity Comparison:** Capable of cross-analyzing multiple companies simultaneously (e.g., *"Compare Microsoft, Apple, and Tesla revenue 2024"*).
* **Automated Feature Engineering (YoY):** Instant calculation of absolute and percentage changes between custom fiscal periods (e.g., *"How has Tesla's net income changed from 2023 to 2025?"*).
* **On-the-Fly Ratio Calculation:** Automatically computes critical financial health metrics based on raw data, including:
  * *Net Profit Margin*
  * *Return on Assets (ROA)*
  * *Debt Ratio (Liabilities-to-Assets)*
  * *Operating Cash Flow (OCF) to Revenue Ratio*
* **Robust Error Handling:** Designed to gracefully handle missing data points, unrecognized queries, and invalid company names, ensuring a seamless UX.

---

## 📊 Project By The Numbers (FY23–FY25 Insights)
The underlying analytical engine processed hundreds of billions of dollars in market data, revealing core operational realities:
* **Microsoft (MSFT):** Demonstrated exceptional profitability, reaching **$281.7 Billion** in revenue for FY2025, alongside a category-leading **~36.1% Net Profit Margin**.
* **Apple (AAPL):** Maintained immense scale with peak revenues of **$416.2 Billion** (FY2025) and robust Operating Cash Flows exceeding **$111 Billion**.
* **Tesla (TSLA):** Showcased high top-line revenue (~$94.8B in FY2025) but highlighted capital-intensive operations, with Net Profit Margins contracting to **~4.01%** in the latest fiscal year.

---

## ⚙️ Technical Architecture & Repository Structure

### 1️⃣ Data Engineering & Enrichment Layer
* `01-GFC_10K_Financial_Data.xlsx`: Raw extraction and financial modeling summary.
* `1-financial_data.csv`: The foundational SEC 10-K dataset.
* `5-financial_analysis.ipynb`: The Jupyter Notebook engine used to ingest raw data, compute multi-year growth rates, derive complex financial ratios, and generate cross-company visual dashboards.
* `6-financial_data_enriched.csv`: The final, scrubbed, and optimized data matrix that powers the chatbot's memory state.

### 2️⃣ The Generative AI Application Layer
* `2-Chatbot.py`: The core Python application script containing the chatbot's pattern-matching logic, mathematical processing functions (`calculate_change`, `get_ratio`), and the interactive command-line loop.
* `3-README.txt`: Operational instructions and query parameters for end-users interacting with the prototype.
* `BCG_GEN_AI_CERTIFICATE.pdf`: Official certification of project completion and verification of competencies by Forage and BCG X.

---

## 🚀 Future Roadmap (Scaling to GenAI)
This rule-based prototype establishes the critical "source of truth" and functional logic. The immediate next steps for the engineering team involve:
* Integrating a Large Language Model (LLM) API (e.g., OpenAI/Gemini) to replace regex with true semantic understanding.
* Implementing Vector Databases (RAG) to allow the chatbot to read unstructured text directly from PDFs.
* Developing a React/Streamlit frontend to replace the CLI for executive stakeholders.
