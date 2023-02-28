import copy
import string
import sys
from collections import deque
from os import listdir
import os
import math
import numpy as np
# ç›®æ ‡ï¼š


# \sum_i^{N}math.log(E(g_i))+\sun_i^{N}(g_t/T)


# é—¨èƒ½å¤Ÿæ‰§è¡Œ


from cvxpy.atoms.affine.binary_operators import MulExpression
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Instruction
from qiskit.converters import circuit_to_dag
from qiskit.dagcircuit import DAGCircuit, DAGOpNode
from qiskit.qasm.node import Gate
from qiskit.transpiler import CouplingMap

from FileUtils import FileUtils
from readOpenQASM import configuration, degree_adjcent_matrix, read_open_qasm


class Entry:
    def __init__(self, vars):
        self.vars = vars


class Path:
    def __init__(self, path, dst, vars):
        self.path = path
        self.dst = dst
        self.vars = vars


class SwapInfo:
    def __init__(self, edge, swaps, var1, var2):
        self.edge = edge
        self.swaps = swaps
        self.var1 = var1
        self.var2 = var2


coupling_map = [[0, 1], [1, 0], [0, 5], [5, 0], [1, 2], [2, 1], [1, 6], [6, 1], [1, 7], [7, 1], [2, 3], [3, 2], [2, 7],
                [7, 2], [2, 6], [6, 2], [3, 4], [4, 3], [3, 8], [8, 3], [3, 9], [9, 3], [4, 9], [9, 4], [4, 8], [8, 4],
                [5, 6], [6, 5], [5, 10], [10, 5], [5, 11], [11, 5], [6, 7], [7, 6], [6, 11], [11, 6], [6, 10], [10, 6],
                [7, 8], [8, 7], [7, 12], [12, 7], [7, 13], [13, 7], [8, 9], [9, 8], [8, 13], [13, 8], [8, 12], [12, 8],
                [9, 14], [14, 9], [10, 11], [11, 10], [10, 15], [15, 10], [11, 12], [12, 11], [11, 16], [16, 11],
                [11, 17], [17, 11], [12, 13], [13, 12], [12, 17], [17, 12], [12, 16], [16, 12], [13, 14], [14, 13],
                [13, 18], [18, 13], [13, 19], [19, 13], [14, 19], [19, 14], [14, 18], [18, 14], [15, 16], [16, 15],
                [16, 17], [17, 16], [17, 18], [18, 17], [18, 19], [19, 18]]


def isomorphism(path, file_name, system: string):
    current_path ='%s%s.qasm'%( path,file_name)
    mappingpath = 'pre_ini_qx20/%s' % (file_name)
    position = 20
    if system == 'sydney':
        position = 27
    if os.path.isdir(current_path) or current_path.endswith('.zip'):
        print('The path [%s] is invalid!' % path)
        sys.exit(-1)
    FileUtils.precessReadQasm(current_path, file_name, position)
    os.system(
        'CISC/SubgraphComparing/build/matching/SubgraphMatching.out -d CISC/SubgraphComparing/test/sample_dataset/%s.graph -q pre_result/%s  -filter DPiso -order GQL -engine LFTJ -num 100\n' % (
            system, file_name))
    mapping = FileUtils.loadDataSetFromFile(mappingpath, 'mapping ')
    return mapping


def remove_ancestors(dag: DAGCircuit, revisited_nodes):
    for node in dag.topological_op_nodes():
        if node._node_id in revisited_nodes:
            dag.remove_op_node(node)


def executableQ(qubits, cm):
    for m in cm:
        if qubits[0] == m[0] and qubits[1] == m[1] or qubits[1] == m[0] and qubits[0] == m[1]:
            return True
    return False


def exec_block(Gs, Q, arch, qubits):
    conf, prop = configuration(arch)
    cm = conf.coupling_map
    cm = coupling_map
    count = 0
    for i in Gs:
        if i[0] > count:
            count = i[0]
        if i[1] > count:
            count = i[1]

    qc = QuantumCircuit(QuantumRegister(count + 1))
    for i in Gs:
        qc.cx(i[0], i[1])
    block = circuit_to_dag(qc)
    layers = block.multigraph_layers()
    all_layers = list()
    for fl in layers:
        all_layers.append(fl)
    first_layer = all_layers[1]
    del_nodes = []
    for l in first_layer:
        if len(l.qargs) == 2 and isinstance(l, DAGOpNode) and executableQ(
                [L2P(Q, l.qargs[0].index), L2P(Q, l.qargs[1].index)], cm):
            del_nodes.append(l)
            remove_ancestors(block, [l])
    Gs_new = list()
    for g in block.topological_op_nodes():
        l = list()
        for i in g.qargs:
            l.append(i.index)
        Gs_new.append(l)
    return Gs_new
    pass


