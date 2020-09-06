# 函数装饰器实现单实例模式
def singleton(cls):
    instances = {}

    def getInstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getInstance


@singleton
class MyClass:
    pass


m1 = MyClass()
m2 = MyClass()
print(id(m1))
print(id(m2))


# 类装饰器实现单实例模式
class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self, ):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class Cls2(object):
    def __init__(self):
        pass


cls1 = Cls2()
cls2 = Cls2()
print(id(cls1) == id(cls2))


class Cls3():
    pass


Cls3 = Singleton(Cls3)
cls3 = Cls3()
cls4 = Cls3()
print(id(cls3) == id(cls4))
