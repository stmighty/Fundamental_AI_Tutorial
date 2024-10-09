class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def calculate_age(self, number_of_pass_year) :
      return self.age + number_of_pass_year

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(p1.calculate_age(10))