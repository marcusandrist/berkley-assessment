from src.vehicle import Vehicle

class Compact(Vehicle):
	def __init__(self, identifier):
		super().__init__(4, identifier)

	def __repr__(self):
		return "Compact"

class Full(Vehicle):
	# Optional kwarg in case parking lot wants to change surcharge $ rate
	def __init__(self, identifier, surcharge=2.00):
		super().__init__(4, identifier, surcharge)

	def __repr__(self):
		return "Full"

class Truck(Vehicle):
	# Vehicles wheel count should be constant!
	def __init__(self, identifier, surcharge=3.00):
		super().__init__(4, identifier, surcharge)

	def __repr__(self):
		return "Truck"

class Motorcycle(Vehicle):
	def __init__(self, identifier):
		super().__init__(2, identifier)

	def __repr__(self):
		return "Motorcycle"

class Electric(Vehicle):
	def __init__(self, identifier, surcharge=1.00):
		super().__init__(4, identifier, surcharge)

	def __repr__(self):
		return "Electric"
