import unittest

from shop import apply_discount, calculate_subtotal, qualifies_for_free_shipping


class TestShoppingFunctions(unittest.TestCase):
    def test_calculate_subtotal(self):
        self.fail("Add assertions for a subtotal and currency rounding")

    def test_apply_discount(self):
        self.fail("Add an assertion for a valid percentage discount")

    def test_free_shipping_threshold(self):
        self.fail("Check totals below and at the free-shipping threshold")

    def test_edge_cases_and_invalid_inputs(self):
        self.fail("Add boundary checks and assertRaises tests")


if __name__ == "__main__":
    unittest.main()