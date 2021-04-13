

import  PyQt5
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication

class Ui_home(object):
    def setupUix(self, home):
        home.setObjectName("home")
        home.resize(1183, 727)
        home.setStyleSheet("border-color: rgba(85, 255, 255, 100);")
        self.centralwidget = PyQt5.QtWidgets.QWidget(home)
        self.centralwidget.setObjectName("centralwidget")
        self.image = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.image.setGeometry(PyQt5.QtCore.QRect(20, 20, 111, 161))
        self.image.setStyleSheet("border:none;\n"
"")
        self.image.setText("")
        icon = PyQt5.QtGui.QIcon()
        icon.addPixmap(PyQt5.QtGui.QPixmap("icon/logo.png"), PyQt5.QtGui.QIcon.Normal, PyQt5.QtGui.QIcon.Off)
        self.image.setIcon(icon)
        self.image.setIconSize(PyQt5.QtCore.QSize(110, 330))
        self.image.setObjectName("image")
        self.Add = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(PyQt5.QtCore.QRect(20, 340, 131, 51))
        icon1 = PyQt5.QtGui.QIcon()
        icon1.addPixmap(PyQt5.QtGui.QPixmap("icon/add1.jpg"), PyQt5.QtGui.QIcon.Normal, PyQt5.QtGui.QIcon.Off)
        self.Add.setIcon(icon1)
        self.Add.setIconSize(PyQt5.QtCore.QSize(30, 30))
        self.Add.setObjectName("Add")
        self.Reports = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.Reports.setGeometry(PyQt5.QtCore.QRect(20, 420, 131, 51))
        icon2 = PyQt5.QtGui.QIcon()
        icon2.addPixmap(PyQt5.QtGui.QPixmap("icon/r3.png"), PyQt5.QtGui.QIcon.Normal, PyQt5.QtGui.QIcon.Off)
        self.Reports.setIcon(icon2)
        self.Reports.setIconSize(PyQt5.QtCore.QSize(30, 30))
        self.Reports.setObjectName("Reports")
        self.Result = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.Result.setGeometry(PyQt5.QtCore.QRect(20, 260, 131, 51))
        icon3 = PyQt5.QtGui.QIcon()
        icon3.addPixmap(PyQt5.QtGui.QPixmap("icon/g2.png"), PyQt5.QtGui.QIcon.Normal, PyQt5.QtGui.QIcon.Off)
        self.Result.setIcon(icon3)
        self.Result.setIconSize(PyQt5.QtCore.QSize(30, 30))
        self.Result.setObjectName("Result")
        self.Slider = PyQt5.QtWidgets.QTabWidget(self.centralwidget)
        self.Slider.setGeometry(PyQt5.QtCore.QRect(160, 10, 991, 681))
        self.Slider.setStyleSheet("color: rgb(0, 255, 255);\n"
"color: rgb(0, 0, 127);\n"
"font: 75 13pt \"Arial\";")
        self.Slider.setObjectName("Slider")
        self.login_3 = PyQt5.QtWidgets.QWidget()
        self.login_3.setObjectName("login_3")
        self.Login = PyQt5.QtWidgets.QGroupBox(self.login_3)
        self.Login.setGeometry(PyQt5.QtCore.QRect(200, 120, 541, 241))
        self.Login.setObjectName("Login")
        self.UserName = PyQt5.QtWidgets.QLineEdit(self.Login)
        self.UserName.setGeometry(PyQt5.QtCore.QRect(70, 50, 421, 31))
        self.UserName.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.UserName.setObjectName("UserName")
        self.Password = PyQt5.QtWidgets.QLineEdit(self.Login)
        self.Password.setGeometry(PyQt5.QtCore.QRect(70, 130, 421, 31))
        self.Password.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.Password.setObjectName("Password")
        self.Log = PyQt5.QtWidgets.QPushButton(self.Login)
        self.Log.setGeometry(PyQt5.QtCore.QRect(220, 190, 75, 23))
        self.Log.setObjectName("Log")
        self.Slider.addTab(self.login_3, "Login ")
        self.SerachSlider = PyQt5.QtWidgets.QWidget()
        self.SerachSlider.setObjectName("SerachSlider")
        self.ResultFrame = PyQt5.QtWidgets.QFrame(self.SerachSlider)
        self.ResultFrame.setGeometry(PyQt5.QtCore.QRect(100, 100, 711, 341))
        self.ResultFrame.setFrameShape(PyQt5.QtWidgets.QFrame.StyledPanel)
        self.ResultFrame.setFrameShadow(PyQt5.QtWidgets.QFrame.Raised)
        self.ResultFrame.setObjectName("ResultFrame")
        self.SearchBtn = PyQt5.QtWidgets.QPushButton(self.ResultFrame)
        self.SearchBtn.setGeometry(PyQt5.QtCore.QRect(322, 270, 75, 23))
        self.SearchBtn.setObjectName("SearchBtn")
        self.Levels = PyQt5.QtWidgets.QComboBox(self.ResultFrame)
        self.Levels.setGeometry(PyQt5.QtCore.QRect(132, 160, 451, 22))
        self.Levels.setObjectName("Levels")
        self.nationality = PyQt5.QtWidgets.QComboBox(self.ResultFrame)
        self.nationality.setGeometry(PyQt5.QtCore.QRect(132, 210, 451, 22))
        self.nationality.setObjectName("nationality")
        self.Department = PyQt5.QtWidgets.QComboBox(self.ResultFrame)
        self.Department.setGeometry(PyQt5.QtCore.QRect(132, 110, 451, 22))
        self.Department.setObjectName("Department")
        self.faculty = PyQt5.QtWidgets.QComboBox(self.ResultFrame)
        self.faculty.setGeometry(PyQt5.QtCore.QRect(130, 60, 451, 22))
        self.faculty.setObjectName("faculty")
        self.Slider.addTab(self.SerachSlider, "")
        self.SearchFrame = PyQt5.QtWidgets.QWidget()
        self.SearchFrame.setObjectName("SearchFrame")
        self.SearchBar = PyQt5.QtWidgets.QLineEdit(self.SearchFrame)
        self.SearchBar.setGeometry(PyQt5.QtCore.QRect(260, 90, 301, 31))
        self.SearchBar.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.SearchBar.setObjectName("SearchBar")
        self.SearchBtn_2 = PyQt5.QtWidgets.QPushButton(self.SearchFrame)
        self.SearchBtn_2.setGeometry(PyQt5.QtCore.QRect(700, 90, 101, 31))
        self.SearchBtn_2.setObjectName("SearchBtn_2")
        self.table = PyQt5.QtWidgets.QTableWidget(self.SearchFrame)
        self.table.setGeometry(PyQt5.QtCore.QRect(20, 150, 951, 461))
        self.table.setObjectName("table")
        self.table.setColumnCount(8)
        self.table.setRowCount(0)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        self.SreachBy = PyQt5.QtWidgets.QComboBox(self.SearchFrame)
        self.SreachBy.setGeometry(PyQt5.QtCore.QRect(570, 90, 111, 31))
        self.SreachBy.setObjectName("SreachBy")
        self.SreachBy.addItem("")
        self.SreachBy.setItemText(0, "")
        self.SreachBy.addItem("")
        self.SreachBy.addItem("")
        self.SreachBy.addItem("")
        self.SreachBy.addItem("")
        self.Slider.addTab(self.SearchFrame, "")
        self.addStudent = PyQt5.QtWidgets.QWidget()
        self.addStudent.setObjectName("addStudent")
        self.table_2 = PyQt5.QtWidgets.QTableWidget(self.addStudent)
        self.table_2.setGeometry(PyQt5.QtCore.QRect(10, 110, 951, 541))
        self.table_2.setObjectName("table_2")
        self.table_2.setColumnCount(8)
        self.table_2.setRowCount(0)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(0, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(1, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(2, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(3, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(4, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(5, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(6, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(7, item)
        self.Slider.addTab(self.addStudent, "")
        self.advanced = PyQt5.QtWidgets.QWidget()
        self.advanced.setObjectName("advanced")
        self.EditBar = PyQt5.QtWidgets.QScrollArea(self.advanced)
        self.EditBar.setGeometry(PyQt5.QtCore.QRect(9, 30, 961, 611))
        self.EditBar.setWidgetResizable(True)
        self.EditBar.setObjectName("EditBar")
        self.scrollAreaWidgetContents_3 = PyQt5.QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(PyQt5.QtCore.QRect(0, 0, 959, 609))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.FacultyDeen = PyQt5.QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.FacultyDeen.setGeometry(PyQt5.QtCore.QRect(30, 20, 901, 181))
        self.FacultyDeen.setObjectName("FacultyDeen")
        self.comboBox_22 = PyQt5.QtWidgets.QComboBox(self.FacultyDeen)
        self.comboBox_22.setGeometry(PyQt5.QtCore.QRect(290, 50, 531, 22))
        self.comboBox_22.setObjectName("comboBox_22")
        self.pushButton_15 = PyQt5.QtWidgets.QPushButton(self.FacultyDeen)
        self.pushButton_15.setGeometry(PyQt5.QtCore.QRect(400, 130, 75, 23))
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_7 = PyQt5.QtWidgets.QLabel(self.FacultyDeen)
        self.label_7.setGeometry(PyQt5.QtCore.QRect(120, 50, 101, 21))
        self.label_7.setObjectName("label_7")
        self.DepartmentManger = PyQt5.QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.DepartmentManger.setGeometry(PyQt5.QtCore.QRect(30, 260, 901, 231))
        self.DepartmentManger.setObjectName("DepartmentManger")
        self.comboBox_23 = PyQt5.QtWidgets.QComboBox(self.DepartmentManger)
        self.comboBox_23.setGeometry(PyQt5.QtCore.QRect(170, 60, 671, 22))
        self.comboBox_23.setObjectName("comboBox_23")
        self.pushButton_16 = PyQt5.QtWidgets.QPushButton(self.DepartmentManger)
        self.pushButton_16.setGeometry(PyQt5.QtCore.QRect(380, 170, 75, 23))
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_8 = PyQt5.QtWidgets.QLabel(self.DepartmentManger)
        self.label_8.setGeometry(PyQt5.QtCore.QRect(40, 62, 101, 21))
        self.label_8.setObjectName("label_8")
        self.comboBox_24 = PyQt5.QtWidgets.QComboBox(self.DepartmentManger)
        self.comboBox_24.setGeometry(PyQt5.QtCore.QRect(170, 118, 671, 22))
        self.comboBox_24.setObjectName("comboBox_24")
        self.label_9 = PyQt5.QtWidgets.QLabel(self.DepartmentManger)
        self.label_9.setGeometry(PyQt5.QtCore.QRect(40, 120, 101, 21))
        self.label_9.setObjectName("label_9")
        self.EditBar.setWidget(self.scrollAreaWidgetContents_3)
        self.Slider.addTab(self.advanced, "")
        self.ReportGraph = PyQt5.QtWidgets.QWidget()
        self.ReportGraph.setObjectName("ReportGraph")
        self.widget_3 = PyQt5.QtWidgets.QWidget(self.ReportGraph)
        self.widget_3.setGeometry(PyQt5.QtCore.QRect(90, 110, 851, 391))
        self.widget_3.setObjectName("widget_3")
        self.Slider.addTab(self.ReportGraph, "")
        self.Search = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.Search.setGeometry(PyQt5.QtCore.QRect(20, 500, 131, 51))
        icon4 = PyQt5.QtGui.QIcon()
        icon4.addPixmap(PyQt5.QtGui.QPixmap("icon/s1.png"), PyQt5.QtGui.QIcon.Normal, PyQt5.QtGui.QIcon.Off)
        self.Search.setIcon(icon4)
        self.Search.setIconSize(PyQt5.QtCore.QSize(20, 20))
        self.Search.setObjectName("Search")
        self.Settings = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.Settings.setGeometry(PyQt5.QtCore.QRect(20, 570, 131, 51))
        icon5 = PyQt5.QtGui.QIcon()
        icon5.addPixmap(PyQt5.QtGui.QPixmap("icon/seting1.png"), PyQt5.QtGui.QIcon.Normal, PyQt5.QtGui.QIcon.Off)
        self.Settings.setIcon(icon5)
        self.Settings.setIconSize(PyQt5.QtCore.QSize(30, 30))
        self.Settings.setObjectName("Settings")
        home.setCentralWidget(self.centralwidget)

        self.retranslateUi(home)
        self.Slider.setCurrentIndex(0)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "Al-Azhar"))
        # home.setWindowIcon(_translate())
        home.setWindowIcon(PyQt5.QtGui.QIcon('icon/logo.png'))

        self.Add.setText(_translate("home", "add"))
        self.Reports.setText(_translate("home", "reports "))
        self.Result.setText(_translate("home", "Resluts"))
        self.Login.setTitle(_translate("home", "Login"))
        self.UserName.setPlaceholderText(_translate("home", "User mail"))
        self.Password.setPlaceholderText(_translate("home", "Password"))
        self.Log.setText(_translate("home", "Log"))
        self.SearchBtn.setText(_translate("home", "Search"))
        self.Slider.setTabText(self.Slider.indexOf(self.SerachSlider), _translate("home", "Resluts"))
        self.SearchBar.setPlaceholderText(_translate("home", "Search by name or id"))
        self.SearchBtn_2.setText(_translate("home", "Search"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("home", "New Column"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("home", "id"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("home", "name"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("home", "mark"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("home", "New Column"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("home", "mark"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("home", "New Column"))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("home", "mark"))
        self.SreachBy.setItemText(1, _translate("home", "subject code"))
        self.SreachBy.setItemText(2, _translate("home", "student id"))
        self.SreachBy.setItemText(3, _translate("home", "subject name"))
        self.SreachBy.setItemText(4, _translate("home", "subject id"))
        self.Slider.setTabText(self.Slider.indexOf(self.SearchFrame), _translate("home", "search"))
        item = self.table_2.horizontalHeaderItem(0)
        item.setText(_translate("home", "New Column"))
        item = self.table_2.horizontalHeaderItem(1)
        item.setText(_translate("home", "id"))
        item = self.table_2.horizontalHeaderItem(2)
        item.setText(_translate("home", "name"))
        item = self.table_2.horizontalHeaderItem(3)
        item.setText(_translate("home", "mark"))
        item = self.table_2.horizontalHeaderItem(4)
        item.setText(_translate("home", "New Column"))
        item = self.table_2.horizontalHeaderItem(5)
        item.setText(_translate("home", "mark"))
        item = self.table_2.horizontalHeaderItem(6)
        item.setText(_translate("home", "New Column"))
        item = self.table_2.horizontalHeaderItem(7)
        item.setText(_translate("home", "mark"))
        self.Slider.setTabText(self.Slider.indexOf(self.addStudent), _translate("home", "addStrudents"))
        self.FacultyDeen.setTitle(_translate("home", "Faculty Deen"))
        self.pushButton_15.setText(_translate("home", "ok"))
        self.label_7.setText(_translate("home", "Select"))
        self.DepartmentManger.setTitle(_translate("home", "Department "))
        self.pushButton_16.setText(_translate("home", "ok"))
        self.label_8.setText(_translate("home", "Proffessor"))
        self.label_9.setText(_translate("home", "Deparment"))
        self.Slider.setTabText(self.Slider.indexOf(self.advanced), _translate("home", "settings"))
        self.Slider.setTabText(self.Slider.indexOf(self.ReportGraph), _translate("home", "Reports"))
        self.Search.setText(_translate("home", "Search"))
        self.Settings.setText(_translate("home", "settings"))



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    home = PyQt5.QtWidgets.QMainWindow()
    ui = Ui_home()
    

    ui.setupUix(home)
    home.show()
    sys.exit(app.exec_())
