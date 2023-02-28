from base.Edge import Edge
from base.Gate import Gate
from base.NeighborResult import NeighborResult
from base.Score import Score
from base.Solution import Solution
from qct_tools.utils.FileUtils import FileUtils
import time


def computeCCAValue(dist, locations, currentLayers, nextLayers_1, delta):
    result = Score()
    score = 0.0
    submake = 0.0
    subbreak = 0.0
    for i in range(len(currentLayers)):
        loc1 = locations[currentLayers[i].control]
        loc2 = locations[currentLayers[i].target]
        distance = dist[loc1][loc2]
        gate = currentLayers[i]
        getsubscore(gate, distance.paths)
        if gate.subscore > gate.last_subscore:
            subbreak += gate.subscore
            gate.last_subscore = gate.subscore
        else:
            submake += gate.subscore
            gate.last_subscore = gate.subscore
        score += gate.subscore
    subscore = submake - subbreak
    if len(nextLayers_1) > 0:
        for i in range(len(currentLayers)):
            loc1 = locations[currentLayers[i].control]
            loc2 = locations[currentLayers[i].target]
            distance = dist[loc1][loc2]
            gate = currentLayers[i]
            getsubscore(gate, distance.paths)
            score += (gate.subscore * delta)
    result.score = score
    result.subscore = subscore

    return result

def computeCCAValue1(oldlocation, dist, locations, currentLayers, nextLayers_1, delta,system:str):
    result = Score()
    submake = 0.0
    subbreak = 0.0
    FileUtils.compute_depth(currentLayers,system)
    for i in range(len(currentLayers)):
        oldloc1 = oldlocation[currentLayers[i].control]
        oldloc2 = oldlocation[currentLayers[i].target]

        loc1 = locations[currentLayers[i].control]
        loc2 = locations[currentLayers[i].target]
        distance = dist[loc1][loc2].distance
        result.score += distance
        if distance > dist[oldloc1][oldloc2].distance:
            subbreak += 1
        elif distance < dist[oldloc1][oldloc2].distance:
            submake += 1
    subscore = subbreak - submake
    result.subscore = subscore
    submake = 0.0
    subbreak = 0.0
    if len(nextLayers_1) > 0:
        for i in range(len(currentLayers)):
            oldloc1 = oldlocation[currentLayers[i].control]
            oldloc2 = oldlocation[currentLayers[i].target]
            loc1 = locations[currentLayers[i].control]
            loc2 = locations[currentLayers[i].target]
            distance = dist[loc1][loc2].distance
            result.score += distance * delta
            if distance > dist[oldloc1][oldloc2].distance:
                subbreak += 1
            elif distance < dist[oldloc1][oldloc2].distance:
                submake += 1
        subscore = subbreak - submake
        result.subscore += subscore * delta


    return result

def addQX20SwapGates(e: Edge, graph: set, circuits: list):
    cnot = Gate()
    cnot.type = 'cx'
    cnot2 = Gate()
    cnot2.type = 'cx'
    cnot.control = e.source
    cnot.target = e.target
    cnot2.control = e.target
    cnot2.target = e.source
    gg = Gate()
    gg.control = cnot.control
    gg.target = cnot.target
    gg.type = 'SWP'
    circuits.append(cnot)
    circuits.append(cnot2)
    circuits.append(cnot)
    # circuits.append(gg)
    # print(gg.type,gg.control,gg.target)

