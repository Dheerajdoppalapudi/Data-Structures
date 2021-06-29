class Graph:
    def __init__(self, src, dest, wgt):
        self.src = src
        self.dest = dest
        self.wgt = wgt

    def __lt__(self, other):
        return self.wgt < other.wgt

class Kruskals:
    def __init__(self, vert):
        self.vert = vert

    def sort(self, list):
        list.sort(reverse=False)

    def findparent(self, parent, identity):
        if parent[identity] == -1:
            return identity
        if parent[identity] != -1:
            return self.findparent(parent, parent[identity])

    def union(self, parent, x, y):
        parent[x] = y

    def circularloop(self, list):
        parent = [-1] * (self.vert)
        # print(parent)
        for i in list:
            x = self.findparent(parent, i.src)
            y = self.findparent(parent, i.dest)
            if x == y:
                continue
            else:
                self.union(parent, x, y)
                Mst.append(i)

list = []
Mst = []

def addedge(src, dest, wgt):
    list.append(Graph(src, dest, wgt))


addedge(0, 1, 8)
addedge(0, 2, 5)
addedge(1, 2, 9)
addedge(1, 3, 11)
addedge(2, 3, 15)
addedge(2, 4, 10)
addedge(3, 4, 7)
G = Kruskals(5)
G.sort(list)
G.circularloop(list)
for i in Mst:
    print("Edge {}-->{} and weight is {} ".format(i.src, i.dest, i.wgt))

    # sort all the (edges, vertices) in increasing order of weight
    # pic the least edge and add to the weight
    # check if the newly added edge creates a cycle or not
    # if it creates a cycle discard it and choose the next least edge and repeat step 2 and 3
