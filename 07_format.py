import math
import json

year = 2026
event = "Referendum"
str = f"Result of the {year} {event}"
print(str)

yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes

result = "{:-9} YES votes  {:2.2%}".format(yes_votes, percentage)
print(result)

# repr 字符串原样输出
hello = "hello, world\n"
print(repr(hello))

# 将pi的值保留三位小数
print(f"The value of pi is approximately {math.pi:.3f}.")

# ':'后传递整数，位改字段设置最小字符宽度，常用于列对齐：
table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 7678}
for name, phone in table.items():
    print(f"{name:10} ==> {phone:10d}")

# = 说明符可被用于将一个表达式扩展为表达式文本、等号再加表达式求值结果的形式。
bugs = "roaches"
count = 13
area = "living room"
print(
    f"Debugging {bugs=} {count=} {area=}"
)  # Debugging bugs='roaches' count=13 area='living room'

# 字符串format()方法
print(
    'We are the {} who say "{}!"'.format("knights", "Ni")
)  # We are the knights who say "Ni!"

# 花括号中的数字表示传递给 str.format() 方法的对象所在的位置。
print("{0} and {1}".format("spam", "eggs"))  # spam and eggs
print("{1} and {0}".format("spam", "eggs"))  # eggs and spam

# str.format() 方法中使用关键字参数名引用值。
print(
    "this {food} is {adjective}.".format(food="spam", adjective="absolutely horrible")
)

print("The story of {0}, {1}, and {other}.".format("Bill", "Manfred", other="Georg"))

table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
print("Jack: {0[Jack]}; Sjoerd: {0[Sjoerd]:d}; " "Dcab: {0[Dcab]:d}".format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# str.zfill(), 该方法在数值字符串左边填充零，且能识别正负号：
print('12'.zfill(5)) # '00012'
print('-3.14'.zfill(7)) # '-003.14'

# 读写文件
# f = open('workflie.txt', 'w', encoding="utf-8")

# 再处理文件对象时，最好使用with关键字，优点是，子句体结束后，文件会正确关闭，即便触发异常也可以。而且，使用 with 相比等效的 try-finally 代码块要简短得多：
with open('workfile.txt', 'r+',encoding="utf-8") as f:
    read_data = f.read()
    f.write('This is a test\n')
    print(read_data) # 输出文本内容
print(f.close)

# 将列表转为字符串输出
x = [1, 'simple', 'list']
k = json.dumps(x)
print(k)