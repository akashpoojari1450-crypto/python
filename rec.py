def rec(x):
    if x%2==0:
        return "even"
    else:
        return "odd"
rec(17)        
print(rec(17))

#factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
factorial(3)
print(factorial(3))

#recursion types:tail and no tails recursion
def tail(n,a=1):
    if n==0:
        return a
    else:
        return tail(n-1,a*n)
def non_tail(n):
    if n==0:
        return 1
    else:
        return n*non_tail(n-1)

print(tail(3))
print(non_tail(3))            