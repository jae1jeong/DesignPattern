
# 생성과정이 복잡할때 쓰임
from PrototypePattern import BlackCat


class Cat:

    def __init__(self,height,weight,color) -> None:
        self.height = height
        self.weight = weight
        self.color = color

    # 단일 책임 원칙에 벗어남 참고 
    def print(self):
        print(f'{self.height}cm {self.weight}kg {self.color}')

class CatBuilder:
    def __init__(self) -> None:
        self.height = None
        self.weight = None
        self.color = None
    
    def setHeight(self,height):
        self.height = height
        return self

    def setWeight(self,weight):
        self.weight = weight
        return self
    
    def setColor(self,color):
        self.color = color
        return self
    
    def build(self) -> Cat:
        return Cat(self.height,self.weight,self.color)


cat_builder = CatBuilder().setColor("white").setHeight(180).setWeight(100).build()
cat_builder.print()

class WhiteCatBuilder(CatBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.color = "white"

class BlackCatBuilder(CatBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.color = "black"

white_cat = WhiteCatBuilder().setHeight(120).setWeight(120).build()
black_cat = BlackCatBuilder().setHeight(120).setWeight(120).build()
white_cat.print()
black_cat.print()

class Director:
    def setSmallCat(self,builder:CatBuilder):
        builder.setWeight(5)
        builder.setHeight(5)

    def setBigCat(self,builder:CatBuilder):
        builder.setHeight(50)
        builder.setWeight(50)


director = Director()
cat_builder = BlackCatBuilder()
director.setBigCat(cat_builder)
cat = cat_builder.build()
cat.print()