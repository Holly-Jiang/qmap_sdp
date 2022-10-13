import string
from os import listdir

import cvxpy as cp
import math
import numpy as np
# 目标：
# 整个电路的fidelity最小
# 单量子比特门的error，双量子门的error
# 单量子比特门的执行时间，双量子门的执行时间
# \sum_i^{N}math.log(E(g_i))+\sun_i^{N}(g_t/T)

# qubit 限制：
# 块内的条件编织：一个逻辑qubit映射到一个物理qubit，
# 物理连接的限制，只能在相邻的位置交换 x_{mn}==1表示q_m,q_n相邻，能够进行交换
# 按照门的顺序执行
# 门能够执行
# 门不能执行-》需要调整，有些什么限制，门执行的条件，<q_i,q_j>分别映射到不相邻的<Q_m,Q_n>，
# 通过限制<Q_m,Q_n>必须要相邻，并且要按照门的顺序满足，
# 然后能找到一条路径
# 如何表示qubit的交换:x_{mn}交换q_m,q_n
# A.增加交换x_{mn}，使得门能够执行，以及目标函数最小
# 在每一个门前面都需要插入所有的交换可能性，然后搜索所有的交换排列能够达到A
from cvxpy.atoms.affine.binary_operators import MulExpression
from qiskit import QuantumCircuit
from qiskit.circuit import Instruction
from qiskit.dagcircuit import DAGCircuit, DAGOpNode
from qiskit.qasm.node import Gate
from qiskit.transpiler import CouplingMap

from readOpenQASM import configuration, degree_adjcent_matrix, read_open_qasm


# qubit 限制：
# 块内的条件编织：一个逻辑qubit映射到一个物理qubit，
# 物理连接的限制，只能在相邻的位置交换 x_{mn}==1表示q_m,q_n相邻，能够进行交换
# 按照门的顺序执行
# 门能够执行
# 门不能执行-》需要调整，有些什么限制，门执行的条件，<q_i,q_j>分别映射到不相邻的<Q_m,Q_n>，
# 通过限制<Q_m,Q_n>必须要相邻，并且要按照门的顺序满足，
# 然后能找到一条路径
# 如何表示qubit的交换:x_{mn}交换q_m,q_n
# A.增加交换x_{mn}，使得门能够执行，以及目标函数最小
# 在每一个门前面都需要插入所有的交换可能性，然后搜索所有的交换排列能够达到A

class GateInfo:
    def __init__(self, name, qargs):
        self.name = name
        self.qargs = qargs


def build_coupling_constraint(coupling: list, n: list):
    constraints = [[-1] * range(n) for i in range(n)]
    for c in coupling:
        constraints[c[0]][c[1]] = 1
    return constraints


# l: the number of logical qubit
# n: the number of physical qubit
# 逻辑比特到物理比特是一一对应的

def build_ini_constraints(l: int, n: int, constraints):
    v1 = generate_int_variables(n)
    v2 = generate_int_variables(l)


def build_unique_constraints(X: list, constraints):
    # X: index is logical qubit, and the value is the corresponding physical qubit, default to -1
    # Y: index is physical qubit, and the value is the corresponding logical qubit, default to -1\
    # X 中两两不相等=》没有一个物理比特上映射两个逻辑比特 假设有和物理比特一样数目的逻辑比特

    for i in range((len(X) - 1)):
        # variables are integer, if we want to X[i] !=X[i+1], the abs of them is >0, then >=1
        # cvxpy limit the strict > <
        constraints.extend([cp.abs(X[i] - X[i + 1]) >= 1])
    return constraints


# the neighbor of all physical node of dag
def generate_candidate_set(coupling_map: list, dag: DAGCircuit, X: list):
    res = list()
    # map the logical qubits to physical qubits
    qubits = list()
    for q in dag.qubits:
        qubits.append(X[q])
    for c in coupling_map:
        if c[0] in qubits or c[1] in qubits:
            res.append(c)
    return res


