class Placeholder(object):
    pass


def _transform_value(value, mapping_class, mapping_transformer):
    if isinstance(value, mapping_class):
        return mapping_transformer(value)
    elif isinstance(value, list):
        return [_transform_value(item, mapping_class, mapping_transformer)
                for item in value]
    else:
        return value


def dict_to_object(dict_payload):
    placeholder = Placeholder()
    for key, value in dict_payload.iteritems():
        setattr(placeholder, key,
                _transform_value(value, dict, dict_to_object))
    return placeholder


def _is_builtin(name):
    return name.startswith("__") and name.endswith("__")


def object_to_dict(value):
    placeholder = {}
    for key in filter(_is_builtin, value):
        placeholder[key] = _transform_value(
            getattr(value, key), Placeholder, object_to_dict)
    return placeholder
