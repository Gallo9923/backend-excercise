import unittest

from store.checkout.discount import Discount
class DiscountTestCase(unittest.TestCase):

    def test_discount(self):
        name: str = "Voucher Discount"
        discount: float = 0.0
        d: Discount = Discount(name=name, discount=discount)

        self.assertEqual(d.name, name)
        self.assertEqual(d.discount, discount)


if __name__ == '__main__':
    unittest.main()