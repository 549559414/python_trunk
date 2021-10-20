import socket
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader

msg1 = "\x55\x55\x55\x00\x00\x00\x00\x55\x55\x55"
msg2 = "\x55\x55\x55\x00\x00\x00\x01\x55\x55\x55"


class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('.\\ui\\继电器开关.ui')

        self.ui.Button.clicked.connect(self.handleCalc1)
        self.ui.Button_2.clicked.connect(self.handleCalc2)

    def handleCalc1(self):
        # 1.创建一个udp套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 2.准备接收方的地址
        # 192.168.65.149 表示目的地ip
        # 30000  表示目的地端口
        udp_socket.sendto(msg1.encode("utf-8"), ("192.168.10.199", 5000))
        # 3.关闭套接字
        udp_socket.close()
    def handleCalc2(self):
        # 1.创建一个udp套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 2.准备接收方的地址
        # 192.168.65.149 表示目的地ip
        # 30000  表示目的地端口
        udp_socket.sendto(msg2.encode("utf-8"), ("192.168.10.199", 5000))
        # 3.关闭套接字
        udp_socket.close()

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()