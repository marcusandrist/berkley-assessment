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
	def __init__(self, maximum_capacity: int, vehicles: dict={}):
		self.maximum_capacity = maximum_capacity
		self.vehicles = vehicles
		self.revenue = RevenueTracker(WHEEL_PRICE, VEHICLE_TYPES)
	
	# Quick falsey check method for once parking lot is full
	def __getitem__(self, total_vehicles) -> bool:
		return total_vehicles < self.maximum_capacity

	# Would implement with a sqlite or db w/ ACID-compliance in prod
	def park_vehicle(self, vehicle_type):
		# Check that vehicle type and parking space exists
		if vehicle_type not in VEHICLE_TYPES.keys():
			raise KeyError(f"Vehicle Type: {vehicle_type} not found")
		if not self[len(self.vehicles.values())]:
			raise RuntimeError("Parking lot is full")
		# Add vehicle to parking lot at AUTO-INCREMENT
		new_id = max(self.vehicles.keys(), default = 0) + 4
		# Create vehicle, pay for parking, and add to parking lot
		new_vehicle = VEHICLE_TYPES[vehicle_type](new_id)
		self.revenue.pay(new_vehicle)
		self.vehicles.update({new_id: new_vehicle})

	def unpark_vehicle(self, vehicle_id):
		try:
			vehicle = self.vehicles.pop(vehicle_id)
		except KeyError as e:
			return (f"Vehicle ID: {vehicle_id} not found")

	def list_vehicles(self):
		vehicle_list = []
		for vehicle in self.vehicles.values():
			vehicle_list.append(vehicle)
		return vehicle_list

	def list_vehicles_by_type(self):
		vehicle_list = self.list_vehicles()
		sorted_vehicles = sorted(vehicle_list, key=repr)
		return sorted_vehicles

	def list_vehicles_by_identifier(self):
		vehicle_list = self.list_vehicles()
		vehicle_list.sort(key=lambda vehicle: vehicle.identifier)
		return vehicle_list
