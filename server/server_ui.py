# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serveraikUuu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(632, 468)
        MainWindow.setMinimumSize(QSize(632, 468))
        MainWindow.setMaximumSize(QSize(632, 468))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogInformation))
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 632, 468))
        self.listWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.CrossCursor))
        self.listWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.listWidget.setStyleSheet(u"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0441\u0430\u043c\u043e\u0433\u043e \u0432\u0438\u0434\u0436\u0435\u0442\u0430 \u0441\u043f\u0438\u0441\u043a\u0430 (\u043e\u043a\u043d\u043e \u0442\u0435\u0440\u043c\u0438\u043d\u0430\u043b\u0430) */\n"
"QListWidget, QListView {\n"
"    background-color: #1a0f02;       /* \u041e\u0447\u0435\u043d\u044c \u0442\u0435\u043c\u043d\u044b\u0439, \u043f\u043e\u0447\u0442\u0438 \u0447\u0435\u0440\u043d\u044b\u0439 \u0444\u043e\u043d \u0441 \u0442\u0435\u043f\u043b\u044b\u043c \u043e\u0442\u0442\u0435\u043d\u043a\u043e\u043c */\n"
"    border: 2px solid #3d2406;        /* \u0422\u0435\u043c\u043d\u043e-\u044f\u043d\u0442\u0430\u0440\u043d\u0430\u044f \u0442\u043e\u043d\u043a\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    color: #ffaa00;                  /* \u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u044f\u043d\u0442\u0430\u0440\u043d\u043e-\u043e\u0440\u0430\u043d\u0436\u0435\u0432\u044b\u0439 \u0446\u0432\u0435\u0442"
                        " \u0442\u0435\u043a\u0441\u0442\u0430 (\u043a\u0430\u043a \u0432 neofetch) */\n"
"    font-family: \"Courier New\", \"Lucida Console\", \"Consolas\", monospace; /* \u041c\u043e\u043d\u043e\u0448\u0438\u0440\u0438\u043d\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 16px;\n"
"    outline: none;                   /* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u043f\u0443\u043d\u043a\u0442\u0438\u0440\u043d\u0443\u044e \u0440\u0430\u043c\u043a\u0443 \u0444\u043e\u043a\u0443\u0441\u0430 Qt */\n"
"}\n"
"\n"
"/* \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438, \u0447\u0442\u043e\u0431\u044b \u043e\u043d\u0430 \u043d\u0435 \u043f\u043e\u0440\u0442\u0438\u043b\u0430 \u0440\u0435\u0442\u0440\u043e-\u0432\u0438\u0434 */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #1a0f02;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #54"
                        "340a;\n"
"    min-height: 20px;\n"
"}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* \u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0432\u043e \u0432\u0441\u0435\u0445 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f\u0445 (\u043e\u0431\u044b\u0447\u043d\u043e\u0435, \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0435, \u0432\u044b\u0431\u043e\u0440) */\n"
"QListWidget::item, \n"
"QListWidget::item:hover, \n"
"QListWidget::item:disabled,\n"
"QListWidget::item:selected, \n"
"QListWidget::item:selected:active, \n"
"QListWidget::item:selected:!active {\n"
"    background: transparent;          /* \u041d\u0438\u043a\u0430\u043a\u043e\u0439 \u043f\u043e\u0434\u0441\u0432\u0435\u0442\u043a\u0438 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u0438 \u043a\u043b"
                        "\u0438\u043a\u0430\u0445 */\n"
"    color: #ffaa00;                   /* \u0422\u0435\u043a\u0441\u0442 \u0432\u0441\u0435\u0433\u0434\u0430 \u043e\u0441\u0442\u0430\u0435\u0442\u0441\u044f \u044f\u043d\u0442\u0430\u0440\u043d\u044b\u043c */\n"
"    border: none;                     /* \u041d\u0438\u043a\u0430\u043a\u0438\u0445 \u0440\u0430\u043c\u043e\u043a \u0432\u043e\u043a\u0440\u0443\u0433 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438 */\n"
"    padding: 3px 5px;                 /* \u041d\u0435\u0431\u043e\u043b\u044c\u0448\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0434\u043b\u044f \u0438\u043c\u0438\u0442\u0430\u0446\u0438\u0438 \u0441\u0442\u0440\u043e\u043a \u0442\u0435\u0440\u043c\u0438\u043d\u0430\u043b\u0430 */\n"
"}\n"
"")
        self.setting_frame = QFrame(self.centralwidget)
        self.setting_frame.setObjectName(u"setting_frame")
        self.setting_frame.setGeometry(QRect(420, 250, 191, 201))
        self.setting_frame.setStyleSheet(u"/* \u0413\u043b\u0430\u0432\u043d\u044b\u0439 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440 */\n"
"QFrame {\n"
"    background-color: #12110f; /* \u0421\u0434\u0435\u043b\u0430\u0435\u043c \u0447\u0443\u0442\u044c \u0442\u0435\u043c\u043d\u0435\u0435 \u0434\u043b\u044f \u043b\u0443\u0447\u0448\u0435\u0433\u043e \u043a\u043e\u043d\u0442\u0440\u0430\u0441\u0442\u0430 */\n"
"    border: 1px solid #ffb000;\n"
"    border-radius: 0px;\n"
"    font-family: \"Courier New\", \"Lucida Console\", monospace;\n"
"}\n"
"\n"
"/* \u041f\u043e\u0434\u043f\u0438\u0441\u0438 \u2014 \u0423\u0411\u0418\u0420\u0410\u0415\u041c \u0420\u0410\u041c\u041a\u0423 (border: none) */\n"
"QLabel {\n"
"    color: #ffb000;\n"
"    font-size: 13px;\n"
"    background: transparent;\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u043d\u0435\u043d\u0443\u0436\u043d\u044b\u0435 \u0440\u0430\u043c\u043a\u0438 \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u043e\u0434\u043f\u0438\u0441"
                        "\u0435\u0439 */\n"
"    padding: 2px 0px;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 */\n"
"QLineEdit {\n"
"    background-color: #1a1815; \n"
"    border: 1px solid #c88a00;\n"
"    color: #ffb000;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"    font-family: \"Courier New\", \"Lucida Console\", monospace;\n"
"    selection-background-color: #ffb000;\n"
"    selection-color: #12110f;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #ffb000;\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0430 \u2014 \u041f\u0420\u0418\u041d\u0423\u0414\u0418\u0422\u0415\u041b\u042c\u041d\u041e \u0417\u0410\u0414\u0410\u0415\u041c \u041c\u041e\u041d\u041e\u0428\u0418\u0420\u0418\u041d\u041d\u042b\u0419 \u0428\u0420\u0418\u0424\u0422 */\n"
"QPushButton {\n"
"    background-color: #ffb000;  /* \u0421\u0434\u0435\u043b\u0430\u0435\u043c \u0435\u0451 \u0437\u0430\u043b\u0438\u0442\u043e\u0439 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e, \u043a\u0430\u043a \u0443"
                        " \u0432\u0430\u0441 */\n"
"    border: 1px solid #ffb000;\n"
"    color: #12110f;             /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u043d\u0430 \u043e\u0440\u0430\u043d\u0436\u0435\u0432\u043e\u043c \u0444\u043e\u043d\u0435 */\n"
"    padding: 6px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    font-family: \"Courier New\", \"Lucida Console\", monospace; /* \u0418\u0441\u043f\u0440\u0430\u0432\u043b\u044f\u0435\u0442 \u0448\u0440\u0438\u0444\u0442 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e09b00;\n"
"    border-color: #e09b00;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #12110f;  /* \u0418\u043d\u0432\u0435\u0440\u0441\u0438\u044f \u043f\u0440\u0438 \u043a\u043b\u0438\u043a\u0435 */\n"
"    color: #ffb000;\n"
"}\n"
"")
        self.setting_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.setting_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.widget = QWidget(self.setting_frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 150, 159))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.users_count = QLineEdit(self.widget)
        self.users_count.setObjectName(u"users_count")

        self.verticalLayout.addWidget(self.users_count)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.port = QLineEdit(self.widget)
        self.port.setObjectName(u"port")

        self.verticalLayout.addWidget(self.port)

        self.run_button = QPushButton(self.widget)
        self.run_button.setObjectName(u"run_button")

        self.verticalLayout.addWidget(self.run_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Server log", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Users count (1-4)", None))
        self.users_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Server port", None))
        self.port.setText(QCoreApplication.translate("MainWindow", u"8080", None))
        self.run_button.setText(QCoreApplication.translate("MainWindow", u"Run server", None))
    # retranslateUi

