def introspection_info(obj):
    dictionary = {}
    dictionary['type'] = type(obj)
    dictionary['attributes'] =  [atribut for atribut in dir(obj) if '__' in atribut]
    dictionary['methods'] = [method for method in dir(obj) if '__' not in method]
    dictionary['module'] = introspection_info.__module__
    return dictionary



number_info = introspection_info(42)
print(number_info)

# {'type': 'int', 'attributes': ['__abs__', '__add__', ...], 'methods': [], 'module': '__main__'}
