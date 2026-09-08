# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientSirvHm.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(588, 468)
        MainWindow.setMinimumSize(QSize(588, 468))
        MainWindow.setMaximumSize(QSize(588, 468))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InsertLink))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Google Sans"])
        font.setBold(False)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"/* =========================================================\n"
"   NEO-SKEUO / CLIENT MANAGER\n"
"   Qt Widgets QSS\n"
"   ========================================================= */\n"
"\n"
"* {\n"
"    font-family: \"Google Sans\";\n"
"    font-size: 13px;\n"
"    color: #242424;\n"
"}\n"
"\n"
"/* =========================================================\n"
"   MAIN WINDOW\n"
"   ========================================================= */\n"
"\n"
"QWidget {\n"
"    background: #eeeae1;\n"
"}\n"
"\n"
"QMainWindow,\n"
"QWidget#centralWidget {\n"
"    background:\n"
"        qlineargradient(\n"
"            x1: 0, y1: 0,\n"
"            x2: 0, y2: 1,\n"
"            stop: 0 #f5f2eb,\n"
"            stop: 1 #e5e1d8\n"
"        );\n"
"}\n"
"\n"
"/* =========================================================\n"
"   LABELS\n"
"   ========================================================= */\n"
"\n"
"QLabel {\n"
"    background: transparent;\n"
"    color: #292929;\n"
"    padding: 2px 3px;\n"
"}\n"
"\n"
"QLabel:hov"
                        "er {\n"
"    color: #111111;\n"
"}\n"
"\n"
"/* IP / PORT / USERNAME labels */\n"
"QLabel#ipLabel,\n"
"QLabel#portLabel,\n"
"QLabel#usernameLabel {\n"
"    font-weight: 500;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* =========================================================\n"
"   LIST\n"
"   ========================================================= */\n"
"\n"
"QListWidget {\n"
"    background:\n"
"        qlineargradient(\n"
"            x1: 0, y1: 0,\n"
"            x2: 0, y2: 1,\n"
"            stop: 0 #faf9f5,\n"
"            stop: 1 #eeeae2\n"
"        );\n"
"\n"
"    border: 1px solid #858585;\n"
"    border-radius: 2px;\n"
"\n"
"    padding: 6px;\n"
"\n"
"    outline: none;\n"
"\n"
"    /* subtle inset-like shadow */\n"
"    selection-background-color: #d9d5cc;\n"
"    selection-color: #171717;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background: transparent;\n"
"\n"
"    border: 1px solid transparent;\n"
"    border-radius: 3px;\n"
"\n"
"    padding: 3px 4px;\n"
"    margin: 1px 0;\n"
"}\n"
"\n"
"QList"
                        "Widget::item:hover {\n"
"    background:\n"
"        qlineargradient(\n"
"            x1: 0, y1: 0,\n"
"            x2: 0, y2: 1,\n"
"            stop: 0 #f4f2ed,\n"
"            stop: 1 #dedbd3\n"
"        );\n"
"\n"
"    border: 1px solid #b7b3aa;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background:\n"
"        qlineargradient(\n"
"            x1: 0, y1: 0,\n"
"            x2: 0, y2: 1,\n"
"            stop: 0 #e5e1d8,\n"
"            stop: 1 #cbc7be\n"
"        );\n"
"\n"
"    color: #111111;\n"
"\n"
"    border: 1px solid #9b978e;\n"
"}\n"
"\n"
"/* =========================================================\n"
"   LINE EDIT\n"
"   ========================================================= */\n"
"\n"
"QLineEdit {\n"
"    background:\n"
"        qlineargradient(\n"
"            x1: 0, y1: 0,\n"
"            x2: 0, y2: 1,\n"
"            stop: 0 #ffffff,\n"
"            stop: 0.08 #fafafa,\n"
"            stop: 1 #ebe9e4\n"
"        );\n"
"\n"
"    border: 1px solid #858585;\n"
"    border-radius: 2px"
                        ";\n"
"\n"
"    padding: 5px 7px;\n"
"\n"
"    selection-background-color: #c9c5bc;\n"
"    selection-color: #111111;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #686868;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background: #ffffff;\n"
"    border: 1px solid #555555;\n"
"}\n"
"\n"
"/* Placeholder */\n"
"QLineEdit[placeholderText] {\n"
"    color: #77736c;\n"
"}\n"
"\n"
"/* =========================================================\n"
"   BUTTONS\n"
"   ========================================================= */\n"
"\n"
"QPushButton {\n"
"    background:\n"
"        qlineargradient(\n"
"            x1: 0, y1: 0,\n"
"            x2: 0, y2: 1,\n"
"\n"
"            stop: 0 #faf9f5,\n"
"            stop: 0.45 #e9e6df,\n"
"            stop: 0.55 #dedbd3,\n"
"            stop: 1 #c9c5bc\n"
"        );\n"
"\n"
"    border: 1px solid #77746d;\n"
"    border-radius: 3px;\n"
"\n"
"    padding: 5px 14px;\n"
"\n"
"    color: #252525;\n"
"\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    ba"
                        "ckground:\n"
