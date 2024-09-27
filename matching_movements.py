# matching_process.py

import pandas as pd
from rapidfuzz import process, fuzz

# Load the dummy data
bank_df = pd.read_csv('dummy_bank_statement.csv', parse_dates=['date'])
sap_df = pd.read_csv('dummy_sap_records.csv', parse_dates=['date'])

# Rename columns for clarity
bank_df.rename(columns={'date': 'bank_date', 'amount': 'bank_amount', 'description': 'bank_description'}, inplace=True)
sap_df.rename(columns={'date': 'sap_date', 'amount': 'sap_amount', 'description': 'sap_description'}, inplace=True)

# Initialize a list to store matched results
matches = []

# Iterate through each bank transaction
for bank_index, bank_row in bank_df.iterrows():
    # Find the best match in SAP records using rapidfuzz based on description
    matched_sap_row, score, _ = process.extractOne(
        bank_row['bank_description'],
        sap_df['sap_description'],
        scorer=fuzz.token_sort_ratio
    )

    # Get the matched SAP row details
    sap_match = sap_df[sap_df['sap_description'] == matched_sap_row].iloc[0]
    
    # Check if the match is within a reasonable range of amount and date
    amount_match = abs(bank_row['bank_amount'] - sap_match['sap_amount']) <= bank_row['bank_amount'] * 0.05
    date_match = abs((bank_row['bank_date'] - sap_match['sap_date']).days) <= 3

    if amount_match and date_match:
        matches.append({
            'bank_date': bank_row['bank_date'],
            'bank_amount': bank_row['bank_amount'],
            'bank_description': bank_row['bank_description'],
            'sap_date': sap_match['sap_date'],
            'sap_amount': sap_match['sap_amount'],
            'sap_description': sap_match['sap_description'],
            'fuzzy_score': score
        })

# Create a DataFrame from the matched results
matched_df = pd.DataFrame(matches)

# Save the matched results to a CSV file
matched_df.to_csv('matched_transactions.csv', index=False)

print("Matching process completed using RapidFuzz. Results have been saved to 'matched_transactions.csv'.")
print("\nSample of matched results:\n", matched_df.head())
