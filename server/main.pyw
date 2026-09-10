from PySide6.QtCore import (
    QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QTimer
)

from PySide6.QtGui import (
    QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform
)

from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget
)

from PySide6.QtNetwork import (
    QTcpServer, QTcpSocket, QHostAddress
)
import server_ui
from datetime import datetime


class ServerWindow(QMainWindow, server_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Server manager 1.0")

    def connectSlots(self):
        self.run_button.clicked.connect(self.runButton)

    @staticmethod
    def executeWindow():
        global server_window
        server_window = ServerWindow()
        server_window.connectSlots()
        server_window.show()

    def runButton(self):
        try:
            user_count = int(self.users_count.text())

            if not 5 > user_count > 0:
                raise ValueError("Users count: 1-4")

            port = int(self.port.text())

            if not main_server.listen(QHostAddress.Any, port):
                raise RuntimeError(main_server.errorString())

            main_server.setMaxPendingConnections(user_count)

            self.setting_frame.setVisible(False)
            self.out(f"Server started on port {port}")

        except Exception as e:
            self.out(f"Bind: {e}")

    def out(self, msg: str):

        msg = f"{datetime.now().strftime("%H:%M")}: {msg}"
        self.listWidget.addItem(msg)


def user_connect_waiting():
    while main_server.hasPendingConnections():
        client = main_server.nextPendingConnection()
        clients.append(client)

        client.readyRead.connect(
            lambda c=client: receive_data(c)
        )

        client.disconnected.connect(
            lambda c=client: client_disconnected(c)
        )

        server_window.out(
            f"Client connected: {client.peerAddress().toString()}:{client.peerPort()}"
        )


def receive_data(client):
    data = client.readAll().data()

    if not data:
        return

    try:
        data = data.decode("utf-8").split("%%")

        if len(data) < 2:
            return

        send_data = f"{data[0]} : {data[1]}"

        server_window.out(send_data)

        for target in clients:
            if target.state() == QTcpSocket.ConnectedState:
                target.write(send_data.encode("utf-8"))

    except Exception as e:
        server_window.out(f"Receive: {e}")


def client_disconnected(client):
    if client in clients:
        clients.remove(client)

    server_window.out("Client disconnected")
    client.deleteLater()


def main():
    global main_server, clients

    app = QApplication()

    clients = []
    main_server = QTcpServer()

    main_server.newConnection.connect(user_connect_waiting)

    ServerWindow.executeWindow()

    app.exec()


if __name__ == "__main__":
    main()