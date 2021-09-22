import prettytable

table = prettytable.PrettyTable()


class User:
    def __init__(self, id, username):
        print("New user being created...")
        self.id = id
        self.username = username
        self.likes = 0

    def add_likes(self, likes):
        self.likes = self.likes + likes


user_1 = User(1, "arsovskidev")
user_1.add_likes(75)

table.add_column("ID", [user_1.id])
table.add_column("USERNAME", [user_1.username])
table.add_column("LIKES", [user_1.likes])
table.align = "l"

print(table)
