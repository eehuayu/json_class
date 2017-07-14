from field import Field


class Model(object):
    @property
    def _fields_dict(self):

        fields_dict = dict()

        for attr in dir(self.__class__):
            val = getattr(self.__class__, attr)
            if isinstance(val, Field):
                fields_dict[attr] = val

        return fields_dict

    def json_to_cls(self, json_object):

        json_value = json_object['__value__']
        for attr in self._fields_dict:
            if attr in json_value:
                setattr(self, attr, json_value[attr])

    def cls_to_json(self):
        value = dict()
        for attr in self._fields_dict:
            value[attr] = getattr(self, attr, None)

        json_object = dict(
            __class__=self.__class__.__name__,
            __value__=value,
        )

        return json_object
