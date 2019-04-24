""""
#Average Function
def average(a=10,b=20):
    print(a)
    print(b)
    return (a+b)/2
print(average(a=30))
"""

#calculator
def calc(a,b):
    x=a+b
    y=a-b
    z=a*b
    u=a/b
    return x,y,z,u

result = calc(10,5)
print("calculator" + str(result))
for i in result:print(i)

#Factorial
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result

print(factorial(3))

