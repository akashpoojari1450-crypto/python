#lamda functionn is used when logic is simple, it does have function
a=lambda x:x*2
print(a(5))

#map is used when we want to apply a function to a lambda
n=[2,3,6,7,8,9]
a=map(lambda x:x**2,n)
print(list(a))

#filter is used when we want to filter the data based on some condition
n=[2,3,6,7,8,9]
a=filter(lambda x:x%2==0,n )
print(list(a))

#reduce is used when we want to reduce the data to a single value
from functools import reduce
n=[2,3,6,7,8,9]
a=reduce(lambda x,y:x+y,n)
print(a)