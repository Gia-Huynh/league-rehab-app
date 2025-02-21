import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
import sys
from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, Qt
from Main_UI import Ui_Dialog  # Import the generated class
import util_function, ast, json
class MyMainWindow(QMainWindow):
    def loadConfig (self, CONFIG_FILE_LOCATION = "params.ini"):
        self.ConfigData = util_function.load_config (CONFIG_FILE_LOCATION)
        self.checkbox_variables = {
            self.ui.CB_Monday: False,
            self.ui.CB_Tuesday: False,
            self.ui.CB_Wednesday: False,
            self.ui.CB_Thursday: False,
            self.ui.CB_Friday: False,
            self.ui.CB_Saturday: False,
            self.ui.CB_Sunday: False,
            self.ui.CB_Classic: self.ConfigData["GameModeList"]["classic"] == '1',
            self.ui.CB_Aram: self.ConfigData["GameModeList"]["aram"] == '1',
            self.ui.CB_PracticeTool: self.ConfigData["GameModeList"]["practicetool"] == '1',
            self.ui.CB_CustomGame: self.ConfigData["GameTypeList"]["matched_game"]== '1',
            self.ui.CB_MatchedGame: self.ConfigData["GameTypeList"]["custom_game"]== '1',
        }
        self.spinbox_variables = {
            self.ui.TimeOffset: self.ConfigData["CoreSetting"]["timeoffset"],
            self.ui.CheckingDuration: 0,
            self.ui.MinGameLength: 0,
            self.ui.MaxGameCount: 0,
            self.ui.MaxGameLength: 0,
            #DateTime
            self.ui.TimeFrameBegin: 0,
            self.ui.TimeFrameEnd: 0
            }
    def updateUI (self):
        for checkbox in self.checkbox_variables:
            checkbox.setCheckState(PySide6.QtCore.Qt.CheckState (2*(self.checkbox_variables[checkbox] == True)))
        self.ui.TimeOffset.setValue (int(self.ConfigData["CoreSetting"]["timeoffset"]))
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setRowCount(len(ast.literal_eval(self.ConfigData["limits"]['limits'])))
        rowPosition = self.ui.tableWidget.rowCount()
        rowPosition = 0
        for nigger in ast.literal_eval(self.ConfigData["limits"]['limits']):
            #print (nigga)
            #nigger = nigga)
            print (nigger)
            self.ui.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(nigger[5])))
            self.ui.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(nigger[4])))
            self.ui.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(nigger[0])))
            self.ui.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(nigger[1])))
            self.ui.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(nigger[2])))
            self.ui.tableWidget.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(str(nigger[3])))
            self.ui.tableWidget.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem(str(nigger[6])))
            rowPosition += 1
    def addOneLimit (self):
        oneLimit = [-1, -1, -1, 24, [0, 1, 2, 3, 4, 5, 6], [0, 4], 'Everyday, auto turn off lol at 00:00'] #Temp variable
        indexBinding = {0: self.ui.MaxGameCount,
                        1: self.ui.MinGameLength,
                        2: self.ui.MaxGameLength,
                        3: self.ui.CheckingDuration
                        }
        for i in indexBinding.keys():
            oneLimit[i] = self.spinbox_variables[indexBinding[i]]
        #timeFrame
        oneLimit[5] = [self.spinbox_variables[self.ui.TimeFrameBegin].hour(), self.spinbox_variables[self.ui.TimeFrameEnd].hour()]
        #LimitName
        oneLimit[6] = self.ui.plainTextEdit.toPlainText()
        #DayInWeek
        DayInWeekBinding = {
            self.ui.CB_Monday: 0,
            self.ui.CB_Tuesday: 1,
            self.ui.CB_Wednesday: 2,
            self.ui.CB_Thursday: 3,
            self.ui.CB_Friday: 4,
            self.ui.CB_Saturday: 5,
            self.ui.CB_Sunday: 6,
        }
        oneLimit[4] = [DayInWeekBinding[i] for i in DayInWeekBinding.keys() if self.checkbox_variables[i] == True]
        limitString = '%s' % json.dumps(oneLimit)
        self.ConfigData["limits"]['limits'] = self.ConfigData["limits"]['limits'][0] + limitString + ',\n'+self.ConfigData["limits"]['limits'][1:]
        self.updateUI()
    def removeLimit (self):
        #print (self.ui.tableWidget.selectionModel().selectedIndexes().row())
        RowList = sorted(list(set([i.row() for i in self.ui.tableWidget.selectionModel().selectedIndexes()])))[::-1]
        ay = ast.literal_eval(self.ConfigData["limits"]['limits'])
        for i in RowList:
            del ay[i]
        FinalString = '%s' % json.dumps(ay[0])
        for i in range (1, len(ay)):
            FinalString = FinalString + ',\n' + '%s' % json.dumps(ay[i])
        self.ConfigData["limits"]["limits"] = '['+FinalString+']'
        self.updateUI()
        #pass
    def ExportConfig (self):
        util_function.save_config (self.ConfigData, "params.ini")
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Assuming you've already set up the UI
        self.ui.setupUi(self)
        self.loadConfig ()
        self.updateUI()
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        #Check_box_related
        self.checkboxName_variables = {}
        for checkbox in self.checkbox_variables:
            self.checkboxName_variables [checkbox.objectName()] = self.checkbox_variables[checkbox]
            checkbox.stateChanged.connect(self.handle_checkbox_state)
            
        #Spinbox related
        self.spinboxName_variables = {}
        for spinbox in self.spinbox_variables:
            self.spinboxName_variables [spinbox.objectName()] = self.spinbox_variables[spinbox]
            try:
                spinbox.textChanged.connect(self.handle_spinbox_state)
            except Exception:
                spinbox.timeChanged.connect(self.handle_spinbox_state)
                            
        #Select day in week button
        self.ui.SelectAllDay.clicked.connect(self.toggle_allday_checkboxes)
        self.ui.SelectWeekday.clicked.connect(self.toggle_weekday_checkboxes)
        self.ui.SelectWeekend.clicked.connect(self.toggle_weekend_checkboxes)
        self.ui.Button_AddLimit.clicked.connect(self.addOneLimit)
        self.ui.Button_RemoveLimit.clicked.connect(self.removeLimit)
        self.ui.Button_Export_Config.clicked.connect(self.ExportConfig)
        #self.ui.TimeFrameBegin.timeChanged.connect(self.handle_spinbox_state)
        #self.ui.TimeFrameEnd.timeChanged.connect(self.handle_spinbox_state)

        self.all_day_in_week = {
            self.ui.CB_Monday,self.ui.CB_Tuesday,self.ui.CB_Wednesday,self.ui.CB_Thursday,self.ui.CB_Friday,self.ui.CB_Saturday,self.ui.CB_Sunday
            }
        self.weekend = {
            self.ui.CB_Saturday,self.ui.CB_Sunday
            }
    def toggle_allday_checkboxes(self):
        for checkbox in self.all_day_in_week:
            checkbox.setChecked(True)
    def toggle_weekday_checkboxes(self):
        for checkbox in self.all_day_in_week:
            checkbox.setChecked(False)
        for checkbox in self.all_day_in_week:
            if checkbox not in (self.weekend):
                checkbox.setChecked(True)
    def toggle_weekend_checkboxes(self):
        for checkbox in self.all_day_in_week:
            checkbox.setChecked(False)
        for checkbox in self.weekend:
            checkbox.setChecked(True)
    def handle_spinbox_state(self, state):
        sender_spinbox = self.sender()
        self.spinbox_variables[sender_spinbox] = state
        self.spinboxName_variables[sender_spinbox.objectName()] = state
        print(f"{sender_spinbox.objectName()}: {state}")
    def handle_checkbox_state(self, state):
        # Find the checkbox that triggered the signal
        sender_checkbox = self.sender()
        # Update the associated Python variable based on checkbox state
        self.checkbox_variables[sender_checkbox] = state == 2
        self.checkboxName_variables [sender_checkbox.objectName()] = state == 2
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
