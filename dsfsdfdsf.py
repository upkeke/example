def add(n, i):
    return n + i


def qtest1():
    for i in range(4):
        yield i


# -- coding: utf-8 --
import _example as kk


def gest_fun1():
    x = kk.add(10, 12)
    print(x)
    kk.introduce()
    # kk.h1("dddd")
    # kk.hello("bbb")
    i = [1, 4, 6, 7, 8]
    for a in i:
        print(a)


class A():
    def __init__(self):
        self.x = 1
        self.__y = 'A'

    def show_y(self):
        print(self.__y)


class B(A):
    def __init__(self):
        #super(B, self).__init__()
        self.__y = "B"

    def show_y(self):
        print(self.__y)


a = A()
b = B()
print(dir(a))
print(dir(b))

print(f"a.y={a._A__y}")
print(f"b.by={b._B__y}")
#print(f"b.ay={b._A__y}")

print(a.__dict__)
print(b.__dict__)
print("hello github")
x=1