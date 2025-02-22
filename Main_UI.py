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
    QFrame, QGridLayout, QHeaderView, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpinBox,
    QTableWidget, QTableWidgetItem, QTimeEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1161, 808)
        self.GameModeFrame = QFrame(Dialog)
        self.GameModeFrame.setObjectName(u"GameModeFrame")
        self.GameModeFrame.setGeometry(QRect(10, 10, 841, 151))
        self.GameModeFrame.setMinimumSize(QSize(651, 109))
        font = QFont()
        font.setPointSize(12)
        self.GameModeFrame.setFont(font)
        self.GameModeFrame.setFrameShape(QFrame.StyledPanel)
        self.GameModeFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.GameModeFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.CB_CustomGame = QCheckBox(self.GameModeFrame)
        self.CB_CustomGame.setObjectName(u"CB_CustomGame")
        self.CB_CustomGame.setFont(font)

        self.gridLayout_2.addWidget(self.CB_CustomGame, 3, 2, 1, 1)

        self.CB_PracticeTool = QCheckBox(self.GameModeFrame)
        self.CB_PracticeTool.setObjectName(u"CB_PracticeTool")
        self.CB_PracticeTool.setFont(font)

        self.gridLayout_2.addWidget(self.CB_PracticeTool, 1, 1, 1, 1)

        self.CB_Classic = QCheckBox(self.GameModeFrame)
        self.CB_Classic.setObjectName(u"CB_Classic")
        self.CB_Classic.setFont(font)

        self.gridLayout_2.addWidget(self.CB_Classic, 1, 0, 1, 1)

        self.CB_Aram = QCheckBox(self.GameModeFrame)
        self.CB_Aram.setObjectName(u"CB_Aram")
        self.CB_Aram.setFont(font)

        self.gridLayout_2.addWidget(self.CB_Aram, 3, 0, 1, 1)

        self.TimeOffset = QSpinBox(self.GameModeFrame)
        self.TimeOffset.setObjectName(u"TimeOffset")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TimeOffset.sizePolicy().hasHeightForWidth())
        self.TimeOffset.setSizePolicy(sizePolicy)
        self.TimeOffset.setFont(font)
        self.TimeOffset.setMaximum(24)

        self.gridLayout_2.addWidget(self.TimeOffset, 4, 1, 2, 1)

        self.label = QLabel(self.GameModeFrame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)

        self.label_2 = QLabel(self.GameModeFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 4, 2, 1, 1, Qt.AlignVCenter)

        self.CB_MatchedGame = QCheckBox(self.GameModeFrame)
        self.CB_MatchedGame.setObjectName(u"CB_MatchedGame")
        self.CB_MatchedGame.setFont(font)

        self.gridLayout_2.addWidget(self.CB_MatchedGame, 1, 2, 1, 1)

        self.line = QFrame(self.GameModeFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 6, 0, 1, 3, Qt.AlignVCenter)

        self.PerLimit_2 = QLabel(self.GameModeFrame)
        self.PerLimit_2.setObjectName(u"PerLimit_2")

        self.gridLayout_2.addWidget(self.PerLimit_2, 0, 0, 1, 3, Qt.AlignTop)

        self.CB_Classic.raise_()
        self.CB_Aram.raise_()
        self.TimeOffset.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.CB_PracticeTool.raise_()
        self.CB_CustomGame.raise_()
        self.CB_MatchedGame.raise_()
        self.line.raise_()
        self.PerLimit_2.raise_()
        self.LimitTimeFrame = QFrame(Dialog)
        self.LimitTimeFrame.setObjectName(u"LimitTimeFrame")
        self.LimitTimeFrame.setGeometry(QRect(10, 350, 1001, 161))
        self.LimitTimeFrame.setMinimumSize(QSize(651, 161))
        self.LimitTimeFrame.setFont(font)
        self.LimitTimeFrame.setFrameShape(QFrame.StyledPanel)
        self.LimitTimeFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.LimitTimeFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.SelectWeekend = QPushButton(self.LimitTimeFrame)
        self.SelectWeekend.setObjectName(u"SelectWeekend")
        self.SelectWeekend.setFont(font)

        self.gridLayout_4.addWidget(self.SelectWeekend, 6, 3, 1, 2)

        self.label_3 = QLabel(self.LimitTimeFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.SelectWeekday = QPushButton(self.LimitTimeFrame)
        self.SelectWeekday.setObjectName(u"SelectWeekday")
        self.SelectWeekday.setFont(font)

        self.gridLayout_4.addWidget(self.SelectWeekday, 6, 1, 1, 2)

        self.label_10 = QLabel(self.LimitTimeFrame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_4.addWidget(self.label_10, 4, 0, 1, 1)

        self.SelectAllDay = QPushButton(self.LimitTimeFrame)
        self.SelectAllDay.setObjectName(u"SelectAllDay")
        self.SelectAllDay.setFont(font)

        self.gridLayout_4.addWidget(self.SelectAllDay, 6, 5, 1, 2)

        self.label_5 = QLabel(self.LimitTimeFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_4.addWidget(self.label_5, 0, 1, 1, 1)

        self.TimeFrameEnd = QTimeEdit(self.LimitTimeFrame)
        self.TimeFrameEnd.setObjectName(u"TimeFrameEnd")
        self.TimeFrameEnd.setFont(font)

        self.gridLayout_4.addWidget(self.TimeFrameEnd, 0, 4, 1, 1)

        self.label_4 = QLabel(self.LimitTimeFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_4.addWidget(self.label_4, 0, 3, 1, 1, Qt.AlignHCenter)

        self.TimeFrameBegin = QTimeEdit(self.LimitTimeFrame)
        self.TimeFrameBegin.setObjectName(u"TimeFrameBegin")
        self.TimeFrameBegin.setFont(font)

        self.gridLayout_4.addWidget(self.TimeFrameBegin, 0, 2, 1, 1)

        self.CB_Monday = QCheckBox(self.LimitTimeFrame)
        self.CB_Monday.setObjectName(u"CB_Monday")
        self.CB_Monday.setFont(font)

        self.gridLayout_4.addWidget(self.CB_Monday, 4, 1, 1, 1)

        self.CB_Sunday = QCheckBox(self.LimitTimeFrame)
        self.CB_Sunday.setObjectName(u"CB_Sunday")
        self.CB_Sunday.setFont(font)

        self.gridLayout_4.addWidget(self.CB_Sunday, 4, 8, 1, 1)

        self.CB_Tuesday = QCheckBox(self.LimitTimeFrame)
        self.CB_Tuesday.setObjectName(u"CB_Tuesday")
        self.CB_Tuesday.setFont(font)

        self.gridLayout_4.addWidget(self.CB_Tuesday, 4, 2, 1, 1)

        self.CB_Wednesday = QCheckBox(self.LimitTimeFrame)
        self.CB_Wednesday.setObjectName(u"CB_Wednesday")
        self.CB_Wednesday.setFont(font)

        self.gridLayout_4.addWidget(self.CB_Wednesday, 4, 3, 1, 1)

        self.CB_Thursday = QCheckBox(self.LimitTimeFrame)
        self.CB_Thursday.setObjectName(u"CB_Thursday")
        self.CB_Thursday.setFont(font)

        self.gridLayout_4.addWidget(self.CB_Thursday, 4, 4, 1, 1)

        self.CB_Friday = QCheckBox(self.LimitTimeFrame)
        self.CB_Friday.setObjectName(u"CB_Friday")
        self.CB_Friday.setFont(font)

        self.gridLayout_4.addWidget(self.CB_Friday, 4, 5, 1, 1)

        self.CB_Saturday = QCheckBox(self.LimitTimeFrame)
        self.CB_Saturday.setObjectName(u"CB_Saturday")
        self.CB_Saturday.setFont(font)

        self.gridLayout_4.addWidget(self.CB_Saturday, 4, 6, 1, 1)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 540, 1121, 266))
        self.frame.setMinimumSize(QSize(651, 266))
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Button_AddLimit = QPushButton(self.frame)
        self.Button_AddLimit.setObjectName(u"Button_AddLimit")
        self.Button_AddLimit.setFont(font)

        self.gridLayout_5.addWidget(self.Button_AddLimit, 0, 0, 1, 1)

        self.Button_RemoveLimit = QPushButton(self.frame)
        self.Button_RemoveLimit.setObjectName(u"Button_RemoveLimit")
        self.Button_RemoveLimit.setFont(font)

        self.gridLayout_5.addWidget(self.Button_RemoveLimit, 0, 1, 1, 1)

        self.Button_Export_Config = QPushButton(self.frame)
        self.Button_Export_Config.setObjectName(u"Button_Export_Config")
        self.Button_Export_Config.setFont(font)

        self.gridLayout_5.addWidget(self.Button_Export_Config, 0, 2, 1, 1)

        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font1 = QFont()
        font1.setPointSize(8)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.gridLayout_5.addWidget(self.tableWidget, 1, 0, 1, 3)

        self.LimitValue = QFrame(Dialog)
        self.LimitValue.setObjectName(u"LimitValue")
        self.LimitValue.setGeometry(QRect(10, 160, 861, 181))
        self.LimitValue.setMinimumSize(QSize(651, 141))
        self.LimitValue.setFont(font)
        self.LimitValue.setFrameShape(QFrame.StyledPanel)
        self.LimitValue.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.LimitValue)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(25)
        self.label_14 = QLabel(self.LimitValue)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout.addWidget(self.label_14, 3, 2, 1, 1)

        self.MinGameLength = QSpinBox(self.LimitValue)
        self.MinGameLength.setObjectName(u"MinGameLength")
        self.MinGameLength.setFont(font)
        self.MinGameLength.setMinimum(-1)
        self.MinGameLength.setMaximum(9999)

        self.gridLayout.addWidget(self.MinGameLength, 2, 1, 1, 1)

        self.label_13 = QLabel(self.LimitValue)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.gridLayout.addWidget(self.label_13, 2, 2, 1, 1)

        self.label_6 = QLabel(self.LimitValue)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.MaxGameCount = QSpinBox(self.LimitValue)
        self.MaxGameCount.setObjectName(u"MaxGameCount")
        self.MaxGameCount.setFont(font)
        self.MaxGameCount.setMinimum(-1)
        self.MaxGameCount.setMaximum(99999)

        self.gridLayout.addWidget(self.MaxGameCount, 1, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.LimitValue)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFont(font)

        self.gridLayout.addWidget(self.plainTextEdit, 2, 3, 3, 1)

        self.LimitName = QLabel(self.LimitValue)
        self.LimitName.setObjectName(u"LimitName")
        self.LimitName.setFont(font)
        self.LimitName.setLayoutDirection(Qt.LeftToRight)
        self.LimitName.setScaledContents(False)
        self.LimitName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.LimitName, 1, 3, 1, 1)

        self.MaxGameLength = QSpinBox(self.LimitValue)
        self.MaxGameLength.setObjectName(u"MaxGameLength")
        self.MaxGameLength.setFont(font)
        self.MaxGameLength.setMinimum(-1)
        self.MaxGameLength.setMaximum(9999)

        self.gridLayout.addWidget(self.MaxGameLength, 3, 1, 1, 1)

        self.CheckingDuration = QSpinBox(self.LimitValue)
        self.CheckingDuration.setObjectName(u"CheckingDuration")
        self.CheckingDuration.setFont(font)
        self.CheckingDuration.setMinimum(-1)
        self.CheckingDuration.setMaximum(9999)

        self.gridLayout.addWidget(self.CheckingDuration, 4, 1, 1, 1)

        self.label_8 = QLabel(self.LimitValue)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_12 = QLabel(self.LimitValue)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout.addWidget(self.label_12, 4, 2, 1, 1)

        self.label_7 = QLabel(self.LimitValue)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_9 = QLabel(self.LimitValue)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.PerLimit = QLabel(self.LimitValue)
        self.PerLimit.setObjectName(u"PerLimit")

        self.gridLayout.addWidget(self.PerLimit, 0, 0, 1, 4)

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
        self.LimitName.raise_()
        self.plainTextEdit.raise_()
        self.PerLimit.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"LoL Rehab App", None))
