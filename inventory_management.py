inventory = {
    "apples": {"price": 1.00, "quantity": 100},
    "bananas": {"price": 0.50, "quantity": 150},
    "oranges": {"price": 2.00, "quantity": 120},
}

# Add a New Product

inventory["mangoes"] = {"price": 0.80, "quantity": 110}

# Update Product Price

inventory["bananas"]["price"] = 0.60

# Sell 25 Apples

inventory["apples"]["quantity"] -= 25

print(inventory)

# Calculate Total Inventory Value

total_value = sum(product["price"] * product["quantity"] for product in inventory.values())
print(total_value)

# Find Low Stock Products

low_stock_products = [name for name, product in inventory.items() if product["quantity"] < 100]

print(low_stock_products)