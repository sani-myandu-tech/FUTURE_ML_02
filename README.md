# 🎫 TicketSense AI — Support Ticket Classification & Prioritization
### FUTURE_ML_02 | NLP + Machine Learning Internship Project

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-orange)](https://scikit-learn.org)
[![NLTK](https://img.shields.io/badge/NLTK-3.8-green)](https://nltk.org)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey)]()

> **An end-to-end NLP + ML system that reads customer support tickets, classifies them into categories, and flags priority level — automating triage that currently takes support teams 3–6 hours per day.**

---

## 📌 Business Scenario

**Company:** NovaTech SaaS — a mid-size cloud platform with 50,000 business customers  
**Problem:** NovaTech receives ~1,200 support tickets per day across 5 categories. Manual triage by a 4-person ops team adds 3–6 hours of routing delay. Urgent issues (payment failures, account lockouts, critical crashes) sit in the general queue alongside low-priority feature requests.  
**Impact:** Customer satisfaction scores dropped 18% due to slow response on urgent tickets.  
**Solution:** TicketSense AI — an ML-powered triage system that auto-classifies and prioritises every incoming ticket in under 200ms, routing it directly to the right team.

---

## 🗂️ Repository Structure

```
FUTURE_ML_02/
│
├── 📂 data/
│   ├── raw/                          # Original Kaggle dataset
│   │   └── README.md                 # Download instructions
│   └── processed/                    # Cleaned, encoded data
│
├── 📂 notebooks/
│   └── ticket_classification.ipynb   # Full analysis notebook (executed)
│
├── 📂 images/                        # All 8 generated charts
│   ├── 01_category_distribution.png
│   ├── 02_priority_distribution.png
│   ├── 03_word_frequency.png
│   ├── 04_response_time.png
│   ├── 05_confusion_matrix.png
│   ├── 06_model_comparison.png
│   ├── 07_confidence_distribution.png
│   └── 08_f1_per_category.png
│
├── 📂 models/                        # Serialised model files
│   ├── logistic_regression_model.pkl
│   ├── naive_bayes_model.pkl
│   ├── random_forest_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── label_encoder_category.pkl
│
├── 📂 reports/
│   └── business_insights.md          # Executive summary & recommendations
│
├── 📂 src/
│   └── predict.py                    # Standalone prediction script
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tools & Technologies

| Category | Tools |
|---|---|
| **Language** | Python 3.10+ |
| **NLP** | NLTK, scikit-learn TF-IDF |
| **ML Models** | scikit-learn (LogisticRegression, MultinomialNB, RandomForest) |
| **Data** | pandas, NumPy |
| **Visualisation** | Matplotlib, Seaborn |
| **Model Saving** | joblib |
| **Imbalance** | class_weight='balanced' |

---

## 🔤 NLP Pipeline

```
Raw Ticket Text
      ↓
  Lowercase
      ↓
  Remove URLs / emails
      ↓
  Remove punctuation & numbers
      ↓
  Tokenise (split on whitespace)
      ↓
  Remove stopwords (170 common English words)
      ↓
  Lemmatise (reduce to base form)
      ↓
  TF-IDF Vectorisation (5,000 features, unigrams + bigrams)
      ↓
  ML Classifier → Category + Priority
```

---

## 🤖 Models Used

| Model | Notes |
|---|---|
| **Logistic Regression** ✅ | Best performer — fast, interpretable, handles multi-class well |
| **Multinomial Naive Bayes** | Strong text baseline — very fast inference |
| **Random Forest** | Non-linear, captures complex patterns |

**Class Imbalance Handling:** `class_weight='balanced'` applied to LR and RF — automatically up-weights minority classes (Shipping & Delivery at 9%) to prevent bias.

---

## 📊 Model Performance

| Model | Accuracy | F1 (weighted) |
|---|---|---|
| **Logistic Regression ✅** | **~89%** | **0.89** |
| Multinomial Naive Bayes | ~84% | 0.84 |
| Random Forest | ~87% | 0.87 |

> **Best Model:** Logistic Regression — highest F1 score, fastest inference, best probability calibration for confidence scoring.

---

## 🔮 Priority System

| Layer | Signal | Assigned Priority |
|---|---|---|
| 1. Keyword | `urgent`, `crash`, `payment failed`, `unauthorized`… | **High** 🔴 |
| 2. Keyword | `not working`, `incorrect`, `missing`, `slow`… | **Medium** 🟡 |
| 3. Model confidence | Probability < 50% → uncertain → escalate | **High** 🔴 |
| 4. Default | No signals, confident prediction | **Low** 🟢 |

---

## 🎯 Example Predictions

| Ticket | Category | Priority |
|---|---|---|
| *"I was charged twice and need refund urgently"* | Billing & Payments | 🔴 High |
| *"My password reset link is not working"* | Account Management | 🟡 Medium |
| *"How do I upgrade my plan?"* | Product & Features | 🟢 Low |
| *"System crashed — lost all our data immediately"* | Technical Support | 🔴 High |
| *"Can you send me the API documentation?"* | Product & Features | 🟢 Low |

---

## 💼 Business Value

- **85%+ tickets** auto-classified and routed without human triage
- **High priority tickets** surfaced in <200ms vs 3–6 hour manual delay
- **Support agents** spend time resolving, not sorting
- **Customer satisfaction** improves as urgent issues reach specialists faster
- **Ops team** can monitor queue health by category and priority in real time

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/FUTURE_ML_02.git
cd FUTURE_ML_02

# 2. Install dependencies
pip install -r requirements.txt

# 3. Open the notebook
jupyter notebook notebooks/ticket_classification.ipynb

# 4. Or run a single prediction
python src/predict.py "I was charged twice and need a refund urgently"
```

---

## 📋 Requirements

```
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
seaborn>=0.12
scikit-learn>=1.3
nltk>=3.8
joblib>=1.3
imbalanced-learn>=0.11
jupyter>=1.0
```

---

## 🔭 Future Improvements

1. **BERT / DistilBERT** — transformer-based model for 94%+ accuracy
2. **Sentiment analysis** — angry tone → boost priority
3. **Multilingual support** — detect and translate non-English tickets
4. **FastAPI deployment** — REST endpoint for Zendesk/Freshdesk webhook
5. **Active learning** — agent feedback loop to retrain on uncertain predictions
6. **Real-time dashboard** — ops team view of queue health by category/priority

---

## 👤 Author

**[Lungisani Mnyandu]**  


---
TicketSense AI | Internship Portfolio Project | 2025*

