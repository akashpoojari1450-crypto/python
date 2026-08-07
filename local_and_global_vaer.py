#local variable
def hi():
    msg="hello"
    print(msg)
hi()    
#global variable
a=input("Enter:")
def n():
    print("inside",a)
n()
print("outside",a)    

#example
def a():
    s="me too"
    print(s)
s="HI"
a()
print(s)    

    