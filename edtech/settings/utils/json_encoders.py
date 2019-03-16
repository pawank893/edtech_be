import json
from decimal import Decimal


class ObjectEncoder(json.JSONEncoder):
    """
    For more details [JSON ENcoder](https://docs.python.org/2/library/json.html#json.JSONEncoder)
    This will override the cls of the JSON Encoder of json.dumps()

    The job of this is two fold:
        - Try to get a serializable value of an object in the value part of a dict passed to this encoder.
            This is accomplished by the ```def default``` method.
            For ex: json.dumps({'aa':Decimal(10.00)})
        - To avoid raising any type error if the key part of a dict passed is not of basic python types.
            This is not the behaviour we want as the errors are suppressed but in some cases it is better
            to retain a partial record than to lose an entire one.
            This is accomplished by ```skipkeys=True```.
            For ex: json.dumps({Decimal(10.00):'aa'})

    """

    def __init__(self, skipkeys=False, ensure_ascii=True, check_circular=True,
                 allow_nan=True, sort_keys=False, indent=None,
                 separators=None, encoding='utf-8', default=None):
        # Explicitly setting skipkeys=True.
        skipkeys = True
        super(ObjectEncoder, self).__init__(skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular,
                                            allow_nan=allow_nan, sort_keys=sort_keys, indent=indent,
                                            separators=separators, encoding=encoding, default=default)

    def default(self, obj):
        if hasattr(obj, "to_json"):
            return self.default(obj.to_json())
        elif hasattr(obj, "__dict__"):
            return self.default({k: v for k, v in obj.__dict__.items() if not str(k).startswith('_')})
        elif isinstance(obj, Decimal):
            return float(obj)
        else:
            return super(ObjectEncoder, self).default(obj)
