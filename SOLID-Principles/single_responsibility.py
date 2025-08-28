"""When defining a class, that class should have only one reason to exist
and should be responsible for only one aspect of a functionality."""


# Let's create a RaceCar class. In this example the RaceCar class is responsible
# for accelerating and also by declaring that it finished the race.
class RaceCar:
    def __init__(self, number):
        self.number = number

    def accelerate(self):
        print("Pedal to the metal!")

    def finishRace(self):
        print("I reached the finish line!")


# To adhere to the SRP, we can refactor the code to use two different classes
# that would each have one responsibility:
class RaceCarSRP:
    def __init__(self, number):
        self.number = number

    def accelerate(self):
        print("Pedal to the metal!")


class Race:
    def __init__(self):
        self.race_results = []

    @property
    def results(self):
        return f"Results: {self.race_results}"

    def finish(self, car: RaceCarSRP):
        self.race_results.append(car.number)
        print(f"Car {car.number} finished the race!")


if __name__ == "__main__":
    car_1 = RaceCarSRP(1)
    car_1.accelerate()
    car_2 = RaceCarSRP(2)
    car_2.accelerate()

    race = Race()
    race.finish(car_1)
    race.finish(car_2)
    print(race.results)
