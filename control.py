from gas import*
from data import*
from car import*

class Control:
	def __init__(self):
		self.car_list = {}
		self.car_data = {}
		self.dist_data = {}
		self.budget_data = {}
		self.gas_list = {}
	def set_car_data(self, name, cylinder, torque, hp, weight, engine):
		data = {}
		data['name'] = name
<<<<<<< HEAD
<<<<<<< HEAD
		data['cylinder'] = ord(cylinder) - ord(0)
		data['torque'] = ord(torque) - ord(0)
		data['hp'] = ord(hp) - ord(0)
		data['weight'] = ord(weight) - ord(0)
		data['engine'] = engine
		self.car_data = data
		print sel.car_data
=======
		data['cylinder'] = cylinder
		data['torque'] = torque
		data['hp'] = hp
		data['weight'] = weight
		data['engine'] = engine
		self.car_data = data
		print self.car_data
>>>>>>> eb93270308c2fa499dee2b4973837475834c7e8b
	def set_dist_data(self, dist, gasType):
=======
		data['cylinder'] = int(cylinder)
		data['torque'] = int(torque)
		data['hp'] = int(hp)
		data['weight'] = int(weight)
		data['engine'] = engine
		self.car_data = data
		print sel.car_data
	def set_dist_data(self, car_name, dist, gasType):
>>>>>>> aa
		data = {}
		data['car_name'] = car_name
		data['distance'] = int(dist)
		data['gas_type'] = gasType
		self.dist_data = data
		print self.dist_data
	def set_budget_data(self, car_name, money, gasType):
		data = {}
		data['car_name'] = car_name
		data['money'] = int(money)
		data['gas_type'] = gasType
		self.budget_data = data
		print self.budget_data
	def get_car_data(self):
		return self.get_car_list
	def create_car(self, car_data):
		car = Car()
		car.set_input(self.car_data)
		self.car_list[car.get_name()] = car
	def get_cars(self):
		return self.car_list