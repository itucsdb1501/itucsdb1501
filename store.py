class Store:
    def __init__(self):
        self.teams = {}
        self.users = {}
        self.fixtures = {}
        self.anthems = {}
        self.last_key_team = 0
        self.last_key_user = 0
        self.last_key_fixture = 0
        self.last_key_anthem = 0

    def add_team(self, team):
        self.last_key_team += 1
        self.teams[self.last_key_team] = team

    def delete_team(self, key_team):
        del self.teams[key_team]

    def get_team(self, key_team):
        return self.teams[key_team]

    def get_teams(self):
        return sorted(self.teams.items())
    
    
    def add_anthem(self, anthem):
        self.last_key_anthem += 1
        self.anthems[self.last_key_anthem] = anthem

    def delete_anthem(self, key_anthem):
        del self.anthems[key_anthem]

    def get_anthem(self, key_anthem):
        return self.anthems[key_anthem]

    def get_anthems(self):
        return sorted(self.anthems.items())
    
    
    
    

    def add_fixture(self, fixture):
        self.last_key_fixture += 1
        self.fixtures[self.last_key_fixture] = fixture

    def delete_fixture(self, key_fixture):
        del self.fixtures[key_fixture]

    def get_fixture(self, key_fixture):
        return self.fixtures[key_fixture]

    def get_fixtures(self):
        return sorted(self.fixtures.items())

    def add_user(self, user):
        self.last_key_user += 1
        self.users[self.last_key_user] = user

    def delete_user(self, key_user):
        del self.users[key_user]

    def get_user(self, key_user):
        return self.users[key_user]

    def get_users(self):
        return sorted(self.users.items())