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
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

# %d对应数字; %s 对应字符串
# 打印名片
#1. 请使用input获取必要的信息
name = input("请输入名字：")
# 2. 使用print来打印名片
print("==========")
print("姓名：%s"%name)
print("==========")

# 请输入QQ号

# 开始以为python的数字输入时不同input的，后来查看了帮助，才知道需要进行类型的转换。
# n1=input("a num:")
# n2=int(n1)

number = input("请输入QQ号:")
qq = int(number)
print("我的qq号是:%d"%qq)