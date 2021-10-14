 
class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):  
        print("meow")


class CatProxy(Animal):
    def __init__(self,cat:Cat) -> None:
        self.cat = cat
    
    def speak(self):
        print("before speak")
        self.cat.speak()
        print("after speak")

# 인터페이스로도 가능
kitty = Cat()
kitty_proxy = CatProxy(kitty)
kitty_proxy.speak()

# 클라이언트가 직접 오브젝트를 사용하는 것보다 같은  인터페이스를 가진 오브젝트를 사용하는 경우가 필요할때 쓰임