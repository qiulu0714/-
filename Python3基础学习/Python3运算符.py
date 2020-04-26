# 什么是运算符？
# 本章节主要说明Python的运算符。举个简单的例子 4 +5 = 9 。 例子中，4 和 5 被称为操作数，"+" 称为运算符。
# Python语言支持以下类型的运算符:
# 算术运算符
# 比较（关系）运算符
# 赋值运算符
# 逻辑运算符
# 位运算符
# 成员运算符
# 身份运算符
# 运算符优先级
# -----------------------Python算术运算符--------------------------------

# 以下假设变量a为10，变量b为21：
# +	        加 - 两个对象相加	                                a + b 输出结果 31

# -	        减 - 得到负数或是一个数减去另一个数	                a - b 输出结果 -11

# *	        乘 - 两个数相乘或是返回一个被重复若干次的字符串	    a * b 输出结果 210

# /	        除 - x 除以 y	                                    b / a 输出结果 2.1

# %     	取模 - 返回除法的余数	                            b % a 输出结果 1

# **	    幂 - 返回x的y次幂	                                a**b 为10的21次方

# //	    取整除 - 向下取接近商的整数                         9//2=4      -9//2 =-5
# 以下实例演示了Python所有算术运算符的操作：
a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b
print("5 - c 的值为：", c)

