from dataclasses import dataclass

@dataclass
class Article:
    title:str
    author:str
    content:str
    def __repr__(self):
        return f'{self.title} {self.author} {self.content}'

@dataclass(init=False)
class PythonArticle(Article):
    language:str
    author:str
    price:int=30
    def __repr__(self):
        return f'{self.language} {self.author} {self.price} zł'

    def __init__(self,title,price):
        self.title = title
        self.price = price
        self.language = "Python 3"
        self.author = "Marcin Albiniak"
        self.content = "Opis wybranych aspektów użycia języka Python"

    def infoarticle(self):
        return f'Publikacja {self.title}, autor: {self.author}, rabat [10%]: {0.1*self.price} zł'

a = Article("Typowanie w Pythonie","Eryk Kos","Takie tam...")
print(a)

art = PythonArticle("Algorytmy DL",88)
print(art)
print(art.infoarticle())

# art = PythonArticle("x","DD",4)
# print(art)
# print(art.infoarticle())