def fun_inimaping(path):
    path = path.split('.qasm')[0]
    if not os.path.isfile(path):
        path = path + ".qasm.txt"
    f = open(path, 'r')
    line = f.readline()
    print(line)
    line = line.split('[')[1].split(']')[0]
    arr = line.split(',')
    l = len(arr)
    q = [[0 for i in range(l)] for j in range(l)]
    phy = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    loc = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    for i in range(len(arr)):
        if int(str.strip(arr[i])) != 20:
            phy = phy - set([i])
            loc = loc - set([int(str.strip(arr[i]))])
            q[i][int(str.strip(arr[i]))] = 1
    phy = list(phy)
    loc = list(loc)
    for i in range(len(phy)):
        q[phy[i]][loc[i]] = 1
    return q


def build_dist_table_tabu(n: int, graph: list):
    dist = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i][j] = bfsForTabu(i, j, graph)
            else:
                dist[i][i] = ShortPath()
    return dist


def bfsForTabu(startindex: int, goal: int, graph: list):
    reslut = ShortPath()
    solutions = []
    edges = []
    queue = []
    v = []
    v.append(startindex)
    queue.append(v)
    length = 0
    successors = []
    while len(queue) > 0:
        v = queue[0]
        queue.pop(0)
        current = v[len(v) - 1]
        if current == goal:
            length = len(v)
            solutions.append(v)
            break
        else:
            successors.clear()
            it = graph
            for e in it:
                if e[0] == current and not (e[1] in v) and not (e[1] in successors):
                    successors.append(e[1])
                if e[1] == current and not (e[0] in v) and not (e[0] in successors):
                    successors.append(e[0])
            # successors = sorted(successors)
            su = iter(successors)
            for succ in su:
                v2 = list(v)
                v2.append(succ)
                queue.append(v2)
    # while len(queue) > 0:
    while len(queue) > 0 and len(queue[0]) == length:
        if queue[0][len(queue[0]) - 1] == goal:
            solutions.append(queue[0])
        queue.pop(0)
    for i in range(len(solutions)):
        v1 = solutions[i]
        e1 = []
        for j in range(len(v1) - 1):
            source = v1[j]
            target = v1[j + 1]
            e1.append([source, target])
        edges.append(e1)
    reslut.distance = (length - 1) * 3
    reslut.paths = edges
    return reslut


class ShortPath:
    def __init__(self):
        self.paths = []
        self.distance = 0


# é—¨èƒ½å¤Ÿæ‰§è¡Œ


class GateInfo:
    def __init__(self, name: string, qargs: list):
        self.name = name
        self.qargs = qargs


def matrix_row_swap(s, x: list, y: list):
    for i in range(len(x[s[0]])):
        row1 = x[s[0]][i]
        x[s[0]][i] = x[s[1]][i]
        x[s[1]][i] = row1

        row1 = y[s[0]][i]
        y[s[0]][i] = y[s[1]][i]
        y[s[1]][i] = row1
    return x, y


def matrix_add(x1: list, y1: list, x2: list, y2: list):
    for i in range(len(x1)):
        for j in range(len(x1[i])):
            x1[i][j] += x2[i][j]
            y1[i][j].union(y2[i][j])
    return x1, y1


def MatrixMulti(S: list, x: list):
    M = [[0 for i in range(len(S))] for j in range(len(S))]
    for i in range(len(S)):
        for j in range(len(x)):
            for k in range(len(S[i])):
                if (isinstance(S[i][k], int) and S[i][k] == 0) or (isinstance(x[k][j], int) and x[k][j] == 0):
                    pass
                elif isinstance(S[i][k], int) and S[i][k] == 1:
                    M[i][j] += x[k][j]
                elif isinstance(x[k][j], int) and x[k][j] == 1:
                    M[i][j] += S[i][k]
                else:
                    M[i][j] += S[i][k] * x[k][j]
    return M


def build_coupling_constraint(coupling: list, n: list):
    constraints = [[-1] * range(n) for i in range(n)]
    for c in coupling:
        constraints[c[0]][c[1]] = 1
    return constraints


def build_unique_constraints(x: list, constraints, param):
    i = 0
    while i < len(x):
        j = 0
        row = 0
        col = 0
        # variables are integer, if we want to x[i] !=x[i+1], the abs of them is >0, then >=1
        # cvxpy limit the strict > <
        while j < len(x):
            if not isinstance(x[i][j], int):
                # print(i, j)
                pass
            row += x[i][j]
            col += x[j][i]
            j += 1
        if (isinstance(row, int) and row > 1) or (not isinstance(row, int)):
            constraints.extend([row <= param])
        if (isinstance(col, int) and col > 1) or (not isinstance(row, int)):
            constraints.extend([col <= param])
        i += 1
    return constraints


