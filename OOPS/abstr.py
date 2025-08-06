from abc import ABC,abstractmethod

class Device(ABC):
    @abstractmethod
    def start(self):
        pass
    

class Laptop(Device):
    def start (self):
        print("Laptop is Turning on.")

class SmartPhone(Device):
    def start(self):
        print("Smartphone is Turning on.")

L1 = Laptop()
L1.start()

S1 = SmartPhone()
S1.start()