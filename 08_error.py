import sys

try:
    f = open("workfile.txt")
    s = f.readline()
    # i = int(s.strip())
    print(s)
except OSError as error:
    print("OS error:", error)
except ValueError:  # 捕获的值转换异常
    print("Could not convert data to an integer.")
except Exception as err:  # Exception 捕获基本所有的异常
    print(f"unexpected {err=}, {type(err)=}")
    raise
else:  # 没有触发异常的时候会进入else
    print("has", len(f.readline()), "lines")
    f.close()

# raise 语句支持强制出发指定的异常。
# raise NameError('HiThere') # NameError: HiThere

# 定义清理操作
# try:
#     raise KeyboardInterrupt
# finally: # 无论是否有异常都会触发fially （注意：如果执行 try 语句时遇到 break、continue 或 return 语句，则 finally 子句在执行 break、continue 或 return 语句之前执行。）
#     print("Goodbye, world!")


# ExceptionGroup 引发和处理多个不相关的异常
def f():
    excs = [OSError("error 1"), SystemError("error 2")]
    raise ExceptionGroup("there were problems", excs)


try:
    f()
except Exception as e:
    print(f"caught {type(e)}: {e}")

# 异常有一个 add_note方法用注释细化异常情况, 当一个异常被创建以引发时，它通常被初始化为描述所发生错误的信息
try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise
