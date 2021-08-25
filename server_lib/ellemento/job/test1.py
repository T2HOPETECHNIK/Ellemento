def new__init__(self):
    raise ValueError('Cannot invoke init!')

class Meta(type):
    def __new__(cls, name, bases, namespace):
        old_init = namespace.get('__init__')
        namespace['__init__'] = new__init__
        def factory_build_object(cls_obj, *args, **kwargs):
            obj = cls_obj.__new__(cls_obj, *args, **kwargs)
            return old_init(obj, *args, **kwargs)
        namespace['factory_build_object'] = classmethod(factory_build_object)
        return super().__new__(cls, name, bases, namespace)


class Foo(metaclass=Meta):
    def __init__(self, *args, **kwargs):
        print('init')