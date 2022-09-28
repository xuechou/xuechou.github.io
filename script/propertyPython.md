# @property convert one attribute to setAttribute(),getAttribute() and deleteAttribute()

```py
class ClassWithProperties:
    def __init__(self):
        self.someAttribute = 'some initial value'
    @property
    def someAttribute(self): # This is the "getter" method.
        return self._someAttribute # must be _someAttribute, not someAttribute
    @someAttribute.setter
    def someAttribute(self, value): # This is the "setter" method.
        self._someAttribute = value
    @someAttribute.deleter
    def someAttribute(self): # This is the "deleter" method.
        del self._someAttribute
```

## why need @property

### read-only attribute

TODO:

### Using Setters to Validate Data

TODO:

## reference

`BEYOND THE BASIC STUFF WITH PYTHON`


