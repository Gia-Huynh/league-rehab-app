# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main User Interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QDialog,
    QFrame, QHeaderView, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QTimeEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(774, 767)
        self.Button_AddLimit = QPushButton(Dialog)
        self.Button_AddLimit.setObjectName(u"Button_AddLimit")
        self.Button_AddLimit.setGeometry(QRect(430, 480, 93, 28))
        self.Button_Export_Config = QPushButton(Dialog)
        self.Button_Export_Config.setObjectName(u"Button_Export_Config")
        self.Button_Export_Config.setGeometry(QRect(550, 730, 191, 28))
        self.Button_RemoveLimit = QPushButton(Dialog)
        self.Button_RemoveLimit.setObjectName(u"Button_RemoveLimit")
        self.Button_RemoveLimit.setGeometry(QRect(530, 480, 161, 28))
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(90, 140, 611, 20))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.LimitTimeFrame = QFrame(Dialog)
        self.LimitTimeFrame.setObjectName(u"LimitTimeFrame")
        self.LimitTimeFrame.setGeometry(QRect(90, 150, 591, 151))
        self.LimitTimeFrame.setFrameShape(QFrame.StyledPanel)
        self.LimitTimeFrame.setFrameShadow(QFrame.Raised)
        self.CB_Monday = QCheckBox(self.LimitTimeFrame)
        self.CB_Monday.setObjectName(u"CB_Monday")
        self.CB_Monday.setGeometry(QRect(20, 130, 71, 20))
        self.CB_Tuesday = QCheckBox(self.LimitTimeFrame)
        self.CB_Tuesday.setObjectName(u"CB_Tuesday")
        self.CB_Tuesday.setGeometry(QRect(100, 130, 81, 20))
        self.CB_Friday = QCheckBox(self.LimitTimeFrame)
        self.CB_Friday.setObjectName(u"CB_Friday")
        self.CB_Friday.setGeometry(QRect(360, 130, 81, 20))
        self.CB_Sunday = QCheckBox(self.LimitTimeFrame)
        self.CB_Sunday.setObjectName(u"CB_Sunday")
        self.CB_Sunday.setGeometry(QRect(510, 130, 81, 20))
        self.CB_Wednesday = QCheckBox(self.LimitTimeFrame)
        self.CB_Wednesday.setObjectName(u"CB_Wednesday")
        self.CB_Wednesday.setGeometry(QRect(180, 130, 91, 20))
        self.CB_Saturday = QCheckBox(self.LimitTimeFrame)
        self.CB_Saturday.setObjectName(u"CB_Saturday")
        self.CB_Saturday.setGeometry(QRect(430, 130, 81, 20))
        self.CB_Thursday = QCheckBox(self.LimitTimeFrame)
        self.CB_Thursday.setObjectName(u"CB_Thursday")
        self.CB_Thursday.setGeometry(QRect(280, 130, 81, 20))
        self.TimeFrameEnd = QTimeEdit(self.LimitTimeFrame)
        self.TimeFrameEnd.setObjectName(u"TimeFrameEnd")
        self.TimeFrameEnd.setGeometry(QRect(200, 30, 91, 22))
        self.SelectAllDay = QPushButton(self.LimitTimeFrame)
        self.SelectAllDay.setObjectName(u"SelectAllDay")
        self.SelectAllDay.setGeometry(QRect(300, 90, 151, 28))
        self.SelectWeekend = QPushButton(self.LimitTimeFrame)
        self.SelectWeekend.setObjectName(u"SelectWeekend")
        self.SelectWeekend.setGeometry(QRect(160, 90, 131, 28))
        self.TimeFrameBegin = QTimeEdit(self.LimitTimeFrame)
        self.TimeFrameBegin.setObjectName(u"TimeFrameBegin")
        self.TimeFrameBegin.setGeometry(QRect(60, 30, 101, 22))
        self.label_4 = QLabel(self.LimitTimeFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 30, 21, 20))
        self.label_3 = QLabel(self.LimitTimeFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 81, 20))
        self.SelectWeekday = QPushButton(self.LimitTimeFrame)
        self.SelectWeekday.setObjectName(u"SelectWeekday")
        self.SelectWeekday.setGeometry(QRect(20, 90, 131, 28))
        self.label_10 = QLabel(self.LimitTimeFrame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 70, 81, 20))
        self.label_5 = QLabel(self.LimitTimeFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 30, 41, 20))
        self.GameModeFrame = QFrame(Dialog)
        self.GameModeFrame.setObjectName(u"GameModeFrame")
        self.GameModeFrame.setGeometry(QRect(100, 10, 561, 131))
        self.GameModeFrame.setFrameShape(QFrame.StyledPanel)
        self.GameModeFrame.setFrameShadow(QFrame.Raised)
        self.CB_Classic = QCheckBox(self.GameModeFrame)
        self.CB_Classic.setObjectName(u"CB_Classic")
        self.CB_Classic.setGeometry(QRect(10, 10, 81, 20))
        self.CB_Aram = QCheckBox(self.GameModeFrame)
        self.CB_Aram.setObjectName(u"CB_Aram")
        self.CB_Aram.setGeometry(QRect(10, 40, 81, 20))
        self.CB_MatchedGame = QCheckBox(self.GameModeFrame)
        self.CB_MatchedGame.setObjectName(u"CB_MatchedGame")
        self.CB_MatchedGame.setGeometry(QRect(200, 10, 121, 20))
        self.label = QLabel(self.GameModeFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 100, 111, 20))
        self.CB_PracticeTool = QCheckBox(self.GameModeFrame)
        self.CB_PracticeTool.setObjectName(u"CB_PracticeTool")
        self.CB_PracticeTool.setGeometry(QRect(10, 70, 121, 20))
        self.TimeOffset = QSpinBox(self.GameModeFrame)
        self.TimeOffset.setObjectName(u"TimeOffset")
        self.TimeOffset.setGeometry(QRect(101, 100, 61, 22))
        self.TimeOffset.setMaximum(24)
        self.CB_CustomGame = QCheckBox(self.GameModeFrame)
        self.CB_CustomGame.setObjectName(u"CB_CustomGame")
        self.CB_CustomGame.setGeometry(QRect(200, 40, 111, 20))
        self.label_2 = QLabel(self.GameModeFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 100, 41, 20))
        self.LimitValue = QFrame(Dialog)
        self.LimitValue.setObjectName(u"LimitValue")
        self.LimitValue.setGeometry(QRect(50, 320, 341, 121))
        self.LimitValue.setFrameShape(QFrame.StyledPanel)
        self.LimitValue.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.LimitValue)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 30, 201, 20))
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8 = QLabel(self.LimitValue)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(110, 0, 101, 20))
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.MinGameLength = QSpinBox(self.LimitValue)
        self.MinGameLength.setObjectName(u"MinGameLength")
        self.MinGameLength.setGeometry(QRect(221, 30, 51, 22))
        self.MinGameLength.setMinimum(-1)
        self.MinGameLength.setMaximum(9999)
        self.MaxGameCount = QSpinBox(self.LimitValue)
        self.MaxGameCount.setObjectName(u"MaxGameCount")
        self.MaxGameCount.setGeometry(QRect(221, 0, 51, 22))
        self.MaxGameCount.setMinimum(-1)
        self.MaxGameCount.setMaximum(99999)
        self.MaxGameLength = QSpinBox(self.LimitValue)
        self.MaxGameLength.setObjectName(u"MaxGameLength")
        self.MaxGameLength.setGeometry(QRect(221, 60, 51, 22))
        self.MaxGameLength.setMinimum(-1)
        self.MaxGameLength.setMaximum(9999)
        self.label_6 = QLabel(self.LimitValue)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-20, 60, 231, 20))
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_13 = QLabel(self.LimitValue)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(280, 30, 51, 20))
        self.label_14 = QLabel(self.LimitValue)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(280, 60, 51, 20))
        self.label_9 = QLabel(self.LimitValue)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(100, 90, 111, 20))
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_12 = QLabel(self.LimitValue)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(280, 90, 51, 20))
        self.CheckingDuration = QSpinBox(self.LimitValue)
        self.CheckingDuration.setObjectName(u"CheckingDuration")
        self.CheckingDuration.setGeometry(QRect(221, 90, 51, 22))
        self.CheckingDuration.setMinimum(-1)
        self.CheckingDuration.setMaximum(9999)
        self.CheckingDuration.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.MinGameLength.raise_()
        self.MaxGameCount.raise_()
        self.MaxGameLength.raise_()
        self.label_6.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_9.raise_()
        self.label_12.raise_()
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font = QFont()
        font.setPointSize(8)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 520, 701, 201))
        font1 = QFont()
        font1.setPointSize(10)
        self.tableWidget.setFont(font1)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.plainTextEdit = QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(430, 350, 261, 81))
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(430, 320, 121, 20))
        self.label_11.setLayoutDirection(Qt.LeftToRight)
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.LimitValue.raise_()
        self.GameModeFrame.raise_()
        self.LimitTimeFrame.raise_()
        self.Button_AddLimit.raise_()
        self.Button_Export_Config.raise_()
        self.Button_RemoveLimit.raise_()
        self.line.raise_()
        self.tableWidget.raise_()
        self.plainTextEdit.raise_()
        self.label_11.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(whatsthis)
        self.Button_AddLimit.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Add the limit into the list</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Button_AddLimit.setText(QCoreApplication.translate("Dialog", u"Add Limit", None))
