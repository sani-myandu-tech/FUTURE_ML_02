"""
predict.py — TicketSense AI Standalone Prediction Script
FUTURE_ML_02 | NovaTech SaaS Support Triage System

Usage:
    python predict.py "I was charged twice and need a refund urgently"
    python predict.py  (interactive mode)
"""

import sys, re, string, joblib
import numpy as np

# ── Load saved models ──────────────────────────────────────────────────────
MODEL_DIR = '../models/'
try:
    lr      = joblib.load(MODEL_DIR + 'logistic_regression_model.pkl')
    tfidf   = joblib.load(MODEL_DIR + 'tfidf_vectorizer.pkl')
    le_cat  = joblib.load(MODEL_DIR + 'label_encoder_category.pkl')
except FileNotFoundError:
    print("❌ Model files not found. Run the notebook first to generate them.")
    sys.exit(1)

# ── Stopwords (no NLTK required) ──────────────────────────────────────────
STOPWORDS = set(['i','me','my','we','our','you','your','he','him','his','she',
'her','it','its','they','them','their','this','that','these','those','am','is',
'are','was','were','be','been','being','have','has','had','do','does','did','a',
'an','the','and','but','if','or','as','of','at','by','for','with','about','to',
'from','in','out','on','off','then','when','where','how','all','both','each',
'no','not','only','so','than','too','very','can','will','just','should','now',
'please','need','want','would','could','d','s','t'])

HIGH_KW = ['urgent','immediately','asap','critical','crash','crashed',
           'charged twice','double charge','unauthorized','suspended',
           'cannot access','payment failed','data loss','money deducted']
MED_KW  = ['not working','issue','problem','incorrect','slow','broken',
           'missing','wrong item','not received','stopped','failed']

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'http\S+|\S+@\S+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    tokens = [t for t in text.split() if t not in STOPWORDS and len(t) > 2]
    return ' '.join(tokens)

def predict_priority(ticket_text: str) -> tuple:
    t = ticket_text.lower()
    if any(kw in t for kw in HIGH_KW):
        return 'High', 'Urgent keyword detected'
    if any(kw in t for kw in MED_KW):
        return 'Medium', 'Issue keyword detected'
    cleaned = clean_text(ticket_text)
    vec = tfidf.transform([cleaned])
    conf = lr.predict_proba(vec).max()
    if conf < 0.50:
        return 'High', f'Low model confidence ({conf:.0%}) — escalate for review'
    return 'Low', f'No urgent signals ({conf:.0%} confidence)'

def predict_ticket(ticket_text: str) -> dict:
    cleaned    = clean_text(ticket_text)
    vec        = tfidf.transform([cleaned])
    cat_idx    = lr.predict(vec)[0]
    cat_proba  = lr.predict_proba(vec)[0]
    category   = le_cat.inverse_transform([cat_idx])[0]
    confidence = cat_proba.max()
    priority, note = predict_priority(ticket_text)
    return {
        'category':   category,
        'confidence': f'{confidence:.1%}',
        'priority':   priority,
        'note':       note
    }

def print_result(ticket: str, result: dict):
    icon = '🔴' if result['priority']=='High' else '🟡' if result['priority']=='Medium' else '🟢'
    print(f"\n{'─'*60}")
    print(f"  Ticket    : {ticket[:57]}")
    print(f"  Category  : {result['category']}")
    print(f"  Confidence: {result['confidence']}")
    print(f"  {icon} Priority : {result['priority']}")
    print(f"  Note      : {result['note']}")
    print(f"{'─'*60}")

if __name__ == '__main__':
    print("\n🎫 TicketSense AI — Prediction System")
    print("   NovaTech SaaS | FUTURE_ML_02\n")

    if len(sys.argv) > 1:
        # Command-line mode
        ticket = ' '.join(sys.argv[1:])
        result = predict_ticket(ticket)
        print_result(ticket, result)
    else:
        # Interactive mode
        print("Interactive mode — type a ticket or 'quit' to exit.\n")
        while True:
            ticket = input("  Enter ticket: ").strip()
            if ticket.lower() in ('quit', 'exit', 'q'):
                print("\n  Goodbye! 👋\n"); break
            if not ticket:
                continue
            result = predict_ticket(ticket)
            print_result(ticket, result)
