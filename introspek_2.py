def introspection_info(obj):
    dictionary = {}
    dictionary['type'] = type(obj)
    for x in dir(obj):
        if not callable(getattr(obj, f'{x}')):
            dictionary['attributes'] = getattr(obj, f'{x}')
    dictionary['methods'] = [method for method in dir(obj) if '' in method]
    dictionary['module'] = introspection_info.__module__
    return dictionary

number_info = introspection_info(42)
print(number_info)
# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