#if QT_CONFIG(whatsthis)
        self.Button_Export_Config.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Save config to file</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Button_Export_Config.setText(QCoreApplication.translate("Dialog", u"Export config", None))
#if QT_CONFIG(whatsthis)
        self.Button_RemoveLimit.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Remove the selected limit from the list</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Button_RemoveLimit.setText(QCoreApplication.translate("Dialog", u"Remove Selected Rows of Limit", None))
        self.CB_Monday.setText(QCoreApplication.translate("Dialog", u"Monday", None))
        self.CB_Tuesday.setText(QCoreApplication.translate("Dialog", u"Tuesday", None))
        self.CB_Friday.setText(QCoreApplication.translate("Dialog", u"Friday", None))
        self.CB_Sunday.setText(QCoreApplication.translate("Dialog", u"Sunday", None))
        self.CB_Wednesday.setText(QCoreApplication.translate("Dialog", u"Wednesday", None))
        self.CB_Saturday.setText(QCoreApplication.translate("Dialog", u"Saturday", None))
        self.CB_Thursday.setText(QCoreApplication.translate("Dialog", u"Thursday", None))
#if QT_CONFIG(tooltip)
        self.TimeFrameEnd.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Ending time</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.SelectAllDay.setText(QCoreApplication.translate("Dialog", u"Select All Days In Week", None))
        self.SelectWeekend.setText(QCoreApplication.translate("Dialog", u"Select Only Weekend", None))
