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

# 二分查找的前提是已排序的列表

def binarySearch(alist, key):
    low = 0
    high = len(alist) - 1
    time = 0

    while high > low:
        time += 1
        mid = (low + high) // 2

        if key > alist[mid]:
            low = mid -1
        elif key < alist[mid]:
            high = mid + 1
        else:
            print("{} times".format(time))
            return mid

    print("{} times".format(time))
    return False

if __name__ == '__main__':
    alist = [x for x in range(100)]

    result = binarySearch(alist, 50)

    print(result)