############################
# __new__ 方式实现单例模式

class Singleton(object):
    __isinstance = False  # 默认没有被实例化

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance:
            return cls.__isinstance  # 返回实例化对象
        cls.__isinstance == object.__new__(cls)  # 实例化
        return cls.__isinstance


class _Singleton(object):
    pass


# Singleton = _Singleton()
# del _Singleton
one = Singleton()
another = Singleton()  # 没用，绕过
print(id(Singleton()))
print(id(another))
print(id(one))
print(type(Singleton))
print(type(another))
print(type(one))


class Single(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Single, cls).__new__(cls, *args, **kwargs)
        return cls._instance


s1 = Single()
s2 = Single()
assert id(s1) == id(s2)
print(id(s1) == id(s2))

import threading


class Singleton2(object):
    objs = {}
    objs_locker = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls in cls.objs:
            return cls.objs[cls]
        cls.objs_locker.acquire()
        try:
            if cls in cls.objs:
                return cls.objs[cls]
            cls.objs[cls] = object.__new__(cls)
        finally:
            cls.objs_locker.release()


# 利用经典的双检查锁机制，确保了在并发环境下Singleton的正确实现。
# 但这个方案并不完美，至少还有以下两个问题：
# ·如果Singleton的子类重载了__new__()方法，会覆盖或者干扰Singleton类中__new__()的执行，
# 虽然这种情况出现的概率极小，但不可忽视。
# ·如果子类有__init__()方法，那么每次实例化该Singleton的时候，
# __init__()都会被调用到，这显然是不应该的，__init__()只应该在创建实例的时候被调用一次。
# 这两个问题当然可以解决，比如通过文档告知其他程序员，子类化Singleton的时候，请务必记得调用父类的__new__()方法；
# 而第二个问题也可以通过偷偷地替换掉__init__()方法来确保它只调用一次。
# 但是，为了实现一个单例，做大量的、水面之下的工作让人感觉相当不Pythonic。
# 这也引起了Python社区的反思，有人开始重新审视Python的语法元素，发现模块采用的其实是天然的单例的实现方式。
# ·所有的变量都会绑定到模块。
# ·模块只初始化一次。
# ·import机制是线程安全的（保证了在并发状态下模块也只有一个实例）。
# 当我们想要实现一个游戏世界时，只需简单地创建World.py就可以了。

# World.py
import Sun


def run():
    while True:
        Sun.rise()
        Sun.set()


# main.py
import World

World.run()
