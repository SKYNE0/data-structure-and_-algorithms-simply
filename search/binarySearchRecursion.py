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

# 利用递归代替while循环

def binarySearchRecursion(alist, key):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2

        if key == alist[mid]:
            return alist[mid]
        else:
            if key > alist[mid]:
                return binarySearchRecursion(alist[mid + 1:], key)
            else:
                return binarySearchRecursion(alist[:mid], key)


if __name__ == '__main__':
    alist = [x for x in range(100)]

    result = binarySearchRecursion(alist, 90)

    print(result)