#if QT_CONFIG(tooltip)
        self.CB_CustomGame.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Do you want to count custom games?</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CB_CustomGame.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Do you want to count custom games in your total play time?</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CB_CustomGame.setText(QCoreApplication.translate("Dialog", u"CUSTOM GAME", None))
        self.CB_PracticeTool.setText(QCoreApplication.translate("Dialog", u"PRACTICE TOOL", None))
#if QT_CONFIG(whatsthis)
        self.CB_Classic.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Do you want to count classic Summoner's Rift games?</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CB_Classic.setText(QCoreApplication.translate("Dialog", u"CLASSIC", None))
        self.CB_Aram.setText(QCoreApplication.translate("Dialog", u"ARAM", None))
#if QT_CONFIG(whatsthis)
        self.TimeOffset.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Entered 6 means that any game played before 6AM of a day will be counted as the day before, useful if you don't want to reset the gaming counter after midnight</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Entered 6 means that any game played before 6AM of a day will be counted as the day before, useful if you don't want to reset the gaming counter after midnight, prevent abusing by waiting after midnight to play right away.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Entered 6 means that any game played before 6AM of a day will be counted as the day before, useful if you don't want to reset the gaming counter after midnight</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("Dialog", u"Daily Time Offset:", None))
#if QT_CONFIG(whatsthis)
        self.label_2.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Entered 6 means that any game played before 6AM of a day will be counted as the day before, useful if you don't want to reset the gaming counter after midnight</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("Dialog", u"(hours)", None))
