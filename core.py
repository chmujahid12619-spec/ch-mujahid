import sys, json, os
from datetime import datetime

def bill_maker(name):
    if not name: name="UK Client 5000"
    parts=name.split()
    client=" ".join(parts[:-1]) if len(parts)>1 else "UK Client"
    amount=parts[-1] if parts[-1].isdigit() else "5000"
    bill=f"""
╔════════════════════════════╗
║ 👑 CHAPEX BRANDING BILL ║
╠════════════════════════════╣
║ Client: {client[:20]:<20} ║
║ Amount: Rs {amount:<15} ║
║ JazzCash & NayaPay: 03084513994 ║
║ Status: PAY NOW ║
║ Date: {datetime.now().strftime('%d-%m-%Y')} ║
╚════════════════════════════╝
    """
    open("bill.txt","w").write(bill)
    print(bill)
    print("💰 bill.txt Ready!")

def whatsapp_jin(number):
    if not number: number="447000000000"
    msg="Sir your website is ready 👑 - CHAPEX BRANDING%0A%0AYour Preview: https://ch-mujahid-global-empire.pages.dev%0A%0APay to activate: JazzCash 03084513994%0A%0A- CHAPEX, Lahore"
    link=f"https://wa.me/{number}?text={msg}"
    print(f"🤖 JIN READY FOR {number}\nLink: {link}")

def god_map():
    print("🌍 CHAPEX GLOBAL EMPIRE MAP\nUK 👑👑👑 3 Clients\nUAE 👑 1 Client (Dubai)\nPK 👑 HQ Lahore - 03084513994")

if "--bill" in sys.argv:
    bill_maker(sys.argv[2] if len(sys.argv)>2 else "")
elif "--whatsapp" in sys.argv:
    whatsapp_jin(sys.argv[2] if len(sys.argv)>2 else "")
elif "--map" in sys.argv:
    god_map()
else:
    print("👑 CHAPEX GOD MODE V2 - 3 JADU ACTIVE")
