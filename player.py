class Player(object):
    score = 0
    rounds = 0
    shotguns = 0
    name = "Guest"

    def __init__(self, name):
        self.score = 0
        self.rounds = 0
        self.shotguns = 0
        self.name = name

    def __repr__(self):
        return self.name

    def increment(self, score):
        self.score += score

    def shotgun(self):
        self.shotguns += 1

    def reset_shotguns(self):
        self.shotguns = 0

    def reset(self):
        self.score = 0
        self.rounds = 0
        self.shotguns = 0
