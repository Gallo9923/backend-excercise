from dataclasses import dataclass
from enum import Enum

class Code(str, Enum):
    VOUCHER = "VOUCHER"
    TSHIRT = "TSHIRT"
    PANTS = "PANTS"

@dataclass
class Product():
    """Represents a product from the store"""
    
    code: Code
    name: str
    price: float

