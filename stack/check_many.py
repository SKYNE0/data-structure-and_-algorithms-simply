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

# 简单应用，匹配多个括号是否成对
def checker(symbolString):
    s = stack()

    balanced = True

    index = 0

    while index < len(symbolString) and balanced:

        symbol = symbolString[index]

        if symbol in "([{":
            s.push(symbol)

        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closes = ")]}"

    return opens.index(open) == closes.index(close)

if __name__ == '__main__':

    print(checker('([{}])'))
    print(checker('(((]}'))