def build_constraint(X: list, coupling_map: list, dag: DAGCircuit):
    # X: index is logical qubit, and the value is the corresponding physical qubit, default to -1
    # Y: index is physical qubit, and the value is the corresponding logical qubit, default to -1
    # 假设有物理比特一样数目的逻辑比特
    vars = list()
    # The qubits of a gate in the list "all_gate" are the physical qubits
    all_gates = list()
    constraints = []
    # for all i in range(X), X[i]!=-1 and
    # if X[i]==j for all k!=i and k in range(X) X[k]!=j
    build_unique_constraints(X, constraints)

    # physical coupling constraint:
    # coupling_const = build_coupling_constraint(coupling=coupling_map, n=len(X))

    # 编码门的顺序 在当前映射下门能执行门，再看下一个门
    # iterate the gate ordered by the topological order
    # if the two mapped physical qubit adjcent, the gate can be executed
    # todo prune
    # the neighbor of all physical node of dag
    C = generate_candidate_set(coupling_map, dag, X)
    for node in dag.topological_op_nodes():
        edge = list()
        for q in node.qargs:
            edge.append(X[q.index])
        if len(node.qargs) == 2:
            if True:
                # 增加SWAP门集S，使得所有的门都可以执行
                # 在每一个门前都有所有的交换候选集C，长度最长是耦合图的最长路径
                # todo prune
                # 用一个矩阵M表示如果交换(x,y)则将矩阵M_{xy}==第几次交换，矩阵能交换的为0不能交换的-1
                # 禁忌策略：最近交换过的边不要再交换回去，todo 如果遇到禁忌策略回退
                # 最坏情况：最长路径l*边条数e个变量-》每次选择邻接
                # swap[i]：行初等变换
                # v1: the number of Swaps
                # v2: the number of identity matrices

                swaps, v1, v2 = generate_variables_matrix(len(X), C)
                vars.append(v1)
                vars.append(v2)
                X = np.vstack(X)
                for i in range(len(swaps)):
                    X = np.dot(np.array(swaps[i]), X)
                    constraints.extend([v1[i] + v2[i] == 1])
                    # insert the swap gate into the gate sequence
                    s1 = GateInfo(node.op, v1[i] * np.hstack(C[i]))
                    all_gates.append(s1)
                    s2 = GateInfo(node.op, v1[i] * np.hstack([C[i][1], C[i][0]]))
                    all_gates.append(s2)
                    all_gates.append(s1)
                edge[0] = X[node.qargs[0].index]
                edge[1] = X[node.qargs[1].index]
            # 判断边edge是否在coupling_map中存在 若edge 存在coupling的邻接矩阵A中，则A[edge[0]][edge[1]]==1
            # insert enough swap gates to the edge in coupling map
            set_constraints, v3 = build_set_inter_constraint(coupling_map, len(X))
            e = np.hstack(edge)
            constraints.extend([e - set_constraints == np.zeros(len(X))])
            constraints.extend([v3 == 1])
            pass
        g = GateInfo(node.op, edge)
        all_gates.append(g)
    return constraints, vars, all_gates


# 构造coupling的邻接矩阵有边相邻则为1
# # todo consider using the fidelity of edge
# def build_set_inter_constraint(M: list, n: int):
#     res = np.zeros((n, n))
#     for i in range(len(M)):
#         res[M[i][0]][M[i][1]] = 1
#     return res


# [[0, 1], [1, 0], [1, 2], [1, 4], ...]
# generate the variables list  v1
# res: [0*x1+1*x2+1*x3+1*x4...,1*x1+0*x2+2*x3+4*x4]
# x1+x2+x3+x4+...=1, for  x1,x2,...\in {0, 1}
def build_set_inter_constraint(M: list, n: int):
    v1 = generate_boolean_variables(len(M))
    res = [0, 0]
    res2 = 0
    for i in range(len(M)):
        res[0] = res[0] + M[i][0] * v1[i]
        res[1] = res[1] + M[i][1] * v1[i]
        res2 += v1[i]
    return res, res2


# name:gate name
# qubits: operation qubits
# gates: the gate errors and time of architecture
def edge_info(name, qubits, gates: list):
    for c in gates:
        if c.gate == name and c.qubits == qubits:
            return c.parameters


# 根据门的名字，作用qubit，需要的qubit信息name{gate_length,gate_error}
# 架构名字
def gate_info(g: Gate, name: string, arch: string):
    conf, prop = configuration(arch)
    for gate in prop.gates:
        if gate.gate == g.name:
            if gate.qubit[0] == g.id:
                for p in gate.parameters:
                    if p.name == name:
                        return p.value
                    elif p.name == name:
                        return p.value


# 将插入SWAP的矩阵转化为SWAP依次插入的位置list
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


# variable 才是SDP能够求解出来的，
# 遍历dag，V是变量的矩阵列表
# 计算在dag中门的执行过程中插入门后生成的电路的fidelity
# 有一个硬性限制，矩阵中的值数量不超过目标电路的最长路径
# obj=\sum_g g.e-\sum_q q.t/q.T
# def objective_function(dag: DAGCircuit, V: list, map: list):
#     count = 0
#     obj = 1
#     l = len(V[count])
#     for node in dag.topological_op_nodes():
#         M = matrix2list(V[count])
#         count += 1
#         # 插入的SWAP门误差
#         for i in M:
#             param = edge_info(node.name, [i[0], i[1]], map)
#             obj *= param[1].value
#         # original 门的误差
#         if len(node.qargs) == 2:
#             c = node.qargs[0].index
#             t = node.qargs[1].index
#             param = edge_info(node.name, [c, t], map)
#             obj *= param[1].value
#     return obj


