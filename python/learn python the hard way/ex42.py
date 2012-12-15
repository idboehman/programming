# Exercise 42: Is-a, Has-a

## Animal is-a object
class Animal(object):
        pass

# A Dog is-a Animal 
class Dog(Animal):
        def __init__(self, name):
                # A Dog has-a name
                self.name = name

# A Cat is-a Animal
class Cat(Animal)
    def __init__(self, name):
            # A Cat has-a name
            self.name = name

# A Person is-a object
class Person(object):
        def __init__(self, name):
                # A Person has-a name
                self.name = name
                # A Person has-a pet of some kind
                self.pet = None

# A Employeed is-a Person
class Employee(Person):
        def __init__(self, name, salary):
                # A Employee is-a Person, has-a name
                super(Employee, self).__init__(name)
                # A Employee has-a salary
                self.salary = salary

# A Fish is-a object
class Fish(object):
        pass

# A Salmon is-a Fish
class Salmon(Fish):
        pass

# A Halibut is-a Fish
class Halibut(Fish):
        pass

# rover is-a Dog
rover = Dog('Rover')

# satan is-a Cat
satan = Cat('Satan')

# mary is-a Person
mary = Person('Mary')

# mary has-a pet, satan
mary.pet = satan

# frank is-a Employee w/ salary 120000
frank = Employee('Frank', 120000)

# frank has-a pet, rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon, is-a Fish
crouse = Salmon()

# harry is-a Halibut, is-a Fish
harry = Halibut()
