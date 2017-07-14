from example import Example
from main import class_dict


def class_to_json():
    """
    class转json示例
    :return:
    """
    a = Example()
    print(a.cls_to_json())


def json_to_class():
    """
    json转class示例
    :return:
    """

    json_object = dict(
        __class__='Example',
        __value__=dict(
            a=10000000000,
            b=33,
            x=dict(r=11),
        )
    )

    # 初始化对象
    aa = class_dict[json_object['__class__']]()
    # 加载属性
    aa.json_to_cls(dict(
        __class__='A',
        __value__=dict(
            a=10000000000,
            b=33,
            x=dict(r=11),
        )
    ))

    print(aa.a, aa.b, aa.x, aa.sum_ab())


# 执行下面的代码，成功将class和json互相转化
class_to_json()
json_to_class()
