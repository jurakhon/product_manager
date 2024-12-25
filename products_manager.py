products = {}

def add_product():
    name = input("Enter the name of the product: ")
    price = int(input("Enter the price of the product: "))
    products[name] = price
    print(f"Product {name} added successfully")





while True:
    print("Welcome to my products manager")
    print("1. Add a product")
    print("2. Update price")
    print("3. Delete a product")
    print("4. Total price")
    print("5. Save products to a file")
    print("5. Print current list")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_product()

    elif choice == "5":
        print(products)

