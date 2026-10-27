# 作用域示例
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam  ## nonlocal 用于修改该函数作用域外层的作用域的变量的值
        spam = "nonlocal spam"

    def do_global():
        global spam  ## global指当前 Python 模块的顶层作用域
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)


## 定义一个class 类
class Complex:
    # __init__是类实例化的时候会调用的方法，就跟构造函数差不多
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


# 类的实例化
x = Complex(3.0, -4.5)
print(x.i, x.r)

## 直接在实例化后的对象上定义属性
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2

print(x.counter)
del x.counter


class Dog:

    kind = "canine"  # 类变量被所有实例所共享

    def __init__(self, name):
        self.name = name  # 实例变量为每个实例所独有


d = Dog("Fido")
e = Dog("Buddy")
print(d.kind, e.kind)  # 被所有的 Dog 实例所共享
print(d.name, e.name)

# 类的继承


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # 原始 update() 方法的私有副本


# MappingSubclass 继承了 Mapping 基类
class MappingSubclass(Mapping):

    def update(self, keys, values):
        # 为 update() 提供了新的签名
        # 但不会破坏 __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
