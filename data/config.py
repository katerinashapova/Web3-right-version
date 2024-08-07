import os
import sys

from pathlib import Path
from web3 import Web3

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()


ABIS_DIR = os.path.join(ROOT_DIR, 'abis')

TOKEN_ABI = os.path.join(ABIS_DIR, 'token.json')
WOOFI_ABI = os.path.join(ABIS_DIR, 'woofi.json')


privat_key = '5083f1c16e64a7904cec6e5d8c23fe816988d0262c494117c39fb5c926072062'
seed = 'space riot aim twenty brown pill cliff upset useful brisk arena flee'
eth_rpc = 'https://mainnet.infura.io/v3/'
arb_rpc = 'https://arb1.arbitrum.io/rpc/'
