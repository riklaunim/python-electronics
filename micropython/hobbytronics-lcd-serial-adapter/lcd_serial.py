import pyb


class LCD(object):
    """
    Handles LCD serial adapter from Hobbytronics
    http://www.hobbytronics.co.uk/i2clcd-backpack-v2
    Allows displaying text on various 16-pin LCD displays
    """
    END = chr(0xFF)

    def __init__(self, device, rows, columns):
        self.commands = {
            'display_string': chr(1),
            'set_cursor_position': chr(2),
            'clear_line': chr(3),
            'clear': chr(4),
            'set_lcd_type': chr(5),
            'backlight': chr(7)
        }
        self.device = device
        self.rows = rows
        self.columns = columns
        self.connection = None

    def configure(self):
        self.connection = pyb.UART(self.device, 9600)
        pyb.delay(1000)
        self.execute_command('set_lcd_type', chr(self.rows) + chr(self.columns))
        self.clear()

    def clear(self):
        self.execute_command('clear', '')

    def clear_line(self, line):
        self.execute_command('clear_line', chr(line))

    def set_backlight(self, brightness):
        self.execute_command('backlight', chr(brightness))

    def set_cursor_position(self, row, column):
        self.execute_command('set_cursor_position', chr(row) + chr(column))

    def display_string(self, string):
        self.execute_command('display_string', string)

    def close(self):
        self.connection.deinit()

    def execute_command(self, command, payload):
        self.connection.send(self.commands[command] + payload + self.END)
