#! venv/bin/python
#_*_ encoding:utf-8 _*_
"""
@Python -V: 3.X
@SoftWave: Pycharm
@OS: Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 20184.
"""

def shellSort(alist):
    sublistconut = len(alist) // 2

    while sublistconut > 0:
        for startposition in range(sublistconut):
            gapInsertionSort(alist,startposition,sublistconut)

        sublistconut = sublistconut // 2


    return alist


def gapInsertionSort(alist,start,gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position= position -gap

        alist[position] = currentvalue

if __name__ == '__main__':
    from random import randint

    alist = []

    for i in range(100):
        alist.append(randint(1, 9999))

    print("The old array is {}".format(alist))

    result = shellSort(alist)

    print("The new array is {}".format(result))
