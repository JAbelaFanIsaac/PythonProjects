import math

#function
def f(x):
    function = math.pow(x,3)+math.pow(x,2)
    return function
print("func", f(10))

#trapezium rule
def trapezium(fun,a,b,n):
    height = (b-a)/n
    total = (fun(a)+fun(b))/2
    for i in range(n-2):
        point = fun(a+height*(i+1))
        total += point
    total = (b-a)*total
    return total

print("error", abs(8500/3-trapezium(f, 0, 10, 2)))

def simpson(fun,a,b,n):
    dx = (b-a)/(n-1)
    total = 0
    for i in range(n):
        print(i)
        if i == 0:
            total+=fun(a)
        if i == (n-1):
            total += fun(b)
            total = dx*total/3
            return total
        elif i % 2 == 1:
            total += fun(a+dx*i)*4
        elif i % 2 == 0:
            total += fun(a+dx*i)*2

print(simpson(f,0,10,3))

def gauss_quad(f,w,a,b):
    x1 = (1/2)*((a+b)-(b-a)/(3**(1/2)))
    x2 = (1/2)*((a+b)+(b-a)/(3**(1/2)))
    total = (f(x1) + f(x2))*(b-a)*w
    return total
print(gauss_quad(f,0.5, 0,10))
