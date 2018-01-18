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

# for循环
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
        continue  # 执行到这里，后面的语句不执行，继续while循环
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
print(len(name))  # 占用4个字节
# 字符串的相加
a = "aaaa"
b = "bbbb"
c = a + b
print(c)
# 组成字符串的2种方式
print("===" + c + "===")
print("===%s===" % c)

# 字符串中的下标
name = "qwer"
print(name[2])
print(name[-1])
print(name[-2])
print(name[len(name) - 1])

# 切片、字符串逆序
name = "asdfghjkl"
print(name[2:5])
print(name[2:-1])
print(name[2:])  # 冒号后不写默认取到最后一个字符
print(name[2:-1:2])  # :2表示间隔是2
print(name[0:])
print(name[-1:])  # 表示从l到最后
# 对字符串进行倒序（逆序）
print(name[-1:0])
print(name[-1:0:-1])  # lkjhgfds,但是没有输出a
print(name[-1::-1])  # lkjhgfdsa,输出a
print(name[::-1])

# 列表引入、定义
names = ["a", "b", "c"]
print(names)
# C语言中的数组 int nums[] = {1,2,3,4}
nums = [1, 2, 3, 4]
print(nums)
# python 可以存储多种类型
type1 = [1, 2, 3, 4, "A", "B"]
print(type1)

# 列表的增删改查
names1 = ["a", "b", "c"]
# 添加元素：3种append、insert、extend
# 方式一
names1.append("d")
print(names1)
# name.insert（位置，要添加的内容）
# 方式二
names1.insert(1, "f")
print("name1")
print(names1)

names2 = ["z", "x", "c"]
# 2个列表的相加
print("name1 + name2")
print(names1 + names2)
print("-----------")
# 方式三
A = [1, 2]
B = [3, 4]
A.extend(B)
# 注意; 直接写print(A.extend(B)) 输出的是None, 必须是输出A才能输出,
# 为什么？因为A.extend(B)只是一个执行将内容加载进A里了，但不是输出所以为None，输出最终的A就好，这点不要与所谓的引用对象混淆！
print(A)
# list1 = ['Google', 'Runoob', 'Taobao']
# list2=list(range(5)) # 创建 0-4 的列表
# list1.extend(list2)  # 扩展列表
# print ("扩展后的列表：", list1)

# 删除元素:3种pop、remove、del
a = [1, 2, 3, 3, 4]
print("pop")
# b = a.pop() # b = 3说明a.pop()返回值是整数，而且还是最后一个元素的长度
# print(b)  # 输出删除的最后一个元素
# print(a.pop()) # 输出删除的元素值
print(a)
# print("remove")
# a.remove(3)  # 找到删除的值，只删除一次
# print(a)
# print("del")
# del a[0]  # 通过下标删除
# print(a)

# 改元素
print("修改元素")
a[0] = 7
print()
# 查询元素：可以用in或者not in 判断
print("查询元素")
if 7 in a:
    print("元素找到")
else:
    print("没找到")
if 7 not in a:
    print("可以添加元素")
else:
    print("元素已经存在")

# 名字管理系统
# print("=" * 50)
# print("名字管理系统 v1.0")
# print("1.添加一个新的名字")
# print("2.删除一个名字")
# print("3.修改一个名字")
# print("4.查询一个名字")
# print("5.退出系统")
# print("=" * 50)
# names = []  # 定义一个空的列表用来存储添加的名字
# while True:
#     # 获取用户输入
#     num = int(input("请输入功能序号："))
#     if num == 1:
#         new_name = input("请输入名字：")
#         names.append(new_name)
#         print(names)
#     elif num == 2:
#         del_name = input("请输入你要删除的名字：")
#         if del_name in names:
#             names.remove(del_name)
#             print("该名字已经成功删除！")
#         else:
#             print("查无此人！")
#     elif num == 3:
#         modify_name = input("请输入要修改的名字：")
#         if modify_name in names:
#             index = names.index(modify_name)
#             new_modify_name = input("找到你要找的人了, 请输入新的名字：")
#             names[index] = new_modify_name
#             print(names)
#         else:
#             print("查无此人！")
#     elif num == 4:
#         find_name = input("请输入要查询的名字：")
#         if find_name in names:
#             print("找到你要找的人了!")
#             names.index(find_name)
#         else:
#             print("查无此人!")
#     elif num == 5:
#         break
#     else:
#         print("您的输入有误，请重新输入")
# print("您已经成功退出该系统，欢迎再次使用！")

