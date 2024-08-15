def introspection_info(obj):
    dictionary = {}
    dictionary['type'] = type(obj)
    dictionary['attributes'] = dir(obj)
    dictionary['methods'] = []
    dictionary['module'] = introspection_info.__module__
    return dictionary



number_info = introspection_info(42)
print(number_info)

# {'type': 'int', 'attributes': ['__abs__', '__add__', ...], 'methods': [], 'module': '__main__'}