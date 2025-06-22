import requests

BOT_TOKEN = 'YOUR_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'  # Optional: Use bot to fetch user_id if needed

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    requests.post(url, data=payload)
