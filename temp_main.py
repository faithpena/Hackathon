from control import*

def main():
	control = Control()
	data = {'name': 'Family Car', 'weight': 100, 'hp': 120, 'cylinder': 4, 'torque': 10, 'engine': 2}
	control.create_car(data)
	cars = control.get_cars()
	print cars[0].get_name, cars[0].get_weight