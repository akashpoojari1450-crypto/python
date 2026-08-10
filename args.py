#normally in function it has fixed number of arg
def add(a,b):
    return a+b
print(add(2,3))    

#we use *args to add multiple arguments
def add(*args):
    return args
print(add(8,9,7,6))    #it reurns in tuple ,so we use loops

def add(*args):
     total=0
     for num in args:
        total=total+num
     return total
print(add(8,9,7,6))     

#or
def add(*args):
    return sum(args)
print(add(8,9,7,6))    