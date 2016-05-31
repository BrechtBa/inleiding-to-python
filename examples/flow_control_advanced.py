# dictionaries
A = {'foo': 'bar',
     'spam': 'eggs',
	 'bacon': 'spam'}

for key in A:
	print('{}: {}'.format(key,A[key]))

for key,val in A.iteritems():
	print('{}: {}'.format(key,val))

# enumerate
B = [1,11,111,1111]
for i,b in enumerate(B):
	print('B[{}] = {}'.format(i,b))	
	
# zip
C = [1,2,3]
D = [7,8,9]
for c,d in zip(C,D):
	print('c = {:.0f}, d = {:.3f}'.format(c,d))
		
