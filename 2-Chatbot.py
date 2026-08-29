"""
GFC AI Financial Chatbot — Advanced Rule‑Based Prototype
Supports: latest values, YoY changes, custom year ranges, ratios, multi‑company comparison
Data source: financial_data.csv
"""

import pandas as pd
import re

# --------------------- Load Data ---------------------
try:
    df = pd.read_csv('financial_data.csv')
    df['Year'] = df['Year'].astype(int)
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: financial_data.csv not found.")
    exit()

# Column mapping (user phrase → CSV column)
COLUMN_MAP = {
    'revenue': 'Total_Revenue_B',
    'net income': 'Net_Income_B',
    'profit': 'Net_Income_B',
    'assets': 'Total_Assets_B',
    'total assets': 'Total_Assets_B',
    'liabilities': 'Total_Liabilities_B',
    'total liabilities': 'Total_Liabilities_B',
    'operating cash flow': 'Operating_CF_B',
    'cash flow': 'Operating_CF_B',
    'ocf': 'Operating_CF_B'
}

# Ratio keywords
RATIO_KEYWORDS = [
    'net profit margin', 'profit margin',
    'debt ratio', 'debt to assets',
    'roa', 'return on assets',
    'ocf to revenue', 'operating cash flow to revenue'
]

# --------------------- Helper Functions ---------------------
def get_value(company, year, column):
    """Get value for a specific company, year, and column."""
    row = df[(df['Company'].str.lower() == company.lower()) & (df['Year'] == year)]
    if row.empty:
        return None
    return row.iloc[0][column]

def get_latest_value(company, column):
    """Get the most recent year's value for a column."""
    company_data = df[df['Company'].str.lower() == company.lower()]
    if company_data.empty:
        return None
    latest_year = company_data['Year'].max()
    return get_value(company, latest_year, column)

def calculate_change(company, column, start_year=None, end_year=None):
    """
    Calculate absolute and percentage change.
    If years are not given, uses the two most recent years.
    """
    company_data = df[df['Company'].str.lower() == company.lower()].sort_values('Year')
    if len(company_data) < 2:
        return None, None, None, None, None

    if start_year is None or end_year is None:
        end_row = company_data.iloc[-1]
        start_row = company_data.iloc[-2]
        end_year = int(end_row['Year'])
        start_year = int(start_row['Year'])
    else:
        end_row = company_data[company_data['Year'] == end_year]
        start_row = company_data[company_data['Year'] == start_year]
        if end_row.empty or start_row.empty:
            return None, None, None, None, None
        end_row = end_row.iloc[0]
        start_row = start_row.iloc[0]

    end_val = end_row[column]
    start_val = start_row[column]
    change = end_val - start_val
    pct = (change / start_val) * 100 if start_val != 0 else 0
    return end_val, change, pct, start_year, end_year

def get_ratio(company, ratio_name, year=None):
    """Calculate a financial ratio for a given company and year (default latest)."""
    if year is None:
        rev = get_latest_value(company, 'Total_Revenue_B')
        ni = get_latest_value(company, 'Net_Income_B')
        assets = get_latest_value(company, 'Total_Assets_B')
        liab = get_latest_value(company, 'Total_Liabilities_B')
        ocf = get_latest_value(company, 'Operating_CF_B')
    else:
        rev = get_value(company, year, 'Total_Revenue_B')
        ni = get_value(company, year, 'Net_Income_B')
        assets = get_value(company, year, 'Total_Assets_B')
        liab = get_value(company, year, 'Total_Liabilities_B')
        ocf = get_value(company, year, 'Operating_CF_B')

    if None in [rev, ni, assets, liab, ocf]:
        return None

    ratio_name = ratio_name.lower()
    if ratio_name in ['net profit margin', 'profit margin']:
        return (ni / rev) * 100
    elif ratio_name in ['debt ratio', 'debt to assets']:
        return liab / assets
    elif ratio_name in ['roa', 'return on assets']:
        return (ni / assets) * 100
    elif ratio_name in ['ocf to revenue', 'operating cash flow to revenue']:
        return (ocf / rev) * 100
    else:
        return None

def extract_company_and_metric(query):
    """Extract company name and metric keyword from user query."""
    query_lower = query.lower()
    company = None
    for comp in ['microsoft', 'apple', 'tesla']:
        if comp in query_lower:
            company = comp.capitalize()
            break

    metric_col = None
    metric_name = None
    for word, col in COLUMN_MAP.items():
        if word in query_lower:
            metric_col = col
            metric_name = word
            break

    ratio_keyword = None
    if metric_col is None:
        for rkw in RATIO_KEYWORDS:
            if rkw in query_lower:
                ratio_keyword = rkw
                break

    return company, metric_col, metric_name, ratio_keyword

def extract_years(query):
    """Extract four-digit years from query. Returns (start_year, end_year) or (None, None)."""
    years = re.findall(r'\b(20\d{2})\b', query)
    years = [int(y) for y in years]
    if len(years) >= 2:
        return min(years), max(years)
    elif len(years) == 1:
        return years[0], years[0]
    return None, None

