class Data:
	def __init__(self):
		self.money = 0 #can also be called cost for distance
		self.gasType = 0 #fuel type
		self.gasAmt = 0 #amount of gas to buy
		self.dist = 0 #how far you can go or will go
		self.mode = 0 #0 for distance, 1 for budget
	def set_input_dist(self, input):
		self.money = input['money']
		self.gasType = input['gas_amt']
	def set_input_bud(self, input):
		self.dist = input['distance']
		self.gasType = input['gas_amt']
	def set_gasAmt(self, gas):
		self.gasAmt = gas
	def compute_dist(self, dist):
		self.dist = dist
	def compute_gasAmt(self, amt):
		self.gasAmt = amt
	def get_gasAmt(self):
		return self.gasAmt
	def get_dist(self):
		return self.dist
	def get_money(self):
		return self.money