#if QT_CONFIG(tooltip)
        self.TimeFrameBegin.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time to begin checking for game</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Ending time</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Dialog", u"TO", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time in day that this limit is applicable. (Example: Only enforce limit after 6PM)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time in day that this limit is applicable. (Example: Only enforce limit after 6PM)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Time Frame: ", None))
        self.SelectWeekday.setText(QCoreApplication.translate("Dialog", u"Select Only Weekday", None))
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Day in week that this limit apply</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_10.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Day in week that this limit apply</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Day in week:", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time to begin checking for game</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Dialog", u"FROM ", None))
#if QT_CONFIG(whatsthis)
        self.CB_Classic.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Do you want to count classic Summoner's Rift games?</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CB_Classic.setText(QCoreApplication.translate("Dialog", u"CLASSIC", None))
        self.CB_Aram.setText(QCoreApplication.translate("Dialog", u"ARAM", None))
#if QT_CONFIG(tooltip)
        self.CB_MatchedGame.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Do you want to count normal match-making games?</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CB_MatchedGame.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Do you want to count normal match-making games?</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CB_MatchedGame.setText(QCoreApplication.translate("Dialog", u"MATCHED GAME", None))
#if QT_CONFIG(whatsthis)
        self.label.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Entered 6 means that any game played before 6AM of a day will be counted as the day before, useful if you don't want to reset the gaming counter after midnight</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("Dialog", u"Daily Time Offset:", None))
        self.CB_PracticeTool.setText(QCoreApplication.translate("Dialog", u"PRACTICE TOOL", None))
