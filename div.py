import sys
def smallestDiv(n):
    divisors = [x for x in range(1,(n+1))]
    for i in xrange(2520,sys.maxint,n):
        if(all(i%x == 0 for x in divisors)):
            return i

print (smallestDiv(20))
