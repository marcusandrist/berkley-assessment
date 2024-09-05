import unittest
import random
from unittest.mock import Mock
from src.parking_lot import ParkingLot, VEHICLE_TYPES
from src.revenue_tracker import RevenueTracker
from src.vehicle_children import Compact, Full, Truck, Motorcycle, Electric
from src.vehicle import Vehicle

PARKING_LOT_SIZE = 100
WHEEL_PRICE = 5

class TestParkingLot(unittest.TestCase):

	def setUp(self, vehicles=None):
		self.parking_lot = ParkingLot(PARKING_LOT_SIZE, vehicles)
		if vehicles is None:
			self.parking_lot.vehicles = {}
	
	# Helper method for parking random cars
	def park_n_random_vehicles(self, n):
		vehicle_selections = []
		for i in range(n):
			random_vehicle = random.choice(list(VEHICLE_TYPES.keys()))
			self.parking_lot.park_vehicle(random_vehicle)
			vehicle_selections.append(random_vehicle)
		return vehicle_selections

	# Ask the parking lot if there's room for any more cars
	def test_capacity(self):
		# case: open parking lot
		self.assertEqual(True,
			self.parking_lot[0])
		# case: one parking spot left
		self.assertEqual(True,
			self.parking_lot[PARKING_LOT_SIZE-1])
		# case: full lot
		self.assertEqual(False,
			self.parking_lot[PARKING_LOT_SIZE])

	def test_park_vehicle(self):
		# case: one vehicle
		self.parking_lot.park_vehicle("Motorcycle")
		self.assertEqual(4, self.parking_lot.vehicles[4].identifier) 
		self.assertEqual(2, self.parking_lot.vehicles[4].wheels)
		# case: full lot
		self.setUp()
		[self.parking_lot.park_vehicle("Truck") for i in range(100)]
		with self.assertRaises(RuntimeError):
			self.parking_lot.park_vehicle("Electric")
		# case: KeyError (vehicle_type invalid)
		with self.assertRaises(KeyError):
			self.parking_lot.park_vehicle("full")

	def test_unpark_vehicle(self):
		# case: unpark one vehicle
		self.setUp()
		self.parking_lot.park_vehicle("Motorcycle")
		# ID will become 4 for initial vehicle in lot
		self.parking_lot.unpark_vehicle(4)
		self.assertEqual({}, self.parking_lot.vehicles)
		# case: unpark the last vehicle
		[self.parking_lot.park_vehicle("Motorcycle") for i in range(100)]
		self.parking_lot.unpark_vehicle(400)
		self.assertEqual(99, len(self.parking_lot.vehicles))
		# case: unpark a vehicle that doesn't exist
		self.assertEqual("Vehicle ID: 9999 not found",
			self.parking_lot.unpark_vehicle(9999))
	
	def test_list_vehicles(self):
		# case: empty lot
		self.setUp()
		self.assertEqual([], self.parking_lot.list_vehicles())
		# case: full lot
		[self.parking_lot.park_vehicle("Truck") for i in range(100)]
		self.assertEqual(100, len(self.parking_lot.list_vehicles()))

	def test_list_vehicles_by_type(self):
		# case: 10 random vehicles
		self.setUp()
		vehicle_selections = self.park_n_random_vehicles(10)
		vehicle_selections.sort()
		vehicle_list = []
		test_parking_lot = ParkingLot(PARKING_LOT_SIZE)
		# take sorted list of random vehicle and instantiate in order
		for i in vehicle_selections:
			test_parking_lot.park_vehicle(i)
		assert all(repr(test_vehicle) == repr(vehicle) for test_vehicle,
			vehicle in zip(test_parking_lot.list_vehicles(), 
			self.parking_lot.list_vehicles_by_type()))
		#self.assertEqual(test_parking_lot.list_vehicles(),
		#	self.parking_lot.list_vehicles_by_type())

	def test_list_vehicles_by_identifier(self):
		# case: empty lot
		self.setUp()
		self.park_n_random_vehicles(100)
		original_vehicles = self.parking_lot.vehicles
		shuffled_vehicles_list = list(original_vehicles.items())
		random.shuffle(shuffled_vehicles_list)
		shuffled_vehicles = dict(shuffled_vehicles_list)
		# instantiate a new lot with vehicles randomized
		self.setUp(vehicles=shuffled_vehicles)
		sorted_vehicles = self.parking_lot.list_vehicles_by_identifier()
		sorted_vehicles_identifiers = [vehicle.identifier for vehicle in 
			sorted_vehicles]
		self.assertEqual(list(range(4, 404, 4)), sorted_vehicles_identifiers)

