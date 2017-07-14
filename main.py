from example import Example, Example1, Example2


def list_class(*args):
    return dict([(cls.__name__, cls) for cls in args])


class_dict = list_class(Example, Example1, Example2)
