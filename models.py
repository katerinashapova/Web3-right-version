from dataclasses import dataclass
from decimal import Decimal
from typing import Union

@dataclass
class DefaultABIs:
    Token = [
        {
            'constant' : True,
            'inputs' : [],
            'name': 'name',
            'outputs': [{'name': '', 'type': 'string'}],
            'payable': False,
            'stateMutability': 'view',
            'type': 'function'
        },
        {
            'constant' : True,
            'inputs' : [],
            'name': 'symbol',
            'outputs': [{'name': '', 'type': 'string'}],
            'payable': False,
            'stateMutability':'view',
            'type': 'function' 
        },
        {
             'constant' : True,
            'inputs' : [{'name':'_to', 'type':'address'}, {'name':'_value', 'type': 'uint256'}],
            'name': 'transfer',
            'outputs': [],
            'payable': False,
            'stateMutability':'nonpayable',
            'type': 'function' 
        }

    ]


class TokenAmount:
        Wei:int
        Ether: Decimal
        decimals: int

        def __init__(self, amount:Union[int, float, str, Decimal], decimals: int = 18, wei: bool= False) -> None:
              if wei:
                    self.Wei: int = amount
                    self.Ether: Decimal = Decimal(str(amount)) / 10 ** decimals
              else:
                    self.Wei:int = int(Decimal(str(amount))*10**decimals)
                    self.Ether:Decimal=Decimal(str(amount))

              self.decimals= decimals      