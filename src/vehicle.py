class Vehicle:
	# Include a surcharge optionally, no name-mangling/private for prototype
	def __init__(self, wheels, identifier, surcharge=None):
		self._identifier = identifier
		self._wheels = wheels
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
