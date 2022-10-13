# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from qiskit import QuantumCircuit
from qiskit.dagcircuit import DAGCircuit


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#将电路根据破圈的规则进行划分
#无向图中边的数量大于等于节点个数及有环
def circuit_partition(dag: DAGCircuit):
    edges=dag.edges()
    ton=dag.topological_op_nodes()
    tn=dag.topological_nodes()
    edge_count=0
    node_count=0
    dag.extract_dag_overlap_sets()
    for edge in edges:
        pass
    pass


def initial_mapping():
    pass


def qubit_adjust():
    pass


if __name__ == '__main__':
    print_hi('PyCharm')
    path=""
    circuit_partition()
    initial_mapping()
    qubit_adjust()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
