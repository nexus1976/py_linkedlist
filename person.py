class Person():
    def __init__(self, name: str = 'John Doe') -> None:
        self._name:str = name
        self._needsToPee:bool = True

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value:str):
        if value != self._name:
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

myPeople = [Person('Mike'), Person('Mary'), Person('Felicity')]
firstPerson = myPeople[0]
secondPerson = myPeople[1]
thirdPerson = myPeople[2]
