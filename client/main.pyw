
from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtNetwork import QTcpSocket
import client_ui

#-----------------UI-----------------

# Execute Qt Window
class ClientWindow(QMainWindow, client_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Client manager 1.1.2")

    def connectSlots(self):
        self.send_connect.clicked.connect(sendConnect)
        self.send_message.clicked.connect(sendMessage)

    @staticmethod
    def executeWindow():
        global client_window
        client_window = ClientWindow()
        client_window.connectSlots()
        client_window.show()

    def updatingList(self):
        data = client_socket.readAll().data()
        if data:
            message = data.decode("utf-8", errors="replace")
            self.out(message)

    def out(self, msg: str):
        self.logs.addItem(msg)
    
# Execute Qt Window



#-----------------UI-----------------


#--------------SOCKETS-------------

def executeClientSocket():
    global client_socket
    try:
        #client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket = QTcpSocket()
        client_socket.readyRead.connect(client_window.updatingList)
        client_socket.connected.connect(clientConnected)

    except Exception as e:
        client_window.out(e)
        
def clientConnected():
    client_window.out("Успешное подключение к серверу.")

def sendConnect():
    client_window.out('Подключение к серверу...')
    client_socket.connectToHost(str(client_window.internet_protocol.text()), int(client_window.port.text()))

def sendMessage():
    client_socket.write(f"{client_window.username.text()}%%{client_window.message.text()}".encode('utf-8'))

#--------------SOCKETS-------------

def main():
    app = QApplication()
    ClientWindow.executeWindow()
    executeClientSocket()
    app.exec()
if __name__ == "__main__":
    main()

    

    







