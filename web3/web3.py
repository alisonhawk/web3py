import math
from decimal import Decimal
from fractions import Fraction

unit_map = {
    "noether": "0",
    "wei": "1",
    "kwei": "1000",
    "Kwei": "1000",
    "babbage": "1000",
    "femtoether": "1000",
    "mwei": "1000000",
    "Mwei": "1000000",
    "lovelace": "1000000",
    "picoether": "1000000",
    "gwei": "1000000000",
    "Gwei": "1000000000",
    "shannon": "1000000000",
    "nanoether": "1000000000",
    "nano": "1000000000",
    "szabo": "1000000000000",
    "microether": "1000000000000",
    "micro": "1000000000000",
    "finney": "1000000000000000",
    "milliether": "1000000000000000",
    "milli": "1000000000000000",
    "ether": "1000000000000000000",
    "kether": "1000000000000000000000",
    "grand": "1000000000000000000000",
    "mether": "1000000000000000000000000",
    "gether": "1000000000000000000000000000",
    "tether": "1000000000000000000000000000000",
}

BIG0 = 0
RAT0 = Fraction(0, 1)

class Provider:
    pass

class RequestManager:
    pass

class Eth:
    pass

class Net:
    pass

class Web3:
    def __init__(self, provider: Provider):
        self.provider = provider
        self.request_manager = RequestManager()
        self.eth = Eth()
        self.net = Net()
