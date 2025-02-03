import math
import random

#Monte Carlo
def intergrte(f,a,b,n):
    ans = 0
    for i in range(n):
        x = random.uniform(-a,a)
        y = random.uniform(-b,b)
        ans += f(x,y)

    ans = (4*a*b)*ans/n
    return ans

def function1(x,y):
    return math.exp(x*y)*math.sin(x**2)*(math.cos(y)**2)


print(intergrte(function1, 1, 1, 10**2))
print(intergrte(function1, 1, 1, 10**5))
print(intergrte(function1, 1, 1, 10**6))

def function2(x,y):
    if x**2 + y**2 <= 1:
        return 1
    else:
        return 0

print(intergrte(function2, 1, 1, 10**2))
print(intergrte(function2, 1, 1, 10**5))
print(intergrte(function2, 1, 1, 10**6))
