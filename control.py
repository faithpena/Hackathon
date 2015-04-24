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
		self.gas_list = create_gas_list()
	def set_car_data(self, name, cylinder, mpg, hp, weight, engine):
		data = {}
		data['name'] = name
<<<<<<< HEAD
		data['cylinder'] = cylinder
		data['mpg'] = mpg
		data['hp'] = hp
		data['weight'] = weight
		data['engine'] = engine
		self.car_data = data
		print self.car_data
	def set_dist_data(self, car_name, dist, luggage, gasType):
=======
		data['cylinder'] = int(cylinder)
		data['cylinder'] = int(cylinder)
		data['torque'] = int(torque)
		data['hp'] = int(hp)
		data['weight'] = int(weight)
		data['engine'] = engine
		self.car_data = data
		print self.car_data
	def set_dist_data(self, car_name, dist, gasType):
>>>>>>> eee381f5dc93fec486cbd5c6ef468d883bf82704
		data = {}
		data['car_name'] = car_name
		data['distance'] = int(dist)
		data['luggage'] = int(luggage)
		data['gas_type'] = gasType
		self.dist_data = data
		print self.dist_data
	def set_budget_data(self, car_name, money, luggage, gasType):
		data = {}
		data['car_name'] = car_name
		data['money'] = int(money)
		data['luggage'] = int(luggage)
		data['gas_type'] = gasType
		self.budget_data = data
		print self.budget_data
	def get_car_data(self):
		return self.get_car_list
	def create_car(self):
		car = Car()
		car.set_input(self.car_data)
		self.car_list[car.get_name()] = car
	def create_gas_list(self):
		gas = Gas()
		gas.set('Gasoline', 15)
		self.gas_list['Gasoline'] = gas
		gas.set('Diesel', 16)
		self.gas_list['Diesel'] = gas
		gas.set('Petrol', 17)
		self.gas_list['Petrol'] = gas
		gas.set('Compressed Natural Gas', 18)
		self.gas_list['Compressed Natural Gas'] = gas
		gas.set('Ethenol', 19)
		self.gas_list['Ethenol'] = gas
	def get_cars(self):
<<<<<<< HEAD
		return self.car_list
	def compute_budget(self):
		car = self.car_list[self.budget_data['car_name']]
		mpg = car.get_mpg()
		mpg = mpg/(1+int(self.budget_data['luggage']))
		kpl = mpg * 1.609344 / 3.78541178
		gas_cost = self.gas_list[self.budget_data['gas_type']].get_cost()
		money = int(self.budget_data['money'])
		gas_amt = money/gas_cost
		distance = kpl*gas_amt
		output = {'Liters': gas_amt, 'Distance': distance}
		return output
	def compute_distance(self):
		car = self.car_list[self.dist_data['car_name']]
		mpg = car.get_mpg()
		mpg = mpg/(1+int(self.budget_data['luggage']))
		kpl = mpg * 1.609344 / 3.78541178
		gas_cost = self.gas_list[self.budget_data['gas_type']].get_cost()
		distance = int(self.budget_data['distance'])
		gas_amt = distance*(1/kpl)
		money = gas_cost*gas_amt
		output = {'Liters': gas_amt, 'Cost': money}
		return output
=======
		return self.car_list.keys()
>>>>>>> eee381f5dc93fec486cbd5c6ef468d883bf82704
