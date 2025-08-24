"""It should not be necessary to know how a feature is implemented to use it. To
solve this problem we can define contracts for the classes using Interfaces.
Two key ways of doing it are using Abstract Base Classes and Protocols"""

# To use the Abstract Base Class, first we nee to import the ABC class and
# abstractmethod decorator. Then we define the class.
from abc import ABC, abstractmethod


class ItemInterface(ABC):
    # The abstractmethod decorator forces any class that inherits this interface
    # to implement this method. If you try to instantiate a child class that
    # have not implemented this method, you'll get a TypeError exception.
    @abstractmethod
    def use(self):
        pass


class HealthPotion(ItemInterface):
    def use(self):
        print("You are healed!")


class ManaPotion(ItemInterface):
    def use(self):
        print("Mana restored!")


if __name__ == "__main__":
    HealthPotion().use()
    ManaPotion().use()
