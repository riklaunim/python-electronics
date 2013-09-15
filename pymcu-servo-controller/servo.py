import sys

from PyQt4 import QtCore
from PyQt4 import QtGui
import pymcu

from servo_gui import Ui_MainWindow


class ServoApp(QtGui.QMainWindow):
    # This looks valid for TowerPro SG90 9G
    START_POSITION = 800
    END_POSITION = 2000
    CURRENT_POSITION = None

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.left, QtCore.SIGNAL("pressed()"), self.move_left)
        QtCore.QObject.connect(self.ui.right, QtCore.SIGNAL("pressed()"), self.move_right)
        self.mcu = pymcu.mcuModule()
        self._prepare_servo()

    def _prepare_servo(self):
        self.mcu.pulseOut(1, self.START_POSITION, 40)
        self.CURRENT_POSITION = self.START_POSITION
        self.ui.label.setText(str(self.CURRENT_POSITION))
        self._handle_edge_positions(self.CURRENT_POSITION)

    def move_left(self):
        self._move_servo(100)

    def move_right(self):
        self._move_servo(-100)

    def _move_servo(self, modifier):
        position = self._get_new_position(modifier)
        if self._position_allowed(position):
            self.mcu.pulseOut(1, position, 2)
            self._update_current_position(position)

    def _get_new_position(self, modifier):
        return self.CURRENT_POSITION + modifier

    def _update_current_position(self, position):
        self.CURRENT_POSITION = position
        self.ui.label.setText(str(position))
        self._handle_edge_positions(position)

    def _handle_edge_positions(self, position):
        if position == self.START_POSITION:
            self.ui.right.setEnabled(False)
        else:
            self.ui.right.setEnabled(True)

        if position == self.END_POSITION:
            self.ui.left.setEnabled(False)
        else:
            self.ui.left.setEnabled(True)

    def _position_allowed(self, position):
        return self.START_POSITION <= position <= self.END_POSITION


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = ServoApp()
    myapp.show()
    sys.exit(app.exec_())