# 字典的定义、引用
banzhang = ["班长", "山东", 18]
print("%s %d %s" % (banzhang[0], banzhang[2], banzhang[1]))
# info = {键：值， 键：值}
info = {"name": "班长", "addr": "山东", "age": 18}
print("%s %s %d" % (info["name"], info["addr"], info["age"]))
print("%s %d %s" % (info["addr"], info["age"], info["name"]))

# 字典的增、删、改、查
# 添加元素
# info = {"name": "a"}
# info["age"] = 10
# info["QQ"] = 10086
# 上面3行代码系统建议采用下面方式
info = {"name": "a", "age": 10, "QQ": 10086}
print(info)
# 修改元素，通过key来查询
info["QQ"] = 100000
print(info)
# 删除元素
del info["QQ"]
print(info)
#  没有QQ时del info["QQ"] KeyError: 'QQ'
# del info["QQ"]
# print(info)
# 查询元素
print(info.get("age"))
# 不建议用del info去查询已经删除的内容，可以用get去获取
print(info.get("QQ"))

# 补充：
print("字典补充")
temps = [{"name": "aa", "age": 18}, {"name": "bb", "age": 18}]
for temp in temps:
    # print(temp) # 输出{'name': 'aa', 'age': 18} {'name': 'bb', 'age': 18}
    print(temp["name"])  # 输出aa bb

# 名片管理系统
# print("=" * 50)
# print("名片管理系统 v1.0")
# print("1.添加一个新的片")
# print("2.删除一个名片")
# print("3.修改一个名片")
# print("4.查询一个名片")
# print("5.显示所有的名片")
# print("6.退出系统")
# print("=" * 50)
# # 定义一个字典列表
# card_info = []
# while True:
#     num = int(input("请输入功能序号："))
#     if num == 1:
#         # dasfdf
#         new_name = input("请输入新的名字：")
#         new_qq = input("请输入新的QQ：")
#         new_weixin = input("请输入新的微信：")
#         new_addr = input("请输入新的地址：")
#         new_info = {"name": new_name, "qq": new_qq, "weixin": new_weixin, "addr": new_addr}
#         card_info.append(new_info)
#         print(card_info)  # [{'name': 'jh', 'qq': '111', 'weixin': '2222', 'addr': '3333333333'}]
#     elif num == 2:
#         pass
#     elif num == 3:
#         pass
#     elif num == 4:
#         find_name = input("请输入要查找的名字：")
#         find_flag = 0  # 默认表示没有找到
#         for temp in card_info:
#             if find_name == temp["name"]:
#                 print("姓名\tQQ\t微信\t住址")
#                 print("%s\t%s\t%s\t%s" % (temp["name"], temp["qq"], temp["weixin"], temp["addr"]))
#                 find_flag = 1  # 表示找到了
#                 break  # break 可以结束while循环也可以结束for循环
#             # else:
#             #     print("查无此人！")
#             #     # 输出：加上else：明明有aa，却输出查无此人！是因为遍历到bb的时候出现的！说明这样写是不对的！
#         # 判断是否找到了
#         if find_flag == 0:
#             print("查无此人！")
#     elif num == 5:
#         print("姓名\tQQ\t微信\t住址")
#         for temp in card_info:
#             # print(temp)
#             # 制表
#             print("%s\t%s\t%s\t%s" % (temp["name"], temp["qq"], temp["weixin"], temp["addr"]))
#     elif num == 6:
#         break
#     else:
#         print("您的输入有误，请重新输入")
#     print("")
# print("您已经成功退出该系统，欢迎再次使用！")

# while、 for循环遍历列表,
nums = [11, 22, 33, 44, 55]
# 用len得到列表长度！
nums_length = len(nums)
i = 0
while i < nums_length:
    print(nums[i])
    i = i + 1
