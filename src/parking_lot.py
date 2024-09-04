class ParkingLot:
	
	def __init__(self, maximum_capacity: int):
		self.maximum_capacity = maximum_capacity

	def describe_parking_lot(self) -> int:
		return self.maximum_capacity

if __name__ == '__main__':
	main = ParkingLot(100)
	print(main.describe_parking_lot())
