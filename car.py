class Car:
	def __init__(self):
		self.name = " "
		self.weight = 0
		self.hp = 0
		self.cylinder = 0
		self.torque = 0
		self.engine = 0
	def set_input(self, input):
		self.name = input['name']
		self.weight = input['weight']
		self.hp = input['hp']
		self.cylinder = input['cylinder']
		self.torque = input['torque']
		self.engine = input['engine']
	def get_weight(self):
		return self.weight