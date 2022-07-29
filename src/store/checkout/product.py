from dataclasses import dataclass

@dataclass
class Product():
    """Represents a product from the store"""
    
    code: str
    name: str
    price: float
