class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def Display(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,roll_no,total):
        super().__init__(name,age)
        self.roll_no=roll_no
        self.total=total

    def Display(self):
        super().Display()
        print(self.roll_no,self.total)

class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary


    def Display(self):
        print(self.salary,self.name,self.age)



    

s0=Student('Tejas',18,0,150)
s1=Employee('',23,52000)

s0.Display()
s1.Display()