# the node in the shortest path
# def generate_candidate_set(dist, node: DAGOpNode, x: list):
#     res = list()
#     # map the logical qubits to physical qubits
#     # qubits = list()
#     # for q in dag.qubits:
#     #     qubits.append(x[q])
#     print(x[node.qargs[0].index][0], x[node.qargs[1].index][0])
#     path = dist[x[node.qargs[0].index][0]][x[node.qargs[1].index][0]].paths
#     print(path)
#     for c in path:
#         for k in c:
#             res.append(k)
#         # if c[0] in qubits or c[1] in qubits:
#         #     res.append(c)
#     return res


# initial mapping
# give the logical qubit, return the mapped physical qubit
def L2P(x: list, q: int):
    for i in range(len(x)):
        if isinstance(x[i][q], int) and x[i][q] != 0:
            return i
        elif not isinstance(x[i][q], int):
            return None
    pass


# give the logical qubit, return the mapped physical qubit
def L2PP(x: list, q: int):
    phy_var = list()
    for i in range(len(x)):
        if isinstance(x[i][q], int) and x[i][q] != 0:
            return [i]
        elif not isinstance(x[i][q], int):
            phy_var.append(i)
    return phy_var


def P2L(x: list, q: int):
    for i in range(len(x)):
        if x[q][i] == 1:
            return i


def matrix_deepcopy(x):
    res = list()
    for i in x:
        r = list()
        for j in i:
            r.append(j)
        res.append(r)
    return res


def generate_multi_phy_qubit(x, qargs):
    if len(qargs) == 2:
        q1 = L2PP(x, qargs[0].index)
        q2 = L2PP(x, qargs[1].index)
        res = list()
        for i in range(len(q1)):
            for j in range(len(q2)):
                if q1[i] != q2[j]:
                    # physical qubit list
                    res.append([q1[i], q2[j]])
    else:
        # physical qubit list
        res = L2PP(x, qargs[0].index)
    return res


def matrix_add_var(x1: list, y1: list, v1, vars):
    for i in range(len(x1)):
        for j in range(len(x1[i])):
            if isinstance(x1[i][j], int) and x1[i][j] != 0:
                x1[i][j] = (x1[i][j] + v1) / 2
                y1[i][j] = y1[i][j] | set(vars)
    return x1, y1


# æž„é€ couplingçš„é‚»æŽ¥çŸ©é˜µæœ‰è¾¹ç›¸é‚»åˆ™ä¸º1
# # todo consider using the fidelity of edge
# def build_set_inter_constraint(M: list, n: int):
#     res = np.zeros((n, n))
#     for i in range(len(M)):
#         res[M[i][0]][M[i][1]] = 1
#     return res


# name: gate name
# qubits: operation qubits
# gates: the gate errors and time of architecture

#
def edge_info(g, gates: list):
    for c in gates:
        if c.gate == g.name and set(g.qargs) == set(c.qubits):
            return c.parameters
    pass


def gate_info(name: string, qs: list, para: string, arch: string):
    real_name = ''
    if name.__eq__('t') or name.__eq__('tdg') or name.__eq__('z') or name.__eq__('s') or name.__eq__('sdg'):
        real_name = 'u1'
    elif name.__eq__('h'):
        real_name = 'u2'
    elif name.__eq__('x') or name.__eq__('y'):
        real_name = 'u3'
    g = GateInfo(real_name, qs)
    conf, prop = configuration(arch)
    for gate in prop.gates:
        if gate.gate == g.name:
            if len(set(gate.qubits).intersection(set(g.qargs))) == len(g.qargs):
                for p in gate.parameters:
                    if p.name == para:
                        return p.value
    pass


def matrix2list(M: list):
    l = len(M)
    res = list()
    flag = False
    for i in range(l * l):
        for j in range(l):
            for k in range(l):
                if i == M[j][k]:
                    res.append([j, k])
                    flag = True
                    break
            if flag == True:
                flag = False
                break
    return res


# obj=\sum_g g.e-\sum_q q.t/q.T
# def objective_function(dag: DAGCircuit, V: list, map: list):
#     count = 0
#     obj = 1
#     l = len(V[count])
#     for node in dag.topological_op_nodes():
#         M = matrix2list(V[count])
#         count += 1

