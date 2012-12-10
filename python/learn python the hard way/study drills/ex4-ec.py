# Exercise 4: Variables And Names
# number of cars available for carpool
cars = 100
# number of people a car can hold
space_in_a_car = 4
# number of available drivers for the car pool
drivers = 30
# number of passengers for the car pool
passengers = 90
# cars not utilized by the car pool
cars_not_driven = cars - drivers
# number of cars that will be driven for car pool
cars_driven = drivers

# number of passengers the carpool can handle
carpool_capacity = cars_driven * space_in_a_car
# average number of passengers in each car driven in car pool
average_passengers_per_car = passengers / cars_driven

print 'There are', cars, 'cars available.'
print 'There are only', drivers, 'drivers available.'
print 'There will be', cars_not_driven, 'empty cars today.'
print 'We can transport', carpool_capacity, 'people today.'
print 'We have', passengers, 'to carpool today.'
print 'We need to put about', average_passengers_per_car, 'in each car.'

""" Study Drills
1. Not necessary, results do not change significantly using int 4.
2. Floating points are a method of representing real numbers and can be thought of as a computer's way of using scientific notation. It cannot precisely represent all real numbers and true arithmetic operations. A way of representing irrational numbers in a computer.
3. See above
4. = assigns the the variable name to the value.
5. Understood.
"""