# 用for循环更简单来遍历
for num in nums:
    print(num)

# for-else的应用
# 列表有内容还是没有内容，else语句都执行，如果加了break在for语句中会退出整个for-else语句
# 关于这个方法：
# 可以用在上面的名片管理系统序号等于4的地方：
# 加了break就是找了，输出：找到！没找到就是else:没找到，要会灵活运用！
# nums = [1, 2, 3, 4]
# find_num = int(input("输入你要找的数字："))
# # nums = []
# for num in nums:
#     # print(num)
#     if num == find_num:
#         print("找到了！")
#         break
# else:
#     print("没找到！")

# 列表的append与extend
a = [1, 2, 3]
b = ["a", "b"]
# a.extend(b)  # 输出：[1, 2, 3, 2, 3]
a.append(b)  # 输出：[1, 2, 3, [2, 3]]
print(a)

# 列表append的注意项
a = [1, 2, 3]
b = ["a", "b"]
a = a.append(b)
print(a)  # 输出None 要注意

# 元组tuple
# 元祖和列表十分相似，
# 不过元组是不可变的。即你不能修改元组。
# 元组通过圆括号中用逗号分隔的项目定义。
# 元组通常用在使语句或用户定义的函数能够安全的采用一组值的时候，即被使用的元组的值不会改变。元组可以嵌套。
nums = [11, 22, 33]
print(type(nums))  # <class 'list'>
nums2 = (1, 2, 3, 3, 4)
print(type(nums2))  # <class 'tuple'>
nums[0] = 100
print(nums)
print(nums2)
print(nums2.count(4))  # 相同元素中个数
print(nums2.index(2))  # 查找元素的第一个索引值

# 字典的常见操作、遍历
info = {"name": "as", "age": 12}
print(info.keys())  # 输出所有的keys：dict_keys(['name', 'age'])
print(info.values())  # 输出所有的值：dict_values(['as', 12])
for temp in info.keys():
    print(temp)
for temp in info.values():
    print(temp)
for temp in info.items():
    print(temp)  # 输出元组：('name', 'as') ('age', 12)
# 通过下标取数据
for temp in info.items():
    # key = name, value = as key = age, value = 12
    print("key = %s, value = %s" % (temp[0], temp[1]))

# 关于items在循环时可以进行拆包分析
for A, B in info.items():
    print("key = %s, value = %s" % (A, B))

a = (11, 22)
b = a
print(b)

c, d = a
print("%d,%d" % (c, d))

# 函数
# 打印佛祖 鼠标左键选中，
# 光标在当前要选中的位置（或者先选中一个单词）再按Alt+J，即可选中下一个同样的单词。
# Pycharm在Edit->Find中有提示.

print("                            _ooOoo_  ")
print("                           o8888888o  ")
print("                           88  .  88  ")
print("                           (| -_- |)  ")
print("                            O\\ = /O  ")
print("                        ____/`---'\\____  ")
print("                      .   ' \\| |// `.  ")
print("                       / \\||| : |||// \\  ")
print("                     / _||||| -:- |||||- \\  ")
print("                       | | \\\\\\ - /// | |  ")
print("                     | \\_| ''\\---/'' | |  ")
print("                      \\ .-\\__ `-` ___/-. /  ")
print("                   ___`. .' /--.--\\ `. . __  ")
print("                ."" '< `.___\\_<|>_/___.' >'"".  ")
print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
print("         ======`-.____`-.___\\_____/___.-`____.-'======  ")
print("                            `=---='  ")
print("  ")
print("         .............................................  ")
print("                  佛祖镇楼                  BUG辟易  ")
print("          佛曰:  ")
print("                  写字楼里写字间，写字间里程序员；  ")
print("                  程序人员写程序，又拿程序换酒钱。  ")
print("                  酒醒只在网上坐，酒醉还来网下眠；  ")
print("                  酒醉酒醒日复日，网上网下年复年。  ")
print("                  但愿老死电脑间，不愿鞠躬老板前；  ")
print("                  奔驰宝马贵者趣，公交自行程序员。  ")
print("                  别人笑我忒疯癫，我笑自己命太贱；  ")
print("                  不见满街漂亮妹，哪个归得程序员？  ")


