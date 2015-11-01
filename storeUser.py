class StoreUser:
    def __init__(self):
        self.users = {}
        self.last_key = 0

    def add_user(self, user):
        self.last_key += 1
        self.users[self.last_key] = user

    def delete_user(self, key):
        del self.users[key]

    def get_user(self, key):
        return self.users[key]

    def get_users(self):
        return sorted(self.users.items())