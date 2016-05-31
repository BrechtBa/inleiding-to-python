class IdealGas(object):
	"""
	A class defining an ideal gas
	"""
	def __init__(self,name,R):
		"""
		Returns a Gas Instance
		
		Parameters:
		name: string, name of the gas
		R: float, specific gas constant
		"""
		self.name = name
		self.R = R
	
	def __str__(self):
		return '{}, R={} J/kgK'.format(self.name,self.R)
		
	def density(self,P,T):
		"""
		Returns the density of the gas in kg/m3
		
		Parameters:
		P: float, pressure in Pa
		T: float, Temperature in K
		"""
		return P/self.R/T
				
if __name__ == '__main__':
	help(IdealGas.density)

	a = IdealGas('air',287)	
	print(a)
	print('rho = {:.3f} kg/m3'.format(a.density(101325,293.15)))