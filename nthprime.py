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

def term(n):
    x = 0
    count = 0
    while count != n:
        x = x + 1
        if is_prime(x) == True:
            count = count + 1
    return x


print term(1000)