# 函数：把一个独立的功能的代码块当作一个整体，就是一个函数,
# 下面的函数方法体写法符合我们看到的流程图，先判断-在结果！
# 多个函数的定义与调用
def print1():
    print(1)
    print("end")


def print2():
    print(2)
    print("end")


print1()
print2()


# 定义一个函数,带参函数
# def sum_2_sum(a, b):
#     # a = 10
#     # b = 20
#     result = a + b
#     print("%d + %d = %d" % (a, b, result))
#
#
# num1 = int(input("请输入第1个数字："))
# num2 = int(input("请输入第2个数字："))
# # 调用函数
# sum_2_sum(num1, num2)


# return的作用：
def get_wendu():
    wendu = 22
    print("当前温度是%d" % wendu)
    return wendu


def get_wendu_huashi(result):
    result = result + 3
    print("得到的结果是%d" % result)


result = get_wendu()
get_wendu_huashi(result)


def test():
    a = 11
    b = 22
    c = 33
    # 第1种方式用列表来封装3个变量的值
    # d = [a, b, c]
    # return d
    # 第二种
    # return [a, b, c]
    # 第三种
    # return (a, b, c)
    return a, b, c


result = test()
print(result)


# 函数的嵌套调用
def test():
    print("as")


def test2():
    print("2.1")
    print("2.2")


def test3():
    print("3.1")
    test2()
    print("3.2")


test3()


# 学会多去运用函数调用
def print_line():
    print("-----------------")


def print_5_line():
    i = 0
    while i < 5:
        # print("-----------------")
        print_line()
        i += 1


print_5_line()

# 函数的嵌套的应用-计算3个数的和,并求平均值
# def sum_3_sums(a, b, c):
#     result = a + b + c
#     # print("%d + %d + %d = %d" % (a, b, c, result))
#     return result
#
#
# def average_3_nums1(a, b, c):
#     result = sum_3_sums(a, b, c)
#     result = result / 3
#     print("平均值是：%d" % result)
#     return result
#
#
# def average_3_nums2(a, b, c):
#     result = sum_3_sums(a, b, c)
#     result = result / 3
#     print("平均值是：%d" % result)
#     return result
#
#
# def sum_2_avarage(a, b):
#     sum = a + b
#     print("得到2个平均值的和是%d" % sum)
#
#
# # 获取3个数
# num1 = int(input("第1个值："))
# num2 = int(input("第2个值："))
# num3 = int(input("第3个值："))
# num4 = int(input("第4个值："))
# num5 = int(input("第5个值："))
# num6 = int(input("第6个值："))
#
# # sum_3_sums(num1, num2, num3)
# sum1 = average_3_nums1(num1, num2, num3)
# sum2 = average_3_nums2(num4, num5, num6)
# sum_2_avarage(sum1, sum2)


# 局部变量、全局变量
print("局部变量/全局变量")
a = 100


def test1():
    # 局部变量
    a = 100
    print("a = %d" % a)


# 出错：TypeError: not all arguments converted during string formatting
def test2():
    a = 50
    print("a = %d" % a)


test1()
test2()
# TypeError: not all arguments converted during string formatting
print("a = %d" % a)


# 局部变量、全局变量的区别
# 下面是2个例子：
def get_wendu():
    wendu = 33
    return wendu


def print_wendu(wendu):
    print("温度是%d" % wendu)  # 输出：温度是33


result = get_wendu()
print_wendu(result)

# 定义一个全局变量
wendu = 0


# global的用法
def get_wendu():
    # 使用global用来对一个全局变量的声明，
    # 那么这个函数中的wendu=33就不是定义一个局部变量，而是对全局变量进行修改
    global wendu
    wendu = 33


def print_wendu():
    global wendu
    wendu = -1
    print("温度是%d" % wendu)  # 输出：温度是33


get_wendu()
print_wendu()
# 全局变量的位置,放在方法之前
a = 100


def test():
    print("a = %d" % a)
    print("b = %d" % b)
    # print("ab = %d" % ab)  # NameError: name 'ab' is not defined


