import unittest
from unittest.mock import Mock
from src.parking_lot import ParkingLot, VEHICLE_TYPES
from src.revenue_tracker import RevenueTracker
from src.vehicle_children import Compact, Full, Truck, Motorcycle, Electric

PARKING_LOT_SIZE = 100
WHEEL_PRICE = 5

# Global vehicle fixtures (vehicle_id)-arbitrary
small_car = Compact(4) 
sedan = Full(88)
f150 = Truck(97)
dirtbike = Motorcycle(111)
elons_tesla = Electric(1)
# Mocked global vehicle fixture
mock_repr = Mock()
mock_repr.__repr__ = Mock(return_value="Invalid vehicle type")


class TestParkingLot(unittest.TestCase):

	def setUp(self):
		self.parking_lot = ParkingLot(PARKING_LOT_SIZE)

	def test_capacity(self):
		# Ask the parking lot if there's room for any more cars,
		# case: open parking lot
		self.assertEqual(True,
			self.parking_lot[0])
		# case: one parking spot left
		self.assertEqual(True,
			self.parking_lot[PARKING_LOT_SIZE-1])
		# case: full lot
		self.assertEqual(False,
			self.parking_lot[PARKING_LOT_SIZE])

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
		
	def test_revenue_key(self):
		# case: vehicle type doesn't exist
		with self.assertRaises(KeyError):
			self.revenue_tracker.pay(mock_repr)
		
		
	def test_vehicle_type_revenue(self):
		# Initialize revenue_tracker
		self.setUp()
		# case: compact revenue
		
		# case: full size revenue
		# case: truck revenue
		# case: motorcycle revenue
		# case: electric revenue

if __name__ == '__main__':
	unittest.main()
