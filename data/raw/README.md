# 📂 data/raw — Dataset Instructions

## Dataset: Customer Support Ticket Dataset

This project uses the **Customer Support Ticket Dataset** from Kaggle — one of the most realistic publicly available support ticket datasets for NLP classification projects.

---

## How to Download

### Option A: Kaggle Website
1. Create a free account at [kaggle.com](https://www.kaggle.com)
2. Visit: [https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset](https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset)
3. Click **Download** → extract the ZIP
4. Place `customer_support_tickets.csv` in this folder (`data/raw/`)

### Option B: Kaggle CLI
```bash
pip install kaggle
kaggle datasets download -d suraj520/customer-support-ticket-dataset
unzip customer-support-ticket-dataset.zip -d data/raw/
```

---

## Dataset Details

| Property | Value |
|---|---|
| **Rows** | 8,469 support tickets |
| **Key Columns** | ticket_id, customer_name, product_purchased, ticket_type, ticket_subject, ticket_description, ticket_priority, ticket_status |
| **Categories** | Billing, Technical, Account, Returns, Product |
| **Priority Labels** | Critical, High, Medium, Low |
| **Format** | CSV (UTF-8) |
| **License** | CC0 Public Domain |

---

## How to Use the Real File

Replace the `generate_ticket_dataset()` call in **Section B** of the notebook with:

```python
df_raw = pd.read_csv('../data/raw/customer_support_tickets.csv')

# Use the text description column as ticket_text
df_raw['ticket_text'] = df_raw['ticket_description'].fillna('') + ' ' + df_raw['ticket_subject'].fillna('')

# Map priority labels to match this project's format
priority_map = {'Critical': 'High', 'High': 'High', 'Medium': 'Medium', 'Low': 'Low'}
df_raw['priority'] = df_raw['ticket_priority'].map(priority_map)

# Use ticket_type as category
df_raw['category'] = df_raw['ticket_type']

# Select relevant columns
df_raw = df_raw[['ticket_text', 'category', 'priority']].dropna()
```

---

## Why This Dataset?

- **Real ticket language** — actual customer-written text, not synthetic
- **Multiple categories** — broad enough to test multi-class classification properly  
- **Priority labels included** — no need to derive ground truth
- **Publicly available** — reproducible for reviewers and recruiters
- **Industry representative** — mirrors the structure of Zendesk/Freshdesk ticket exports
