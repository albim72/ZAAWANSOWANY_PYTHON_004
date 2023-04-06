from dataclasses import dataclass
from datetime import datetime

@dataclass
class NewPerson:
    firstname:str
    lastname:str
    year_of_birth:int

    @property
    def age(self):
        return datetime.now().year - self.year_of_birth

    @property
    def czypelno(self):
        return self.age>=18

p = NewPerson("Janusz","Gierej",1967)
print(p)
print(p.age)
print(p.czypelno)
