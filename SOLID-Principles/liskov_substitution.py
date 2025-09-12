"""According to the LSP, if a program uses objects of a superclass, then the
substitution of these objects with objects of a subclass should not change
the correctness and expected behavior of the program."""

# First let's see an example that doesn't folow the LSP


class Weapon:
    """Base weapon class with the attack method."""

    def attack(self, target) -> int: ...


class DivineSword(Weapon):
    """Subclass that implements the attack method with the same contract,
    returning an integer."""

    def __init__(self, base_damage: int):
        self.damage = base_damage

    def attack(self, target):
        if getattr(target, "type", "") == "undead":
            return (2 * self.damage) - getattr(target, "armor", 0)

        return self.damage - getattr(target, "armor", 0)


class IcyStaff(Weapon):
    """Subclass that implements the attack method while breaking the original
    contract, because it might return a string instead of an integer, possibly
    causing runtime errors."""

    def __init__(self, base_damage: int):
        self.damage = base_damage

    def attack(self, target):
        if getattr(target, "type", "") == "ice_troll":
            return "The attack was ineffective"

        return self.damage - getattr(target, "resistance", 0)


# To fix the IcyStaff class we can change it so it returns 0 when the attack
# is ineffective.


class IcyStaffLSP(Weapon):
    def __init__(self, base_damage: int):
        self.damage = base_damage

    def attack(self, target):
        if getattr(target, "type", "") == "ice_troll":
            return 0

        return self.damage - getattr(target, "resistance", 0)


# Mock target objects
class Skeleton:
    type = "undead"
    armor = 2
    resistance = 1


class IceTroll:
    type = "ice_troll"
    armor = 5
    resistance = 3


if __name__ == "__main__":
    sword = DivineSword(10)
    staff = IcyStaffLSP(5)

    total_damage = 0

    total_damage += sword.attack(Skeleton())
    total_damage += staff.attack(IceTroll())

    print("Total damage:", total_damage)

    # To see the error the IcyStaff that doesn't follow the LSP causes, just
    # uncomment the following code:
    # bad_staff = IcyStaff(10)
    # total_damage += bad_staff.attack(IceTroll())
