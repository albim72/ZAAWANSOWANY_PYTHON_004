from dataclasses import dataclass

class Liczba:
    def __init__(self,x):
        self.x = x

zk = Liczba(2)
print(zk.x)

@dataclass
class DLiczba:
    x:int

dk = DLiczba(9)
print(dk.x)

@dataclass
class Dane:
    nazwa:str
    filia: int
    licznik:int = 0
    cena:float = 0.0
    

    def __repr__(self):
        return f"liczba sztuk: {self.licznik}, cena: {self.cena} zł"
    def __call__(self, *args, **kwargs):
        print(f"kwota do zapłaty: {self.licznik*self.cena} zł")
    def opisz(self):
        return f"opis produktu: {self.nazwa}"


d = Dane("talerz",2,5,32)

print(d)
print(d.opisz())
d()
