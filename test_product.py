import unittest
from product import product_details

class TestProductDetails(unittest.TestCase):

    def test_product_details(self):
        expected = (
            "Product ID: P101\n"
            "Product Name: Laptop\n"
            "Quantity: 5\n"
            "Price: 55000"
        )

        result = product_details("P101", "Laptop", 5, 55000)

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
