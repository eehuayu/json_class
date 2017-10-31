from jsonx.field import Field


class Model:
    @property
    def fields_dict(self):

        fields_dict = dict()

        for attr in dir(self.__class__):
            val = getattr(self.__class__, attr)
            if isinstance(val, Field):
                fields_dict[attr] = val

        return fields_dict

    def cls_to_json(self):
        value = dict()
        for attr in self.fields_dict:
            value[attr] = getattr(self, attr, None)

        json_object = dict(
            __class__=self.__class__.__name__,
            __value__=value,
        )

        return json_object

