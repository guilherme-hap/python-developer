from abc import ABC, abstractmethod, abstractproperty


class RemoteControl(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @property
    @abstractproperty
    def brand(self):
        pass


class TVControl(RemoteControl):
    def turn_on(self):
        print("Turning on the TV...")
        print("On!")

    def turn_off(self):
        print("Turning off the TV...")
        print("Off!")

    @property
    def brand(self):
        return "Philco"


class AirConditionerControl(RemoteControl):
    def turn_on(self):
        print("Turning on the air conditioner...")
        print("On!")

    def turn_off(self):
        print("Turning off the air conditioner...")
        print("Off!")

    @property
    def brand(self):
        return "LG"


control = TVControl()
control.turn_on()
control.turn_off()
print(control.brand)


control = AirConditionerControl()
control.turn_on()
control.turn_off()
print(control.brand)