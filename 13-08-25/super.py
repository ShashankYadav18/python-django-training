# super() keyword

class parent:
    
    def __init__(self,name):
        self.name = name
        print("parent __init__called")
        
class child(parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print("child __init__ called")
        
obj = child("rahul",55)
        
