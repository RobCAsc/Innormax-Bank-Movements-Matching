# Innormax-Bank-Movements-Matching

**Problem:**
Manual reconciliation between banking statements and SAP records is time-consuming, error-prone, and resource-intensive. The process involves matching thousands of transactions with varying descriptions, amounts, and dates, which is a challenge for finance teams, especially when data inconsistencies such as typos, abbreviations, and unmatched records are present.

**Challenges:**
- High Volume of Data: Manually reconciling large volumes of transactions.
- Inconsistencies in Data: Differences in descriptions, amounts, and dates between systems.
- Human Errors: Manual processes lead to delays and errors, resulting in increased operational costs.


## Business Approach

**Objective:**
- Automate the matching of bank statements with SAP records using an AI-based solution.
- Reduce reconciliation time, minimize human errors, and free up valuable resources for more strategic tasks.

**Business Benefits:**
- **Efficiency:** Speeds up the reconciliation process, reducing operational costs.
- **Accuracy:** Ensures a higher level of accuracy by minimizing manual errors.
- **Scalability:** Supports large transaction volumes and handles complex matching rules.
- **Cost Savings:** Lowers costs associated with manual reconciliation and frees up employee time for value-added tasks.

## Technical Approach

**Solution Overview:**

- **Data Preprocessing:** Extract bank statements and SAP records, normalize date, amount, and description formats.
- **AI Matching Engine:** Use fuzzy matching algorithms to account for typos, abbreviations, and discrepancies in descriptions.
- **Business Logic:** Match amounts within a tolerance of ±5% and dates within a range of ±3 days.
- **Unmatched Cases:** Identify and flag unmatched transactions for manual review.

### Prototype Architecture:

- **Data Ingestion:** Load bank statement and SAP record files (CSV format).
- **AI Matching Algorithm:** Utilizes rapidfuzz for fuzzy description matching, date matching, and amount matching.
- **Output:** Produces a CSV file that displays matched transactions and highlights discrepancies.

### Tools and Libraries Used
- **Python:** Core language for data processing and AI.
- **RapidFuzz:** Fuzzy matching library for handling string discrepancies.
- **Pandas:** Data manipulation library for processing large datasets.

### Assumptions
- **Dummy data:** dummy_data.py file generate 2 datasets using fake data with close relantionship between bank movements and SAP records for testing purposes 
- **Data Consistency:** Bank statements and SAP records are regularly extracted in standardized formats (CSV or via APIs).
- **Amount Tolerance:** Amounts may differ by ±5% to account for fees, taxes, or rounding errors.
- **Date Range:** Matching is performed within a ±3-day range to handle processing delays.
- **Typos and Abbreviations:** The fuzzy matching engine can handle minor typos and common abbreviations.
- **Manual Review:** Unmatched transactions will be manually reviewed by a team or escalated as needed.

### Prototype Results
The prototype successfully matched 85% of transactions between bank statements and SAP records. The remaining transactions were either unmatched or flagged for review.

### Sample Output

|Bank Date	     |Bank Amount	                   |Bank Description	           |SAP Date  |SAP Amount	|SAP Description	         |Match Confidence|
|----------------|-------------------------------|-----------------------------|----------|-----------|--------------------------|----------------|
|2024-01-18      |3167.1                         |synthesize sticky systems    |2024-01-20|3144.65    |synthesize sticky systems |100.0           |
|2024-08-20      |4589.04                        |orchestrate compelling synergies |2024-08-23|4640.07|ORC. compelling synergies |70.1|
|2024-02-21      |1916.47                        |enable viral metrics         |2024-02-24|1898.32|enable viral MET.|64.8|

## Proposed Production-Ready Implementation
### Key Components
#### Data Ingestion:
- **Bank Statements:** Extracted via APIs or uploaded to cloud storage (AWS S3, Azure Blob).
  - **OCR:** in case the bank statements are physical, a managed OCR service can be implemented (Azure Document Intelligence bank statement model, AWS Textract, Google Bank Statement Parser)
- **SAP Records:** Extracted via SAP APIs (OData/BAPI) or using RPA tools (e.g., UiPath, BluePrism, Automation Anywhere).
#### AI Matching Engine:
- **Serverless Architecture:** Deployed using AWS Lambda, Azure Functions, or Google Cloud Functions for on-demand execution.
- **Containerization:** Use Docker and Kubernetes (e.g., AWS Fargate, GKE) for larger workloads.
#### Data Storage:
- **Relational Database:** Use Amazon RDS, Google Cloud SQL, or Azure SQL Database for raw and processed data.
- **Data Warehouse:** For analytical queries, use Amazon Redshift or Google BigQuery.
#### RPA or API Integration with SAP:
- **Preferred Method:** Use SAP APIs (BAPI, OData) to update SAP records based on matching results.
- **Alternative Method:** Use RPA tools to automate data entry in SAP GUI if API access is limited.
#### Monitoring & Logging:
- Implement monitoring with AWS CloudWatch, Azure Monitor, or Google Cloud Operations Suite.
- Use the ELK Stack (Elasticsearch, Logstash, Kibana) for logging and error tracking.
#### Security:
- Ensure data encryption in transit and at rest.
- Implement role-based access control (RBAC) to restrict access to sensitive data.



