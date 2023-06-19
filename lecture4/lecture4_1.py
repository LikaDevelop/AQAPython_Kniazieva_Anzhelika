from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Mammals(Animal):

    name = 'Mammal'
    voice = 'some voice'

    def eat(self):
        print('I like that meal')

    def sleep(self):
        print('Hrrr')

    def _protected(self):
        pass

    def __private(self):
        pass

class Dog(Mammals):
    def __init__(self, name=None, voice=None):
        if name:
            self.name = name
        if voice:
            self.voice = voice

dog_1 = Dog('Bobik')
dog_2 = Dog()
dog_3 = Dog('Bobik', 'vouf')

print(dog_1.name)
print(dog_1.voice)