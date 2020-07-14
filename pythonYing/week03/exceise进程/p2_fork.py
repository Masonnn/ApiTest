# 区分父子进程
import os
import time

res = os.fork()
time.sleep(1)
print(f'res == {res}')

if res == 0:
    print(f"我是子进程， pid: {os.getpid()}, 我的父进程pid是：{os.getppid()}")
else:
    print(f"我是父进程， pid: {os.getpid()}")