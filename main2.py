from data.config import privat_key, arb_rpc
from client import Client
from woofi import WooFi
from models import TokenAmount

from eth_account.signers.local import LocalAccount

client  = Client(privat_key=privat_key, rpc=arb_rpc)
#print(client.get_decimals(contract_address='0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8'))

#print(client.check_balance_interface(token_address= '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8', min_value=5))

# check the swap
woofi = WooFi(client=client)

#amount = TokenAmount(amount= 0.001)


tx = woofi.swap_usdc_to_eth()



res= woofi.client.verif_tx(tx_hash=tx)
print(res)

