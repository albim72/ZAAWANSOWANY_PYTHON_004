class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls in cls._instances:
            raise Exception("nie możesz utworzyć kolejnej instancji!")
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class RegularClass():
    pass

x = RegularClass()
y = RegularClass()

print(x==y)

print(x)
print(y)

class SingletonClass(metaclass=Singleton):
    pass

a = SingletonClass()
b = SingletonClass()
print(a==b)
