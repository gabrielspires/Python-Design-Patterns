"""It should not be necessary to know how a feature is implemented to use it. To
solve this problem we can define contracts for the classes using Interfaces.
Two key ways of doing it are using Abstract Base Classes and Protocols"""

################################################################################
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


################################################################################
# Using Protocols is a more flexible way to create interfaces known as
# structural duck typing, where an object is considered valid if it has certain
# attributes or method regardless of it's actual inheritance.

# One advantage of using Protocols is that structural duck typing is determined
# at compile time. This means that your IDE will be able to catch error before
# you need to run the program, making your applications more robust and easier to
# debug.

# First we import the Protocol class from the typing module and then we define
# a class that will serve as the interface. We also import the runtime_checkable
# decorator just to show at runtime that it works as intended.

from typing import Protocol, runtime_checkable


@runtime_checkable
class Dragon(Protocol):
    def fly(self) -> None: ...
    def fire_breath(self) -> None: ...


# That all we need to do. Now every class that has a fly method and a
# fire_breath method will be considered a Dragon, where it explictly inherits
# from the Dragon class or not!


class RedDragon:
    def fly(self) -> None:
        print(f"The {self.__class__.__name__} is flying!")

    def fire_breath(self) -> None:
        print(f"{self.__class__.__name__} used Fire Breath!")


class BlackDragon:
    def fly(self) -> None:
        print(f"The {self.__class__.__name__} is flying!")

    def fire_breath(self) -> None:
        print(f"{self.__class__.__name__} used Fire Breath!")


def release_dragon(dragon: Dragon):
    # The 'isinstance' only works because of the runtime_checkable decorator.
    if isinstance(dragon, Dragon):
        dragon.fly()
        dragon.fire_breath()


if __name__ == "__main__":
    # Testing interfaces with ABC
    HealthPotion().use()
    ManaPotion().use()

    # Testing interfaces with Protocols
    release_dragon(RedDragon())
    release_dragon(BlackDragon())
