class User:
    def __init__(self, user_id="", level=0):
        self.user_id = user_id
        self.level = level


user1 = User()
user1.user_id = "codetree"
user1.level = 10

u2_id, u2_level = input().split()
user2 = User()
user2.user_id = u2_id
user2.level = int(u2_level)

print("user", user1.user_id, "lv", user1.level)
print("user", user2.user_id, "lv", user2.level)