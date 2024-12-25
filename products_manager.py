products = {}

def add_product():
    name = input("Enter the name of the product: ")
    price = int(input("Enter the price of the product: "))
    products[name] = price
    print(f"Product {name} added successfully")


def update_price():
    name = input("Enter the name of the product: ")
    price = int(input("Enter the new price of the product: "))
    products[name] = price
    print(f"Price of {name} updated successfully")

def delete_product():
    name = input("Enter the name of the product to delete: ")
    del products[name]
    print(f"{name} was deleted successfully from the list")



while True:
    print("Welcome to my products manager")
    print("1. Add a product")
    print("2. Update price")
    print("3. Delete a product")
    print("4. Total price")
    print("5. Save products to a file")
    print("6. Print current list")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_product()

    elif choice == "2":
        update_price()

    elif choice == "3":
        delete_product()


    elif choice == "6":
        print(products)

