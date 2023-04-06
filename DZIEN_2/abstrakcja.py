from abc import ABC,abstractmethod


class A(ABC):pass

class Prototyp(ABC):
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def info(self,msg):
        return f'ważna informacja: {msg}'

    @abstractmethod
    def opis(self):pass

    @abstractmethod
    def policz_w(self):
        return self.x+2*self.y


class Regular(Prototyp,A):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z=z

    def opis(self):
        return "to jest klasa Regular"

    def policz_w(self):
        return super().policz_w() + 3*self.z


r = Regular(4,7,8)
print(r.opis())
print(f"wynik: {r.policz_w()}")
