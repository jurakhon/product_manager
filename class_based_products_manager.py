class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"

class ProductManager:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price):
        self.products[name] = price


product_manager = ProductManager()


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
        name = input("Enter the name of the product: ")
        price = int(input("Enter the price of the product: "))
        product_manager.add_product(name, price)
        print(f"Product {name} added successfully")
        print(product_manager.products)