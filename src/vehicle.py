class Vehicle:
	# Include a surcharge optionally	
	def __init__(self, wheels, identifier, surcharge=None):
		self._wheels = wheels
		self._identifier = identifier
		self._surcharge = surcharge

	@property
	def wheels(self):
		return self._wheels

	@property
	def identifier(self):
		return self._identifier

	@property
	def surcharge(self):
		return self._surcharge
