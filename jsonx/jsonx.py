class Application:

    _models = None

    def __init__(self):
        self._models = dict()

    def json_loads(self, json_object):
        class_name = json_object['__class__']

        assert class_name in self._models

        class_object = self._models[class_name]()

        value = json_object['__value__']

        for attr in class_object.fields_dict:
            if attr in value:
                setattr(class_object, attr, value[attr])

        return class_object

    def json_dumps(self, class_object):

        assert class_object.__class__.__name__ in self._models

        value = dict()
        for attr in class_object.fields_dict:
            value[attr] = getattr(class_object, attr, None)

        json_object = dict(
            __class__=class_object.__class__.__name__,
            __value__=value,
        )

        return json_object

    def register_models(self, *args):
        self._models.update(
            dict([(arg.__name__, arg) for arg in args])
        )