# --------------------- Core Chatbot Logic ---------------------
def process_query(user_input):
    query = user_input.strip()
    query_lower = query.lower()

    # Help
    if query_lower in ["help", "what can you do", "commands"]:
        return (
            "I can answer financial questions for Microsoft, Apple, and Tesla:\n"
            "• Latest values: 'What is Apple's revenue?'\n"
            "• YoY change: 'How has Tesla's net income changed?'\n"
            "• Custom year range: 'Microsoft revenue change from 2022 to 2024'\n"
            "• Ratios: 'What is Microsoft's net profit margin?' / 'Tesla debt ratio'\n"
            "• Specific year: 'Apple 2023 assets'\n"
            "• Compare: 'Compare Microsoft and Apple net income'\n"
            "Type 'quit' to exit."
        )

    # Multi-company comparison
    if "compare" in query_lower or "versus" in query_lower or " vs " in query_lower:
        companies_in_query = []
        for comp in ['Microsoft', 'Apple', 'Tesla']:
            if comp.lower() in query_lower:
                companies_in_query.append(comp)
        if len(companies_in_query) < 2:
            return "Please specify at least two companies to compare. Example: 'Compare Apple and Microsoft revenue'"

        metric_col = None
        metric_label = None
        for word, col in COLUMN_MAP.items():
            if word in query_lower:
                metric_col = col
                metric_label = word
                break
        if metric_col is None:
            for rkw in RATIO_KEYWORDS:
                if rkw in query_lower:
                    metric_label = rkw
                    break
            if metric_label is None:
                return "Please specify what to compare (e.g., revenue, net income, debt ratio)."

        year, _ = extract_years(query)
        responses = []
        for comp in companies_in_query:
            if metric_label in RATIO_KEYWORDS:
                val = get_ratio(comp, metric_label, year)
                if val is not None:
                    if 'margin' in metric_label or 'roa' in metric_label or 'ocf' in metric_label:
                        responses.append(f"{comp}: {val:.2f}%")
                    else:
                        responses.append(f"{comp}: {val:.3f}")
            else:
                if year:
                    val = get_value(comp, year, metric_col)
                else:
                    val = get_latest_value(comp, metric_col)
                if val is not None:
                    responses.append(f"{comp}: ${val:.2f}B")
        if not responses:
            return "Could not retrieve comparison data."
        year_str = f" ({year})" if year else " (latest)"
        return f"{metric_label.title()}{year_str}:\n" + "\n".join(responses)

    # Single metric query
    company, metric_col, metric_name, ratio_keyword = extract_company_and_metric(query)
    if company is None:
        return "Please specify a company: Microsoft, Apple, or Tesla."

    start_year, end_year = extract_years(query)

    # Handle ratios
    if ratio_keyword:
        year = start_year if start_year else None
        val = get_ratio(company, ratio_keyword, year)
        if val is None:
            return f"Sorry, I couldn't calculate {ratio_keyword} for {company}."
        if 'margin' in ratio_keyword or ratio_keyword in ['roa', 'return on assets', 'ocf to revenue']:
            return f"{company}'s {ratio_keyword} {f'in {year}' if year else 'latest'} is {val:.2f}%."
        else:
            return f"{company}'s {ratio_keyword} {f'in {year}' if year else 'latest'} is {val:.3f}."

    # Handle regular metrics
    if metric_col is None:
        return "I couldn't identify the financial metric. Try revenue, net income, assets, etc."

    # Change query?
    if any(w in query_lower for w in ["change", "increased", "decreased", "growth", "grew", "from"]):
        if start_year and end_year and start_year != end_year:
            end_val, change, pct, sy, ey = calculate_change(company, metric_col, start_year, end_year)
        else:
            end_val, change, pct, sy, ey = calculate_change(company, metric_col)

        if end_val is None:
            return f"Sorry, I need at least two years of data to calculate change for {company}."
        direction = "increased" if change >= 0 else "decreased"
        return (f"{company}'s {metric_name} {direction} by ${abs(change):.2f} billion "
                f"({pct:.1f}%) from FY{sy} to FY{ey}.")

    # Specific year query
    if start_year:
        val = get_value(company, start_year, metric_col)
        if val is None:
            return f"Sorry, I don't have {metric_name} data for {company} in {start_year}."
        return f"{company}'s {metric_name} in FY{start_year} was ${val:.2f} billion."

    # Default: latest value
    val = get_latest_value(company, metric_col)
    if val is None:
        return f"Sorry, I couldn't find {metric_name} data for {company}."
    return f"{company}'s latest {metric_name} is ${val:.2f} billion."

# --------------------- Main Loop ---------------------
print("\n" + "="*60)
print("GFC Advanced Financial Chatbot (type 'quit' to exit)")
print("="*60)
print("Type 'help' to see what I can do.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit', 'q']:
        print("Chatbot: Goodbye!")
        break
    response = process_query(user_input)
    print(f"Chatbot: {response}\n")
