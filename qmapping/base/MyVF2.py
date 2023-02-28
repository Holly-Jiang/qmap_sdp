from queue import Queue

from base.IniGraph import IniGraph


def connectAllocateRemaining(querygraph, targetgraph, mappingresult, mapping,system:str):
    max_core = []
    max_count = 0
    for key, value in mappingresult.items():
        if max_count < value:
            max_count = value
    for key, value in mappingresult.items():
        if max_count == value:
            mapkey = mapping[int(key)]
            queue = Queue()
            for i in range(len(mapkey)):
                if mapkey[i] == 99999:
                    queue.put(i)
            while not queue.empty():
                queryId = queue.get()

                targetAdj = targetgraph.getAdjacencyMatrix()
                queryAdj = querygraph.getAdjacencyMatrix()

                flag = False
                treemap = dict()  # treemap 按照key降序排序  key是queryGraph中与queryId相连的边 key是连接次数最多的节点
                for m in range(len(queryAdj[queryId])):
                    if mapkey[m] != 99999:
                        content = '%s-%s' % (chr(queryAdj[queryId][m]+98), chr(mapkey[m]+97))
                        # content = '%s-%s' % (queryAdj[queryId][m], mapkey[m])
                        treemap.update({content: m})
                while len(treemap) > 0:
                    keys = list(treemap.keys())
                    keys = sorted(keys, reverse=True)
                    targetNode = mapkey[treemap.get(keys[0])]
                    treemap.pop(keys[0])
                    k = 0
                    for k in range(len(targetAdj[targetNode])):
                        if ((targetAdj[targetNode][k] != -1 or targetAdj[k][targetNode] != -1)) and not (k in mapkey):
                            mapkey[queryId] = k
                            break

                    if k != len(targetAdj[targetNode]) - 1:
                        break
            max_core.append(mapkey)

    return max_core


def degreeAllocateRemaining(querygraph, targetgraph, mappingresult, mapping:list,system:str):
    max_core = []
    max_count = 0
    for key1, value1 in mappingresult.items():
        if max_count < value1:
            max_count = value1
    for key, value in mappingresult.items():
        if max_count == value:
            mapkey = mapping[int(key)]
            queue = []
            for i in range(len(mapkey)):
                if mapkey[i] == 99999:
                    queue.append(i)
            while len(queue) > 0:
                queryId = queue[0]
                queue.remove(queue[0])

                targetAdj = targetgraph.getAdjacencyMatrix()
                queryAdj = querygraph.getAdjacencyMatrix()

                treemap = dict()  # 根据m的度数排序，优先匹配度数大的节点
                for m in range(len(queryAdj[queryId])):
                    if mapkey[m] != 99999:
                        nearId=mapkey[m]
                        for k in range(len(targetAdj[nearId])):
                            if (not  k in mapkey) and targetAdj[nearId][k]!=-1:
                                content = '%s-%s' % (targetgraph.nodes[targetAdj[nearId][k]].label, targetAdj[nearId][k])
                                treemap.update({content: k})
                if len(treemap) > 0:
                    keys = list(treemap.keys())
                    keys = sorted(keys, reverse=True)
                    targetNode =treemap.get(keys[0])
                    treemap.pop(keys[0])
                    mapkey[queryId] = targetNode

            max_core.append(mapkey)

    return max_core


class MyVF2:

    def dealData(self, graphset: list, querygraph: IniGraph, mappingresult: dict, type: int, mapping: list,system:str):
        res = []
        if type == 0:
            for targetgraph in graphset:
                res = connectAllocateRemaining(querygraph, targetgraph, mappingresult, mapping, system)
        else:
            for targetgraph in graphset:
                res = degreeAllocateRemaining(querygraph, targetgraph, mappingresult, mapping, system)
        return res
