#! venv/bin/python
#_*_ encoding:utf-8 _*_
"""
@Python -V: 3.X
@SoftWave: Pycharm
@OS: Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.3.30
"""

"""
这个快速排序，虽然懂了他的原理，但没法说出来，涉及到递归的概念,有点难以阐述。
"""

def quick_sort(array):

    if len(array) < 2:
        return array

    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)



if __name__ == '__main__':

    from random import randint

    arr = []

    for i in range(100):
        arr.append(randint(1, 9999))

    print("The old array is {}".format(arr))

    result = quick_sort(arr)

    print("The new array is {}".format(result))


