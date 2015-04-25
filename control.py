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
		self.gas_list = self.create_gas_list()
		#print self.gas_list.keys()
	def set_car_data(self, name, cylinder, mpg, hp, weight, engine):
		data = {}
		data['name'] = name
		data['cylinder'] = int(cylinder)
		data['mpg'] = int(mpg)
		data['hp'] = int(hp)
		data['weight'] = int(weight)
		data['engine'] = engine
		self.car_data = data
		#print self.car_data
		self.create_car()
	def set_dist_data(self, car_name, dist, luggage, gasType):
		data = {}
		data['car name'] = car_name
		data['distance'] = int(dist)
		data['luggage'] = int(luggage)
		data['gas_type'] = gasType
		self.dist_data = data
		return data
	def set_budget_data(self, car_name, money, luggage, gasType):
		data = {}
		data['car name'] = car_name
		data['money'] = int(money)
		data['luggage'] = int(luggage)
		data['gas_type'] = gasType
		self.budget_data = data
		return data
	def get_car_data(self):
		return self.get_car_list
	def create_car(self):
		car = Car()
		car.set_input(self.car_data)
		self.car_list[car.get_name()] = car
	def create_gas_list(self):
		gas_list = {}
		gas = Gas()
		gas.set('Gasoline', 15)
		gas_list['Gasoline'] = gas
		gas.set('Diesel', 16)
		gas_list['Diesel'] = gas
		gas.set('Petrol', 17)
		gas_list['Petrol'] = gas
		gas.set('Compressed Natural Gas', 18)
		gas_list['Compressed Natural Gas'] = gas
		gas.set('Ethanol', 19)
		gas_list['Ethanol'] = gas
		return gas_list
	def get_cars(self):
		return self.car_list.keys()
	def compute_budget(self, budget_data):
		#print budget_data
		car = self.car_list[budget_data['car name']]
		mpg = car.get_mpg()
		mpg = mpg/(1+int(budget_data['luggage']))
		kpl = mpg * 1.609344 / 3.78541178
		gas_cost = self.gas_list[budget_data['gas_type']].get_cost()
		money = int(budget_data['money'])
		gas_amt = money/gas_cost
		distance = kpl*gas_amt
		output = {'Liters': gas_amt, 'Distance': distance}
		#print output
		return output
	def compute_distance(self, dist_data):
		#print dist_data
		car = self.car_list[dist_data['car name']]
		mpg = car.get_mpg()
		mpg = mpg/(1.0+float(dist_data['luggage']))
		kpl = mpg * 1.609344 / 3.78541178
		gas_cost = self.gas_list[dist_data['gas_type']].get_cost()
		distance = self.dist_data['distance']
		gas_amt = distance/kpl
		money = gas_cost*gas_amt
		output = {'Liters': gas_amt, 'Cost': money}
		#print output
		return output