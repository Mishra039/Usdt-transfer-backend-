from flask import Flask, request, jsonify
from web3 import Web3
from utils import send_usdt
from telegram_notify import send_telegram_message

app = Flask(__name__)

@app.route('/transfer', methods=['POST'])
def transfer():
    data = request.json
    user_address = data.get('user_address')
    amount = data.get('amount')

    if not user_address or not amount:
        return jsonify({'error': 'Missing user_address or amount'}), 400

    tx_hash = send_usdt(user_address, amount)
    if tx_hash:
        send_telegram_message(f"✅ USDT Transfer Success
From: {user_address}
Tx: {tx_hash}")
        return jsonify({'success': True, 'tx_hash': tx_hash}), 200
    else:
        return jsonify({'error': 'Transfer failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
