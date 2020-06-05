# Python 条件语句是通过一条或多条语句的执行结果（True 或者 False）来决定执行的代码块。
# 可以通过下图来简单了解条件语句的执行过程:
# https://www.runoob.com/wp-content/uploads/2013/11/if-condition.jpg

# 代码执行过程：
# https://static.runoob.com/images/mix/python-if.webp

# if 语句
# Python中if语句的一般形式如下所示：
# if condition_1:
#     statement_block_1
# elif condition_2:
#     statement_block_2
# else:
#     statement_block_3
# 如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
# 如果 "condition_1" 为False，将判断 "condition_2"
# 如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
# 如果 "condition_2" 为False，将执行"statement_block_3"块语句
# Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。
#
# 注意：
#
# 1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
# 2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
# 3、在Python中没有switch – case语句。
# Gif演示:
# https://www.runoob.com/wp-content/uploads/2014/05/006faQNTgw1f5wnm0mcxrg30ci07o47l.gif
var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
print("Good bye!")
# 从结果可以看到由于变量 var2 为 0，所以对应的 if 内的语句没有执行。

# 以下实例演示了狗的年龄计算判断：

age = 2
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")