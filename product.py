def product_details(pid, name, qty, price):
    return {
        "Product ID": pid,
        "Product Name": name,
        "Quantity": qty,
        "Price": price
    }

# Calling the function
product = product_details(101, "Wooden Toy Car", 5, 350)

# Display product details
print("Product Details:")
for key, value in product.items():
    print(f"{key}: {value}")
