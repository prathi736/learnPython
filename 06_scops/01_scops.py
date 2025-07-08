# Closures in python : Very Important (Also in other programming languages like JavaScript)

def chai(num):
    def actual(x):
        return x ** num
    return actual 

f = chai(2)
g = chai(3)

print(f) # return actual function and memory reference of variables used in this actual function (bag pack hokar aata hai)
print(g)

print(f(3))
print(g(3))