#! venv/bin/python
#_*_ encoding:utf-8 _*_
"""
@Python -V: 3.X
@SoftWave: Pycharm
@OS: Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.4.2
"""
from stack import stack

#  任意十进制整数转化为不大于16进制的进制整数
def baseConverter(decNumber, base):
    s = stack()
    digits = "0123456789ABCDEF"

    while decNumber > 0:
        rem = decNumber % base
        s.push(rem)
        decNumber = decNumber // base

    newSting = ""
    while not s.isEmpty():
        newSting = newSting + digits[s.pop()]

    return newSting

if __name__ == '__main__':
    print(baseConverter(12, 16))  #C
    print(baseConverter(99, 6))   #243

