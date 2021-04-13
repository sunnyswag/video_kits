from pykeyboard import *
from pymouse import *
import codecs
import time
import pyperclip

def read_txt(file_src):
    # 读取 txt 文件, 并用 txt_file 进行存储
    txt_file = []

    with codecs.open(file_src, "r", encoding='utf-8') as fi:
        for line in fi.readlines():
            line = line.strip('\n')
            txt_file.append(line)

    return txt_file

def print_txt(txt_file, fit_time = 2, speed_inteval = 0.02):

    '''
    txt_file: 需要打印的 list
    fit_time: 确定输入位置所花的时间
    speed_inteval: 打印每个字符的间隔时间
    '''

    m = PyMouse() # 建立鼠标对象
    k = PyKeyboard() # 建立键盘对象
    time.sleep(fit_time) # 给时间调整位置
    input_location = m.position() # 获取输入的位置

    for txt in txt_file:
        for c in txt:
            time.sleep(0.02)
            pyperclip.copy(c)
            k.press_key(k.control_key)
            k.tap_key('v')
            k.release_key(k.control_key)

txt_file = read_txt("test.txt")
print_txt(txt_file)

# REF:
# https://zhuanlan.zhihu.com/p/137133751