import socket
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QPixmap

msg1_open = "\x55\x55\x55\x00\x00\x00\x00\x55\x55\x55"
msg1_close = "\x55\x55\x55\x00\x00\x00\x01\x55\x55\x55"

msg2_open = "\x55\x55\x55\x00\x00\x01\x00\x55\x55\x55"
msg2_close = "\x55\x55\x55\x00\x00\x01\x01\x55\x55\x55"

msg3_open = "\x55\x55\x55\x00\x00\x02\x00\x55\x55\x55"
msg3_close = "\x55\x55\x55\x00\x00\x02\x01\x55\x55\x55"

msg4_open = "\x55\x55\x55\x00\x00\x03\x00\x55\x55\x55"
msg4_close = "\x55\x55\x55\x00\x00\x03\x01\x55\x55\x55"

class IPConfig:
    def IPInit(self):
        global ip0
        f = open("ipconfig.txt", "r")  # 设置文件对象

        data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样

        ip0str=data[0]
        ip0=ip0str[4:-1]

        f.close()  # 关闭文件

class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('.\\ui\\继电器开关.ui')

        self.ui.Button.clicked.connect(self.handleCalc1)
        self.ui.Button_2.clicked.connect(self.handleCalc2)

        self.ui.Button_3.clicked.connect(self.handleCalc3)
        self.ui.Button_4.clicked.connect(self.handleCalc4)

        self.ui.Button_5.clicked.connect(self.handleCalc5)
        self.ui.Button_6.clicked.connect(self.handleCalc6)

        self.ui.Button_7.clicked.connect(self.handleCalc7)
        self.ui.Button_8.clicked.connect(self.handleCalc8)
        Pixmap = QPixmap('.\\ui\\福建省高速公路.png')
        self.ui.label4.setPixmap(Pixmap)
        IPConfig.IPInit(self)
        #Stats.handleCalc1(self)

    def handleCalc1(self):
        # 1.创建一个udp套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 2.准备接收方的地址
        # 192.168.10.199 表示目的地ip
        # 5000  表示目的地端口
        #udp_socket.bind(("", 5000))
        udp_socket.sendto(msg1_open.encode("utf-8"), (ip0, 5000))
        # 3. 接收打印数据
        udp_socket.settimeout(5)
        recvData = udp_socket.recvfrom(1024)
        print(recvData)
        # 3.关闭套接字
        udp_socket.close()
        #显示开图标
        self.ui.label.clear()
        self.ui.label.setText("开")
        Pixmap = QPixmap('.\\ui\\绿色.jpg')
        self.ui.label.setPixmap(Pixmap)
        # 实时刷新界面
        QApplication.processEvents()

    def handleCalc2(self):
        # 1.创建一个udp套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 2.准备接收方的地址
        # 192.168.10.199 表示目的地ip
        # 5000  表示目的地端口
        udp_socket.sendto(msg1_close.encode("utf-8"), (ip0, 5000))
        udp_socket.settimeout(5)
        recvData = udp_socket.recvfrom(1024)
        print(recvData)
        # 3.关闭套接字
        udp_socket.close()
        #显示关图标
        self.ui.label.clear()
        self.ui.label.setText("关")
        Pixmap = QPixmap('.\\ui\\红色.jpg')
        self.ui.label.setPixmap(Pixmap)
        # 实时刷新界面
        QApplication.processEvents()

    def handleCalc3(self):
        # 1.创建一个udp套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 2.准备接收方的地址
        # 192.168.10.199 表示目的地ip
        # 5000  表示目的地端口
        #udp_socket.bind(("", 5000))
        udp_socket.sendto(msg2_open.encode("utf-8"), (ip0, 5000))
        # 3. 接收打印数据
        udp_socket.settimeout(5)
        recvData = udp_socket.recvfrom(1024)
        print(recvData)
        # 3.关闭套接字
        udp_socket.close()
        #显示开图标
        self.ui.label5.clear()
        self.ui.label5.setText("开")
        Pixmap = QPixmap('.\\ui\\绿色.jpg')
        self.ui.label5.setPixmap(Pixmap)
        # 实时刷新界面
        QApplication.processEvents()

    def handleCalc4(self):
        # 1.创建一个udp套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 2.准备接收方的地址
        # 192.168.10.199 表示目的地ip
        # 5000  表示目的地端口
        udp_socket.sendto(msg2_close.encode("utf-8"), (ip0, 5000))
        udp_socket.settimeout(5)
        recvData = udp_socket.recvfrom(1024)
        print(recvData)
        # 3.关闭套接字
        udp_socket.close()
        #显示关图标
        self.ui.label5.clear()
        self.ui.label5.setText("关")
        Pixmap = QPixmap('.\\ui\\红色.jpg')
        self.ui.label5.setPixmap(Pixmap)
        # 实时刷新界面
        QApplication.processEvents()

    def handleCalc5(self):
        # 1.创建一个udp套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 2.准备接收方的地址
        # 192.168.10.199 表示目的地ip
        # 5000  表示目的地端口
        #udp_socket.bind(("", 5000))
        udp_socket.sendto(msg3_open.encode("utf-8"), (ip0, 5000))
        # 3. 接收打印数据
        udp_socket.settimeout(5)
        recvData = udp_socket.recvfrom(1024)
        print(recvData)
        # 3.关闭套接字
        udp_socket.close()
        #显示开图标
        self.ui.label6.clear()
        self.ui.label6.setText("开")
        Pixmap = QPixmap('.\\ui\\绿色.jpg')
        self.ui.label6.setPixmap(Pixmap)
        # 实时刷新界面
        QApplication.processEvents()

    def handleCalc6(self):
        # 1.创建一个udp套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 2.准备接收方的地址
        # 192.168.10.199 表示目的地ip
        # 5000  表示目的地端口
        udp_socket.sendto(msg3_close.encode("utf-8"), (ip0, 5000))
        udp_socket.settimeout(5)
        recvData = udp_socket.recvfrom(1024)
        print(recvData)
        # 3.关闭套接字
        udp_socket.close()
        #显示关图标
        self.ui.label6.clear()
        self.ui.label6.setText("关")
        Pixmap = QPixmap('.\\ui\\红色.jpg')
        self.ui.label6.setPixmap(Pixmap)
        # 实时刷新界面
        QApplication.processEvents()

    def handleCalc7(self):
        # 1.创建一个udp套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 2.准备接收方的地址
        # 192.168.10.199 表示目的地ip
        # 5000  表示目的地端口
        #udp_socket.bind(("", 5000))
        udp_socket.sendto(msg4_open.encode("utf-8"), (ip0, 5000))
        # 3. 接收打印数据
        udp_socket.settimeout(5)
        recvData = udp_socket.recvfrom(1024)
        print(recvData)
        # 3.关闭套接字
        udp_socket.close()
        #显示开图标
        self.ui.label_7.clear()
        self.ui.label_7.setText("开")
        Pixmap = QPixmap('.\\ui\\绿色.jpg')
        self.ui.label_7.setPixmap(Pixmap)
        # 实时刷新界面
        QApplication.processEvents()

    def handleCalc8(self):
        # 1.创建一个udp套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 2.准备接收方的地址
        # 192.168.10.199 表示目的地ip
        # 5000  表示目的地端口
        udp_socket.sendto(msg4_close.encode("utf-8"), (ip0, 5000))
        udp_socket.settimeout(5)
        recvData = udp_socket.recvfrom(1024)
        print(recvData)
        # 3.关闭套接字
        udp_socket.close()
        #显示关图标
        self.ui.label_7.clear()
        self.ui.label_7.setText("关")
        Pixmap = QPixmap('.\\ui\\红色.jpg')
        self.ui.label_7.setPixmap(Pixmap)
        # 实时刷新界面
        QApplication.processEvents()


app = QApplication([])
stats = Stats()
stats.ui.show()

app.exec_()