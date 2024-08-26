def introspection_info(obj):

    dictionary = {}

    dictionary['type'] = type(obj)

    dictionary['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]

    dictionary['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]

    dictionary['module'] = introspection_info.__module__

    return dictionary

number_info = introspection_info(42)

print(number_info)

