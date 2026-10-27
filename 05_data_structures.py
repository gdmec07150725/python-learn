from collections import deque

# 列表是可变的，列表元素一般都是同质类型，可迭代访问
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
num = fruits.count("apple")
print(num)
print(fruits.index("banana", 4))

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())  # 从栈顶取出元素,也就是数组最后一项
print(stack.pop())
print(stack)  # [3,4]

# collections.deque 可以快速从两端添加或删除元素
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())  # 取出数组左边开始的第一项，相当于删除第一项
print(queue)

# 创建平方值列表
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# 快捷方式
squares = [x**2 for x in range(10)]
print(squares)

# 以下列表推导式讲两个列表中不相等的元素组合起来
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
# 等价于
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)

vec = [-4, -2, 0, 2, 4]
# 过滤列表以排除负数
print([x for x in vec if x >= 0])

# 对所有元素应用一个函数
print([abs(x) for x in vec])

# 使用两个 "for" 来展平嵌套的列表
vec2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec2 for num in elem])

# del语句
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]  # [1, 66.25, 333, 333, 1234.5]
del a[2:4]  # [1, 66.25, 1234.5]
del a[:]  # []
del a  # 删除了整个a变量，后面再引用 a 就会报错

# 在序列中循环时，用 enumerate() 函数可以同时取出位置索引和对应的值：
for i, v in enumerate(["tic", "tac", "toe"]):
    print(i, v)

# 同时循环两个或多个序列时，用 zip() 函数可以将其内的元素一一匹配：
questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for q, a in zip(questions, answers):
    print("What is your {0}?  It is {1}.".format(q, a))

# 元组由多个用逗号隔开的值组成（是不可变变量，一般可包含异质元素序列），例如：
t = 12345, 54321, "hello"  # 圆括号可有可无
print(t[0])  # 12345
print(t)  # (12345, 54321, 'hello')

# 元组可以嵌套
u = t, (1, 3, 4, 5, 6)
print(u)  # ((12345, 54321, 'hello'), (1, 3, 4, 5, 6))

# 元组是不可变对象
# t[0] = 8888 # 会报错

# 空元组
empty = ()
singleton = ("Hello",)  # 包含一个元素的的元组，注意末尾的逗号
len(empty)  # 0
len(singleton)  # 1

# 元组的解包
x, y, z = t  # 序列解包时，左侧变量与右侧序列元素的数量应相等。

# 集合，创建集合用花括号或set()函数，创建空集合只能用set(), 不能用{}，元素自动去重, 迭代或者打印出来的元素顺序不可控
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(basket)  # {'orange', 'banana', 'pear', 'apple'}

# 快速成员检查
"orange" in basket  # true

# 演示针对两个单词中独有的字母进行集合运算
a = set("abracadabra")
b = set("alacazam")
print(a)  # {'a', 'b', 'r', 'd', 'c'}
print(a - b)  # 存在于 a 中但不存在于 b 中的字母
print(a | b)  # 存在于 a 或 b 中或两者中皆有的字母
print(a & b)  #  同时存在于 a 和 b 中的字母
print(a ^ b)  # 存在于 a 或 b 中但非两者中皆有的字母

# 集合也支持推导式
a = {x for x in "abracadabra" if x not in "abc"}
print(a)  # {'r', 'd'}

# 字典，使用{}来创建空字典，字典的键必须唯一，且是不可变元素
tel = {"jack": 4098, "sape": 4139}
tel["guido"] = 4127
print(tel)
print(tel["guido"])
print(tel.get("irv"))  # 不会报错，但是会返回None
del tel["guido"]
print(tel)
print(list(tel))  # ['jack', 'sape'] list返回的是字典的key列表
print("guido" in tel)  # False

# dict() 构造函数可以直接用键值对序列创建字典：
print(dict([("sape", 4139), ("guido", 4127), ("jack", 4098)]))
# 或者这样
dict(sape=4139, guido=4127, jack=4098)
# 字典推导，可以用任意键值表达式创建字典：
print({x: x**2 for x in (2, 4, 6)})

# 当对字典自行循环时，可以使用items()方法同时提取键及其对应的值
knights = {"gallahad": "the pure", "robin": "the brave"}
for k, v in knights.items():
    print(k, v)
    
print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))
