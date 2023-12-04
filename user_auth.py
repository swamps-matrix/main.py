def login():
    user_id = input("Enter your user ID: ")
    print(f"User {user_id} logged in successfully!")
    return user_id

def logout(user_id):
    print(f"User {user_id} logged out.")
