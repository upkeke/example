import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QApplication


def bounderTo():
    s1=QSize(10,30)
    s2=QSize(30,13)

    #返回两个比例最小值
    s=s1.boundedTo(s2)
    s3=s1.expandedTo(s2)
    print(s,s3)  #PySide6.QtCore.QSize(10, 13) PySide6.QtCore.QSize(30, 30)


def set_w_h():
    s=QSize()
    s.setWidth(12)
    s.setHeight(15)
    print(s)
    print(s.width(),s.height()) #12 15

def isNull():
    s = QSize(25,12)
    s1 = QSize(-25, 12)
    s2 = QSize(25, -12)
    s3 = QSize(-25, 0)
    s4=QSize(0,0)
    print(s.isNull(),s1.isNull(),s2.isNull(),s3.isNull(),s4.isNull())
        #输出 False False False False True
def transposed():
    s=QSize(5,4)
    s2=QSize(9,8)
    #交换w,h
    s2.transpose()  #PySide6.QtCore.QSize(8, 9)
    #返回交换后的值
    s1=s.transposed() #PySide6.QtCore.QSize(4, 5)
    print(s2,s1)
def scaled():
    #三种纵横比模式（AspectRatioMode）
    #Qt.IgnoreAspectRatio 忽略原本的纵横比，强制改为现在纵横比
    #Qt.KeepAspectRatio
    #Qt.KeepAspectRatioByExpanding
    s=QSize(200,200)
    s.scaled(100,100,Qt.IgnoreAspectRatio)
    print(s)

def form(size):
    app=QApplication(sys.argv)
    win=QMainWindow()
    win.setWindowTitle("测试缩放")
    win.setGeometry(0,0,size.width(),size.height())
    win.show()
    sys.exit(app.exec())
s=QSize(100,200)
s1=s.scaled(50,50,Qt.KeepAspectRatio)  #PySide6.QtCore.QSize(25, 50)
s2=s.scaled(500,500,Qt.KeepAspectRatio) #PySide6.QtCore.QSize(250, 500)
print(s1)

form(s1)