#         for i in M:
#             param = edge_info(node.name, [i[0], i[1]], map)
#             obj *= param[1].value
#         # original é—¨çš„è¯¯å·®
#         if len(node.qargs) == 2:
#             c = node.qargs[0].index
#             t = node.qargs[1].index
#             param = edge_info(node.name, [c, t], map)
#             obj *= param[1].value
#     return obj


def generate_degree_mapping(M_P, assign, ini, e1, e2, D_P, D_L):
    if not is_logical_not_location(ini, e1):
        return
    index = -1
    p2 = L2P(ini, e2)
    k = 0
    delta = 3
    adj = list()
    while (k < len(M_P[p2])):
        if M_P[p2][k] != 0:
            if is_not_location(ini, k) and is_logical_not_location(ini, e1):
                adj.append(k)
                if math.fabs(D_P[k] - D_L[e1]) < delta:
                    index = k
                    break
                else:
                    # print("not math.fabs(D_P[j] - D_L[e1]) < ", delta, D_P[k], " ", D_L[e1])
                    delta += k
        k += 1
    if index == -1:
        if len(adj) == 0:
            for i in range(len(M_P)):
                if is_not_location(ini, i) and not i in adj:
                    adj.append(i)
        for i in adj:
            if is_not_location(ini, i) and is_logical_not_location(ini, e1):
                index = i
    ini[index][e1] = 1
    assign.add(e1)


def is_logical_not_location(ini: list, j: int):
    for l in range(len(ini)):
        if ini[l][j] == 1:
            return False
    return True


def is_not_location(ini: list, j: int):
    for l in range(len(ini)):
        if ini[j][l] == 1:
            return False
    return True


def map_dag_degree(dag: DAGCircuit, assign, queue, M_P, ini, D_P, D_L):
    for node in dag.topological_op_nodes():
        if len(node.qargs) == 1:
            continue
        if len(node.qargs) == 2:
            queue.extend([node.qargs[0].index, node.qargs[1].index])
            if len({node.qargs[0].index, node.qargs[1].index} & (assign)) == 0:
                continue

        while len(queue) > 0:
            e1 = queue.pop()
            e2 = queue.pop()
            # if e1 and e2 are not in assigin, they are entered into the queue
            # if e1 and e2 are in assigin, skip them
            # if either e1 or e2 in assigin, we map the unmapped node
            if e1 not in assign and e2 not in assign:
                pass  # todo
            elif e1 in assign and e2 in assign:
                continue
            else:
                if e1 not in assign:
                    generate_degree_mapping(M_P, assign, ini, e1, e2, D_P, D_L)
                else:
                    generate_degree_mapping(M_P, assign, ini, e2, e1, D_P, D_L)
    while len(queue) > 0:
        e1 = queue.pop()
        e2 = queue.pop()
        # if e1 and e2 are not in assigin, they are entered into the queue
        # if e1 and e2 are in assigin, skip them
        # if either e1 or e2 in assigin, we map the unmapped node
        if e1 not in assign and e2 not in assign:
            pass  # todo
        elif e1 in assign and e2 in assign:
            continue
        else:
            if e1 not in assign:
                generate_degree_mapping(M_P, assign, ini, e1, e2, D_P, D_L)
            else:
                generate_degree_mapping(M_P, assign, ini, e2, e1, D_P, D_L)


def map_single_qubit(M_P, q, ini, assign):
    phy_qubits = list()
    for i in range(len(ini)):
        flag = True
        for j in range(len(ini[i])):
            if ini[i][j] == 1:
                flag = False
                break
        if flag:
            phy_qubits.append(i)

    for i in range(len(M_P)):
        for j in range(len(M_P[i])):
            if i in phy_qubits and M_P[i][j] == 0 and is_not_location(ini, j) and is_logical_not_location(ini, q):
                ini[j][q] = 1
            elif j in phy_qubits and M_P[i][j] == 0 and is_not_location(ini, i) and is_logical_not_location(ini, q):
                ini[i][q] = 1
    if L2PP(ini, q) == None:
        for i in range(len(ini)):
            if (not i in phy_qubits) and is_not_location(ini, i) and is_logical_not_location(ini, q):
                ini[i][q] = 1
    assign.add(q)


