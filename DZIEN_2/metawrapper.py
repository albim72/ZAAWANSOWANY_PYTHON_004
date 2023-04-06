from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Pełna nazwa metody:{func.__qualname__}")
        return func(*args,**kwargs)
    return wrapper

def debugmethods(cls):
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls

class DebugMeta(type):
    def __new__(cls, clsname,bases,attribs):
        obj = super().__new__(cls, clsname,bases,attribs)
        obj = debugmethods(obj)
        return obj

class Base(metaclass=DebugMeta):
    pass

class Calculate(Base):
    def add(self,x,y):
        return x+y

    def mul(self,x,y):
        return x*y

mojeobl = Calculate()

print(mojeobl.add(2,3))
print(mojeobl.mul(2,3))

