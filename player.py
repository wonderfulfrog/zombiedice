class Player(object):
	p_score = 0
	p_rounds = 0
	p_cshotguns = 0
	p_name = "Guest"
	
	def __init__ (self, p_name):
		self.p_score = 0
		self.p_rounds = 0
		self.p_cshotguns = 0
		self.p_name = p_name
		
	def score(self, score):
		self.p_score += score
		
	def shotgun(self):
		self.p_cshotguns += 1
		
	def reset_shotguns(self):
		self.p_cshotguns = 0
	
	def reset(self):
		self.p_score = 0
		self.p_rounds = 0
		self.p_cshotguns = 0