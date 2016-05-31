from object_oriented import IdealGas

class PerfectGas(IdealGas):
	"""
	A class defining a perfect gas as an ideal gas with constant cp
	"""
	def __init__(self,name,R,cp):
		"""
		Returns a PerfectGas Instance
		
		Parameters:
		R: float, specific gas constant
		cp: float, heat capacity at constant pressure
		"""
		IdealGas.__init__(self,name,R)
		self.cp = cp
		self.cv = self.cp-self.R
		
	def __str__(self):
		return super(PerfectGas,self).__str__() + ', cp={} J/kgK'.format(self.cp)
		
	def du(self,dT):
		"""
		Returns the change in specific energy of the gas in J/kg
		
		Parameters:
		dT: float, temperature difference in K
		"""
		return self.cv*dT
		
	
if __name__ == '__main__':

	a = IdealGas('air',287)
	b = PerfectGas('air',287,1004)

	print(a)
	print(b)
	
	print('rho = {:.3f} kg/m3'.format(a.density(101325,293.15)))
	print('rho = {:.3f} kg/m3'.format(b.density(101325,293.15)))
	
	print('du = {:.2f} J/kg'.format(b.du(50)))