#if QT_CONFIG(tooltip)
        self.CB_MatchedGame.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Do you want to count normal match-making games?</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CB_MatchedGame.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Normal match-making game vs custom game?</p><p>This should be left toggled on.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.CB_MatchedGame.setText(QCoreApplication.translate("Dialog", u"MATCHED GAME", None))
        self.PerLimit_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Global Limit Setting (Will Apply to All Limits)</span></p></body></html>", None))
        self.SelectWeekend.setText(QCoreApplication.translate("Dialog", u"Select Only Weekend", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time in day that this limit is applicable. (Example: Only enforce limit after 6PM)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time in day that this limit is applicable. </p><p>(Example: Only enforce limit after 6PM)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Time Frame: ", None))
#if QT_CONFIG(whatsthis)
        self.SelectWeekday.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Monday through Friday</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.SelectWeekday.setText(QCoreApplication.translate("Dialog", u"Select Only Weekday", None))
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Day in week that this limit apply</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_10.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Day in week that this limit apply</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Day in week:", None))
        self.SelectAllDay.setText(QCoreApplication.translate("Dialog", u"Select All Days In Week", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time to begin checking for game</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_5.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time in day that this limit is applicable. </p><p>(Example: Only enforce limit after 6PM)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_5.setText(QCoreApplication.translate("Dialog", u"FROM ", None))
#if QT_CONFIG(tooltip)
        self.TimeFrameEnd.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Ending time</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Ending time</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Dialog", u"TO", None))
#if QT_CONFIG(tooltip)
        self.TimeFrameBegin.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time to begin checking for game</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CB_Monday.setText(QCoreApplication.translate("Dialog", u"Monday", None))
        self.CB_Sunday.setText(QCoreApplication.translate("Dialog", u"Sunday", None))
        self.CB_Tuesday.setText(QCoreApplication.translate("Dialog", u"Tuesday", None))
        self.CB_Wednesday.setText(QCoreApplication.translate("Dialog", u"Wednesday", None))
        self.CB_Thursday.setText(QCoreApplication.translate("Dialog", u"Thursday", None))
        self.CB_Friday.setText(QCoreApplication.translate("Dialog", u"Friday", None))
        self.CB_Saturday.setText(QCoreApplication.translate("Dialog", u"Saturday", None))
#if QT_CONFIG(whatsthis)
        self.Button_AddLimit.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Add the limit into the list</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Button_AddLimit.setText(QCoreApplication.translate("Dialog", u"Add Limit", None))
#if QT_CONFIG(whatsthis)
        self.Button_RemoveLimit.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Remove the selected limit from the list</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Button_RemoveLimit.setText(QCoreApplication.translate("Dialog", u"Remove Selected Rows of Limit", None))
#if QT_CONFIG(whatsthis)
        self.Button_Export_Config.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Save config to file</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Button_Export_Config.setText(QCoreApplication.translate("Dialog", u"Export config", None))
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
        self.label_14.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Entered 6 means that any game played before 6AM of a day will be counted as the day before, useful if you don't want to reset the gaming counter after midnight</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_14.setText(QCoreApplication.translate("Dialog", u"(minutes)", None))
#if QT_CONFIG(tooltip)
        self.MinGameLength.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Minimum of game time that makes you satisfied, in case you played 2 games in a row that enemy team surrender at 5 minutes.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_13.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Entered 6 means that any game played before 6AM of a day will be counted as the day before, useful if you don't want to reset the gaming counter after midnight</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_13.setText(QCoreApplication.translate("Dialog", u"(minutes)", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>If your total game time exceed this value, no more game. (Use in case of one long ass 70 minutes game for example)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_6.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>If your total game time exceed this value, no more game. (Use in case of one long ass 70 minutes game for example)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Maximum Total Game Length:", None))
#if QT_CONFIG(tooltip)
        self.MaxGameCount.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Maximum number of games allowed to play. (Game that is too short will be handled by the &quot;Very Satisfying Total Game Length&quot; box below)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.LimitName.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time frame for the limit, game played before this time is not counted.</p><p>Example: 24 hours for daily limit, 168 hours for 7 days limit, 672 hours for 30 days limit</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.LimitName.setText(QCoreApplication.translate("Dialog", u"Limit Name (Can be empty):", None))
#if QT_CONFIG(tooltip)
        self.MaxGameLength.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>If your total game time exceed this value, no more game. (Use in case of one long ass 70 minutes game for example)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.CheckingDuration.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time frame for the limit, game played before this time is not counted.</p><p>Example: 24 hours for daily limit, 168 hours for 7 days limit, 672 hours for 30 days limit</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.CheckingDuration.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time frame for the limit, game played before this time is not counted.</p><p>Example: 24 hours for daily limit, 168 hours for 7 days limit, 672 hours for 30 days limit</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Maximum number of games allowed to play. (Game that is too short will be handled by the &quot;Very Satisfying Total Game Length&quot; box below)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_8.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Maximum number of games allowed to play. (Game that is too short will be handled by the &quot;Very Satisfying Total Game Length&quot; box below)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Max Game Count:", None))
#if QT_CONFIG(whatsthis)
        self.label_12.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Entered 6 means that any game played before 6AM of a day will be counted as the day before, useful if you don't want to reset the gaming counter after midnight</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_12.setText(QCoreApplication.translate("Dialog", u"(hours)", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Minimum of game time that makes you satisfied, in case you played 2 games in a row that enemy team surrender at 5 minutes.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_7.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Minimum of game time that makes you satisfied, in case you played 2 games in a row that enemy team surrender at 5 minutes.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Satisfying Total Game Length:", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time frame for the limit, game played before this time is not counted.</p><p>Example: 24 hours for daily limit, 168 hours for 7 days limit, 672 hours for 30 days limit</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_9.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Time frame for the limit, game played before this time is not counted.</p><p>Example: 24 hours for daily limit, 168 hours for 7 days limit, 672 hours for 30 days limit</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Checking Duration:", None))
        self.PerLimit.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Per Limit Setting</span></p></body></html>", None))
    # retranslateUi

