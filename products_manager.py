
products = {}

def add_product():
    name = input("Enter the name of the product: ")
    try:
        price = int(input("Enter the price of the product: "))
        if price < 0:
            raise ValueError
        elif price is None:
            raise ValueError
        elif price == float(price):
            price = int(price)
        products[name] = price
        print(f"Product {name} added successfully")

    except ValueError:
        print("Enter Integer price. No Negative number, No Float or String.")


def update_price():
    name = input("Enter the name of the product: ")
    if name not in products:
        print("Product not found")
        return

    try:
        price = int(input("Enter the new price of the product: "))
        if price < 0:
            raise ValueError
        elif price is None:
            raise ValueError
        elif price == float(price):
            price = int(price)
        products[name] = price
        print(f"Price of {name} updated successfully")
    except ValueError:
        print("Enter Integer price. No Negative number, No Float or String.")


def delete_product():
    name = input("Enter the name of the product to delete: ")
    if name not in products:
        print("Product not found")
        return
    else:
        print(f"Price of {name} is {products[name]}")
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


def load_products_from_file():
    try:
        filename = input("Enter the name of the file to load: ")
        with open(filename, "r") as file:
            for line in file:
                if '-' not in line:
                    continue
                name, price = line.strip().split("-")
                products[name.strip()] = int(price.strip())
        print(f"Products loaded successfully from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")




while True:
    print("1. Add a product")
    print("2. Update price")
    print("3. Delete a product")
    print("4. Total price")
    print("5. Print current list")
    print("6. Save products to a file")
    print("7. Load products from a file")
    print("8. Exit")
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

    elif choice == "7":
        load_products_from_file()

    elif choice == "8":
        break