b = 200
test()

# ab = 300

# 名片管理系统函数版
# # 用来存储名片
# card_info = []
#
#
# def print_menu():
#     """完成打印功能菜单"""
#     print("=" * 50)
#     print("名片管理系统 v1.0")
#     print("1.添加一个新的片")
#     print("2.删除一个名片")
#     print("3.修改一个名片")
#     print("4.查询一个名片")
#     print("5.显示所有的名片")
#     print("6.退出系统")
#     print("=" * 50)
#
#
# def add_new_card_info():
#     """完成添加名片"""
#     new_name = input("请输入新的名字：")
#     new_qq = input("请输入新的QQ：")
#     new_weixin = input("请输入新的微信：")
#     new_addr = input("请输入新的地址：")
#     new_info = {"name": new_name, "qq": new_qq, "weixin": new_weixin, "addr": new_addr}
#     # 将一个字典添加到列表中
#     card_info.append(new_info)
#     print(card_info)  # [{'name': 'jh', 'qq': '111', 'weixin': '2222', 'addr': '3333333333'}]
#
#
# def find_card_info():
#     find_name = input("请输入要查找的名字：")
#     find_flag = 0  # 默认表示没有找到
#     for temp in card_info:
#         if find_name == temp["name"]:
#             print("姓名\tQQ\t微信\t住址")
#             print("%s\t%s\t%s\t%s" % (temp["name"], temp["qq"], temp["weixin"], temp["addr"]))
#             find_flag = 1  # 表示找到了
#             break  # break 可以结束while循环也可以结束for循环
#         # else:
#         #     print("查无此人！")
#         #     # 输出：加上else：明明有aa，却输出查无此人！是因为遍历到bb的时候出现的！说明这样写是不对的！
#     # 判断是否找到了
#     if find_flag == 0:
#         print("查无此人！")
#
#
# def show_all_info():
#     print("姓名\tQQ\t微信\t住址")
#     for temp in card_info:
#         # print(temp)
#         # 制表
#         print("%s\t%s\t%s\t%s" % (temp["name"], temp["qq"], temp["weixin"], temp["addr"]))
#
#
# # 选中代码块，按Tab。
# # 要是想往左移，就按Shift + Tab
#
# def main():
#     """完成整个函数的调用"""
#     # 打印功能提示
#     print_menu()
#     while True:
#         num = int(input("请输入功能序号："))
#         if num == 1:
#             add_new_card_info()
#         elif num == 2:
#             pass
#         elif num == 3:
#             pass
#         elif num == 4:
#             find_card_info()
#         elif num == 5:
#             show_all_info()
#         elif num == 6:
#             break
#         else:
#             print("您的输入有误，请重新输入")
#         print("")
#     print("您已经成功退出该系统，欢迎再次使用！")
#
#
# # 调用主函数
# main()

# 列表、字典当作全局变量
list = [11, 22, 33]
dic = {"name": "aaaa", "age": 20}


def test():
    print("=============")
    list.append(44)
    dic["qq"] = 100


test()
print(list)
print(dic)

# 缺省参数——默认参数，重新赋值则不是缺省参数b=22,c=10
print("缺省参数")


# 实参与形参命名要一致


def test(a, b=22, c=10):
    result = a + b + c
    print("结果：%d" % result)


test(11, 22)
test(33, 22)
test(44, 22, c=1)

# 不定长参数1 args名称可以自定义
print("不定长参数")


def sum_2_num(a, b, *args):
    print(a)
    print(b)
    print(args)
    result = a + b
    for num in args:
        result += num
    print("result = %d" % result)


sum_2_num(11, 22, 33, 44, 55, 66)
sum_2_num(11, 22, 33)
sum_2_num(11, 22)


# 不定长参数2,最复杂的参数
def test(a, b, c=33, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)  # 输出(4, 5, 6)
    print(kwargs)  # {'done': 5, 'task': 6}


test(1, 2, 3, 4, 5, 6, done=5, task=6)

# 拆包、元组、字典
print("拆包、元组、字典")


# *在实参里是拆包，在形参里用来保存一些值


