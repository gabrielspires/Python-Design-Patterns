"""We must always try to isolate the parts of our code that are most likely to
change and encapsulate them. Two key techniques that can help us achieve this
are Polymorphism and 'getters and setters'."""


################################################################################
# Polymorphism
class Character:
    def __init__(self, power: int):
        self.power: int = power

    # The attack method is created here in the superclass
    # but it's implementation changes for every child class
    def attack(self) -> None:
        pass


class Warrior(Character):
    def attack(self) -> None:
        print(
            f"The {self.__class__.__name__} used Sword Slash "
            f"and caused {self.power} damage!"
        )


class Mage(Character):
    def attack(self) -> None:
        print(
            f"The {self.__class__.__name__} used Fireball "
            f"and caused {self.power} damage!"
        )


################################################################################
# Getters and Setters


class Weapon:
    def __init__(self, ammo: int):
        # While declaring the ammo attribute, we prefix it with double
        # underscores to invoke something called name mangling, which is
        # similar to making the attibute private. This 'forces' the use of
        # the getter and setter methods but it's not strictly necessary.
        self.__ammo: int = ammo

    # When we use the @property decorator, we create a way for the user to
    # access the __ammo attribute by using Weapon().ammo.
    @property
    def ammo(self):
        return self.__ammo

    # Similar to the getter above, when we use the @ammo.setter decorator, we
    # create a way for the user to set Weapon().ammo = value and then inside
    # the method we execute any validations and update the right attribute.
    @ammo.setter
    def ammo(self, value: int):
        if value < 0:
            raise ValueError("Ammo can't be less than zero!")
        self.__ammo = value


if __name__ == "__main__":
    # Testing the Polymorphism
    character_list: list[Character] = [Warrior(200), Mage(150)]
    for character in character_list:
        character.attack()

    # Testing the getters and setters
    weapon = Weapon(30)
    print(f"You have {weapon.ammo} ammo left.")
    weapon.ammo = 10
    print(f"You have {weapon.ammo} ammo left.")
