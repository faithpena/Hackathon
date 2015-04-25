class Gas:
	def __init__(self):
		self.type = " "
		self.cost = 0
	def set(self, type, cost):
		self.type = type
		self.cost = cost
	def get_gas(self):
		gas = {}
		gas['type'] = self.type
		gas['cost'] = self.cost
		return gas
	def get_cost(self):
		return self.cost