"        qlineargradient(\n"
"            x1: 0, y1: 0,\n"
"            x2: 0, y2: 1,\n"
"\n"
"            stop: 0 #ffffff,\n"
"            stop: 0.45 #f0eee9,\n"
"            stop: 0.55 #e4e1da,\n"
"            stop: 1 #d2cfc7\n"
"        );\n"
"\n"
"    border: 1px solid #555555;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:\n"
"        qlineargradient(\n"
"            x1: 0, y1: 0,\n"
"            x2: 0, y2: 1,\n"
"\n"
"            stop: 0 #c6c2b9,\n"
"            stop: 0.5 #d1cec6,\n"
"            stop: 1 #e3e0d9\n"
"        );\n"
"\n"
"    border: 1px solid #555555;\n"
"\n"
"    padding-top: 6px;\n"
"    padding-bottom: 4px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #dedbd4;\n"
"    color: #99958e;\n"
"    border: 1px solid #aaa69e;\n"
"}\n"
"\n"
"/* =========================================================\n"
"   SEND BUTTON\n"
"   ========================================================= */\n"
"\n"
"QPushButton#sendButton {\n"
"    min-width: 55px;\n"
"}\n"
"\n"
""
                        "/* =========================================================\n"
"   CONNECT BUTTON\n"
"   ========================================================= */\n"
"\n"
"QPushButton#connectButton {\n"
"    min-height: 20px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton#connectButton:hover {\n"
"    background:\n"
"        qlineargradient(\n"
"            x1: 0, y1: 0,\n"
"            x2: 0, y2: 1,\n"
"\n"
"            stop: 0 #ffffff,\n"
"            stop: 0.5 #eae7e0,\n"
"            stop: 1 #d0ccc4\n"
"        );\n"
"}\n"
"\n"
"/* =========================================================\n"
"   GROUPBOX\n"
"   ========================================================= */\n"
"\n"
"QGroupBox {\n"
"    background: transparent;\n"
"\n"
"    border: 1px solid #aaa69d;\n"
"    border-radius: 4px;\n"
"\n"
"    margin-top: 10px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"\n"
"    padding: 0 5px;\n"
"\n"
"    background: #eeeae1;\n"
"    color: #4b49"
                        "45;\n"
"}\n"
"\n"
"/* =========================================================\n"
"   SCROLL BAR\n"
"   ========================================================= */\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #e1ded6;\n"
"\n"
"    width: 13px;\n"
"\n"
"    border: 1px solid #aaa69f;\n"
"    border-radius: 3px;\n"
"\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background:\n"
"        qlineargradient(\n"
"            x1: 0, y1: 0,\n"
"            x2: 1, y2: 0,\n"
"\n"
"            stop: 0 #d3d0c8,\n"
"            stop: 0.5 #eeeae4,\n"
"            stop: 1 #c2beb6\n"
"        );\n"
"\n"
"    border: 1px solid #8e8a82;\n"
"    border-radius: 3px;\n"
"\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #d4d1c9;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"}\n"
""
                        "\n"
"/* =========================================================\n"
"   HORIZONTAL SCROLLBAR\n"
"   ========================================================= */\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: #e1ded6;\n"
"\n"
"    height: 13px;\n"
"\n"
"    border: 1px solid #aaa69f;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background:\n"
"        qlineargradient(\n"
"            x1: 0, y1: 0,\n"
"            x2: 0, y2: 1,\n"
"\n"
"            stop: 0 #eeeae4,\n"
"            stop: 0.5 #d3d0c8,\n"
"            stop: 1 #c2beb6\n"
"        );\n"
"\n"
"    border: 1px solid #8e8a82;\n"
"    border-radius: 3px;\n"
"\n"
"    min-width: 30px;\n"
"}\n"
"\n"
"/* =========================================================\n"
"   TOOLTIP\n"
"   ========================================================= */\n"
"\n"
"QToolTip {\n"
"    background: #f5f2eb;\n"
"    color: #222222;\n"
"\n"
"    border: 1px solid #77736c;\n"
"    border-radius: 2px;\n"
"\n"
"    padding: 4px 6px;\n"
""
                        "}")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 371, 431))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logs = QListWidget(self.layoutWidget)
        self.logs.setObjectName(u"logs")
        font1 = QFont()
        font1.setFamilies([u"Google Sans"])
        self.logs.setFont(font1)
        self.logs.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.logs.setWordWrap(True)

        self.verticalLayout.addWidget(self.logs)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.message = QLineEdit(self.layoutWidget)
        self.message.setObjectName(u"message")

        self.horizontalLayout.addWidget(self.message)

        self.send_message = QPushButton(self.layoutWidget)
        self.send_message.setObjectName(u"send_message")
        self.send_message.setFont(font)

        self.horizontalLayout.addWidget(self.send_message)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(410, 100, 161, 242))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.internet_protocol = QLineEdit(self.layoutWidget1)
        self.internet_protocol.setObjectName(u"internet_protocol")

        self.verticalLayout_2.addWidget(self.internet_protocol)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.port = QLineEdit(self.layoutWidget1)
        self.port.setObjectName(u"port")

        self.verticalLayout_2.addWidget(self.port)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.username = QLineEdit(self.layoutWidget1)
        self.username.setObjectName(u"username")

        self.verticalLayout_2.addWidget(self.username)

        self.send_connect = QPushButton(self.layoutWidget1)
        self.send_connect.setObjectName(u"send_connect")
        self.send_connect.setFont(font)

        self.verticalLayout_2.addWidget(self.send_connect)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Client manager", None))
        self.send_message.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.internet_protocol.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0442", None))
        self.port.setText(QCoreApplication.translate("MainWindow", u"8080", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.username.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.send_connect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u0441\u044f", None))
    # retranslateUi

