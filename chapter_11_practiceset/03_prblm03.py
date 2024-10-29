class Employee:
    salary = 234
    increment = 20
    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment= ((salary/self.salary)-1)*100

r = Employee()
# print(r.salaryafterincrement)
r.salaryafterincrement = 280.8
print(r.increment)
    