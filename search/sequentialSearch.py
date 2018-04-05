#! venv/bin/python
#_*_ encoding:utf-8 _*_
"""
@Python -V: 3.X
@SoftWave: Pycharm
@OS: Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.4.5
"""

def sequentialSearch(alist, key):

    for i in range(len(alist)):
        if key == alist[i]:
            return i

    return False

if __name__ == '__main__':
    alist = [25,26,36,98,69,67,89,554,86,9,5,4,2,3,6]

    result = sequentialSearch(alist, 36)

    print(result)