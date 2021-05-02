from pykeyboard import PyKeyboard
from pymouse import PyMouse
import codecs
import time
import os
import pyperclip
import re
from datetime import datetime

class Coding_log:

    '''
    Attributes
    ----------
        file_src(str): 文件的路径
        speed_inteval(float): 打印每个字符的时间间隔
        file_size(int): 文件的大小，用来预测所需的时间

    '''

    def __init__(self, file_src, speed_inteval = 0.01):
        self.file_src = file_src
        self.speed_inteval = speed_inteval
        self.file_size = 0

        self.get_test_file_path()
        self.read_txt()

        self.m = PyMouse() # 建立鼠标对象
        self.k = PyKeyboard() # 建立键盘对象

    def get_test_file_path(self):
        point_index = self.file_src.rindex('.')
        test_file_path = self.file_src[: point_index] + "_test." + self.file_src[point_index + 1:]
        self.test_file_path = test_file_path

    def read_txt(self):
        self.txt_file = []

        with codecs.open(self.file_src, "r", encoding='utf-8') as fi:
            for line in fi.readlines():
                line = line.strip('\n')
                self.file_size += len(line)
                self.txt_file.append(line)

        print("文件读取成功")

    def ctrl_v(self, info, sleep_time):
        time.sleep(sleep_time)
        pyperclip.copy(info)
        self.k.press_key(self.k.control_key)
        self.k.tap_key('v')
        self.k.release_key(self.k.control_key)
    
    def create_test_file(self):
        if os.path.exists(self.test_file_path):
            print("文件已存在，先将其删除后再创建")
            os.remove(self.test_file_path)
        if not os.path.exists(self.test_file_path):
            file = open(self.test_file_path, 'w')
            file.close()
            print("创建文件成功，文件路径为: {}".format(self.test_file_path))

    def open_test_file(self):
        # ctrl + p
        self.k.press_key(self.k.control_key)
        self.k.tap_key('p')
        self.k.release_key(self.k.control_key)
        
        # 在输入框中输入 file_name
        file_name = self.test_file_path[self.test_file_path.rindex('/') + 1: ]
        self.ctrl_v(file_name, sleep_time = 0.1)

        # enter
        time.sleep(0.1)
        self.k.press_key(self.k.enter_key)
        time.sleep(0.1)
    
    def delete_test_file(self):
        os.remove(self.test_file_path)
        print("文件已经被删除")

    def print_txt(self):
        
        self.create_test_file()
        self.open_test_file()

        print("开始打印，预计需要 {}s".format(round(self.file_size * self.speed_inteval * 2, 2)))

        before = datetime.now()
        for txt in self.txt_file:
            for c in txt:
                self.ctrl_v(c, self.speed_inteval)
        after = datetime.now()
        print("打印的实际用时: {}s".format((after - before).seconds))

        self.delete_test_file()

if __name__ == '__main__':
    file_src = './coding_video_log/requirements.txt'
    Coding_log(file_src = file_src).print_txt()

# REF:
# https://zhuanlan.zhihu.com/p/137133751