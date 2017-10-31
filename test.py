from jsonx.field import Field
from jsonx.jsonx_face import json_dumps, json_loads, register_models
from jsonx.model import Model


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


register_models(Example)

a = Example()

# 类属性转化为json对象
print(json_dumps(a))

class_object = json_loads(json_dumps(a))

print(class_object.__dict__)
