# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\wu\ericWorkplace\audioRecognization\audioGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(904, 461)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 651, 441))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.labelStatus = QtWidgets.QLabel(self.centralWidget)
        self.labelStatus.setGeometry(QtCore.QRect(670, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.labelStatus.setFont(font)
        self.labelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatus.setObjectName("labelStatus")
        self.pushButtonStart = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonStart.setGeometry(QtCore.QRect(700, 110, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.pushButtonStop = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonStop.setGeometry(QtCore.QRect(700, 200, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButtonStop.setFont(font)
        self.pushButtonStop.setObjectName("pushButtonStop")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle('❤熊本熊的語音辨識器❤ Bing Speech API')
        self.labelStatus.setText(_translate("MainWindow", "Status: Ready"))
        self.pushButtonStart.setText(_translate("MainWindow", "Start"))
        self.pushButtonStop.setText(_translate("MainWindow", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

