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
时间复杂度:O(n2)
1,创建函数findsmallest()，遍历数组，找到最小值，返回最小值索引
2,在selection_sort()中，不断找出最小值，并删除最小值，并使用新数组存储删除的最小值。
"""


def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selection_sort(arr):
    new_arr = []

    for i in range(len(arr)):
        smallest = findsmallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr


if __name__ == '__main__':

    from random import randint

    arr = []

    for i in range(100):
        arr.append(randint(1, 9999))

    print("The old array is {}".format(arr))

    result = selection_sort(arr)

    print("The new array is {}".format(result))

