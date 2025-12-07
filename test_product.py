def test_product_details():
    expected_output = (
        "Product ID: P101\n"
        "Product Name: Laptop\n"
        "Quantity: 5\n"
        "Price: 55000"
    )

    assert product_details("P101", "Laptop", 5, 55000) == expected_output
