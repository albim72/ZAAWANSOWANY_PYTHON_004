class MultiBases(type):
    def __new__(cls, clsname,bases,attribs):
        if len(bases) >1:
            raise TypeError("Wielodziedziczenie zabronione!!!")
        return super().__new__(cls, clsname,bases,attribs)

class Base(metaclass=MultiBases):
    pass

class A(Base):
    pass

class B(Base):
    pass

class C(A,B):
    pass
