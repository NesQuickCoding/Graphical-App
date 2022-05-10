from PyQt5 import QtWidgets, uic

class ascii_Ui(QtWidgets.QWidget):
    def __init__(self):
        super(ascii_Ui, self).__init__()
        uic.loadUi('../Graphical-App/ascii_conversion/basic.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'enterButton')
        self.button.clicked.connect(self.printButtonPressed)
        self.input = self.findChild(QtWidgets.QLineEdit, 'lineEdit_Output')
        self.radioButtons = self.findChildren(QtWidgets.QRadioButton)

        self.show()

    def printButtonPressed(self):
        toggledButtons = [rb.text() for rb in self.radioButtons if rb.isChecked()]
        val = self.findChild(QtWidgets.QLineEdit, 'lineEdit_Input')
        answer = self.convert_ascii(self, val.text(), toggledButtons[0][0], toggledButtons[1][0])
        self.input.setText(str(answer))

    def convert_ascii(self, val, input_unit, output_unit):
        try:
            if input_unit == 'C':
                if output_unit == 'D':
                    return ord(val)
                elif output_unit == 'H':
                    return hex(ord(val))
                else:
                    return val

            elif input_unit == 'D':
                try:

                    if output_unit == 'C':
                        val = int(val)
                        return chr(val)

                    # Problem with this conversion H
                    elif output_unit == 'H':
                        return hex(int(val))
                    else:
                        return val
                except ValueError:
                    return "Invalid Input"
            elif input_unit == 'H':
                if output_unit == 'D':
                    return int(val,16)
                elif output_unit == 'C':
                    val_str = val[2:]
                    bytes_obj = bytes.fromhex(val_str)
                    ascii_str = bytes_obj.decode("ASCII")
                    return ascii_str
                else:
                    return val
            else:
                return "Invalid Input"

        except ValueError:
            return "Invalid Input"




# Char Test

#ans1 = convert_ascii('A','C','D')
#print(ans1)
#ans2 = convert_ascii('A','C','H')
#print(ans2)
#ans3 = convert_ascii('A','C','C')
#print(ans3)


# Dec Test
#ans1 = convert_ascii(69,'D','C')
#print(ans1)
#ans2 = convert_ascii(69, 'D','H')
#print(ans2)
#ans3 = convert_ascii(69,'D','D')
#print(ans3)


# Hex Test
#ans1 = convert_ascii("0x45",'H','D')
#print(ans1)
#ans2 = convert_ascii("0x45", 'H','C')
#print(ans2)
#ans3 = convert_ascii("0x45",'H','H')
#print(ans3)
