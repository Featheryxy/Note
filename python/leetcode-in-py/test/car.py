class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model 
		self.year = year 
		self.odometer_reading = 0
	
	def get_dec(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_od(self):
		print("This car has " + str(self.odometer_reading )+' miles on in')
	
	def update_odometer(self, mileage):
		self.odometer_reading = mileage
	
		
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_dec())

# 直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_od()

# 通过方法修改属性的值
my_new_car.update_odometer(46)
my_new_car.read_od()

