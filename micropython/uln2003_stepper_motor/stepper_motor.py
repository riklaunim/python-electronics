import pyb


class Stepper:
    """
    Handles common 4-pin ULN2003 stepper motor controllers
    """
    steps = [
        [1],
        [1, 2],
        [2],
        [2, 3],
        [3],
        [3, 4],
        [4],
        [1, 4]
    ]
    step_delay_ms = 5

    def __init__(self, pins):
        self.pins = [pyb.Pin(pin, pyb.Pin.OUT_PP) for pin in pins]
        self.current_step = 0

    def do_step(self):
        self._low_on_all()
        self._high_on_step_pins()
        self._record_step()
        pyb.delay(self.step_delay_ms)

    def _low_on_all(self):
        for pin in self.pins:
            pin.low()

    def _high_on_step_pins(self):
        high_pins = self.steps[self.current_step]
        for pin_number in high_pins:
            self.pins[pin_number - 1].high()

    def _record_step(self):
        self.current_step += 1
        if self.current_step == len(self.steps):
            self.current_step = 0
