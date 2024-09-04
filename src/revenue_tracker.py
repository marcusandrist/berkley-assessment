class RevenueTracker:
	def __init__(self, wheel_price, vehicle_types):
		self.wheel_price = wheel_price
		self.vehicle_types = list(vehicle_types.keys())
		self.revenue_statistics = {vehicle: 0 for vehicle in self.vehicle_types}

	@staticmethod
	def calculate_payment(wheel_price, vehicle):
		surcharge = vehicle.surcharge
		flat_rate = wheel_price * vehicle.wheels
		return (surcharge if surcharge is not None else 0) + flat_rate

	def pay(self, vehicle):
		if repr(vehicle) not in self.vehicle_types:
			raise KeyError("Vehicle type not found.")
		payment = self.calculate_payment(self.wheel_price, vehicle)
		self.revenue_statistics[repr(vehicle)] += payment

	# Total revenue
	def __repr__(self):
		return str(sum(self.revenue_statistics.values()))
