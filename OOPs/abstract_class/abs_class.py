from abc import ABC, abstractmethod
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
    def status(self):
        print("Device is up and running")
class Smartphone(Device):
    def turn_off(self):
        print("smartphone is switched off")
    def turn_on(self):
        print("smartphone is switched on")                
class Laptop(Device):
    def turn_off(self):
        print("Laptop is off")
    def turn_on(self):
        print("Laptop is on")
class Smartwatch(Device):
    def turn_off(self):
        print("watch is turned off")
    def turn_on(self):
        print("watch is turned on")                         
Smrtphone=Smartphone()
lptop=Laptop()
SmrtWatch=Smartwatch()
Smrtphone.turn_off()
Smrtphone.turn_on()
Smrtphone.status()
lptop.turn_off()
lptop.turn_on()
lptop.status()
SmrtWatch.turn_off()
SmrtWatch.turn_on()
SmrtWatch.status()


