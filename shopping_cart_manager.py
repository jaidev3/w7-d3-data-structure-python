shopping_cart = []

def add_item(item):
    shopping_cart.append(item)
    print(f"{item} added to the cart")

def remove_item(item):
    if item in shopping_cart:
        shopping_cart.remove(item)
        print(f"{item} removed from the cart")

def remove_last_item():
    if shopping_cart:
        last_item = shopping_cart.pop()
        print(f"{last_item} removed from the cart")

def display_items_alphabetically():
    sorted_cart = sorted(shopping_cart)
    for index, item in enumerate(sorted_cart):
        print(f"{index}: {item}")

def display_cart_contents_with_indices():
    for index, item in enumerate(shopping_cart):
        print(f"{index}: {item}")

def main():
    while True:
        print("\nShopping Cart Manager")
        print("1. Add Item")
        print("2. Remove a Specific Item")
        print("3. Remove the Last Added Item")
        print("4. Display Items in Alphabetical Order")
        print("5. Display Cart Contents with Indices")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == "2":
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == "3":
            remove_last_item()
        elif choice == "4":
            display_items_alphabetically()
        elif choice == "5":
            display_cart_contents_with_indices()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()