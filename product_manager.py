class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

# Dummy product data
products = [
    Product(1, "Laptop", 1000),
    Product(2, "Smartphone", 500),
    Product(3, "Headphones", 50),
]

def list_products():
    print("Available Products:")
    for product in products:
        print(f"{product.product_id}. {product.name} - ${product.price}")

def add_product_to_cart(user_id, product_id, quantity):
    print(f"User {user_id} added {quantity} units of product {product_id} to the cart.")

def checkout(user_id):
    print(f"User {user_id} checked out. Thank you for shopping!")
