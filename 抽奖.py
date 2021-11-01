import sys
#解决No module named XXX
sys.path.append("D:\\学习\\software_python_code\\python_trunk\\venv\\Lib\\site-packages")

from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import xlrd
import xlwt
import time
import random


class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('.\\ui\\抽奖.ui')

        self.ui.pushButton.clicked.connect(self.handleCalcStart)
        #self.ui.pushButton_2.clicked.connect(self.handleCalcEnd)

    def handleCalcStart(self):
        t = 0
        while t < 3:
            t += 0.1
            time.sleep(0.1)
            student_num = random.randint(0, num_rows)
            self.ui.label.clear()
            self.ui.label.setText(Student_Name.cell_value(student_num, 0))
            # 实时刷新界面
            QApplication.processEvents()


    #def handleCalcEnd(self):
    #    print("end")

class File:
    def Init(self):
        file = '学生花名册.xls'
        wb = xlrd.open_workbook(filename=file)#打开文件
        f = xlwt.Workbook()
        # 抓取所有sheet页的名称
        worksheets = wb.sheet_names()
        # 定位到sheet1
        worksheet1 = wb.sheet_by_name(u'Sheet1')
        global num_rows
        num_rows = worksheet1.nrows - 1
        global Student_Name
        Student_Name = wb.sheet_by_index(0)


app = QApplication([])
student = File()
student.Init()
stats = Stats()
stats.ui.show()

app.exec_()


