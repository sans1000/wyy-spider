import requests
import re
import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTabWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QTextBrowser
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon                       #QSS样式表，可以删除

from qt_material import apply_stylesheet

class Music(object):
    def __init__(self,url,user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'):
        content = self.get_music(url,user_agent)
        self.dowload_music(content)

    def get_music(self,url,user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'):
        header = {
            'user-agent':user_agent
        }

        resp = requests.get(url=url,headers=header)
        QApplication.processEvents()
        return resp.content

    QApplication.processEvents()

    def dowload_music(self,content):
        way = ".\music\song.mp3"
        mkdir('.\\music')
        with open(way,'wb') as f:
            f.write(content)
            message1.setText('done!')
            QApplication.processEvents()

class Gd(object):
    def __init__(self,url,user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'):
        home_page = self.get_homepage(url,user_agent)
        result = self.get_musics(home_page)
        self.information = ''
        for num_id, name in result:
            url = 'http://music.163.com/song/media/outer/url?id=' + str(num_id) + '.mp3'
            respa = self.get_music_content(url)
            file_name = ".\\music\\" + name + ".mp3"
            mkdir('.\\music')
            self.dowload_music(file_name, respa)
            senten = name + 'has been dowlaoded!'
            self.information += senten + '\n'
            message.setText(self.information)


    def get_homepage(self,url,user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'):
        header = {
            'user-agent': user_agent
        }
        resp = requests.get(url = url, headers=header)
        QApplication.processEvents()
        return resp.text

    def get_musics(self,text):
        obj = re.compile(r'<li><a href="/song\?id=(\d+)">(.*?)</a>', re.S)
        result = obj.findall(text)
        QApplication.processEvents()
        return result

    def get_music_content(self,url,user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'):
        header = {
            'user-agent': user_agent
        }
        resp = requests.get(url=url, headers=header)
        QApplication.processEvents()
        return resp.content

    def dowload_music(self,file_name,content):
        with open(file_name, 'wb') as f:
            f.write(content)
            QApplication.processEvents()

######################################################

#提示功能
def url_critical():                  #下载失败
    messagebox = QMessageBox()
    messagebox.critical(w, "错误", "大概率是url有问题，如果无法解决就别用了\nurl示例：\n单曲：http://music.163.com/song/media/outer/url?id=36990266.mp3\n歌单：https://music.163.com/playlist?id=7533687690\nPS:也可能是AU填错了，填不了就别填了宝\nAU示例：Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49")
def you_bing():                      #就是有病
    messagebox = QMessageBox()
    messagebox.critical(w,'你妈逼','给爷爬')

    #按钮响应事件
def download_gd():
    text2 = edit2.text()
    text3 = edit3.text()
    if text2 == '':
        you_bing()
    elif text3 == '':
        try:
            gd = Gd(text2)
            gd.my_str.connect(self.get_sin_out)
        except:
            url_critical()
    else:
        try:
            gd = Gd(text2,text3)
            gd.my_str.connect(self.get_sin_out)
        except:
            url_critical()

def download_music():
    text = edit.text()
    text1 = edit1.text()
    if text == '':
        you_bing()
    elif text1 == '':
        try:
            music = Music(text)
        except:
            url_critical()
    else:
        try:
            music = Music(text,text1)
        except:
            url_critical()


def mkdir(path):
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

######################################################

app = QApplication(sys.argv)

#初始化窗口
w = QMainWindow()
Dialog1 = QDialog()
Dialog2 = QDialog()
Dialog3 = QDialog()

# 设置窗口标题
w.setWindowTitle("wyy音乐下载小工具")
w.resize(300,330)
w.setWindowIcon(QIcon('icon.png'))

apply_stylesheet(w, theme='dark_teal.xml')

######################################################

# 纯文本
title = QLabel("单曲", Dialog1)
title.setGeometry(120, 4, 30, 20)

label = QLabel("url", Dialog1)
label.setGeometry(20, 50, 30, 20)

label1 = QLabel("UA", Dialog1)
label1.setGeometry(20, 80, 30, 20)

# 文本框
edit = QLineEdit(Dialog1)
edit.setPlaceholderText("请输入url")
edit.setGeometry(55, 50, 200, 20)

edit1 = QLineEdit(Dialog1)
edit1.setPlaceholderText("请输入user_agent")
edit1.setGeometry(55, 80, 200, 20)

# 在窗口里面添加控件
btn = QPushButton("确定", Dialog1)
btn.setGeometry(110, 110, 70, 30)

######################################################

# 纯文本
title1 = QLabel("歌单", Dialog2)
title1.setGeometry(120, 4, 30, 20)

label2 = QLabel("url", Dialog2)
label2.setGeometry(20, 50, 30, 20)

label3 = QLabel("UA", Dialog2)
label3.setGeometry(20, 80, 30, 20)

# 文本框
edit2 = QLineEdit(Dialog2)
edit2.setPlaceholderText("请输入url")
edit2.setGeometry(55, 50, 200, 20)

edit3 = QLineEdit(Dialog2)
edit3.setPlaceholderText("请输入user_agent")
edit3.setGeometry(55, 80, 200, 20)

# 在窗口里面添加控件
btn1 = QPushButton("确定", Dialog2)
btn1.setGeometry(110, 110, 70, 30)

message = QTextBrowser(Dialog2)
message.setGeometry(25, 150, 250, 100)
message.setText('歌曲保存在程序所在的文件夹中\n程序无响应为正常现象，请耐心等待\n等待下载中...\n')

message1 = QTextBrowser(Dialog1)
message1.setGeometry(25, 150, 250, 100)
message1.setText('歌曲保存在程序所在的文件夹中\n程序无响应为正常现象，请耐心等待\n等待下载中...\n')

######################################################

browser = QTextBrowser(Dialog3)
browser.setText('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">'
'<html><head><meta name="qrichtext" content="1" /><style type="text/css">'
'p, li { white-space: pre-wrap; }'
'</style></head><body style=" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;">'
'<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">***wyy音乐下载小工具***</span></p>'
'<p style=" margin-top:3px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:30px;">“单曲”标签页用于下载歌曲；<br />“歌单”标签页用于批量下载歌单中的歌曲；<br />url：即爬虫目标的网址；<br />au：可以默认不填，需要在浏览器中抓包获得；<br />本工具仅供个人使用，禁止用于商业用途；<br />PS：由于wyy网页版限制，至多下载10首</p></body></html>')
browser.resize(300,300)

btn.clicked.connect(download_music)
btn1.clicked.connect(download_gd)

TableWidget = QTabWidget(w)
TableWidget.resize(300, 350)
TableWidget.addTab(Dialog1, "单曲")
TableWidget.addTab(Dialog2, "歌单")
TableWidget.addTab(Dialog3, "说明书")

# 展示窗口
w.show()

# 程序进行循环等待状态
app.exec()