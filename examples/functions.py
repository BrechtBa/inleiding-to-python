def spam(A,B,C=0,D=0):
	val = 100*A+10*B+C+0.1*D
	return val
	
A = spam(4,1)
print(A)

B = spam(4,1,5.3)
print(B)

C = spam(4,1,D=3,C=5)
print(C)
print(val)