class TestVehicle(unittest.TestCase):
	
	def setUp(self):
		self.vehicle = Vehicle(18, 22, 2.00)

	# case: internally retrieve identifier	
	def test_identifier(self):
		self.assertEqual(22, self.vehicle.identifier)

	# case. calculate cost via object properties	
	def test_cost(self):
		self.assertEqual(92, self.vehicle.wheels * 5 + \
			self.vehicle.surcharge)

# Vehicle fixtures (vehicle_id)
small_car = Compact(4) 
sedan = Full(88)
f150 = Truck(97)
dirtbike = Motorcycle(11)
elons_tesla = Electric(1)
# Mocked global vehicle fixture
mock_repr = Mock()
mock_repr.__repr__ = Mock(return_value="An invalid vehicle type")

class TestRevenueTracker(unittest.TestCase):
		
	def setUp(self):
		self.revenue_tracker = RevenueTracker(WHEEL_PRICE, VEHICLE_TYPES)

	def test_total_revenue(self):
		# case: total revenue (double-cast for __repr__)
		self.revenue_tracker.pay(small_car)
		self.revenue_tracker.pay(sedan)
		self.revenue_tracker.pay(f150)
		self.revenue_tracker.pay(dirtbike)
		self.revenue_tracker.pay(elons_tesla)
		self.assertEqual(96.0,
			float(str(self.revenue_tracker)))
		
	def test_revenue_key_error(self):
		# case: vehicle type doesn't exist
		with self.assertRaises(KeyError):
			self.revenue_tracker.pay(mock_repr)

	def test_revenue_statistics(self):
		# case: Init state
		self.setUp()
		self.assertEqual({"Compact": 0, "Full": 0, "Truck": 0,
			"Motorcycle": 0, "Electric": 0}, 
			self.revenue_tracker.revenue_statistics)

		# case: 2 motorcycles, 1 electric i.e. (2*5*2 + 4*5 + 1*1)
		self.setUp()
		[self.revenue_tracker.pay(dirtbike) for i in range(2)]
		self.revenue_tracker.pay(elons_tesla)
		self.assertEqual({"Compact": 0, "Full": 0, "Truck": 0,
			"Motorcycle": 20.00, "Electric": 21.00}, 
			self.revenue_tracker.revenue_statistics)
		
		# case: 1 full, 1 compact, 2 trucks
		self.setUp()
		self.revenue_tracker.pay(sedan)
		self.revenue_tracker.pay(small_car)
		[self.revenue_tracker.pay(f150) for i in range(2)]
		self.assertEqual({"Compact": 20.00, "Full": 22.00, "Truck": 46.00,
			"Motorcycle": 0, "Electric": 0}, 
			self.revenue_tracker.revenue_statistics)

		# case: full lot (100 capacity) with vehicles in this order: compact,
		# full, truck, motorcycle, electric, respectively.
		# 11, 22, 44, 13, 10
		self.setUp()
		[self.revenue_tracker.pay(small_car) for i in range(11)]
		[self.revenue_tracker.pay(sedan) for i in range(22)]
		[self.revenue_tracker.pay(f150) for i in range(44)]
		[self.revenue_tracker.pay(dirtbike) for i in range(13)]
		[self.revenue_tracker.pay(elons_tesla) for i in range(10)]
		self.assertEqual({"Compact": 220.00, "Full": 484.00, "Truck": 1012.00,
			"Motorcycle": 130.00, "Electric": 210.00}, 
			self.revenue_tracker.revenue_statistics)

if __name__ == '__main__':
	unittest.main()
