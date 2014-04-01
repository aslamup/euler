n = 13195
l=[]
for i in range(2,n):
	if (n%i ==0):
        	l.append(i)
            	n = n/i
            	i = i -1
		x=l[len(l)-1]
print x
