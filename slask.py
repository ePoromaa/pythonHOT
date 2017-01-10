#a better solution in python

#generate binary nos



def binary(i):
	s=' '
	print s
	while i>0:
		s = s+ str(i%2)
		i=i/2
	while len(s) < i:
		s = 0 + s
	return s[::-1]


n=int(raw_input())
for i in range(1,n+1):
	print binary(i),