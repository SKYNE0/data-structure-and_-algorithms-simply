#! venv/bin/python
#_*_ encoding:utf-8 _*_
"""
@Python -V: 3.X
@SoftWave: Pycharm
@OS: Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.4.3
"""

class deque():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    deque = deque()
    deque.addRear(4)
    deque.addRear('dog')
    deque.addFront('cat')
    deque.addFront('fish')
    print(deque.size())
    print(deque.isEmpty())
    print(deque.removeFront())
    print(deque.removeRear())

