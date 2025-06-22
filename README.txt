SETUP GUIDE:

1. Replace 'YOUR_BOT_TOKEN' in telegram_notify.py with your Telegram bot token.
2. Replace 'YOUR_CHAT_ID' with your Telegram chat ID.
3. Replace 'YOUR_BNB_WALLET_PRIVATE_KEY' in utils.py with your BNB wallet private key.

DEPLOY TO RAILWAY:
1. Push these files to GitHub.
2. Go to Railway → New Project → Deploy from GitHub Repo.
3. Add environment variables if needed.
4. Done. Flask app will run at your Railway URL.

FRONTEND INTEGRATION:
- Make a POST request to /transfer with:
  {
    "user_address": "0xUserWalletAddress",
    "amount": "10"
  }
