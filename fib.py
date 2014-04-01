def fib(n):
	f,s=0,1
	c=[]
	d=[]
	c.append(f)
	while(s<n):
		c.append(s)
		f,s=s,f+s
	for i in c:
		if i%2==0:
			d.append(i)
	return sum(d)
print fib(4000000)
