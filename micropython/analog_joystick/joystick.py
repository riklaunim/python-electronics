import pyb


class Joystick:
    def __init__(self, x_axis_pin, y_axis_pin, button_pin):
        self.x_axis = pyb.ADC(x_axis_pin)
        self.y_axis = pyb.ADC(y_axis_pin)
        self.button = pyb.Pin(button_pin, pyb.Pin.IN, pull=pyb.Pin.PULL_UP)

    def get_state(self):
        return {
            'x': self.x_axis.read(),
            'y': self.y_axis.read(),
            'button': self.button.value()
        }
