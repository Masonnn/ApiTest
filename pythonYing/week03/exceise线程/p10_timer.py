# 定时器： 指定n秒后执行
from threading import Timer


def hello():
    print("Hello, world")


t = Timer(5, hello)
t.start()
