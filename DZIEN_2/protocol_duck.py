from typing import List,Protocol

class Item(Protocol):
    quantity:float
    price:float

class Product:
    def __init__(self,name:str,quantity:float,price:float):
        self.name = name
        self.quantity = quantity
        self.price = price


def calculate_total(items: List[Item])->float:
    return sum([item.quantity*item.price for item in items])

total = calculate_total([
    Product('A',3,156),
    Product('B',1,2030),
    Product('C',11,14.5),
    Product('D',8,4.4),
])

print(f"{total:.2f} zł")





