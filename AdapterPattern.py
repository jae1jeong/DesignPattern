

class Animal:
    def walk(self):
        pass

class Cat(Animal):
    def walk(self):
        print("cat walking")

class Dog(Animal):
    def walk(self):
        print("dog walking")

def makeWalk(animal:Animal):
    animal.walk()


# walk 인터페이스가 없음 동작하게 만들기 위해 어댑터를 만든다. 맞지 않은 인터페이스를 만들어주는 기능을 함
class Fish:
    def swim(self):
        print("fish swimming")

class FishAdapter(Animal):
    def __init__(self,fish:Fish) -> None:
        self.fish = fish
    
    def walk(self):
        self.fish.swim()


kitty = Cat()
doggy = Dog()
makeWalk(kitty)
makeWalk(doggy)
nemo = Fish()
adapter_nemo = FishAdapter(nemo)
adapter_nemo.walk()