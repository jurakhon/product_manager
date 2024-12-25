from fileinput import filename

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

def total_price():
    total = 0
    for product in products.values():
        total += product
    print(f"Total price: {total}")

def save_products_to_file():
    filename = input("Enter the name of the file to save the products: ")
    with open(filename, "w") as file:
        for name, price in products.items():
            file.write(f"{name} - {price}\n")
    print(f"Products saved successfully to {filename}")


while True:
    print("Welcome to my products manager")
    print("1. Add a product")
    print("2. Update price")
    print("3. Delete a product")
    print("4. Total price")
    print("5. Print current list")
    print("6. Save products to a file")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_product()

    elif choice == "2":
        update_price()

    elif choice == "3":
        delete_product()

    elif choice == "4":
        total_price()

    elif choice == "5":
        print(products)

    elif choice == "6":
        save_products_to_file()
