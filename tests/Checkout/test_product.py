import unittest

from Store.Checkout.product import Product

class ProductTestCase(unittest.TestCase):

    def test_product(self):
        
        code: str = "VOUCHER"
        name: str = "Gift Card"
        price: float = 5.0
        p: Product = Product(code=code, name=name, price=price)

        self.assertEqual(p.code, code)
        self.assertEqual(p.name, name)
        self.assertEqual(p.price, price)

if __name__ == '__main__':
    unittest.main()