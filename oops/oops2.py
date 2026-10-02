#single level inheritance

class Car:
     color="Green"
     @staticmethod
     def start():
        print("Car started..")
   
     @staticmethod
     def stop():
        print("Car stoped..")

class Toyotacar(Car):
     def __init__(self,name):
         self.name=name

c1=Toyotacar("Fortuner")
c2=Toyotacar("Ceira")

print(c1.name)
