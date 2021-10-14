# 팩토리에서 객체를 만든 수라던지 상태를 나타내거나, 객체에 특성을 더하고 싶을 경우가 생길 수 있음

from FactoryPattern import AnimalEnum


class Animal():
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("meow")

class Dog(Animal):
    def speak(self):
        print("bark")



class AnimalFactory():
    def createAnimal(self):
        pass


class CatFactory(AnimalFactory):
    def __init__(self) -> None:
        self.count = 0

    def createAnimal(self):
        self.count += 1
        return Cat()

class DogFactory(AnimalFactory):
    def createAnimal(self):
        return Dog()
    
    def makeWings(self,dog:Dog):
        print("dog wing added")
        return dog


cat_fatory = CatFactory()
cat = cat_fatory.createAnimal()
print(cat_fatory.count)

