from typing import Protocol

class EeatsBread(Protocol):
    def eat_bread(self):
        pass

def feed_bread(animal:EeatsBread):
    animal.eat_bread()

class Duck:
    def eat_bread(self):
        print("kaczka nie je chleba")

feed_bread(Duck())
