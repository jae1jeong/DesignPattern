
class Animal:    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("bark",end="")

class Cat(Animal):
    def speak(self):
        print("meow",end="")


class Deco(Animal):
    def __init__(self,animal:Animal) -> None:
        self.animal = animal
    
    def speak(self):
        self.animal.speak()

class WithSmile(Deco):
    def speak(self):
        self.animal.speak()
        print("😄")

class WithHeart(Deco):
    def speak(self):
        self.animal.speak()
        print('🥰')

doggy = Dog()
kitty = Cat()
with_smile_kitty = WithSmile(kitty)
with_heart_doggy = WithHeart(doggy)
with_smile_kitty.speak()
with_heart_doggy.speak()
        