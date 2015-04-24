from gas import*
from data import*
from car import*

class Control:
	def __init__(self):
		self.car_list = {}
		self.car_data = {}
		self.dist_data = {}
		self.budget_data = {}
	def set_car_data(self, name, cylinder, torque, hp, weight, engine):
		data = {}
		data['name'] = name
		data['cylinder'] = int(cylinder)
		data['torque'] = int(torque)
		data['hp'] = int(hp)
		data['weight'] = int(weight)
		data['engine'] = engine
		self.car_data = data
		print self.car_data
		self.create_car()
	def set_dist_data(self, dist, gasType):
		data = {}
		data['distance'] = int(dist)
		data['gas_type'] = gasType
		self.dist_data = data
		print self.dist_data
	def set_budget_data(self, money, gasType):
		data = {}
		data['money'] = int(money)
		data['gas_type'] = gasType
		self.budget_data = data
		print self.budget_data
	def get_car_data(self):
		return self.get_car_list
	def create_car(self):
		car = Car()
		car.set_input(self.car_data)
		self.car_list[car.get_name()] = car
	def get_cars(self):
		print self.car_list.keys()
		return self.car_list.keys()