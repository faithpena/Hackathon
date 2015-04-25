class Car:
	def __init__(self):
		self.name = " "
		self.weight = 0
		self.hp = 0
		self.cylinder = 0
		self.mpg = 0
		self.engine = " "
	def set_input(self, input):
		self.name = input['name']
		self.weight = input['weight']
		self.hp = input['hp']
		self.cylinder = input['cylinder']
		self.mpg = input['mpg']
		self.engine = input['engine']
	def get_weight(self):
		return self.weight
	def get_mpg(self):
		return self.mpg
	def get_name(self):
		return self.name