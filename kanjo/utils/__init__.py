import importlib


def import_from_string(string):
    module_name, name = string.split(':')
    module = importlib.import_module(module_name)
    return getattr(module, name)