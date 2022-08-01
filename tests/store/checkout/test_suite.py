import unittest

from tests.store.checkout.test_calculator import CalculatorTestCase
from tests.store.checkout.test_checkout import CheckoutTestCase
from tests.store.checkout.test_discount import DiscountTestCase
from tests.store.checkout.test_discount_calculator import DiscountCalculatorTestCase
from tests.store.checkout.test_product import ProductTestCase
from tests.store.checkout.test_tshirt_rule import TShirtRuleTestCase
from tests.store.checkout.test_voucher_rule import VoucherRuleTestCase


def suite():

    suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(CalculatorTestCase),
        unittest.TestLoader().loadTestsFromTestCase(CheckoutTestCase),
        unittest.TestLoader().loadTestsFromTestCase(DiscountTestCase),
        unittest.TestLoader().loadTestsFromTestCase(DiscountCalculatorTestCase),
        unittest.TestLoader().loadTestsFromTestCase(ProductTestCase),
        unittest.TestLoader().loadTestsFromTestCase(TShirtRuleTestCase),
        unittest.TestLoader().loadTestsFromTestCase(VoucherRuleTestCase)
    ])

    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())