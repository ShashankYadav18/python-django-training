# oops

student1 = {"name":"rohan", "age":"17", "course":"MERN"}
student2 = {"name":"Amit", "age":"18", "course":"MERN"}
student3 = {"name":"Sahil", "age":"97", "course":"MERN"}
student4 = {"name":"nidhi", "age":"20", "course":"MERN"}


class Student:
    
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
        
        
s1 = Student("rohan",17,"MERN")
s2 = Student("Amit",18,"MERN")
s3 = Student("Sahil",19,"MERN")
s4 = Student("nidhi",20,"MERN")
print(s1)
print(s1.name)
print(s1.age)
print(s1.course)

# type of variable: class and instance variable

# inheritance

class father:
    def __init__(self):
        self.property="2 flat noida mein"
class mother(father):
    def __init__(self):
        self.nature="caring and polite"
class child(mother, father):
    def __init__(self):
        self.goal="still searching for a goal"
        
c1 = child()
c1.location()

# encapsulation

class BankAccount:
    def __init__(self,name, balance, pin):
        self.AccountHolderName = name
        self.__balance = balance
        self.__pin = pin
        
    def __str__(self):
        return f"Account Holder Name:{self.AccountHolderName}"
    
b1 = BankAccount("Ramesh",50000)

print(b1.balance)




# class object attributes methods variable-> class/instance  core principle -> inheritance