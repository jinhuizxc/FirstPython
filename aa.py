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
print(2*2)
print(2**2)  # 次方  2^16 = 65536
print(2**3)
print(2**4)
print("A"*10) # 结果：AAAAAAAAAA

# print一次输出多个变量值,除了%d,s外还有c、i、u、o等可以参考文档资料
name = "jh"
age = 25
addr = "河南"
print("姓名是：%s，年龄是：%d， 地址是：%s" %(name, age, addr))

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

a = int(input("请输入1-2："))
if a == 1:
    print("是1")
elif a == 2:
    print("是2")
else:
    print("不是1、2")