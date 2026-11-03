def greet():
    print("hello, world!")
greet()    

def personalized_greeting(name):
    print("hello, " + name + "!")
personalized_greeting("thabo")

def square(number):
    return number * number

print(square(5))

def rectangle_area(length, width):
    return length * width
print(rectangle_area(4, 5))

def apply_operation(func, number):
    return func(number)
def double(number):
    return number * 2
print (apply_operation(double, 7))
print(apply_operation(square, 3))