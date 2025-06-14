from abc import ABC, abstractmethod
class Device:
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
    def status(self):
        print("Device status checked")
class Smartphone(Device):
    def turn_on(self):
        print("car started")
    def turn_off(self):
        print("car stopped")
class Laptop(Device):
    def turn_on(self):
        print(" laptop started")
    def turn_off(self):
        print(" laptop stopped")
smartphone=Smartphone()
laptop  =Laptop()
smartphone.turn_on()
smartphone.turn_off()
smartphone.status()
laptop.turn_on()
laptop.turn_off()
smartphone.status()
