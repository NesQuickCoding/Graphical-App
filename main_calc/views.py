from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

class MainCalcUI(QWidget):
    def __init__(self, dropMenu):
        super().__init__()
        self.setFixedSize(400, 400)
        layout = QVBoxLayout()
        self.calcOutput = self._createCalcOutput()
        layout.addWidget(self.calcOutput)
        self.calcDropBox = self._createDropBox(dropMenu)
        layout.addWidget(self.calcDropBox)
        buttonLayout = self._createButtons()
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    def _createCalcOutput(self):
        output = QLineEdit()
        output.setFixedHeight(50)
        output.setAlignment(Qt.AlignRight)
        output.setReadOnly(True)
        return output       

    def _createDropBox(self, dropMenu):
        comboBox = QComboBox()
        comboBox.setObjectName("CalcDropBox")
        comboBox.setGeometry(QtCore.QRect(130, 190, 291, 31))
        for item in dropMenu:
            comboBox.addItem(item[0])
        return comboBox

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "/": (0, 3),
            "C": (0, 4),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "*": (1, 3),
            "(": (1, 4),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "-": (2, 3),
            ")": (2, 4),
            "0": (3, 0),
            "00": (3, 1),
            ".": (3, 2),
            "+": (3, 3),
            "=": (3, 4),
        }

        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(55, 55)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])

        return buttonsLayout

    def setDisplayText(self, text):
        """Set display's text."""
        self.calcOutput.setText(text)
        self.calcOutput.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.calcOutput.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")

# Create a subclass of QMainWindow to setup the calculator's GUI
# class MainCalcUi(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.calcMain = MainCalc()
#         self.calcSide = CalcSide()
#         self.generalLayout.addWidget(self.calcMain)
#         self.generalLayout.addWidget(self.calcSide)
