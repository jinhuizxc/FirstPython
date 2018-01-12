# 廖雪峰网站：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000
# 让pytho2识别中文，输入：
#  coding=utf-8 解决中文问题
# 官方推荐写法是：# -*- coding：utf-8 -*-
'''# coding=utf-8'''
# 输入注释
print("hello world")
# Python的语法比较简单，采用缩进方式
# Python使用缩进来组织代码块，请务必遵守约定俗成的习惯，坚持使用4个空格的缩进。
# 在文本编辑器中，需要设置把Tab自动转换为4个空格，确保不混用Tab和空格。


# %d对应数字; %s 对应字符串
# 打印名片
# 1. 请使用input获取必要的信息
# name = input("请输入名字：")
# number = input("请输入QQ号:")
# # 2. 使用print来打印名片
# print("==========")
# print("姓名：%s"%name)
#
# # qq = int(number)
# # print("我的qq号是:%d"%qq)
# print("我的qq号是:%s"%number)
# print("==========")

# 请输入QQ号

# 开始以为python的数字输入时不同input的，后来查看了帮助，才知道需要进行类型的转换。
# n1=input("a num:")
# n2=int(n1)

# python2与python3输入功能的不同：
# python2输入：input()会执行运算：
# 例如：
# name = input("xxxx:")
# 我输入1+2，那么会输出结果3，换言之如果输入名字例如：jh，则因为没有jh的定义出现错误，那么怎么办呢？
# 采用name = raw_input()就可以了，这个方法在python3中已经弃用了，目前主推python3


# python3的input就是输入：
# name = input("xxxx:")
# 我输入1+2，那么会输出结果1+2

# if条件判断，if条件满足时执行的判断，
# 最后的print("-----8-------")一直都会执行啊，区别在于>18时输出，<18也输出，不受影响啊。
age = 16
if age > 18:
    print("-----1-------")
    print("-----1-------")
    print("-----1-------")
    print("-----1-------")
    print("-----1-------")
    print("-----1-------")
    print("-----9-------")
else:
    print("-----2-------")
    print("-----2-------")
    print("-----2-------")
    print("-----2-------")
print("-----8-------")

# 标识符由字母、下划线和数字组成，且数字不能开头
# 关键字：python一些具有特殊功能的标识符，就是所谓的关键字
# 关键字，是python已经在使用，所以不允许开发者自己定义和关键字相同的名字的标识符
import keyword

# 打印出关键字：
# 标识符：['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
str = keyword.kwlist
print("标识符：%s" % str)

# 运算符
a = 5
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # 商2.5
print(a % b)  # 余1
print("=================")
print(2 * 2)
print(2 ** 2)  # 次方  2^16 = 65536
print(2 ** 3)
print(2 ** 4)
print("A" * 10)  # 结果：AAAAAAAAAA

# print一次输出多个变量值,除了%d,s外还有c、i、u、o等可以参考文档资料
name = "jh"
age = 25
addr = "河南"
print("姓名是：%s，年龄是：%d， 地址是：%s" % (name, age, addr))

# 比较运算符
# >=、<=、== 、!=(<>不等于，python2里面用)
# 或者or、并且and
# you = input("看电影么？")
# other = input("吃饭去？")
# # if you == "去" or other == "去":
# if you == "去" and other == "去":
#     print("同时进行！")

# not运算符
a = -1
if a > 0 and a <= 50:  # 建议：if 0 < a <= 50:
    print("在0到50之间")
if not (0 < a <= 50):
    print("小于等于0，大于50")

# if elif elif 条件判断
a = 20
if a >= 40:
    print("大于等于40")
elif a >= 30:
    print("大于等于30")
# elif a >= 20:
else:
    print("大于等于20")
# 例子：
# a = int(input("请输入1-2："))
# if a == 1:
#     print("是1")
# elif a == 2:
#     print("是2")
# else:
#     print("不是1、2")

# while循环
# while 条件：
#     条件成立要做的事
num = 1
while num <= 10:
    print(num)
    num = num + 1
# 输出1-100之间
num = 1
while num <= 100:
    print(num)
    num = num + 1
# if嵌套
# name = input("请输入用户名：")
# password = int(input("请输入密码："))
# if name == "name":
#     print("用户名输入正确")
#     if password == 123:
#         print("密码输入正确")
#         print("用户可以正常登录")
#     else:
#         print("密码输入不正确！，请再次输入")
# else:
#     print("用户名不对！")
#     print("用户名输入不正确，请再次输入")
# while嵌套
# 打印矩形
i = 1
while i <= 5:
    # 打印的操作
    # print("*****")
    j = 1
    while j <= 5:
        print("*", end="")  # end=""横向排列，结果：*************************
        j = j + 1
    print("")
    i = i + 1

# 打印星号
i = 1
while i <= 5:
    # 打印的操作
    # print("*****")
    j = 1
    while j <= i:
        print("*", end="")  # end=""横向排列，结果：*************************
        j = j + 1
    print("")
    i = i + 1

# 复合赋值运算符
# +=、-=、*=、/=、%=、**=、//=
a = 2
b = 4
a += b
print(a)
# 打印九九乘法表, \t 制表符
print("1 \t 2")
i = 1
while i <= 9:
    # 打印的操作
    # print("*****")
    j = 1
    while j <= i:
        # print("%d*%d=%d " % (j, i, j * i), end="")
        print("%d*%d=%d\t" % (j, i, j * i), end="")
        j = j + 1
    print("")
    i = i + 1

# 剪刀石头布
# import random88
# player = int(input("请输入 0剪刀 1石头 2布:"))
# computer = random.randint(0, 2)
# print("电脑输出是：%d " % computer)
# if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
#     print("你赢了！")
# elif player == computer:
#     print("平局，再来！")
# else:
#     print("你输了！")

#for循环
name = "zxcvb"
for s in name:
    print("###")
    print(s)

# break
i = 1
length = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
        length = length + 1
        if length == 20:
            break
    i = i + 1

# break、continue
print("=============================")
i = 1
while i <= 10:
        i = i + 1
        print("-----")
        if i == 3:
            # break
            continue # 执行到这里，后面的语句不执行，继续while循环
        print(i)


print("======")

# while嵌套中break的作用范围
i = 1
while i <= 5:
    # 打印的操作
    # print("*****")
    j = 1
    while j <= i:
        print("*", end="")
        j = j + 1
        break  # 结束内部while循环
    print("")
    i = i + 1

# 字符串在内存中的存储方式
# 1G = 1024M 1M = 1024K 1K = 1024byte(字节)最小的存储单元是字节
name = "asdf"
print(len(name)) # 占用4个字节
# 字符串的相加
a = "aaaa"
b = "bbbb"
c = a + b
print(c)
# 组成字符串的2种方式
print("===" + c + "===")
print("===%s==="%c)
