#! venv/bin/python
#_*_ encoding:utf-8 _*_
"""
@Python -V: 3.X
@SoftWave: Pycharm
@OS: Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.4.3
"""
from deque import deque

# 检测字符串是否是回文
def palChecker(aString):
    d = deque()

    for i in aString:
        d.addRear(i)

    stillEqual = True

    while not d.isEmpty() and stillEqual:
        first = d.removeFront()
        last = d.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

if __name__ == '__main__':
    print(palChecker('sadsdfsdfsdfsdf '))
    print(palChecker('dood'))
