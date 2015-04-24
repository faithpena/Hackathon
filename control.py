from gas import*
from data import*
from car import*

class Control:
	def __init__(self):
		self.car_list = {}
	def get_car_data(self):
		return self.get_car_list
	def create_car(self, car_data):
		car = Car()
		car.set_input(car_data)
		self.car_list[car.get_name] = car
	def get_cars(self):
		return self.car_list