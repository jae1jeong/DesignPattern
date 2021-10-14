import copy

# class Cat:
#     def __init__(self) -> None:
#         self.color = None
#         self.eye_color = None
#         self.nose_color = None
#         self.tail_color = None
#         self.name = None

#비효율적
# kitty = Cat()
# kitty.color = "white"
# kitty.nose_color = "white"
# kitty.eye_color = "white"
# kitty.name = "kitty"
# kitty.tail_color = "white"
# nabi = Cat()
# nabi.color = "white"
# nabi.eye_color = "white"
# nabi.name = "nabi"
# nabi.tail_color = "white"

# 왜 클론을 굳이 쓰느냐 nabi = kitty 이러면 되지 않느냐 하지만 레퍼런스 기반 언어이기 때문에 오브젝트가 복사되는게 아니라 가리키는게 두 개가 생김 그래서 deepcopy



class Cat:
    def __init__(self) -> None:
        self.color = None
        self.eye_color = None
        self.nose_color = None
        self.tail_color = None
        self.name = None
    
    def clone(self):
        return copy.deepcopy(self)
        # copytype 아님? 


class BlackCat(Cat):
    def __init__(self) -> None:
        super().__init__()
        self.color = "black"

class WhiteCat(Cat):
    def __init__(self) -> None:
        super().__init__()
        self.color = "white"

        
blackCat = BlackCat()
blackCat.eye_color = "blue"
blackCat.tail_color = "green"
# 미완성된 cat 객체를 클론해서 완성할 수 있음
kitty = blackCat.clone()
kitty.nose_color = "white"
kitty.name = "kitty"

# 중간단계 오브젝트를 만들어서 딥카피해서 오브젝트를 만들어나가는 디자인 패턴