class CustomMapIterator:
    def __init__(self, input_dict, key_func, value_func):
        self.input_dict = input_dict
        self.key_func = key_func
        self.value_func = value_func
        self.keys = iter(input_dict.keys())

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.keys)
        value = self.input_dict[key]
        transformed_key = self.key_func(key)
        transformed_value = self.value_func(value)
        return transformed_key, transformed_value


class CustomMap:
    def __init__(self, input_dict, key_func, value_func):
        self.input_dict = input_dict
        self.key_func = key_func
        self.value_func = value_func

    def __iter__(self):
        return CustomMapIterator(self.input_dict, self.key_func, self.value_func)


def add_prefix_to_key(key):
    return "key_" + key


def double_value(value):
    return value * 2


input_dict = {'first': 10, 'second': 20, 'third': 30}


custom_map_instance = CustomMap(input_dict, add_prefix_to_key, double_value)


for transformed_key, transformed_value in custom_map_instance:
    print(transformed_key, transformed_value)

