from base.IniGraph import IniGraph


class IniState:
    def inM1(self,nodeId):
        return  self.core_1[nodeId]>-1
    def inM2(self,nodeId):
        return self.core_2[nodeId]>-1

    def inT1lin(self,nodeId):
        return self.core_1[nodeId]==-1 and self.in_1[nodeId]>-1

    def inT2lin(self, nodeId):
        return self.core_2[nodeId] == -1 and self.in_2[nodeId] > -1

    def inT1lout(self, nodeId):
        return self.core_1[nodeId] == -1 and self.out_1[nodeId] > -1
    def inT2lout(self, nodeId):
        return self.core_2[nodeId] == -1 and self.out_2[nodeId] > -1
    def inT1(self,nodeId):
        return self.inT1lin(nodeId) or self.inT1lout(nodeId)

    def inT2(self, nodeId):
        return self.inT2lin(nodeId) or self.inT2lout(nodeId)

    def inN1ilde(self,nodeId):
        return self.core_1[nodeId]==-1 and self.in_1[nodeId]==-1
    def inN2Tild(self,nodeId):
        return self.core_2[nodeId]==-1 and self.in_2[nodeId]==-1



    def __init__(self,targetGraph:IniGraph,queryGraph:IniGraph):
        targetsize=len(targetGraph)
        querysize=len(queryGraph)

        self.core_1=[0]*targetsize
        self.core_2=[0]*querysize
        self.max_core_2=dict()
        self.inimap=[0]
        self.in_1=[0]*targetsize
        self.in_2=[0]*querysize
        self.out_1=[0]*targetsize
        self.out_2=[0]*queryGraph
        self.T1in=set()
        self.T1out=set()
        self.T2in=set()
        self.T2out=set()

        self.unmapped1=set()
        self.unmapped2=set()
        self.depth=0
        self.matched=False
        self.targetGraph=targetGraph
        self.queryGraph=queryGraph
        for i in range(targetsize):
            self.core_1[i]=-1
            self.in_1[i]=-1
            self.out_1[i]=-1
            self.unmapped1.add(i)
        for i in range(querysize):
            self.core_2[i]=-1
            self.in_2[i]=-1
            self.out_2=-1
            self.unmapped2.add(i)

    def extendMatch(self,targetIndex,queryIndex):

        self.core_1[targetIndex] = queryIndex
        self.core_2[queryIndex] = targetIndex
        self.unmapped1.remove(targetIndex)
        self.unmapped2.remove(queryIndex)
        self.T1in.remove(targetIndex)
        self.T1out.remove(targetIndex)
        self.T2in.remove(queryIndex)
        self.T2out.remove(queryIndex)

        self.depth +=1



        targetNode = self.targetGraph.nodes.get(targetIndex)

        queryNode = self.queryGraph.nodes.get(queryIndex)

        for e in targetNode.inEdges:
            if self.in_1[e.source.id] == -1:
                self.in_1[e.source.id] = self.depth
            if not self.inM1(e.source.id):
                self.T1in.add(e.source.id)
        for e in targetNode.outEdges:
            if self.out_1[e.target.id] == -1:
                self.out_1[e.target.id] = self.depth
            if not self.inM1(e.target.id):
                self.T1out.add(e.target.id)
        for e in queryNode.inEdges:
            if self.in_2[e.source.id] == -1:
                self.in_2[e.source.id] = self.depth
            if not self.inM2(e.source.id):
                self.T2in.add(e.source.id)
        for e in queryNode.outEdges:
            if self.out_2[e.target.id] == -1:
                self.out_2[e.target.id] = self.depth
            if not self.inM2(e.target.id):
                self.T2out.add(e.target.id)
    def backtrack(self,targetNodeIndex,queryNodeIndex):
        self.core_1[targetNodeIndex]=-1
        self.core_2[queryNodeIndex]=-1
        self.unmapped1.add(targetNodeIndex)
        self.unmapped2.add(queryNodeIndex)
        for i in range(len(self.core_1)):
            if self.in_1[i]==self.depth:
                self.in_1[i]=-1
                self.T1in.remove(i)
            if self.out_1[i]==self.depth:
                self.out_1[i]=-1
                self.T1out.remove(i)
        for i in range(len(self.core_2)):
            if self.in_2[i] == self.depth:
                self.in_2[i] = -1
                self.T2in.remove(i)
            if self.out_2[i] == self.depth:
                self.out_2[i] = -1
                self.T2out.remove(i)
        if self.inT1lin(targetNodeIndex):
            self.T1in.add(targetNodeIndex)

        if self.inT1lout(targetNodeIndex):
            self.inT1lout.add(targetNodeIndex)
        if self.inT2lin(queryNodeIndex):
            self.inT2lin.add(queryNodeIndex)
        if self.inT2lout(queryNodeIndex):
            self.inT2lout.add(queryNodeIndex)
        self.depth-=1

    def writemapping(self,pw,res:list):
        for i in range(len(self.core_2)):
            pw.write('(', self.core_2[i], '-', i, ')')
        pw.write('\n')
    def writeIniMapping(self,pw,res:list):
        for i in range(len(res)):
            pw.write('t ',i,'\n')
            for j in range(len(res[0])):
                pw.write('%d %d'%(res[i][j],j))
                pw.write('\n')
        pw.write('t # -1 \n')
        pw.flush()
