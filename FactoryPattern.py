
from enum import Enum


class AnimalEnum(Enum):
    CAT = 1
    DOG = 2

class Animal():
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("meow")

class Dog(Animal):
    def speak(self):
        print("bark")


# enum 클래스 사용 권장
def FactoryFn(animal:str) -> Animal:
    if animal == "cat":
        return Cat()
    elif animal == "dog":
        return Dog()

cat = FactoryFn("cat")
dog = FactoryFn("dog")
cat.speak()
dog.speak()

# 클래스 오브젝트로 사용 가능

class AnimalFactory():

    def createAnimal(self,animal:AnimalEnum) -> Animal:
        if animal == animal.CAT:
            return Cat()
        elif animal == animal.DOG:
            return Dog()

cat1 = AnimalFactory().createAnimal(AnimalEnum.CAT)
dog1 = AnimalFactory().createAnimal(AnimalEnum.DOG)
cat1.speak()
dog1.speak()