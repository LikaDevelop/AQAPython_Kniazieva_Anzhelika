class Human:

    favourite_drink = 'beer'

    def __init__(self, age: int):
        self.age = age
        if age < 18:
            self.favourite_drink = 'juice'

    def drink(self):
        print(f'{self.__class__.__name__} likes drink {self.favourite_drink}')


class Worker(Human):
    def __init__(self, age: int, salary: float):
        super().__init__(age)
        self.salary = salary
        if self.salary > 1000 and age >= 18:
            self.favourite_drink = 'wiskey'


print(Human.favourite_drink)

human1 = Human(12)
worker1 = Worker(14, 2000)
worker2 = Worker(25, 1000)
worker3 = Worker(18, 3000)

human1.drink()
worker1.drink()
worker2.drink()
worker3.drink()