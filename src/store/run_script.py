from typing import List
from src.store.checkout.calculator import CalculatorImpl

from src.store.checkout.checkout import Checkout
from src.store.checkout.discount_calculator import DiscountCalculator, DiscountCalculatorImpl
from src.store.checkout.pricing_rule import PricingRule, TShirtRule, VoucherRule
from src.store.checkout.product import Code, Product



def get_pricing_rules() -> List[PricingRule]:
    discounts: List[PricingRule] = []
    discounts.append(VoucherRule(name="Voucher discount"))
    discounts.append(TShirtRule(name="Tshirt discount"))
    return discounts


def get_checkout_obj() -> Checkout:
    pricing_rules: List[PricingRule] = get_pricing_rules()
    discount_calculator: DiscountCalculator = DiscountCalculatorImpl(pricing_rules=pricing_rules)

    return Checkout(calculator=CalculatorImpl(), discount_calculator=discount_calculator)    

def get_example_one_products(): 

    products: List[Product] = []
    products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))
    products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))
    products.append(Product(code=Code.PANTS, name="Summer Pants", price=7.5))

    return products

def get_example_two_products(): 

    products: List[Product] = []
    products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))
    products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))
    products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))

    return products

def get_example_three_products():
    products: List[Product] = []
    products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))
    products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))
    products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))
    products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))
    products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))

    return products

def get_example_four_products(): 

    products: List[Product] = []
    products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))
    products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))
    products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))
    products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))
    products.append(Product(code=Code.PANTS, name="Summer Pants", price=7.5))
    products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))
    products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))

    return products    

def scan_products(checkout: Checkout, products: List[Product]):
    for product in products:
        checkout.scan(product=product)

def main():

    checkout: Checkout = get_checkout_obj()
    # products: List[Product] = get_example_one_products()
    # products: List[Product] = get_example_two_products()
    # products: List[Product] = get_example_three_products()
    products: List[Product] = get_example_four_products()
    scan_products(checkout=checkout, products=products)
    
    print(checkout.get_total())



if __name__ == '__main__':
    main()