def test(a, b, c=33, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)  # 输出(4, 5, 6)
    print(kwargs)  # {'done': 5, 'task': 6}


A = (44, 55, 66)
B = {"name": "aa", "age": 10}
test(11, 22, 33, A, B)  # ((44, 55, 66), {'name': 'aa', 'age': 10})
test(11, 22, 33, *A, **B)  # (44, 55, 66) {'name': 'aa', 'age': 10}

# 引用 在C++中a有内存空间b=a,b也有内存空间
# 在python中a = 100，知道有100，a指向100，b=a，b指向100
# 用id可以知道占用内存空间的地址 , 指向地址
print("引用")
a = 100
b = a
print(id(a))  # 1762187872  指向地址
print(id(b))  # 1762187872  指向地址

# 不可变、可变类型
# 不可变类型：数字、字符串、元组
print("不可变、可变类型")
info = {"name": "aa", 3.14: "bb", (11, 22): "cc"}
# infos = {"name": "aa", 3.14: "bb", (11, 22): "cc", [1, 2]: "dd"}
print(info)  # 哈希算法， 可变类型不允许当作key值
# print(infos)  # TypeError: unhashable type: 'list'

# 递归 5！= 4*3*2*1
i = 1
result = 1
while i <= 4:
    result = result * i
    i += 1
print(result)


# 5！ = 5*4！ 函数自身调用自己——递归
# 计算4的阶乘！
def getNums(num):
    if num > 1:
        return num * getNums(num - 1)
    else:
        return num


print(getNums(5))


# ============================================================
# 匿名函数,可以解决一些简单的计算，复杂的实现不了
# lambda 参数：式子
def test(a, b):
    a + b


result1 = test(11, 22)
print("result1 = %s" % result1)  # result1 = None
fun = lambda a, b: a + b
result2 = fun(11, 22)
print("result2 = %s" % result2)  # result1 = 33

# 匿名函数的操作
num = [11, 22, 33, 123, 1, 2, 3]
num.sort()  # 从小到大排列
print(num)
info = [{"name": "cc", "age": 13}, {"name": "bb", "age": 12}, {"name": "aa", "age": 14}]
print(info)
info.sort(key=lambda x: x["name"])
print(info)
info.sort(key=lambda x: x["age"])
print(info)


# 匿名函数的应用1
def test(a, b, func):
    result = func(a, b)
    print(result)


test(11, 22, lambda x, y: x + y)

# 匿名函数的应用2 python是动态语言
# def test(a, b, func):
#     result = func(a, b)
#     print(result)
#
#
# # 请输入一个匿名函数:lambda x,y:x+y+100     133
# func_new = input("请输入一个匿名函数:")
# func_new = eval(func_new)  # 在python2里没错，但是python3不加这句报错：'str' object is not callable
# test(11, 22, func_new)

# 知识点补充1
# a = 100是不可变类型，a =[100]是可变类型
# a = 100
a = [100]


def test(num):
    num += num
    # print("num = %d" % num)  # num = 200 4，相当于自己进行修改
    print(num)  # [100, 100]


test(a)
# print("a = %d" % a) # a = 100
print(a)  # [100, 100]

# 交换2个变量
a = 4
b = 5
# 交换方式1
c = 0
c = a
a = b
b = c
print(a, b)
# 交换方式2
a = a + b  # 最前面的a可以用别的字母所代替比如c等
b = a - b
a = a - b
print(a, b)
# 方式3
a, b = b, a
print(a, b)

# 知识补充2
print("知识补充2")

# a = 100
a = [100]


def test(num):
    num = num + num  # 理解： num+=num--->num=num+num----->[100]+[100]----->[100,100]
    # c、c++对于这样的计算是一样的，
    # python是+=：直接修改值，xx+xx是开辟一块新内存，所以a不变，输出[100]
    print(num)  # [100, 100]


test(a)
print(a)  # [100]

