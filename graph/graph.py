#! venv/bin/python
#_*_ encoding:utf-8 _*_
"""
@Python -V: 3.X
@SoftWave: Pycharm
@OS: Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.4.7
"""

# 图的顶点
class Vertex():

    def __init__(self, key):
        self.id = key
        self.connentTo = {}

    def addNeighbor(self, nbr, weight = 0):
        self.connentTo[nbr] = weight

    def __str__(self):
        return str(self.id) + "connentTo:" + str([x.id for x in self.connentTo])

    def getConnentions(self):
        return self.connentTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connentTo[nbr]

class Graph():

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

        return newVertex

    def getVerex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, fristin, tlink, cost = 0):
        if fristin not in self.vertList:
            newVertex = self.addVertex(fristin)

        if tlink not in self.vertList:
            newVertex = self.addVertex(tlink)

        self.vertList[fristin].addNeighbor(self.vertList[tlink], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


