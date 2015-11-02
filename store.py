class Store:
    def __init__(self):
        self.teams = {}
        self.users = {}
        self.last_key_team = 0
        self.last_key_user = 0

    def add_team(self, team):
        self.last_key_team += 1
        self.teams[self.last_key_team] = team

    def delete_team(self, key_team):
        del self.teams[key_team]

    def get_team(self, key_team):
        return self.teams[key_team]

    def get_teams(self):
        return sorted(self.teams.items())

