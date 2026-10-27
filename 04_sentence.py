x = int(input("Please enter an integer: "))
print(x)
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:  # elif是else if的缩写
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

# for 语句
# 度量一些字符串
words = ["cat", "window", "defenestrate"]
for w in words:
    print(w, len(w))


# 很难正确地在迭代多项集的同时修改多项集的内容。更简单的方法是迭代多项集的副本或者创建新的多项集：
users = {"Hans": "active", "Éléonore": "inactive", "景太郎": "active"}

# 迭代一个副本
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

print(users)

# range() 函数，用于生成等差数列, 不包含终止值，返回来的结果是一个迭代器对象：
for i in range(5):
    print(i)
# range 可以不从0开始，且可以按给定的步长递增：
list(range(5, 10))  # [5,6,7,8,9]
list(range(0, 10, 3))  # [0,3,6,9] 步长是3
print(list(range(-10, -100, -30))) # [-10, -40, -70]

# match语句，类似case的语法

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I am a teapot"
        case _: # _是通配符，必定会匹配成功，就像是switch的default一样
            return "Something's wrong with the internet"

# 定义函数使用def关键字
def fib(n):
    a,b = 0,1
    while a < n:
        print(a, end=" ")
        a,b = b, a+b
    print()

fib(2000)

# 函数参数的/(仅限位置形参)，*（仅限关键字形参）
def standard_arg(arg): # 位置形参和关键字形参都可以
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
    
standard_arg(1)
standard_arg(arg=1)
pos_only_arg(1)
kwd_only_arg(arg=1)
combined_example(1, standard=1, kwd_only=2)

# 解包实参列表
list(range(3,6))
args = [3,6]
list(range(*args))

# 用**操作符传递关键字参数：
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

# 函数注解：
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs