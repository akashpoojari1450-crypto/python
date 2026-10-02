def fun():
    print("hi")
fun()    

#function arguments
def evenodd(a):
    if(a%2==0):
        return "even"
    else:
        return "odd"
print(evenodd(9))
print(evenodd(10))


def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"
x=int(input("Eneter number:"))
print(evenOdd(x))

#anotehr example
def nam(name,age):
    print("Hi,I am",name)
    print("My age is",age,"year")
print("Case 1:")
nam("Akash",20)
print("Case 2:")
nam(28,"Hi")    

#pass by value and pass by reference
def myfun(x):
    x[0]=20
b=[10,11,12,13]
myfun(b)
print(b)
def myfun2(x):
    x=30
a=33
myfun2(a)
print(a)


