class Gas:
	def __init__(self):
		self.type = " "
		self.cost = 0
		self.mode = 0
	def set_type(self, type):
		self.type = type
	def set_cost(self, cost):
		self.cost = cost
	def set_mode(self, mode):
		self.mode = mode
	def get_gas(self):
		gas = {}
		gas['type'] = self.type
		gas['cost'] = self.cost
		gas['mode'] = self.mode
		return gas