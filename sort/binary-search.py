#! venv/bin/python
#_*_ encoding:utf-8 _*_
"""
@Python -V: 3.X
@SoftWave: Pycharm
@OS: Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.3.29
"""

"""
时间复杂度:O(logN)
前提：必须是有序的序列
1, 取数组中间值与寻找值对比，
2, 小于寻找值，则在小于部分，取中间值与寻找值对比，反之则反
3,重复1,2,直到找到寻找值，或者找不到
"""

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low < high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid

        elif guess > item:
            high = mid - 1

        else:
            low = mid + 1

    return None



if __name__ == '__main__':
    list = [x for x in range(0,999999)]

    item = 69

    result = binary_search(list, item)

    print("Item in the list th {}".format(result))