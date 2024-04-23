from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_test import Ui_Dialog  # Import the generated class
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Assuming you've already set up the UI
        self.ui.setupUi(self)
        # Create a Python variable to store checkbox state
        self.checkbox_variables = {
            self.ui.CB_Monday: False,
            self.ui.CB_Tuesday: False,
            self.ui.CB_Wednesday: False,
            self.ui.CB_Thursday: False,
            self.ui.CB_Friday: False,
            self.ui.CB_Saturday: False,
            self.ui.CB_Sunday: False,
            self.ui.CB_Classic: False,
            self.ui.CB_Aram: False,
            self.ui.CB_CustomGame: False,
            self.ui.CB_MatchedGame: False,
            self.ui.CB_PracticeTool: False,
            # Add more checkboxes and variables as needed
        }
        for checkbox in self.checkbox_variables:
            checkbox.stateChanged.connect(self.handle_checkbox_state)

        self.spinbox_variables = {
            self.TimeOffset: 0
            }
    def handle_checkbox_state(self, state):
        # Find the checkbox that triggered the signal
        sender_checkbox = self.sender()
        # Update the associated Python variable based on checkbox state
        self.checkbox_variables[sender_checkbox] = state == 2
        # Example: Print the state of the checkbox
        print(f"{sender_checkbox.text()}: {'Checked' if self.checkbox_variables[sender_checkbox] else 'Unchecked'}")
    def get_checkbox_state (self):
        test = {}
        for checkbox in self.checkbox_variables:
            test[checkbox.text()] = self.checkbox_variables[checkbox]
        return test
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
