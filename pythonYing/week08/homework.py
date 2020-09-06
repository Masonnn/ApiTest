from functools import wraps
import time


# map()

def mapper(func, *iterables):
    for args in zip(*iterables):
        yield func(*args)


# def timer(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         print("=========begin===========")
#         begin = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print("=========end===========")
#         print(f"{func.__name__}运行用时： {end - begin}")
#         return result
#
#     return inner
#
#
# @timer
# def myfunc(a):
#     for _ in range(100000000):
#         a += 1
#     # print(a)
#     print("hello world ================")
#     print(myfunc.__name__)
#     return a


if __name__ == '__main__':
    myfunc(100)
