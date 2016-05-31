def spam(A,B,C=0,D=0):
	"""
	returns a a number as if the arguments were different digits in the number
	
	Parameters:
	A: float, hundreds
	B: float, decades
	C: float, units
	D: float, tenths
	"""
	
	val = 100*A+10*B+C+0.1*D
	return val
	
A = spam(4,1)
print(A)

B = spam(4,1,5.3)
print(B)

C = spam(4,1,D=3,C=5)
print(C)
print(val)
