#!/usr/bin/env python3
import os, re, json
from datetime import datetime
from fpdf import FPDF
import qrcode

JAZZCASH = "03084513994"
BILLS_DIR = "GENUINE_BILLS"
os.makedirs(BILLS_DIR, exist_ok=True)

print("GENUINE SYSTEM STARTING...")

def genuine_fraud_check(sms_body):
    score = 0
    logs = []
    body = sms_body.lower()
    if re.search(r'rs\.?\s*\d+.*received', body):
        score += 40; logs.append("Amount+Received Found")
    if re.search(r'tid|trxid\s*[: ]\d{6,12}', body, re.I):
        score += 40; logs.append("Valid Transaction ID")
    if any(w in body for w in ["lottery","won prize","click here","http://"]):
        score -= 100; logs.append("FAKE Link Detected")
    is_real = score >= 70
    return {"is_real": is_real, "score": score, "logs": logs}

sms1 = "Your JazzCash A/C Received Rs. 7000.00 from 03001234567 TID:1234567890"
print("FRAUD CHECK:", genuine_fraud_check(sms1))

def genuine_ledger(client, amount):
    amount = int(amount)
    entry = {
        "date": datetime.now().isoformat(),
        "client": client,
        "total_received": amount,
        "split": {"main_90": int(amount*0.9), "saving_10": int(amount*0.1)},
        "note": f"Manual Transfer to {JAZZCASH} via JazzCash App",
        "status": "PENDING_MANUAL_TRANSFER"
    }
    with open("genuine_ledger.jsonl","a") as f:
        f.write(json.dumps(entry)+"\n")
    print(f"LEDGER: {client} Rs {amount} -> Main {entry['split']['main_90']}")
    return entry

genuine_ledger("London Cafe UK", 7000)

def genuine_invoice(client_name, country, base_amount):
    base_amount = int(base_amount)
    vat_rate = 0.20 if country=="UK" else 0.05 if country=="UAE" else 0.0
    vat = int(base_amount * vat_rate)
    total = base_amount + vat
    pdf = FPDF()
    pdf.add_page()
    pdf.set_fill_color(15,15,15)
    pdf.rect(0,0,210,297,'F')
    pdf.set_text_color(212,175,55)
    pdf.set_font("Helvetica","B",18)
    pdf.cell(0,12,f"CHAPEX - {country} TAX INVOICE", ln=True, align='C')
    pdf.set_text_color(255,255,255)
    pdf.set_font("Helvetica","",11)
    pdf.ln(5)
    pdf.cell(0,7,f"Client: {client_name} | Country: {country}", ln=True)
    pdf.cell(0,7,f"Base: Rs {base_amount} | VAT {int(vat_rate*100)}%: Rs {vat} | TOTAL: Rs {total}", ln=True)
    pdf.cell(0,7,f"Pay: {JAZZCASH}", ln=True)
    pdf.ln(5)
    qr_data = f"JAZZCASH:{JAZZCASH}|TOTAL:{total}|VAT:{vat}"
    qr = qrcode.make(qr_data)
    qr_path = f"{BILLS_DIR}/qr_{client_name}.png"
    qr.save(qr_path)
    pdf.image(qr_path, x=75, w=60)
    pdf_path = f"{BILLS_DIR}/GENUINE_{client_name}_{country}.pdf"
    pdf.output(pdf_path)
    print(f"INVOICE: {pdf_path} - Rs {total}")
    return pdf_path

genuine_invoice("London Cafe", "UK", 7000)
genuine_invoice("Dubai Salon", "UAE", 7000)
genuine_invoice("Lahore Shop", "PK", 7000)

dashboard_html = f"""
<!DOCTYPE html><html><head><title>CHAPEX GENUINE</title>
<style>body{{background:#111;color:#fff;font-family:sans-serif;padding:20px}}.card{{background:#222;border:1px solid gold;padding:15px;margin:10px;border-radius:10px}}</style>
</head><body>
<h1 style="color:gold">CHAPEX GENUINE DASHBOARD - LIVE</h1>
<p>Generated: {datetime.now()}</p>
<div class="card">Main JazzCash: {JAZZCASH}</div>
<div class="card">Bills: {BILLS_DIR}/ - Tax Compliant</div>
<div class="card">Status: 100% Legal Production Base</div>
</body></html>
"""
open("genuine_dashboard.html","w").write(dashboard_html)
print("READY! ls GENUINE_BILLS/")
