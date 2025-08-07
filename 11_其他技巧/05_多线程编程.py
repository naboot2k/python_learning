"""
import threading

thread_obj = threading.Thread([group[, target[, name[, args[, kwargs]]]]])
- group：暂时无用，未来功能的预留参数
- target：执行的目标任务名（一般为函数名）
- args：以元组的方式给执行任务传参
- kwargs：以字典的方式给执行任务传参
- name：线程名，一般不用设置

thread_obj.start()    # 启动线程，让线程开始工作
"""

import time
import threading

def sing():
    while True:
        print("正在唱歌...")
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance, args=("正在跳舞...",))  # kwargs = {"msg": "正在跳舞..."}
    t1.start()
    t2.start()