c = a // b
print("6 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("7 - c 的值为：", c)

a = 10
b = 5
c = a // b
print("8 - c 的值为：", c)
print('\n-------------------------------------------------------\n')
# -----------------------------Python比较运算符-----------------------------------------

# 以下假设变量a为10，变量b为20：
# ==	        等于 - 比较对象是否相等	                (a == b) 返回 False。
# !=	        不等于 - 比较两个对象是否不相等	        (a != b) 返回 True。
# >	            大于 - 返回x是否大于y	                (a > b) 返回 False。
# <	            小于 - 返回x是否小于y。	                (a < b) 返回 True。
# >=	        大于等于 - 返回x是否大于等于y。	        (a >= b) 返回 False。
# <=	        小于等于 - 返回x是否小于等于y。	        (a <= b) 返回 True。
# 注意:
# 所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。

# 以下实例演示了Python所有比较运算符的操作：
a = 21
b = 10

if (a == b):
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if (a != b):
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if (a < b):
    print("3 - a 小于 b")
else:
    print("3 - a 大于等于 b")

if (a > b):
    print("4 - a 大于 b")
else:
    print("4 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5;
b = 20;
if (a <= b):
    print("5 - a 小于等于 b")
else:
    print("5 - a 大于  b")

if (b >= a):
    print("6 - b 大于等于 a")
else:
    print("6 - b 小于 a")
print('\n-------------------------------------------------------\n')
# ----------------------------Python赋值运算符-----------------------------

# 以下假设变量a为10，变量b为20：
# =	            简单的赋值运算符	            c = a + b 将 a + b 的运算结果赋值为 c
# +=	        加法赋值运算符	                c += a 等效于 c = c + a
# -=	        减法赋值运算符	                c -= a 等效于 c = c - a
# *=	        乘法赋值运算符	                c *= a 等效于 c = c * a
# /=	        除法赋值运算符	                c /= a 等效于 c = c / a
# %=	        取模赋值运算符	                c %= a 等效于 c = c % a
# **=	        幂赋值运算符	                c **= a 等效于 c = c ** a
# //=	        取整除赋值运算符	            c //= a 等效于 c = c // a
# :=	        海象运算符，可在表达式内部为变量赋值。Python3.8 版本新增运算符。
# 在这个示例中，赋值表达式可以避免调用 len() 两次:
# if (n := len(a)) > 10:
#     print(f"List is too long ({n} elements, expected <= 10)")

# 以下实例演示了Python所有赋值运算符的操作：
a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c += a
print("2 - c 的值为：", c)

c *= a
print("3 - c 的值为：", c)

c /= a
print("4 - c 的值为：", c)

c = 2
c %= a
print("5 - c 的值为：", c)

c **= a
print("6 - c 的值为：", c)

c //= a
print("7 - c 的值为：", c)
print('\n-------------------------------------------------------\n')
# -------------------------------------Python位运算符---------------------------------

# 按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：
# 下表中变量 a 为 60，b 为 13二进制格式如下：
# &	            按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	                            (a & b) 输出结果 12 ，二进制解释： 0000 1100
# |         	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	                                        (a | b) 输出结果 61 ，二进制解释： 0011 1101
# ^         	按位异或运算符：当两对应的二进位相异时，结果为1	                                                        (a ^ b) 输出结果 49 ，二进制解释： 0011 0001
# ~	            按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1	                        (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
# <<	        左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	        a << 2 输出结果 240 ，二进制解释： 1111 0000
# >>	        右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数	                a >> 2 输出结果 15 ，二进制解释： 0000 1111

a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0
c = a & b;  # 12 = 0000 1100
print("1 - c 的值为：", c)

c = a | b;  # 61 = 0011 1101
print("2 - c 的值为：", c)

c = a ^ b;  # 49 = 0011 0001
print("3 - c 的值为：", c)

c = ~a;  # -61 = 1100 0011
print("4 - c 的值为：", c)

c = a << 2;  # 240 = 1111 0000
print("5 - c 的值为：", c)

c = a >> 2;  # 15 = 0000 1111
print("6 - c 的值为：", c)
print('\n-------------------------------------------------------\n')
# ------------------------------Python逻辑运算符----------------------------------------------------

''' and	            可以对符号两侧的值进行'与'运算只有在符号两侧的值都为True时，才会返回True，只要有一个False就返回False
                    '与'运算是找False的，如果第一个值为False，则不再看第二个值'''

# AND_布尔           符号两侧的值为 True 和 False（boolean布尔值）  结果只有 True 和 False,
#                    当两侧都为 True 时， 结果才为 True 。其它结果为 False 。
logic_bool = True and True
print(logic_bool)

logic_bool = True and False
print(logic_bool)

logic_bool = False and True
print(logic_bool)

logic_bool = False and False
print(logic_bool)
print('\n-------------------------------------------------------\n')

# AND_数字          符号两侧的值为 数字    结果为 右侧值 或 0
#                   当两侧值全非0时，结果取符号右侧值；
#                   当两侧至少有一个值为0时， 结果 为 0 。
logic_figure = 3 and 5
print(logic_figure)

logic_figure = 0 and 5
print(logic_figure)

logic_figure = 3 and 0
print(logic_figure)

logic_figure = 0 and 0
print(logic_figure)
print('\n-------------------------------------------------------\n')

# AND_string        符号两侧的值为 字符串， 结果为 右侧值 或 （输出）空行
#                   当两侧值为非空字符串时， 结果取符号右侧值；
#                   当两侧至少有一个值为空字符串时，结果 为（输出）空行
logic_str = '汉字' and '成语'
print('---------'+logic_str+'---------')

logic_str = '' and '成语'
print('---------'+logic_str+'---------')

logic_str = '汉字' and ''
print('---------'+logic_str+'---------')

logic_str = '' and ''
print('---------'+logic_str+'---------')
print('\n-------------------------------------------------------\n')

''' or	            可以对符号两侧的值进行'或'运算或运算两个值中只要有一个True，就会返回True
                    '或'运算是找True的,如果第一个值为True，则不再看第二个值'''

# OR_布尔           符号两侧的值为 True 和 False（boolean布尔值）  结果只有 True 和 False
#                   当两侧值都为False ， 结果才为 False 。
logic_bool = True or True
print(logic_bool)

logic_bool = True or False
print(logic_bool)

logic_bool = False or True
print(logic_bool)

logic_bool = False or False
print(logic_bool)
print('\n-------------------------------------------------------\n')

# OR_数字           符号两侧的值为 数字    结果为 数字 或 0
#                   当两侧非0， 结果取左侧值；
#                   当其中一值为 0 ，另一值为 非0， 结果取非0值；
#                   当两侧为0， 结果为 0
logic_figure = 3 or 5
print(logic_figure)

logic_figure = 0 or 5
print(logic_figure)

logic_figure = 3 or 0
print(logic_figure)

logic_figure = 0 or 0
print(logic_figure)
print('\n-------------------------------------------------------\n')

# OR_string         符号两侧的值为 字符串， 结果为 字符串 或 （输出）空行
#                   当两侧非空， 结果取左侧值；
#                   当其中一值为 空 ，另一值为 非空， 结果取非空值；
#                   当两侧为空， 结果为 输出空行 。
logic_str = '汉字' or '成语'
print('---------'+logic_str+'---------')

logic_str = '' or '成语'
print('---------'+logic_str+'---------')

logic_str = '汉字' or ''
print('---------'+logic_str+'---------')

logic_str = '' or ''
print('---------'+logic_str+'---------')
print('\n-------------------------------------------------------\n')

# OR              符号两侧的值为数字与boolean ，结果为 数字，Boolean值。 非0 ， 0 ， True，False。
#                 当两侧非0或非False， 结果取左侧值；
#                 当两侧一值非0或非False,另一值为0或False, 结果取非0或True。
#                 当两侧为 0，False, 结果为 右侧值
logic = True or 2
print(logic)

logic = 5 or True
print(logic)

logic = 0 or True
print(logic)

logic = True or 0
print(logic)

logic = 3 or False
print(logic)

logic = False or 2
print(logic)

logic = 0 or False
print(logic)

logic = False or 0
print(logic)
print('\n-------------------------------------------------------\n')

''' not	            可以对符号右侧的值进行'非'运算
                    对于布尔值，非运算会对其进行取反操作，True变False，False变True
                    对于非布尔值，非运算会先将其转换为布尔值，然后再取反。
                    字符串，有内容为True,空字符串为False.
# 　　              数字，0 为 False ,其它 为 True .'''

# -------------------------------Python成员运算符---------------------------------------------
# 除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
# in	               如果在指定的序列中找到值返回 True，否则返回 False。	         x 在 y 序列中 , 如果 x 在 y 序列中返回 True
# not in	           如果在指定的序列中没有找到值返回 True，否则返回 False。	     x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True.

a = 10
b = 2
list = [1, 2, 3, 4, 5];

if (a in list):
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if (a not in list):
    print("2 - 变量 a 不在给定的列表中 list 中")
else:
    print("2 - 变量 a 在给定的列表中 list 中")

if (b in list):
    print("3 - 变量 b 在给定的列表中 list 中")
else:
    print("3 - 变量 b 不在给定的列表中 list 中")

if (b not in list):
    print("3 - 变量 b 不在给定的列表中 list 中")
else:
    print("3 - 变量 b 在给定的列表中 list 中")
print('\n-------------------------------------------------------\n')

# --------------------------------Python身份运算符-----------------------------
# 身份运算符用于比较两个对象的存储单元
# is	            is 是判断两个标识符是不是引用自一个对象               	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
# is not	        is not 是判断两个标识符是不是引用自不同对象	            x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
a = 20
b = 20

if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if (id(a) == id(b)):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")
print('\n-------------------------------------------------------\n')

# 修改变量 b 的值
b = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")

# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
print('\n-------------------------------------------------------\n')

# ----------------------Python运算符优先级-------------------------------
# 以下表格列出了从最高到最低优先级的所有运算符：
# **	                        指数 (最高优先级)
# ~ + -	                        按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
# * / % //	                    乘，除，求余数和取整除
# + -	                        加法减法
# >> <<	                        右移，左移运算符
# &         	                位 'AND'
# ^ |	                        位运算符
# <= < > >=	                    比较运算符
# == !=	                        等于运算符
# = %= /= //= -= += *= **=	    赋值运算符
# is is not	                    身份运算符
# in not in	                    成员运算符
# not and or	                逻辑运算符
a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("(a + b) * c / d 运算结果为：", e)

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：", e)

e = (a + b) * (c / d);  # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：", e)

e = a + (b * c) / d;  # 20 + (150/5)
print("a + (b * c) / d 运算结果为：", e)
print('\n-------------------------------------------------------\n')

# and 拥有更高优先级:
x = True
y = False
z = False

if x or y and z:
    print("yes")
else:
    print("no")

# 注意：Pyhton3 已不支持 <> 运算符，可以使用 != 代替，如果你一定要使用这种比较运算符，可以使用以下的方式：
# >>> from __future__ import barry_as_FLUFL
# >>> 1 <> 2
# True