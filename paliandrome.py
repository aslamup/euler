def paliandrom():
	a=[]
	for i in range(100,1000):
		for j in range(100,1000):
			k=i*j
			if str(k) == str(k)[::-1]:
				a.append[[k,i,j]]
	return max(a)
print paliandrom()
