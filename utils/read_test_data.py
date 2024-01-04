import json
from collections import OrderedDict, namedtuple


def create_namedtuple_from_dict(obj):
    """ Converts given list or dict to named tuples """
    if isinstance(obj, dict):
        fields = sorted(obj.keys())
        namedtuple_type = namedtuple(
            typename='TestData',
            field_names=fields,
            rename=True,
        )
        field_value_pairs = OrderedDict(
            (str(field), create_namedtuple_from_dict(obj[field]))
            for field in fields
        )
        try:
            return namedtuple_type(**field_value_pairs)
        except TypeError:
            return dict(**field_value_pairs)
    elif isinstance(obj, (list, set, tuple, frozenset)):
        return [create_namedtuple_from_dict(item) for item in obj]
    else:
        return obj


def inject_test_data(file):
    """ Read the content of the JSON file and convert it to a named tuple """
    file = str(file)
    with open(file) as f:
        raw_data = json.load(f)
    return create_namedtuple_from_dict(raw_data)
