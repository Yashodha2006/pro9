from exercise8.pro import product_details
def test_product_details():
    expected_output = {
        "Product ID":"P101"
        "Product Name": "Laptop"
        "Quantity":5
        "Price": 55000
    }
    assert product_details("P101", "Laptop", 5, 55000) == expected_output
