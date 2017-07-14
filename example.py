from field import Field
from model import Model


class Example(Model):
    a = Field()
    b = Field()
    x = Field()
    v = 0

    def __init__(self):
        self.a = 3
        self.b = 4
        self.x = {"11": 11}

    def sum_ab(self):
        return self.a + self.b


class Example1(Model):
    pass


class Example2(Model):
    pass
