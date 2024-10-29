class Programmer:
    def __init__ (self,name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

a = Programmer("Ayush",2000000,400615)
b = Programmer("Jassuh",2000000,400602)
print(a.name,a.salary,a.pin)
print(b.name,b.salary,b.pin)