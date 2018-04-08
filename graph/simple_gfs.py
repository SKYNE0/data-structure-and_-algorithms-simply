#! venv/bin/python
#_*_ encoding:utf-8 _*_
"""
@Python -V: 3.X
@SoftWave: Pycharm
@OS: Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.3.31
"""

from collections import deque

class simple_bfs():

    def __init__(self, graph, start_name, search_name):
        self.search_queue = deque()
        self.graph = graph
        self.search_name = search_name
        self.start_name = start_name

    def search(self, name):
        if name == self.search_name:
            return True
        else:
            return False

    def bfs(self):
        self.search_queue += self.graph[self.start_name]
        searched = []
        while(self.search_queue):
            name = self.search_queue.popleft()
            if not name in searched:
                if self.search(name):
                    print("Name be find!{}".format(name))
                    return True
                else:
                    self.search_queue += self.graph[name]
                    searched.append(name)

        return False


if __name__ == '__main__':
    names = ['skyne','mask','apple','coco','nike','pepsi','vivo','oppo',]
    friends = [['mask', 'coco','vivo'],['skyne','coco','pepsi','apple'],['skyne', 'mask', 'oppo'],[],[],[],[],[]]
    graph = dict(zip(names, friends))
    print(graph)
    bfs = simple_bfs(graph, 'skyne', 'oppo')
    print(bfs.bfs())