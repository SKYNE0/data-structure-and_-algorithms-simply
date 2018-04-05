#! venv/bin/python
#_*_ encoding:utf-8 _*_
"""
@Python -V: 3.X
@SoftWave: Pycharm
@OS: Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.4.4
"""
def insertionSort(alist):

    for index in range(1, len(alist)):

        currentvalue = alist[index]

        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = currentvalue

    return alist

if __name__ == '__main__':
    from random import randint

    alist = []

    for i in range(100):
        alist.append(randint(1, 9999))

    print("The old array is {}".format(alist))

    result = insertionSort(alist)

    print("The new array is {}".format(result))