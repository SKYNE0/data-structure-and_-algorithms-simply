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

def bubbleSort(arr):
    bubble = [0] * (max(arr) - min(arr) + 1)

    for i in range(len(arr)):
        bubble[arr[i] - min(arr)] += 1

    result = []

    for i in range(len(bubble)):
        if bubble[i] != 0:
            result += [i + min(arr)] * bubble[i]

    return result

if __name__ == '__main__':

    from random import randint

    arr = []

    for i in range(10):
        arr.append(randint(1, 9999))

    print("The old array is {}".format(arr))

    result = bubbleSort(arr)

    print("The new array is {}".format(result))

