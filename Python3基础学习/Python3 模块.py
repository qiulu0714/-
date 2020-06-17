# 在前面的几个章节中我们脚本上是用 python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。
# 为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
# 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
# 下面是一个使用 python 标准库中模块的例子。
import sys
print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')

#   1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
#   2、sys.argv 是一个包含命令行参数的列表。
#   3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。

# ---------------------import 语句
# 想使用Python源文件，只需在另一个源文件里执行import 语句，语法如下：
# import module1[, module2[, ... moduleN]
#
# 当解释器遇到import 语句，如果模块在当前的搜索路径就会被导入。
# 搜索路径是一个解释器会先进行搜索的所有目录的列表。如想要导入模块support，需要把命令放在脚本的顶端：
# support.py文件代码

def print_func(par):
    print("Hello : ", par)
    return

# test.py引入support模块：
# test.py文件代码
# 导入模块
# import support

# 现在可以调用模块里包含的函数了
# support.print_func("Runoob")

# 一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。
# 当我们使用import语句的时候，Python解释器是怎样找到对应的文件的呢？
# 这就涉及到Python的搜索路径，搜索路径是由一系列目录名组成的，Python解释器就依次从这些目录中去寻找所引入的模块。
# 这看起来很像环境变量，事实上，也可以通过定义环境变量的方式来确定搜索路径。
# 搜索路径是在Python编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在sys模块中的path变量，做一个简单的实验，
# 在交互式解释器中，输入以下代码：
import sys
print(sys.path)

# sys.path 输出是一个列表，其中第一项是空串''，代表当前目录（若是从一个脚本中打印出来的话，可以更清楚地看出是哪个目录），
# 亦即我们执行python解释器的目录（对于脚本的话就是运行的脚本所在的目录）。
# 因此若像我一样在当前目录下存在与要引入模块同名的文件，就会把要引入的模块屏蔽掉。
# 了解了搜索路径的概念，就可以在脚本中修改sys.path来引入一些不在搜索路径中的模块。
# 现在，在解释器的当前目录或者 sys.path 中的一个目录里面来创建一个fibo.py的文件，代码如下：
def fib(n):  # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


# 然后进入Python解释器，使用下面的命令导入这个模块：
# import fibo

# 这样做并没有把直接定义在fibo中的函数名称写入到当前符号表里，只是把模块fibo的名字写到了那里。
# 可以使用模块名称来访问函数：