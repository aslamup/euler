import math
def is_prime(number):
        if number<=1:
            return False 
        if number==2:
            return True
        if number%2==0:
            return False
        for i in range(3,int(math.sqrt(number))+1):
            if number%i==0:
                return False
        return True

def sum_prime(n):
    x = 2
    s=[]
    while x<n:
        if is_prime(x) == True:
	    s.append(x)
	    x=x+1
	else:
	    x=x+1
    return sum(s)


print sum_prime(2000)
