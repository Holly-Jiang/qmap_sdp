
from base.IniNode import IniNode


class IniEdge:
    def __init__(self, g, source: IniNode, tartget: IniNode, label: int):
        self.graph = g
        self.source = source
        self.target = tartget
        self.outEdges = []
        self.inEdges = []
        self.inEdges.append(self)
        self.outEdges.append(self)
        self.label = label
