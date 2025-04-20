import time
from datetime import datetime
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json

# Supported EVM-compatible chains
chains = {
    'ethereum': {'rpc': 'https://ethereum-rpc.publicnode.com', 'chain_id': 1},
    'arbitrum': {'rpc': 'https://arb1.arbitrum.io/rpc', 'chain_id': 42161},
    'optimism': {'rpc': 'https://mainnet.optimism.io', 'chain_id': 10},
    'base': {'rpc': 'https://mainnet.base.org', 'chain_id': 8453},
    'bsc': {'rpc': 'https://bsc-dataseed1.binance.org/', 'chain_id': 56},
    'polygon': {'rpc': 'https://polygon-rpc.com/', 'chain_id': 137},
    'fantom': {'rpc': 'https://rpcapi.fantom.network', 'chain_id': 250},
    'gravity': {'rpc': 'https://rpc.gravity.xyz', 'chain_id': 1625},
    'sonic': {'rpc': 'https://sonic.api.onfinality.io/public', 'chain_id': 146},
    'soneium': {'rpc': 'https://soneium.drpc.org', 'chain_id': 1868},
    'zora': {'rpc': 'https://rpc.zora.energy', 'chain_id': 7777777}
}

# List of tokens to rescue
ERC20_ABI = json.loads('[{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"type":"function"}]')

tokens = [
    # Ethereum
    {'symbol': 'USDC', 'address': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606EB48'},
    {'symbol': 'DAI', 'address': '0x6B175474E89094C44Da98b954EedeAC495271d0F'},
    {'symbol': 'UNI', 'address': '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984'},
    # BSC
    {'symbol': 'BUSD', 'address': '0xe9e7cea3dedca5984780bafc599bd69add087d56'},
    {'symbol': 'CAKE', 'address': '0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82'},
    # Polygon
    {'symbol': 'WMATIC', 'address': '0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270'},
    {'symbol': 'QUICK', 'address': '0x831753dd7087cac61ab5644b308642cc1c33dc13'},
    # Arbitrum
    {'symbol': 'ARB', 'address': '0x912CE59144191C1204E64559FE8253a0e49E6548'},
    # Optimism
    {'symbol': 'OP', 'address': '0x4200000000000000000000000000000000000042'},
    # Fantom
    {'symbol': 'FTM', 'address': '0x21be370d5312f44cb42ce377bc9b8a0cef1a4c83'}
]

# Wallets
wallets = [
    {
        'private_key': 'YOUR_PRIVATE_KEY_1',
        'from_address': Web3.to_checksum_address('0xYourWalletAddress1'),
        'safe_address': Web3.to_checksum_address('0xYourSafeWalletAddress1')
    },
    {
        'private_key': 'YOUR_PRIVATE_KEY_2',
        'from_address': Web3.to_checksum_address('0xYourWalletAddress2'),
        'safe_address': Web3.to_checksum_address('0xYourSafeWalletAddress2')
    }
    # Add more wallets as needed
]

def log(msg):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.now().isoformat()} | {msg}\n")
    print(msg)

def rescue_tokens(w3, wallet, safe_address, nonce):
    for token in tokens:
        try:
            token_address = Web3.to_checksum_address(token['address'])
            contract = w3.eth.contract(address=token_address, abi=ERC20_ABI)
            balance = contract.functions.balanceOf(wallet['from_address']).call()
            if balance > 0:
                gas_price = w3.eth.gas_price
                tx = contract.functions.transfer(safe_address, balance).build_transaction({
                    'from': wallet['from_address'],
                    'nonce': nonce,
                    'gas': 100000,
                    'gasPrice': gas_price,
                    'chainId': w3.eth.chain_id
                })
                signed_tx = w3.eth.account.sign_transaction(tx, wallet['private_key'])
                tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
                log(f"[TOKEN:{token['symbol']}] Sent from {wallet['from_address']} to {safe_address} -> {tx_hash.hex()}")
                nonce += 1
        except Exception as e:
            log(f"[TOKEN:{token['symbol']}] Error for {wallet['from_address']}: {str(e)}")
    return nonce

def scan_all_wallets():
    for wallet in wallets:
        for name, chain in chains.items():
            try:
                w3 = Web3(Web3.HTTPProvider(chain['rpc']))
                w3.middleware_onion.inject(geth_poa_middleware, layer=0)
                if not w3.is_connected():
                    log(f"[{name.upper()}] RPC FAILED.")
                    continue

                balance = w3.eth.get_balance(wallet['from_address'])
                log(f"[{name.upper()}] [{wallet['from_address']}] Balance: {w3.from_wei(balance, 'ether'):.18f}")

                nonce = w3.eth.get_transaction_count(wallet['from_address'])
                nonce = rescue_tokens(w3, wallet, wallet['safe_address'], nonce)

                network_gas_price = w3.eth.gas_price
                max_gas_price = w3.to_wei('50', 'gwei')
                gas_price = min(network_gas_price, max_gas_price)
                gas_limit = 21000
                fee = gas_price * gas_limit

                if balance <= fee:
                    log(f"[{name.upper()}] Not enough to cover gas fee.")
                    continue

                buffer = int(fee * 0.01)
                transferable_value = balance - fee - buffer

                if transferable_value <= 0:
                    log(f"[{name.upper()}] Transferable value too small after buffer.")
                    continue

                tx = {
                    'nonce': nonce,
                    'to': wallet['safe_address'],
                    'value': transferable_value,
                    'gas': gas_limit,
                    'gasPrice': gas_price,
                    'chainId': chain['chain_id']
                }

                signed_tx = w3.eth.account.sign_transaction(tx, wallet['private_key'])
                tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
                log(f"[{name.upper()}] Native TX SENT -> {tx_hash.hex()}")

            except Exception as e:
                log(f"[{name.upper()}] [{wallet['from_address']}] Error: {str(e)}")

while True:
    scan_all_wallets()
    time.sleep(30)
