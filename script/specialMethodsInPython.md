# class methods, class attributes and static methods

**avoid** to use these features, just not fear when you see @classmethod @staticmethod

## class attributes in python is like static data member in cpp

```py
class CreateCounter:
    count = 0 # This is a class attribute.
    def __init__(self):
        CreateCounter.count += 1 # this is a object attribute
```
## class methods in python is like static function member in cpp

```py
class ExampleClass:
    def exampleRegularMethod(self):
        print('This is a regular method.')
       
    @classmethod
    def exampleClassMethod(cls): # cls must be the first arguement, cls measns class
        print('This is a class method.')
```

## static methods just like normol function, but defination is in a class

```py
class ExampleClassWithStaticMethod:
    @staticmethod
    def sayHello(): # static method without self or cls as arguements
        print('Hello!')
```