# 字符串常见操作
print("字符串常见操作")
str = "hello world and hello"
print(str.find("a"))  # 找不到下标是-1
print(str.find("world"))  # 找到下标是6
# print(str.index("a"))  # 找不到程序崩溃：ValueError: substring not found
print(str.index("world"))
# rfind
print("------rfind------")
print(str.rfind("a"))
print(str.rfind("world"))
print(str.rfind("hello"))  # 右边的hello
print(str.rindex("hello"))
# print(str.rindex("ab"))  # 没有结果。。。不输出,但后面代码的不输出
# count
print("count")
print(str.count("hello"))
print(str.count("ab"))  # 0
# replace
print("replace")
print(str.replace("world", "WORLD"))
print(str)  # 仅仅是替换，但是没有改变str的值
print(str.replace("hello", "xxx"))  # xxx world and xxx
print(str.replace("hello", "xxx", 1))  # xxx world and hello
# split
print("split")
print(str.split(" "))  # ['hello', 'world', 'and', 'hello']
# capitalize 把第一个字母变成大写
print("capitalize")
print(str.capitalize())  # Hello world and hello
# title 所有字符首字母大写
print("title")
print(str.title())  # Hello World And Hello
# startswith、endswith 以该字母开头、结尾
print(str.startswith("abc"))  # False
print(str.startswith("h"))  # True
print(str.endswith("o"))  # True
print(str.endswith("p"))  # False

# lower、upper将字符串全变成大写或小写
file_name = "xxx.Txt"
print(file_name.upper())  # XXX.TXT
print(file_name.lower())  # xxx.txt

# ljust: 返回一个原字符串左对齐，并使用空格填充至长度width的新字符串
# rjust: 返回一个原字符串右对齐，并使用空格填充至长度width的新字符串
# center: 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格
lyric = "    想带你一起看大海    "
print(lyric.ljust(50))  # 输出：想带你一起看大海
print(lyric.center(50))  # 输出：                     想带你一起看大海
print(lyric.rjust(50))  # 输出：                                          想带你一起看大海
# lstrip 删除左边的空白字符
# rstrip 删除右边的空白字符
print("strip")
print(lyric.lstrip())
print(lyric.rstrip())
print(lyric.strip())
# partition: 把字符以xx分割成三部分，xx前，xx和xx后
mystr = "aa bb cc dd "
print(mystr.partition("bb"))  # ('aa ', 'bb', ' cc dd ')
print(mystr.rpartition("cc"))  # ('aa bb ', 'cc', ' dd ')
# splitlines：按照行分隔，返回一个包含各行作为元素的列表
str = "hello\nworld"
print(str)
print(str.splitlines())
# isalpha：如果所有字符都是字母，返回true，否则返回false
# isdigit:是否是纯数字，返回true，否则返回false
# isalnum: 所有字符都是字母或数字，返回true，否则返回false
print(str.isalpha())
b = "123"
print(b.isdigit())
c = "123abc"
print(c.isalnum())
# isspace：如果字符串中只包含空格，返回true，否则返回false
print("isspace")
d = ""
print(d.isspace())
d = " "
print(d.isspace())
# join:把每个字符后面插入str，构造出一个新的字符串
str = "_"
li = ["my", "name", "is", "aa"]
print(str.join(li))

# 切割字符
content = "asdas sadasd  dfsf  \t\t\t j sd a lk "
print(content.split())  # ['asdas', 'sadasd', 'dfsf', 'j', 'sd', 'a', 'lk']

# 文件操作流程，打开文件open f = open("text.txt", "w")
# 访问模式：
# r 以只读方式 打开文件，文件的指针将会放在文件的开头，这是默认模式
# w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# rb 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# wb 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# rb+ 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# wb+ 以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab+ 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

# 写入
# print(open("haha.txt", "r")) # FileNotFoundError: [Errno 2] No such file or directory: 'haha.txt'
print("写入文件")
# 有的就可以写，没有就创建文件
f = open("haha.txt", "w")
print(f)
f.write("abcdeftttttttttt")
# print(f.write("aabbcc"))   # 6
# 关闭文件
f.close()

# 读取文件一个个读
print("读取文件")
f = open("haha.txt", "r")
# content = f.read()
# print(content)  # abcdeftttttttttt
print(f.read(1))
print(f.read(2))
print(f.read(1))
f.close()
