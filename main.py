import socket
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit
msg1 = "\x55\x55\x55\x00\x00\x00\x00\x55\x55\x55"
msg2 = "\x55\x55\x55\x00\x00\x00\x01\x55\x55\x55"

def handleCalc1():
    # 1.创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.准备接收方的地址
    # 192.168.65.149 表示目的地ip
    # 30000  表示目的地端口
    udp_socket.sendto(msg1.encode("utf-8"), ("192.168.10.199", 5000))

    # 3.关闭套接字
    udp_socket.close()
def handleCalc2():
    # 1.创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.准备接收方的地址
    # 192.168.65.149 表示目的地ip
    # 30000  表示目的地端口
    udp_socket.sendto(msg2.encode("utf-8"), ("192.168.10.199", 5000))

    # 3.关闭套接字
    udp_socket.close()

app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('继电器控制系统')

#textEdit = QPlainTextEdit(window)
#textEdit.setPlaceholderText("请输入薪资表")
#textEdit.move(10,25)
#textEdit.resize(300,350)

button1 = QPushButton('继电器开', window)
button1.move(80,80)
button1.clicked.connect(handleCalc1)

button2 = QPushButton('继电器关', window)
button2.move(320,80)
button2.clicked.connect(handleCalc2)

window.show()

app.exec_()