"""We should prefer composing objects from simpler parts to inheriting
functionalities from a base class."""

# Composing a car using the engine


class Engine:
    # First we create the engine that will be part of the car later.
    def start(self):
        print("Engine started!")


class Car:
    # Now we define the Car class that 'has a' Engine.
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Vroom vroom!")


if __name__ == "__main__":
    car = Car()
    car.start()
