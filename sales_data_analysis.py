sales_data = [("Q1", [("Jan", 1000), ("Feb", 1200), ("Mar", 1100)]),
              ("Q2", [("Apr", 1300), ("May", 1400), ("Jun", 1500)]),
              ("Q3", [("Jul", 1600), ("Aug", 1700), ("Sep", 1800)])]

# Calculate Total Sales per Quarter

for quarter, months in sales_data:
    total_sales = sum(sales for _, sales in months)
    print(f"Total sales for {quarter}: {total_sales}")

# Find the Month with Highest Sales

highest_sales = 0
highest_month = ""

for quarter, months in sales_data:
    for month, sales in months:
        if sales > highest_sales:
            highest_sales = sales
            highest_month = month

print(f"The month with the highest sales is {highest_month} with {highest_sales} sales.")

# Create a Flat List of Monthly Sales

flat_list = []

for quarter, months in sales_data:
    for month, sales in months:
        flat_list.append((month, sales))

print(flat_list)

# Use Unpacking in Loops

for quarter, months in sales_data:
    for month, sales in months:
        print(f"Quarter: {quarter}, Month: {month}, Sales: {sales}")