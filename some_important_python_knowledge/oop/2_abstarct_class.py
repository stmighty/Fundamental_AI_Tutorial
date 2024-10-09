from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__ (self) :
      pass
  
  def test() :
      print("test function")
      
  @abstractmethod
  def speak(self):
    pass



class Dog(Animal):
  def __init__ (self) :
      pass
  
  def speak(self):
    print("Woof")



class Cat(Animal):
  def __init__ (self) :
      pass

  def speak(self):
    print("Meow")  
    
    
class Horse(Animal) :
    def __init__() :
        pass
    
    def test() :
        print("this is a test function")
    

    
    
    
    
    

cat = Cat()
cat.speak()
print()

try :
    animal = Animal()
    print(animal.test())
except :
    print("you cannot initialize class with abstarct method.")
    
try :
    horse = Horse()
except : 
    print("you cannot initialize class without defining abstract method.")


    