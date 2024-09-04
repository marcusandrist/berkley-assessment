from src.vehicle_children import Compact, Full, Truck, Motorcycle, Electric
from src.revenue_tracker import RevenueTracker

WHEEL_PRICE = 5.00

VEHICLE_TYPES = {"Compact": Compact,
				 "Full": Full,	
				 "Truck": Truck, 
				 "Motorcycle": Motorcycle, 
				 "Electric": Electric}

class ParkingLot:

	# Assume if vehicles are in the lot, they paid
	def __init__(self, maximum_capacity: int, vehicles: list=[]):
		self.maximum_capacity = maximum_capacity
		self.vehicles = vehicles
		self.revenue = RevenueTracker(WHEEL_PRICE, VEHICLE_TYPES)
	
	# Quick falsey check method for once parking lot is full
	def __getitem__(self, total_vehicles) -> bool:
		return total_vehicles < self.maximum_capacity

	def describe_parking_lot(self) -> int:
		return self.maximum_capacity

	# Could be implemented much better with a db/json/sqlite
	def park_vehicle(self, vehicle):
		# Check that vehicle type and parking space exists
		if vehicle not in VEHICLE_TYPES.keys():
			raise KeyError(f"Vehicle Type: {vehicle} not found")
		if not self[len(self.vehicles.values())]:
			raise RuntimeError("Parking lot is full")
		# Store payment i+ add vehicle to parking lot at AUTO-INCREMENT
		self.revenue.pay(vehicle)
		new_id = max(self.vehicles.keys(), default = 0) + 4
		self.vehicles.update({new_id: vehicle})

	def unpark_vehicle(self, vehicle_id):
		try:
			vehicle = self.vehicles.pop(vehicle_id)
		except KeyError as e:
			print(f"Vehicle ID: {vehicle_id} not found")

		return vehicle

	def __repr__(self):
		return f"0/{self.maximum_capacity} vehicles in the lot\n\
				e"
