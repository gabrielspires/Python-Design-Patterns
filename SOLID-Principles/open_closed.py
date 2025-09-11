"""Once a software entity is defined and implemented, it should not be
changed to add new functionality. Instead, the entity should be extended
through inheritance or interfaces to accommodate new requirements and behaviors.
"""


# First we'll create an example that violates the OCP


class Bazooka:
    def __init__(self, rockets: int):
        self.rockets = rockets


class Bow:
    def __init__(self, arrows: int):
        self.arrows = arrows


class Character:
    def __init__(self, weapon):
        self.weapon = weapon

    def shoot(self):
        if isinstance(self.weapon, Bazooka):
            print("I'm shooting a rocket!")

        elif isinstance(self.weapon, Bow):
            print("I'm shooting an arrow!")


# In the example above, if we add a third weapon type, we'll need to change
# the Character class so that the Character can shoot with the new weapon.
# To follow the OCP principle, we must create our classes in a way that
# won't make that change necessary.

# First we'll define a interface/protocol

from typing import Protocol


class Weapon(Protocol):
    def shoot(self): ...


# Now we create the weapon classes that conform to the Weapon interface


class DeathLaser:
    def __init__(self, energy: int):
        self.energy = energy

    def shoot(self):
        print("IMA FIRIN MAH LAZER!!!")


class PotatoCannon:
    def __init__(self, potatoes: int):
        self.potatoes = potatoes

    def shoot(self):
        print("Mashed and dispatched!")


# Finally we can create the Character class again, this time following the OCP
class CharacterOCP:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def shoot(self):
        self.weapon.shoot()


# Now we can add as many weapons as we want and the Character class won't have
# to change


class NailGun:
    def __init__(self, nails: int):
        self.nails = nails

    def shoot(self):
        print("Stick around!")


if __name__ == "__main__":
    player_1 = CharacterOCP(DeathLaser())
    player_2 = CharacterOCP(PotatoCannon())
    player_3 = CharacterOCP(NailGun())

    player_1.shoot()
    player_2.shoot()
    player_3.shoot()
