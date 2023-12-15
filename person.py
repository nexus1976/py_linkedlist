from decimal import Decimal
from typing_extensions import Self

class Person():
    def __init__(self, name: str = '', height: Decimal = 0, weight: Decimal = 0) -> None:
        self._name:str = name
        self._needsToPee:bool = True
        self._height:Decimal = height
        self._weight:Decimal = weight
        self._bmi:Decimal = self._weight / self._height
        self._preggoBaby:Self = None

    @property
    def height(self) -> Decimal:
        return self._height
    @height.setter
    def height(self, value:Decimal):
        self._height = value
        self._bmi = self._weight / self._height

    @property
    def weight(self) -> Decimal:
        return self._weight
    @weight.setter
    def weight(self, value:Decimal):
        self._weight = value
        self._bmi = self._weight / self._height

    @property
    def BMI(self) -> Decimal:
        return self._bmi

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value:str):
        self._name = value

    @property
    def needsToPee(self) -> bool:
        return self._needsToPee

    def goToBathroom(self) -> None:
        self._needsToPee = False

class Woman(Person):
    @property
    def gender(self) -> str:
        return 'female'
    
class Man(Person):
    @property
    def gender(self) -> str:
        return 'male'

x = Person('person1', 5.8, 150.6)
x.height = 5.9

y = Person()
y.name = 'person2'
y.weight = 150.9

print(f'{x.name} has a height of {x.height} and a weight of {x.weight} which gives a BMI of {x.BMI}')
# x.height = 6.5
x.weight = 250.5
print(f'{x.name} has a height of {x.height} and a weight of {x.weight} which gives a BMI of {x.BMI}')


mary = Woman('Mary', 5.25, 125)
