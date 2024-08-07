from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account.signers.local import LocalAccount

from data.config import arb_rpc, privat_key 


# подключение
web3 = Web3(Web3.HTTPProvider(endpoint_uri = arb_rpc))
print(f"Is connected: {web3.is_connected()}")  # Is connected: True
# С подключением вас ?

print(f"gas price: {web3.eth.gas_price} ETH")  # кол-во Wei за единицу газа
print(f"current block number: {web3.eth.block_number}")
print(f"number of current chain is {web3.eth.chain_id}")  # 97
#получение баланса кошелька
wallet_address = Web3.to_checksum_address(web3.eth.account.from_key(privat_key).address)
print(wallet_address)  # ваш адрес
#checksum_address = Web3.to_checksum_address(wallet_address)
#balance = web3.eth.get_balance(wallet_address)
#print(f"balance of {wallet_address}={balance} Wei")