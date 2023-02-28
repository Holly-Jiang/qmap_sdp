class IniNode:
    def __init__(self,g,id,label):
        self.graph=g
        self.id=id
        self.label=label
        self.outEdges=[]
        self.inEdges=[]
