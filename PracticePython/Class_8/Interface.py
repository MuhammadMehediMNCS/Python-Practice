# Interface
from abc import ABC, abstractmethod

class IVehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(IVehicle):
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")

class Bike(IVehicle):
    def start(self):
        print("Bike started")
    def stop(self):
        print("Bike stopped")

v1 = Car()
v1.start()  # Car started
v1.stop()

v2 = Bike()
v2.start()  # Bike started
v2.stop()