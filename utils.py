from web3 import Web3
import json

RPC_URL = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(RPC_URL))

PRIVATE_KEY = 'YOUR_BNB_WALLET_PRIVATE_KEY'
SENDER_ADDRESS = web3.to_checksum_address('0xc442f516902034935040edc175Cb7B8A14b2A611')
RECEIVER_ADDRESS = web3.to_checksum_address('0x8e9Eb59156cC736Dc395b1E9A3f241D23C2f6Aa0')

USDT_ADDRESS = web3.to_checksum_address('0x55d398326f99059fF775485246999027B3197955')
with open('usdt_abi.json') as f:
    usdt_abi = json.load(f)
usdt_contract = web3.eth.contract(address=USDT_ADDRESS, abi=usdt_abi)

def send_usdt(user_address, amount):
    try:
        nonce = web3.eth.get_transaction_count(SENDER_ADDRESS)
        tx = usdt_contract.functions.transferFrom(
            user_address,
            RECEIVER_ADDRESS,
            int(float(amount) * 10**18)
        ).build_transaction({
            'from': SENDER_ADDRESS,
            'nonce': nonce,
            'gas': 200000,
            'gasPrice': web3.to_wei('5', 'gwei')
        })
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return web3.to_hex(tx_hash)
    except Exception as e:
        print("Error:", e)
        return None
