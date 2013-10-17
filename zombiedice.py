import random
from player import Player
from dice import GreenDice, YellowDice, RedDice


class Game(object):
    players = []
    numplayers = 0

    def __init__(self):
        print "Welcome to Zombie Dice!"
        print
        numplayers = raw_input("How many players are there? ")
        self.numplayers = int(numplayers)

        for x in range(self.numplayers):
            print "Player %d, what is your name? " % (x + 1)
            self.players.append(Player(raw_input()))
        print

        self.play()

    def play(self):
        # greenDice = GreenDice()
        # yellowDice = YellowDice()
        # redDice = RedDice()
        die = [
            GreenDice(), GreenDice(), GreenDice(), GreenDice(),
            GreenDice(), GreenDice(), YellowDice(), YellowDice(),
            YellowDice(), YellowDice(), RedDice(), RedDice(), RedDice()
        ]
        faces = ['', 'Brain', 'Footprints', 'Shotgun']

        status = True

        while status:
            for current_player in self.players:
                p_turn = True
                print "Current rankings:"
                for scored_player in self.players:
                    print "%s: %d brains" % (
                        scored_player, scored_player.p_score)

                print

                c_pscore = 0
                while p_turn:
                    roll = []
                    print "It's your turn, %s !" % current_player
                    action = raw_input(
                        "What will you do? ('(r)oll', '(s)core') ")
                    if action in ("roll", "r"):
                        die_list = []
                        rolls = []
                        for i in range(3):
                            dice = random.choice(die)
                            die_list.append(dice)
                            rolls.append(dice.roll())

                        print "%s rolled:" % current_player

                        for temp_die, roll in zip(die_list, rolls):
                            print "%s: %s" % (dice, faces[roll])

                        print

                        for roll in rolls:
                            if roll == 1:
                                c_pscore += 1
                            if roll == 3:
                                current_player.shotgun()

                        print "%s's current score:" % current_player
                        print "Brains: %d" % c_pscore
                        print "Shotguns: %d" % current_player.p_cshotguns
                        print

                        if current_player.p_cshotguns >= 3:
                            print "%s was SHOTGUNNED!" % current_player
                            print
                            current_player.p_rounds += 1
                            current_player.reset_shotguns()
                            p_turn = False

                    elif action in ("score", "s"):
                        print "%s scored %d brains!" % (
                            current_player, c_pscore)
                        current_player.score(c_pscore)
                        current_player.p_rounds += 1
                        current_player.reset_shotguns()
                        p_turn = False

                if current_player.p_score >= 13:
                    print "%s has won!" % current_player
                    print
                    status = False
                    break

x = Game()
