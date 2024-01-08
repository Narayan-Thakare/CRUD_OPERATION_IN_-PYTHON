class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def display_info(self):
        print(f"ID: {self.user_id}, Username: {self.username}, Email: {self.email}")


class UserManager:
    def __init__(self):
        self.users = []

    def create_user(self):
        username = input("Enter username: ")
        email = input("Enter email: ")

        new_id = len(self.users) + 1
        new_user = User(new_id, username, email)
        self.users.append(new_user)
        print("User created successfully.")

    def Show_all_users(self):
        print("All Users:")
        for user in self.users:
            user.display_info()

    def Search_user(self):
        user_id = int(input("Enter user ID to display: "))
        user = self.find_user_by_id(user_id)
        if user:
            user.display_info()
        else:
            print("User not found.")

    def update_user(self):
        user_id = int(input("Enter user ID to update: "))
        user = self.find_user_by_id(user_id)
        if user:
            new_username = input("Enter new username: ")
            new_email = input("Enter new email: ")

            user.username = new_username
            user.email = new_email
            print("User updated successfully.")
        else:
            print("User not found.")

    def delete_user(self):
        user_id = int(input("Enter user ID to delete: "))
        user = self.find_user_by_id(user_id)
        if user:
            self.users.remove(user)
            print("User deleted successfully.")
        else:
            print("User not found.")

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None


# Example Usage:
if __name__ == "__main__":
    user_manager = UserManager()

    while True:
        print("\nUser Management Menu:")
        print("1. Create User")
        print("2. Show All Users")
        print("3. Search User by ID")
        print("4. Update User by ID")
        print("5. Delete User by ID")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            user_manager.create_user()
        elif choice == "2":
            user_manager.Show_all_users()
        elif choice == "3":
            user_manager.Search_user()
        elif choice == "4":
            user_manager.update_user()
        elif choice == "5":
            user_manager.delete_user()
        elif choice == "6":
            print("Exiting User Management. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
