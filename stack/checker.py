#! venv/bin/python
#_*_ encoding:utf-8 _*_
"""
@Python -V: 3.X
@SoftWave: Pycharm
@OS: Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.4.1
"""

from stack import stack

# 简单应用，匹配括号是否成对
def checker(symbolString):
    s = stack()

    balanced = True

    index = 0

    while index < len(symbolString) and balanced:

        symbol = symbolString[index]

        if symbol == "(":
            s.push(symbol)

        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':

    print(checker('((()))'))    #True
    print(checker('((()'))      #False