#if QT_CONFIG(tooltip)
        self.CB_CustomGame.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Do you want to count custom games?</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CB_CustomGame.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Do you want to count custom games?</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CB_CustomGame.setText(QCoreApplication.translate("Dialog", u"CUSTOM GAME", None))
#if QT_CONFIG(whatsthis)
        self.label_2.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Entered 6 means that any game played before 6AM of a day will be counted as the day before, useful if you don't want to reset the gaming counter after midnight</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("Dialog", u"(hours)", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Minimum of game time that makes you satisfied, in case you played 2 games in a row that enemy team surrender at 5 minutes.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_7.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Minimum of game time that makes you satisfied, in case you played 2 games in a row that enemy team surrender at 5 minutes.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Satisfying Total Game Length:", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Maximum number of games allowed to play. (Game that is too short will be handled by the &quot;Very Satisfying Total Game Length&quot; box below)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_8.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Maximum number of games allowed to play. (Game that is too short will be handled by the &quot;Very Satisfying Total Game Length&quot; box below)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Max Game Count:", None))
#if QT_CONFIG(tooltip)
        self.MinGameLength.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Minimum of game time that makes you satisfied, in case you played 2 games in a row that enemy team surrender at 5 minutes.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.MaxGameCount.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Maximum number of games allowed to play. (Game that is too short will be handled by the &quot;Very Satisfying Total Game Length&quot; box below)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.MaxGameLength.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>If your total game time exceed this value, no more game. (Use in case of one long ass 70 minutes game for example)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>If your total game time exceed this value, no more game. (Use in case of one long ass 70 minutes game for example)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_6.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>If your total game time exceed this value, no more game. (Use in case of one long ass 70 minutes game for example)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Maximum Total Game Length:", None))
#if QT_CONFIG(whatsthis)
        self.label_13.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Entered 6 means that any game played before 6AM of a day will be counted as the day before, useful if you don't want to reset the gaming counter after midnight</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_13.setText(QCoreApplication.translate("Dialog", u"(minutes)", None))
#if QT_CONFIG(whatsthis)
        self.label_14.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Entered 6 means that any game played before 6AM of a day will be counted as the day before, useful if you don't want to reset the gaming counter after midnight</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_14.setText(QCoreApplication.translate("Dialog", u"(minutes)", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time frame for the limit, game played before this time is not counted.</p><p>Example: 24 hours for daily limit, 168 hours for 7 days limit, 672 hours for 30 days limit</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_9.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time frame for the limit, game played before this time is not counted.</p><p>Example: 24 hours for daily limit, 168 hours for 7 days limit, 672 hours for 30 days limit</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Checking Duration:", None))
#if QT_CONFIG(whatsthis)
        self.label_12.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Entered 6 means that any game played before 6AM of a day will be counted as the day before, useful if you don't want to reset the gaming counter after midnight</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_12.setText(QCoreApplication.translate("Dialog", u"(hours)", None))
#if QT_CONFIG(tooltip)
        self.CheckingDuration.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time frame for the limit, game played before this time is not counted.</p><p>Example: 24 hours for daily limit, 168 hours for 7 days limit, 672 hours for 30 days limit</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CheckingDuration.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time frame for the limit, game played before this time is not counted.</p><p>Example: 24 hours for daily limit, 168 hours for 7 days limit, 672 hours for 30 days limit</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Time Frame", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Day In Week", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Max Game Count", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Satisfying Game Length", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Hard Limit Game Length", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Checking Duration", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Name", None));
#if QT_CONFIG(whatsthis)
        self.label_11.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time frame for the limit, game played before this time is not counted.</p><p>Example: 24 hours for daily limit, 168 hours for 7 days limit, 672 hours for 30 days limit</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Name (Can be empty):", None))
    # retranslateUi
