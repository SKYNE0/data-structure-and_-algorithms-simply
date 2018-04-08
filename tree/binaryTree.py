#! venv/bin/python
#_*_ encoding:utf-8 _*_
"""
@Python -V: 3.X
@SoftWave: Pycharm
@OS: Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.4.6
"""

class binaryTree():

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftchild = None
        self.rightchild = None


    def insertLeft(self, newNode):
        if self.leftchild == None:
            self.leftchild = binaryTree(newNode)
        else:
            tree = binaryTree(newNode)
            tree.leftchild = self.leftchild
            self.leftchild = tree

    def insertRight(self, newNode):
        if self.rightchild == None:
            self.rightchild = binaryTree(newNode)
        else:
            tree = binaryTree(newNode)
            tree.rightchild = self.rightchild
            self.rightchild = tree

    def getLeftChild(self):
        return self.leftchild

    def getRightChild(self):
        return self.rightchild

    def setRootVal(self, obj):
            self.key = obj

    def getRootVal(self):
        return self.key


if __name__ == '__main__':
    r = binaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())