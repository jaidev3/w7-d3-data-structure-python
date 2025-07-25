
products = ["apple", "banana", "cherry", "orange", "pineapple", "mango"]
prices = [199.00, 10.50, 100.75, 150.00, 200.00, 120.00]
quantities = [10, 20, 15, 25, 30, 10]

# Create Product-Price Pairs
product_price_pairs = list(zip(products, prices))
print(product_price_pairs)

# Calculate Total Value for Each Product
product_value_dict = {product: price * quantity for product, price, quantity in zip(products, prices, quantities)}
print(product_value_dict)

# Build a Product Catalog Dictionary
product_catalog = {product: {"price": price, "quantity": quantity} for product, price, quantity in zip(products, prices, quantities)}
print(product_catalog)

# Find Low Stock Products
low_stock_products = [product for product, quantity in zip(products, quantities) if quantity < 10]
print(low_stock_products)