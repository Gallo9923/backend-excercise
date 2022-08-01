import uvicorn 
from fastapi import FastAPI
from typing import List

from store.checkout.calculator import CalculatorImpl
from store.checkout.product import Product
from store.checkout.checkout import Checkout
from store.checkout.discount_calculator import DiscountCalculator, DiscountCalculatorImpl
from store.checkout.pricing_rule import PricingRule, TShirtRule, VoucherRule
from store.checkout.product import Product

app: FastAPI = FastAPI()

def get_pricing_rules() -> List[PricingRule]:
    discounts: List[PricingRule] = []
    discounts.append(VoucherRule(name="Voucher discount"))
    discounts.append(TShirtRule(name="Tshirt discount"))
    return discounts

def get_checkout_obj() -> Checkout:
    pricing_rules: List[PricingRule] = get_pricing_rules()
    discount_calculator: DiscountCalculator = DiscountCalculatorImpl(pricing_rules=pricing_rules)
    return Checkout(calculator=CalculatorImpl(), discount_calculator=discount_calculator)    

@app.post("/")
def read_root(products: List[Product]):

    checkout: Checkout = get_checkout_obj()
    
    for p in products:
        checkout.scan(p)

    return {"total": checkout.get_total()}


def main():
    uvicorn.run("main:app", port=8000, log_level="info") 

if __name__ == "__main__":
    main()
    