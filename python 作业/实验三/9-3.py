import math

class Ladder:
    def __init__(self,up,down,high=1):
        self.a = up
        self.b = down
        self.h = high
    
    def Area(self):
        return (self.a + self.b) * self.h / 2

    def Long(self):
        c = math.sqrt(((self.b - self.a) / 2) ** 2 + self.h ** 2)
        return self.a + self.b + 2 * c
    

ladder_1 = Ladder(up=5,down=8)

# 输出面积和周长
print("面积: ", ladder_1.Area())
print("周长: ", ladder_1.Long())

