# visualize_results.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load matched transactions data
matches_df = pd.read_csv('matched_transactions.csv', parse_dates=['bank_date'])

# Create a scatter plot to visualize the fuzzy matching scores
plt.figure(figsize=(14, 6))
sns.scatterplot(data=matches_df, x='bank_date', y='fuzzy_score', hue='fuzzy_score', palette='viridis', size='fuzzy_score', sizes=(20, 200), alpha=0.7, legend=False)
plt.title('Fuzzy Matching Scores over Time')
plt.xlabel('Bank Transaction Date')
plt.ylabel('Fuzzy Matching Score')
plt.axhline(80, color='red', linestyle='--', label='Matching Threshold (80)')  # Add a threshold line
plt.legend()
plt.grid(True)
plt.show()

# Bar plot showing the number of matched vs unmatched transactions
matches_df['match_status'] = matches_df['sap_id'].apply(lambda x: 'Matched' if pd.notnull(x) else 'Unmatched')
plt.figure(figsize=(8, 6))
sns.countplot(data=matches_df, x='match_status', palette='pastel')
plt.title('Number of Matched vs Unmatched Transactions')
plt.xlabel('Match Status')
plt.ylabel('Count')
plt.show()