# gates: all gates
# params: all information (gate errors and gate execution time) of gate in the architecture
# return: the fidelity of all gates in topologic
def objective_function(gates: list, params: list):
    res = 1
    for g in gates:
        info = edge_info(g.op.name, g.qargs, params)
        res *= info[1].value
    return res


# Map logical qubits to physical qubits according to the degree of nodes
# in interaction graph and coupling graph
#todo 用整体的interaction graph 定位映射的总体位置还是
#仅仅用当前的interaction定位对当前结构最有利的映射
#首先确定一个节点的映射，然后根据边的权重确定先后映射次序
def generate_ini_mapping_by_degree(coupling_map: list, dag: DAGCircuit):
    D_P = degree_adjcent_matrix(coupling_map)
    # compute the cx gate
    edge = list()
    for node in dag.topological_op_nodes():
        if len(node.qargs) == 2:
            edge.append(node.qargs)
    D_L = degree_adjcent_matrix(edge)


# gate basis: ['id', 'rz', 'sx', 'x', 'cx', 'reset']
def SDP_tools(X: list, dag: DAGCircuit, arch: string):
    conf, prop = configuration(arch)
    cm = CouplingMap(conf.coupling_map)
    # g_l = gate_info(g, "gate_length", arch)
    phy_deg, am = degree_adjcent_matrix(cm)
    # variables of the initial mapping
    if len(X) == 0:
        X = generate_ini_mapping_by_degree(conf.coupling_map, dag)
        X = generate_int_variables(len(cm.physical_qubits))
    # vars: the variables of Swaps and identity matrices
    # v1: the variables of Swaps
    cst, vars, all_gates = build_constraint(X, conf.coupling_map, dag)
    obj = objective_function(all_gates, prop.gates)
    cp.Problem(cp.Minimize(obj), cst)
    circ = QuantumCircuit(3)
    circ.cx(1, 0)
    pass


def generate_swap_matrices(n: int, coupling_map: list):
    res = list()
    for i in coupling_map:
        matrix = np.eye(n)
        matrix[i[0]][i[1]] = 1
        matrix[i[1]][i[0]] = 1
        matrix[i[1]][i[1]] = 0
        matrix[i[0]][i[0]] = 0
        res.append(matrix)
    return res


def generate_int_variables(n: int):
    va = list()
    for i in range(n):
        va.append(cp.Variable(integer=True))
    return va


def generate_boolean_variables(n: int):
    va = list()
    for i in range(n):
        va.append(cp.Variable(boolean=True))
    return va


# generate the basic transforation matrics,
# the transformation position v1 and the diagnal position v2 are the variables
# record the transformation matrices M and the correspongding edge C
def generate_eye_list(n: int):
    res = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        res[i][i] = 1
    return res


# generate the swap sequence
# todo prune
# C：the candidates list
def generate_variables_matrix(n: int, C: list):
    res = list()
    v1 = generate_boolean_variables(len(C))
    v2 = generate_boolean_variables(len(C))
    for i in range(len(C)):
        matrix = generate_eye_list(n)
        matrix[C[i][0]][C[i][1]] = v1[i]
        matrix[C[i][1]][C[i][0]] = v1[i]
        matrix[C[i][0]][C[i][0]] = v2[i]
        matrix[C[i][1]][C[i][1]] = v2[i]
        res.append(matrix)
    return res, v1, v2


conf, prop = configuration("sydney")
cm = CouplingMap(conf.coupling_map)
phy_deg, am = degree_adjcent_matrix(cm)

if __name__ == '__main__':
    # read_open_qasm("./test.qasm", "111")
    # read_open_qasm("/Users/jiangqianxi/Desktop/github/TSA/tsa/src/main/resources/data/4gt4-v0_72.qasm", "4gt4-v0_72.qasm")
    files = listdir("/Users/jiangqianxi/Desktop/meloni/qmapping/nam_u/")
    files = sorted(files)
    count = 0
    for path in files:
        print(count, path)
        count += 1
        if count == 1:
            continue
        dags = read_open_qasm("/Users/jiangqianxi/Desktop/meloni/qmapping/nam_u/" + path, path)
        for i in range(len(dags)):
            SDP_tools([], dags[i], "tokyo")

# Create two scalar optimization variables.
# x = cp.Variable()
# y = cp.Variable()
#
# # Create two constraints.
# constraints = [x + y == 1,
#                x - y >= 1]
#
# # Form objective.
# obj = cp.Minimize((x - y)**2)
# cp.MatrixFrac()
# # Form and solve problem.
# prob = cp.Problem(obj, constraints)
# prob.solve()  # Returns the optimal value.
# print("status:", prob.status)
# print("optimal value", prob.value)
# print("optimal var", x.value, y.value)
