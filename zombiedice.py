from player import *
from dice import *

class Game(object):
	g_players = []
	g_numplayers = 0
	g_currp = ''
	
	g_status = True
	
	def __init__(self):
		print "Welcome to Zombie Dice!\n"
		numplayers = raw_input("How many players are there? ")
		self.g_numplayers = int(numplayers)
		
		for x in range(1,self.g_numplayers+1):
			print "Player " + str(x) + ", what is your name?"
			self.g_players.append(Player(raw_input()))
			
		print "\n"
		
		self.play()
			
	def play(self):
		greenDice = GreenDice();
		yellowDice = YellowDice();
		redDice = RedDice();
		die = [ greenDice, greenDice, greenDice, greenDice,
		  		greenDice, greenDice, yellowDice, yellowDice,
		 		yellowDice, yellowDice, redDice, redDice, redDice ]
		faces = [ '', 'Brain', 'Footprints', 'Shotgun' ]
		
		while self.g_status:
			for x in range(0,self.g_numplayers):
				p_turn = True
				print "Current rankings:"
				for y in range(0,self.g_numplayers):
					print self.g_players[y].p_name + ": " + str(self.g_players[y].p_score) + " brains"
					
				print "\n"
				
				c_pscore = 0
				while p_turn:
					roll = []
					print "It's your turn, " + self.g_players[x].p_name + "!"
					action = raw_input("What will you do?  ('(r)oll', '(s)core') ")
					if action=="roll" or action=="r":
						p_die = [ die[random.randint(0,12)], die[random.randint(0,12)], die[random.randint(0,12)] ]
						roll = [ p_die[0].roll(), p_die[1].roll(), p_die[2].roll() ]
						print self.g_players[x].p_name + " rolled:"
						
						for y in range(0,3):
							print p_die[y].d_name + ": " + faces[roll[y]]
							
						print "\n"
						
						for y in roll:
							if y==1:
								c_pscore += 1
							if y==3:
								self.g_players[x].shotgun()
								
						print self.g_players[x].p_name + "'s current score:"
						print "Brains: " + str(c_pscore)
						print "Shotguns: " + str(self.g_players[x].p_cshotguns) + "\n"
						
						if self.g_players[x].p_cshotguns >= 3:
							print self.g_players[x].p_name + " was SHOTGUNNED!\n"
							self.g_players[x].p_rounds += 1
							self.g_players[x].reset_shotguns()
							p_turn = False
							
					elif action=="score" or action=="s":
						print self.g_players[x].p_name + " scored " + str(c_pscore) + " brains!\n"
						self.g_players[x].score(c_pscore)
						self.g_players[x].p_rounds += 1
						self.g_players[x].reset_shotguns()
						p_turn = False
						
				if(self.g_players[x].p_score >= 13):
					print self.g_players[x].p_name + " has won!\n"
					self.g_status = False
					break
		
x = Game()
		
	