class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population

p1 = Person("Alice")
p2 = Person("Bob")
print(Person.get_population())  # Output: 2
