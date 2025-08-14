# polymorphism

class animal:
    
    def speak(self):
        return "animal speaks"
        
        
class dog: 
    
    def speak(self):
        return "woof"
class cat: 
    
    def speak(self):
        return "meow"
    
animal = [dog(), cat()]
for i in animal:
    print(i.speak())
    
##dogesh1 =  dog()
#print (dogesh1.speak())

