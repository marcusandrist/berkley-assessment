import unittest
from src.parking_lot import ParkingLot

PARKING_LOT_SIZE = 100

class TestParkingLot(unittest.TestCase):

	def setUp(self):
		self.parking_lot = ParkingLot(PARKING_LOT_SIZE)

	def test_capacity(self):
		self.assertEqual(PARKING_LOT_SIZE, 
			self.parking_lot.describe_parking_lot())

if __name__ == '__main__':
	unittest.main()
