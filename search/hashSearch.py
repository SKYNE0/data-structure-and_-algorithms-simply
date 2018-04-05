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

# 散列函数有很多：数字分析法，平方取中法，分段叠加法，除留余数法，伪随机数，这里使用除留余数法
class hashSearch():

     def __init__(self, alist):
         self.elem = [None for i in range(len(alist))]
         self.count = len(alist)

     def hash(self, key):
         return key % self.count

     def insertHash(self, key):
         address = self.hash(key)

         while self.elem[address]:
             address = (address + 1) % self.count

         self.elem[address] = key

     def searchHash(self, key):
         start = address = self.hash(key)

         while self.elem[address] != key:
             address = (address + 1) % self.count

             if not self.elem[address] or address == start:
                 return False

         return self.elem[address]


if __name__ == '__main__':
    alist = [23,63,9,8,44,56,87,89,54,656]
    hashSearch = hashSearch(alist)

    for i in alist:
        hashSearch.insertHash(i)

    for i in hashSearch.elem:
        if i:
            print((i, hashSearch.elem.index(i)), end=" ")
    print("\n")

    print(hashSearch.searchHash(63))
    print(hashSearch.searchHash(54))