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
		data['cylinder'] = cylinder
		data['torque'] = torque
		data['hp'] = hp
		data['weight'] = weight
		data['data'] = data
		self.car_data = data
		print self.car_data
	def set_dist_data(self, dist, gasType):
		data = {}
		data['distance'] = dist
		data['gas_type'] = gasType
		self.dist_data = data
	def set_budget_data(self, money, gasType):
		data = {}
		data['money'] = money
		data['gas_type'] = gasType
		self.dist_data = data
	def get_car_data(self):
		return self.get_car_list
	def create_car(self, car_data):
		car = Car()
		car.set_input(car_data)
		self.car_list[car.get_name] = car
	def get_cars(self):
		return self.car_list