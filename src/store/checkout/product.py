from dataclasses import dataclass
from enum import Enum, auto

class Code(Enum):
    VOUCHER = auto()
    TSHIRT = auto()
    PANTS = auto()

@dataclass
class Product():
    """Represents a product from the store"""
    
    code: Code
    name: str
    price: float

