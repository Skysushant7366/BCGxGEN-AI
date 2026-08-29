GFC AI Financial Chatbot – Advanced Rule‑Based Prototype
==========================================================

How it works:
This chatbot uses rule‑based logic to answer a wide range of financial questions
about Microsoft, Apple, and Tesla. It loads real data from 'financial_data.csv'
and calculates responses on the fly—no hardcoded numbers.

Supported Query Types (with examples):
--------------------------------------
1. Latest values:
   • "What is Microsoft's revenue?"
   • "Apple net income"
   • "Tesla total assets"

2. Year‑over‑year changes:
   • "How has Tesla's net income changed?"
   • "Has Microsoft's revenue increased?"

3. Custom year ranges:
   • "Microsoft revenue change from 2022 to 2024"
   • "Apple net income 2022 to 2023"

4. Specific year lookups:
   • "Microsoft 2023 assets"
   • "What was Apple's revenue in 2022?"

5. Financial ratios:
   • "What is Microsoft's net profit margin?"
   • "Tesla debt ratio"
   • "Apple ROA"
   • "Microsoft operating cash flow to revenue"

6. Multi‑company comparison:
   • "Compare Apple and Microsoft net income"
   • "Compare Microsoft, Apple, and Tesla revenue 2023"

7. Help:
   • "help" or "what can you do"

Metrics understood:
--------------------
Revenue, Net Income, Total Assets, Total Liabilities, Operating Cash Flow,
Net Profit Margin, Debt Ratio, ROA, OCF/Revenue.

Limitations:
------------
- Only works for Microsoft, Apple, and Tesla.
- Requires exact or near‑exact phrasing for metric keywords.
- No true natural language understanding—relies on keyword matching.
- Data must be available in 'financial_data.csv' for the requested years.

How to Run:
-----------
1. Install Python 3 and pandas (pip install pandas).
2. Place 'financial_data.csv' in the same folder as 'chatbot.py'.
3. Run: python chatbot.py
4. Type your question and press Enter. Type 'quit' to exit.

Note: This prototype demonstrates rule‑based logic, dynamic data retrieval,
and financial analysis integration—ready for further AI model enhancement.