def addSycamoreSwapGates(e: Edge, graph: set, circuits: list):
    ry_1 = Gate()
    ry_1.type = 'ry'
    ry_1.target = e.target
    ry_1.angle=-90

    ry1 = Gate()
    ry1.type = 'ry'
    ry1.target = e.target
    ry1.angle=90

    cz = Gate()
    cz.type = 'cz'
    cz.control = e.source
    cz.target = e.target

    ry_2 = Gate()
    ry_2.type = 'ry'
    ry_2.target = e.target
    ry_2.angle=-90.0

    ry2 = Gate()
    ry2.type = 'ry'
    ry2.angle=90.0
    ry2.target = e.target
    gg = Gate()
    gg.control = e.source
    gg.target = e.target
    gg.type = 'SWP'
    circuits.append(ry_2)
    circuits.append(cz)
    circuits.append(ry_1)
    circuits.append(ry2)
    circuits.append(cz)
    circuits.append(ry1)
    circuits.append(ry_2)
    circuits.append(cz)
    circuits.append(ry2)
    # circuits.append(gg)
    # print(gg.type,gg.control,gg.target)

# circuits.append(gg)
def computeFidelityValue(dist: list, locations: list, currentLayers: list, nextLayers_1: list, delta: float):
    result = 0.0
    for i in range(len(currentLayers)):
        loc1 = locations[currentLayers[i].control]
        loc2 = locations[currentLayers[i].target]
        distance = dist[loc1][loc2]
        result += distance.distance-3
    if len(nextLayers_1) > 0:
        for i in range(len(nextLayers_1)):
            loc1 = locations[nextLayers_1[i].control]
            loc2 = locations[nextLayers_1[i].target]
            distance = dist[loc1][loc2]
            result += (distance.distance-3) * delta
    # print(result,'-----start')
    result = round(result, 8)
    # print(result,'----end')
    return result

def computeValue(dist: list, locations: list, currentLayers: list, nextLayers_1: list, delta: float):
    result = 0.0
    for i in range(len(currentLayers)):
        loc1 = locations[currentLayers[i].control]
        loc2 = locations[currentLayers[i].target]
        distance = dist[loc1][loc2]
        result += distance.distance-3
    if len(nextLayers_1) > 0:
        for i in range(len(nextLayers_1)):
            loc1 = locations[nextLayers_1[i].control]
            loc2 = locations[nextLayers_1[i].target]
            distance = dist[loc1][loc2]
            result += (distance.distance-3) * delta
    # print(result,'-----start')
    result = round(result, 8)
    # print(result,'----end')
    return result


def computeDepthvalue(currentLayers, nextLayers_1, delta,system:str):
    depthfile = FileUtils.compute_depth(currentLayers,system)
    next = FileUtils.compute_depth(nextLayers_1,system)
    return len(depthfile.layers) + len(next.layers) * delta
def computeDepthvalue1(circuit, nextLayers_1,system:str):
    layer=[]
    if len(circuit) > 0:
        for i in range(len(circuit)):
            layer.append(circuit[i])
    if len(nextLayers_1) > 0:
        for i in range(len(nextLayers_1)):
            layer.append(nextLayers_1[i])
    depthfile = FileUtils.compute_depth(layer,system)
    return len(depthfile.layers)

def computeDepth(currentLayers,system:str):
    depthfile = FileUtils.compute_depth(currentLayers,system)
    return len(depthfile.layers)
def getsubscore(gate:Gate, paths):
    result = 9999999
    for i in range(len(paths)):
        subscore = 0.0
        for j in range(len(paths[i])):
            subscore += paths[i][j].weight
        if subscore < result:
            result = subscore
    gate.subscore = result


