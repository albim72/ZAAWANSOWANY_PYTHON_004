class MojaMeta(type):
    def __new__(cls,clsname,bases,attribs):
        print(f"nazwa klasy: {clsname}")
        print(f"klasy dziedziczone: {bases}")
        print(f"zbiór atrybutów: {attribs}")
        return type.__new__(cls,clsname,bases,attribs)

    def info(cls):
        return "metaklasa działa..."

class Zwykla:
    def fx(self,x,y):
        return x+y

class Pierwsza(Zwykla,metaclass=MojaMeta):
    def fx(self, x, y):
        return super().fx(x, y) + 2

class Druga(Pierwsza):
    pass

class Dodatkowa:
    pass

class Trzecia(Dodatkowa,Druga):
    pass




