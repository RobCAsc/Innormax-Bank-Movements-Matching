# create_dummy_data.py

import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker for generating dummy data
fake = Faker()

# Parameters
num_records = 100  # Number of records for each dataset
date_variability = 3  # Number of days the dates can differ
amount_variability = 0.05  # Allow up to 5% variation in amounts

### Function to introduce typos and abbreviations ###
def modify_description(description):
    words = description.split()
    if len(words) > 1:
        # Introduce typos in 50% of cases
        if random.random() > 0.5:
            typo_index = random.randint(0, len(words) - 1)
            words[typo_index] = words[typo_index][:-1] + random.choice('abcdefghijklmnopqrstuvwxyz')
        
        # Abbreviate a random word in 50% of cases
        if random.random() > 0.5:
            abbr_index = random.randint(0, len(words) - 1)
            words[abbr_index] = words[abbr_index][:3].upper() + '.'
    
    return ' '.join(words)

### STEP 1: Create Dummy Datasets ###

# Generate dummy bank statement data
bank_data = {
    'date': pd.to_datetime([fake.date_this_year() for _ in range(num_records)]),
    'amount': np.round(np.random.uniform(50, 5000, num_records), 2),  # Random amounts between 50 and 5000
    'description': [fake.bs() for _ in range(num_records)],  # Random business descriptions
    'transaction_type': np.random.choice(['debit', 'credit'], num_records)  # Random transaction type
}

bank_df = pd.DataFrame(bank_data)

# Generate dummy SAP records data based on bank data with controlled variability
sap_data = {
    'SAP_id': [fake.uuid4() for _ in range(num_records)],  # Unique IDs
    # Alter dates slightly within a range to simulate small differences
    'date': bank_df['date'] + pd.to_timedelta(np.random.randint(-date_variability, date_variability + 1, num_records), unit='D'),
    # Introduce a slight variation in amounts, but mostly similar
    'amount': bank_df['amount'] * (1 + np.random.uniform(-amount_variability, amount_variability, num_records)),
    # Descriptions will be made similar but with variations
    'description': [desc if random.random() > 0.2 else modify_description(desc) for desc in bank_df['description']],
    'cost_center': np.random.randint(1000, 9999, num_records)  # Random cost center IDs
}

sap_df = pd.DataFrame(sap_data)

### Introduce unmatched cases ###

# Add extra SAP records with no corresponding bank entries
extra_sap_records = pd.DataFrame({
    'SAP_id': [fake.uuid4() for _ in range(5)],
    'date': pd.to_datetime([fake.date_this_year() for _ in range(5)]),
    'amount': np.round(np.random.uniform(50, 5000, 5), 2),
    'description': [fake.catch_phrase() for _ in range(5)],
    'cost_center': np.random.randint(1000, 9999, 5)
})
sap_df = pd.concat([sap_df, extra_sap_records], ignore_index=True)

# Add extra bank entries with no corresponding SAP records
extra_bank_records = pd.DataFrame({
    'date': pd.to_datetime([fake.date_this_year() for _ in range(5)]),
    'amount': np.round(np.random.uniform(50, 5000, 5), 2),
    'description': [fake.bs() for _ in range(5)],
    'transaction_type': np.random.choice(['debit', 'credit'], 5)
})
bank_df = pd.concat([bank_df, extra_bank_records], ignore_index=True)

### STEP 2: Save Dummy Data to CSV ###

bank_df.to_csv('dummy_bank_statement.csv', index=False)
sap_df.to_csv('dummy_sap_records.csv', index=False)

print("Dummy data created successfully with unmatched cases and description variations:")
print("\nBank Statement Data (First 5 Rows):\n", bank_df.head())
print("\nSAP Records Data (First 5 Rows):\n", sap_df.head())
