class User:
    def __init__(self, username):
        self.username = username

class AdminUser(User):
    def get_permissions(self):
        return "Full Access"

class RegularUser(User):
    def get_permissions(self):
        return "Limited Access"

# The Factory function routes user input to the correct subclass
def user_factory(username, role_input):
    if role_input.lower() == "admin":
        return AdminUser(username)
    else:
        return RegularUser(username)

# Usage based on user input
name = input("Enter username: ")
role = input("Enter role (admin/regular): ")

current_user = user_factory(name, role)
print(f"User type: {type(current_user).__name__}")
print(f"Permissions: {current_user.get_permissions()}")