def map_IG_degree(IG: list, assign, queue, M_P, ini, D_P, D_L):
    for ig in IG:
        if len(ig) == 1:
            if is_logical_not_location(ini, ig[0]):
                map_single_qubit(M_P, ig[0], ini, assign)
            continue
        if len({ig[0], ig[1]} & (assign)) == 1:
            queue.extend(ig)
            while len(queue) > 0:
                e1 = queue.pop()
                e2 = queue.pop()
                # if e1 and e2 are not in assigin, they are entered into the queue
                # if e1 and e2 are in assigin, skip them
                # if either e1 or e2 in assigin, we map the unmapped node
                if e1 not in assign and e2 not in assign:
                    pass  # todo
                elif e1 in assign and e2 in assign:
                    continue
                else:
                    if e1 not in assign:
                        generate_degree_mapping(M_P, assign, ini, e1, e2, D_P, D_L)
                    else:
                        generate_degree_mapping(M_P, assign, ini, e2, e1, D_P, D_L)
        elif len({ig[0], ig[1]} & (assign)) == 0:
            queue.extend(ig)
    pass


def generate_ini_mapping_by_degree(coupling_map, dag: DAGCircuit, IG: list, n: int):
    ini = [[0 for i in range(n)] for j in range(n)]
    assign = set()
    D_P, M_P = degree_adjcent_matrix(coupling_map, n)
    edge = list()
    # find the latest degree node
    for node in dag.topological_op_nodes():
        if len(node.qargs) == 2:
            edge.append([node.qargs[0].index, node.qargs[1].index])
    D_L, M_L = degree_adjcent_matrix(edge, n)
    d_max = 0
    d_p_index = -1,
    for j in range(len(D_P)):
        if D_P[j] > d_max:
            d_p_index = j
            d_max = D_P[j]
    d_max = 0
    d_l_index = -1
    for j in range(len(D_L)):
        if D_L[j] > d_max:
            d_l_index = j
            d_max = D_L[j]
    ini[d_p_index][d_l_index] = 1
    assign.add(d_l_index)
    queue = deque()
    map_dag_degree(dag, assign, queue, M_P, ini, D_P, D_L)
    # the unmapped node:
    # map them to  the neighbor of the mapped node with minimal degree
    # d = 10
    # index = -1
    # for j in assign:
    #     if D_L[j] < d:
    #         d = D_L[j]
    #         index = j
    # for j in range(len(M_P[L2P(ini, index)])):
    #     if M_P[L2P(ini, index)][j] != 0 and is_not_location(ini, j):
    map_IG_degree(IG, assign, queue, M_P, ini, D_P, D_L)

    return ini


# gate basis: ['id', 'rz', 'sx', 'x', 'cx', 'reset']
def SDP_tools(x: list, dag: DAGCircuit, IG: list, arch: string):
    conf, prop = configuration(arch)
    cm = CouplingMap(conf.coupling_map)
    # cmaping=conf.coupling_map
    cmapping = coupling_map
    # g_l = gate_info(g, "gate_length", arch)
    phy_deg, am = degree_adjcent_matrix(cmapping, len(cm.physical_qubits))
    # variables of the initial mapping
    if len(x) == 0:
        x = generate_ini_mapping_by_degree(cmapping, dag, IG, len(cm.physical_qubits))
    return x


def filelist(dirstr):
    # dirstr = "/Users/jiangqianxi/Desktop/github/TSA/tsa/src/main/resources/data/"
    files = listdir(dirstr)
    files = sorted(files)
    return files


def func(dirstr, path, arch):
    count = 0
    count += 1
    res = read_open_qasm(dirstr + path, path, arch)
    if res is None:
        return
    dags = res[0]
    IG = res[1]
    gates = res[2]
    names = res[3]
    qubits = res[4]

    inimap = []
    if len(dags) == 0:
        return
    conf, prop = configuration(arch)
    inimap = SDP_tools(inimap, dags[0], IG, arch)
    block = exec_block([[1, 0], [1, 0], [3, 2], [6, 5], [6, 4], [4, 3], [2, 4]],
                       [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]], arch, qubits)
    return gates, inimap, names, qubits


if __name__ == '__main__':
    M = [[0 for i in range(20)] for j in range(20)]
    for i in range(len(coupling_map)):
        M[coupling_map[i][0]][coupling_map[i][1]] = 1
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end=',')
        print(';')
    dirstr = "./data/"
    # dirstr = '/home/jianghui/data/'
    files = listdir(dirstr)
    files = sorted(files)
    count = 0
    value = gate_info("t", [1], 'gate_error', 'tokyo')
    for path in files:
        print(count, path)
        count += 1
        if count < 81:
            continue
        arch = "tokyo"
        res = func(dirstr, path, arch)
        # dags, IG, gates = read_open_qasm(dirstr + path, path, arch)

        # SDP_tools([], dags, IG, arch)
        # inimap = []
        # for i in range(len(dags)):
        #     SDP_tools(inimap, dags[i], IG, arch)
        pass
