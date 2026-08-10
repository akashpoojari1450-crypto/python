#it is used to pass name+value
def fun(**kwargs):
    print(kwargs)
fun(name="Akash",age=20,city="Koppa")    


#for both
def fun(*args,**kwargs):
    print(args)
    print(kwargs)
fun("maths","science",age=20,name="akash")    