class MySolution(Solution):

    def __init__(self, graph, dist, locations, qubits, currentLayers, nextLayers_1):
        self.graph = graph
        self.dist = dist
        self.locations = list(locations)
        self.qubits = list(qubits)
        self.currentLayers = list(currentLayers)
        self.nextLayers_1 = nextLayers_1
        self.circuits = []
        self.swaps = []
        self.score = 9999999
        self.subscore = 9999999
        self.swapped_edge = Edge()


    def getNeighbors(self, type, delta, system:str):
        result = self.computeNeighbor(graph=self.graph, parent=self, dist=self.dist, qubits=self.qubits,
                                      locations=self.locations, currentLayers1=self.currentLayers,
                                      nextLayers_1=self.nextLayers_1, type=type, delta=delta, system=system)
        self.neighbors = result.solutions
        return self.neighbors

    @staticmethod
    def computeNeighbor(graph: set, parent: Solution, dist: list, qubits: list, locations: list,
                        currentLayers1: list, nextLayers_1: list, type: int, delta: float, system:str) -> NeighborResult:
        curr_solved_gates = []
        result = NeighborResult()
        solutions = []
        include_nodes = set()
        currentLayers = list(currentLayers1)
        x = 0
        while x < len(currentLayers):
            loc1 = locations[currentLayers[x].control]
            loc2 = locations[currentLayers[x].target]
            distance = dist[loc1][loc2]
            if  distance.distance <= 3:
                g = Gate()
                g.type =currentLayers[x].type
                g.control = loc1
                g.target = loc2
                curr_solved_gates.append(g)
                del currentLayers[x]
                x = x - 1
            else:
                include_nodes.add(loc1)
                include_nodes.add(loc2)
            x += 1
        for i in range(len(currentLayers)):
            loc1 = locations[currentLayers[i].control]
            loc2 = locations[currentLayers[i].target]
            distance = dist[loc1][loc2]
            paths = distance.paths
            # for k in range(len(paths)):
            #     for j in range(len(paths[k])):
            #         print(loc1,' ', loc2,' ' , dist[loc1][loc2].distance,' path: ',paths[k][j].source , paths[k][j].target)

            for k in range(len(paths)):
                for j in range(len(paths[k])):
                    sour_node = paths[k][j].source
                    tar_node = paths[k][j].target
                    if sour_node in include_nodes or tar_node in include_nodes:
                        newQubits = list(qubits)
                        newLocations = list(locations)

                        q1 = newQubits[paths[k][j].source]
                        q2 = newQubits[paths[k][j].target]
                        newQubits[paths[k][j].source] = q2
                        newQubits[paths[k][j].target] = q1
                        if q1 != -1:
                            newLocations[q1] = paths[k][j].target
                        if q2 != -1:
                            newLocations[q2] = paths[k][j].source

                        s = MySolution(graph, dist, newLocations, newQubits, currentLayers, nextLayers_1)
                        s.neighbors = list()  # linkedlist
                        for m in parent.swaps:
                            s.swaps.append(m)
                        for m in parent.circuits:
                            s.circuits.append(m)
                        for m in curr_solved_gates:
                            s.circuits.append(m)
                        # print(newLocations)
                        s.swaps.append(paths[k][j])
                        s.swapped_edge = paths[k][j]
                        if system.__eq__('sycamore'):
                            addQX20SwapGates(paths[k][j], graph, s.circuits)
                        else:
                            addQX20SwapGates(paths[k][j], graph, s.circuits)
                        if type == 0:
                            #num cca
                            s.score = computeValue(dist, newLocations, currentLayers, nextLayers_1, delta)
                            s.subscore = computeCCAValue1(parent.locations, dist, newLocations, currentLayers, nextLayers_1, delta,system).subscore
                        elif type == 1:
                            #dep num
                            s.score=computeDepthvalue1(s.circuits,nextLayers_1,system)
                            # s.score = computeDepth(s.circuits)
                            s.subscore = computeValue(dist, newLocations, currentLayers, nextLayers_1, delta)
                        elif type==2:
                            # cca num
                            score = computeCCAValue1(parent.locations, dist, newLocations, currentLayers, nextLayers_1, delta,system)
                            s.subscore = computeValue(dist, newLocations, currentLayers, nextLayers_1, delta)
                            s.score =score.subscore
                        else:
                            #num dep
                            s.score = computeValue(dist, newLocations, currentLayers, nextLayers_1, delta)
                            s.subscore = computeDepth(s.circuits)

                        solutions.append(s)
        result.solutions = solutions
        result.curr_solved_gates = curr_solved_gates
        result.current_num = len(currentLayers1)
        return result
