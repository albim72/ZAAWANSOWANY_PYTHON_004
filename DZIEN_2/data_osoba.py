from dataclasses import dataclass,astuple,asdict,field

@dataclass(order=True)
class Person:
    firstname:str = "Jan"
    lastname:str = "Kot"
    age:int = 40
    job:str = "Data Developer"
    full_name:str = field(init=False,repr=False)
    sort_index:int = field(init=False,repr=False)

    def __repr__(self):
        return f"Pracownik: {self.firstname} {self.lastname}, stanowisko: {self.job}"

    def __post_init__(self):
        self.full_name = self.firstname + " " + self.lastname
        self.sort_index = self.age

    def setlastname(self,nowe):
        self.lastname = nowe
        self.full_name = self.firstname + " " + self.lastname


janek = Person()
print(janek)
janek.setlastname("Kozak")
print(janek.full_name)

print(astuple(janek))
print(asdict(janek))


aga = Person("Aga","Nowak",32,"sekretarka")
print(aga)
print(aga.full_name)

print(janek<aga)
