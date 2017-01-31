Brain Academy. Python Course.  
Presentation of class and object

1. Class and object (bicycle example)

```python 
class Bicycle:
    cadence = 0
    speed = 0
    gear = 1

    def changeCadence(self, newValue):
        self.cadence = newValue

    def changeGear(self, newValue):
        self.gear = newValue

    def speedUp(self, increment):
        self.speed = self.speed + increment

    def applyBrakes(self, decrement):
        self.speed = self.speed - decrement

    def printStates(self):
        print("cadence:%s,speed:%s,gear:%s." % (self.cadence, self.speed, self.gear))class Bicycle:
    cadence = 0
    speed = 0
    gear = 1

    def changeCadence(self, newValue):
        self.cadence = newValue

    def changeGear(self, newValue):
        self.gear = newValue

    def speedUp(self, increment):
        self.speed = self.speed + increment

    def applyBrakes(self, decrement):
        self.speed = self.speed - decrement

    def printStates(self):
        print("cadence:%s,speed:%s,gear:%s." % (self.cadence, self.speed, self.gear))
```
2. Class and object (bicycle example) 

```python 
from presentation.class_and_object_example.bicycle_class import Bicycle

# Create two different Bicycle objects
bike1 = Bicycle()
bike2 = Bicycle()

# Invoke methods on those objects
bike1.changeCadence(50)
bike1.speedUp(10)
bike1.changeGear(2)
bike1.printStates()

bike2.changeCadence(50)
bike2.speedUp(10)
bike2.changeGear(2)
bike2.changeCadence(40)
bike2.speedUp(10)
bike2.changeGear(3)
bike2.printStates()
```

Brain Academy. Python Course.  
Class_attribute_and_method

1. Capitalizator

```python 
 Capitalizator:

    # Class Capitalizator - wrapper around a file that converts output to upper-case.

    def __init__(self, f):
        self._f = f

    def read(self, count=-1):
        capitalized_content = self._f.read(count).upper()
        self._f.close()
        return capitalized_content


file_name = 'text.txt'
file_path = cur_package_path() + 'files/' + file_name

file = open(file_path, 'r')
print('\n\tOpened with common file object:', file.read())
file.close()

capitalizator = open_file(file_path)
print('\n\tOpened with Capitalizator instance:', capitalizator.read())
```

2. Class_build_in_attributes

```python 
from presentation.class_attribute_and_method.students import Student

print('Student.__doc__:', Student.__doc__)
print('Student.__name__:', Student.__name__)
print('Student.__module__:', Student.__module__)
print('Student.__bases__:', Student.__bases__)

print('Student.__dict__:')
for element in Student.__dict__:
    print('\t', element)
```
3. Encapsulation

```python 
class Student:
    def __init__(self, name):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __step(self):
        print("%s make step." % self.__name)

    def going_home(self):
        self.__step()

    name = property(get_name, set_name)


student = Student('Bob')

try:
    print(student.__name)  # accessing a private attribute
except AttributeError:
    print("\t{}: name {}".format(AttributeError.__name__, AttributeError.__doc__))

try:
    print(student.__step())  # accessing a private attribute
except AttributeError:
    print("\t{}: step() {}".format(AttributeError.__name__, AttributeError.__doc__))


# public method invocation --> all is OK
student.going_home()
# public method invocation --> all is OK
student.set_name("Alice")
student.going_home()

# accessing an attribute via its property object
student.name = 'Mark'
print(student.name)
```
