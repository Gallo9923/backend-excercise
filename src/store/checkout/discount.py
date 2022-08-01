from dataclasses import dataclass

@dataclass
class Discount():
    """Represents a discount of a product"""

    name:str
    discount: float
    