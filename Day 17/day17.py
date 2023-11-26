class User:
    id = 1

    def __init__(self, username):
        # self.id += 1
        self.id = User.id
        User.id += 1
        self.username = username


user1 = User("Anand")
user2 = User("Brijraj")
user3 = User("Khan")

print(f"user 1 is {user1.id} - {user1.username}")
print(f"user 2 is {user2.id} - {user2.username}")
print(f"user 3 is {user3.id} - {user3.username}")