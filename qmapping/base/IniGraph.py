from base.IniEdge import IniEdge
from base.IniNode import IniNode


class IniGraph:
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.edges = []
        self.adjacencyMatrix = None
        self.adjacencyMatrixUpdateNeeded = True

    def addNode(self, id, label):
        self.nodes.append(IniNode(self, id, label))
        self.adjacencyMatrixUpdateNeeded = True

    def addEdge(self, source: IniNode, target: IniNode, label):
        self.edges.append(IniEdge(self, source, target, label))
        self.adjacencyMatrixUpdateNeeded = True

    def addEdgeById(self, sourceId: int, targetId: int, label: int):
        self.addEdge(self.nodes[sourceId], self.nodes[targetId], label)

    def getAdjacencyMatrix(self):
        if self.adjacencyMatrixUpdateNeeded:
            k = len(self.nodes)
            self.adjacencyMatrix = [[-1] * k for i in range(k)]
            for e in self.edges:
                self.adjacencyMatrix[e.source.id][e.target.id]=e.label
            self.adjacencyMatrixUpdateNeeded = False
        return self.adjacencyMatrix
