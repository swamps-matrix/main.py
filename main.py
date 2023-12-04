from user_auth import login, logout
from product_manager import list_products, add_product_to_cart, checkout

def main():
    print("Welcome to the Online Store!")

    # User authentication
    user_id = login()
    
    # Product management
    list_products()
    add_product_to_cart(user_id, product_id=2, quantity=3)

    # Checkout
    checkout(user_id)

    # Logout
    logout(user_id)

if __name__ == "__main__":
    main()
