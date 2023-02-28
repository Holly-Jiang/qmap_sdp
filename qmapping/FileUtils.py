import os, sys, math

from base.FileResult import FileResult
from base.Gate import Gate
from base.IniGraph import IniGraph
from base.NodeDegree import NodeDegree


def save_result(path, msg):
    msg = str(msg)
    file = open(path, mode='r+')
    file.write(msg)
    file.close()


class FileUtils:
    # positions = 20
    # nqubits = 20
    @classmethod
    def loadDataSetFromFile(self, path, filename):
        result = []
        if not os.path.exists(path):
            return result
        file = open(path, 'r')
        list = []
        line = file.readline().strip()
        while line != ' ' and line != '' and len(line)>0:
            if line.startswith('t'):
                if list != None and len(list) > 0:
                    result.append(list)
                list = []
            else:
                lineSplit = line.split(' : ')
                n = int(lineSplit[1])
                list.append(n)
            line = file.readline().strip()
        if list != None and len(list) > 0:
            result.append(list)
        file.close()
        return result
    @classmethod
    def loadGraphSetFromFile(self, path, filename):
        graphset = []
        if not os.path.exists(path):
            return graphset
        graph = None
        if not os.path.isfile(path):
            return None
        file = open(path, 'r')
        line = file.readline().strip()
        while line != '' and line != '':
            if line.startswith('t'):
                graphId = line.split(' ')[2]
                if graph != None:
                    graphset.append(graph)
                graph = IniGraph('%s%s' %(filename, graphId))
            elif line.startswith('v'):
                lineSplit = line.split(' ')
                nodeId = int(lineSplit[1])
                nodedegree = int(lineSplit[3])
                graph.addNode(nodeId, nodedegree)
            elif line.startswith('e'):
                lineSplit = line.split(' ')
                sourceId = int(lineSplit[1])
                targetId = int(lineSplit[2])
                edgelabel = 0
                graph.addEdgeById(sourceId, targetId, edgelabel)
            line = file.readline().strip()
        for i in range(len(graph.nodes)):
            degree = 0
            for j in range(len(graph.edges)):
                if graph.edges[j].source == graph.nodes[i] or graph.edges[j].target == graph.nodes[i]:
                    degree += 1
        file.close()
        return graphset

        pass

    @classmethod
    def precessReadQasm(self, path, filename,position:int) -> int:
        layers = []
        ngates = 0
        n2gates = 0
        if os.path.isdir(path) or path.endswith('.zip'):
            return
        # Open file

        f = open(path, "r")
        line = f.readline()
        line = line.strip()
        if not line.__eq__("OPENQASM 2.0;"):
            print('ERROR: first line of the file has to be: OPENQASM 2.0;  %s'%path)
            sys.exit(-1)

        line = f.readline()
        line = line.strip()
        if not line.__eq__("include \"qelib1.inc\";"):
            print('ERROR: second line of the file has to be: include \"qelib1.inc\";')
            sys.exit(-1)
        line = f.readline()
        line = line.strip()
        n = -1
        if not line.startswith('qreg'):
            print('ERROR: failed to parse qasm file: ' + line)
            sys.exit(-1)
        n = int(line[7:len(line) - 2])

        line = f.readline()
        line = line.strip()
        if not line.startswith('creg'):
            print('ERROR: failed to parse qasm file: ' + line)
            sys.exit(-1)

        last_layer = []
        for i in range(position):
            last_layer.append(-1)
        while True:
            line = f.readline().strip()
            if not line:
                break
            if line.__eq__(''):
                break
            g = Gate()
            layer = 0
            str = []
            str.append(line.split(' ')[0])
            str.extend(line.split(' ')[1].split(','))
            if len(str) == 3:
                g.type = str[0]
                g.control = int(str[1][2:len(str[1]) - 1])
                g.target = int(str[2][2:len(str[2]) - 2])
                layer = max(last_layer[g.target], last_layer[g.control]) + 1
                last_layer[g.target] = layer
                last_layer[g.control] = layer
                n2gates += 1
            elif len(str) == 2:
                if str[0].startswith('rz'):
                    angle = float(str[0][3:len(str[0]) - 1])
                    g.control = -1
                    g.target = int(str[1][2:len(str[1]) - 2])
                    g.type = 'rz'
                    g.angle = angle
                else:
                    g.type = str[0]
                    g.control = -1
                    g.target = int(str[1][2:len(str[1]) - 2])
                    layer = last_layer[g.target] + 1
                    last_layer[g.target] = layer
            else:
                print("ERROR: could not read gate: " + line)
                sys.exit(-1)
            ngates += 1
            if len(layers) <= layer:
                layers.append([])
            layers[layer].append(g)
        list = set()
        results = []
        max_node = -1
        layer_map = dict()
        i = 0
        while i < len(layers):
            j = 0
            while j < len(layers[i]):
                if layers[i][j].control != -1 and not layer_map.get(
                        '%d-%d' % (layers[i][j].control, layers[i][j].target)) and not layer_map.get(
                    '%d-%d' % (layers[i][j].target, layers[i][j].control)):
                    if max_node < layers[i][j].control:
                        max_node = layers[i][j].control
                    if max_node < layers[i][j].target:
                        max_node = layers[i][j].target
                    temp = []
                    temp.append(layers[i][j].control)
                    temp.append(layers[i][j].target)
                    results.append(temp)
                    layer_map['%d-%d' % (layers[i][j].target, layers[i][j].control)] = 1
                j += 1
            i += 1
        for i in range(max_node + 1):
            list.add(i)
        content = ("t %d %d\n" % ((max_node + 1), len(results)))
        pre_result = "pre_result/%s" % (filename)

        file = open(pre_result, mode='w+')
        # pre_result = "../../pre_result/%s" % (filename)
        file.write(content)
        nds = []
        for it1 in iter(list):
            degree = 0
            for i in range(len(results)):
                if results[i][0] == it1 or results[i][1] == it1:
                    degree += 1
            nd = NodeDegree()
            nd.nodeId = it1
            nd.degree = degree
            nds.append(nd)
        nds = sorted(nds, key=lambda node: node.degree)

        for i in range(len(nds)):
            if nds[i].degree > 0:
                break
            else:
                nd1 = nds[i]
                nd1.degree = nd1.degree + 1
                nd = nds[len(nds) - 1]
                nd.degree = nd.degree + 1
                temp = []
                temp.append(nd1.nodeId)
                temp.append(nd.nodeId)
                results.append(temp)
        nds = sorted(nds, key=lambda nd: nd.nodeId)
        # for i in nds:
        #     print(' ',i.degree, end=' ')
        for i in range(len(nds)):
            content = 'v %d %d %d\n' % (nds[i].nodeId, 0, nds[i].degree)
            file.write(content)
        for i in range(len(results)):
            content = 'e %d %d\n' % (results[i][0], results[i][1])
            file.write(content)
        file.write('t # -1\n')
        file.close()
        return ngates

    @classmethod
    def compute_depth(self, currentlayers: list,system :str):
        layers = []
        ngates = 0
        result = FileResult()
        last_layer = [-1] * 20
        if system.__eq__('sycamore'):
            last_layer = [-1] * 53
        for i in range(len(currentlayers)):
            g = currentlayers[i]
            layer = 0
            if g.control != -1:
                layer = max(last_layer[g.target], last_layer[g.control]) + 1
                last_layer[g.target] = layer
                last_layer[g.control] = layer
            elif g.control + 1 == 0:
                layer = last_layer[g.target] + 1
                last_layer[g.target] = layer
            else:
                print('ERROR: cound not read gate:', currentlayers[i])
                sys.exit(-1)
            ngates += 1

            if len(layers) <= layer:
                layers.append([])
            layers[layer].append(g)
        result.ngates = ngates
        result.layers = layers
        return result

    @classmethod
    def readQasm(self, path, position:int):
        layers = []
        ngates = 0
        n2gates = 0
        if os.path.isdir(path):
            return
        # Open file
        results = FileResult()
        results.layers = layers
        f = open(path, "r")
        line = f.readline()
        line = line.strip()
        if not line.__eq__("OPENQASM 2.0;"):
            print('ERROR: first line of the file has to be: OPENQASM 2.0; %s' %path)
            sys.exit(-1)

        line = f.readline()
        line = line.strip()
        if not line.__eq__("include \"qelib1.inc\";"):
            print('ERROR: second line of the file has to be: include \"qelib1.inc\";')
            sys.exit(-1)
        line = f.readline()
        line = line.strip()
        n = -1
        if not line.startswith('qreg'):
            print('ERROR: failed to parse qasm file: ' + line)
            sys.exit(-1)
        n = int(line[7:len(line) - 2])

        line = f.readline()
        line = line.strip()
        if not line.startswith('creg'):
            print('ERROR: failed to parse qasm file: ' + line)
            sys.exit(-1)

        last_layer = []
        for i in range(position):
            last_layer.append(-1)
        while True:
            line = f.readline().strip()
            if not line:
                break
            if line.__eq__(''):
                break
            g = Gate()
            layer = 0
            str = []
            str.append(line.split(' ')[0])
            str.extend(line.split(' ')[1].split(','))
            if len(str) == 3:
                g.type = str[0]
                g.control = int(str[1][2:len(str[1]) - 1])
                g.target = int(str[2][2:len(str[2]) - 2])
                layer = max(last_layer[g.target], last_layer[g.control]) + 1
                last_layer[g.target] = layer
                last_layer[g.control] = layer
                n2gates += 1
            elif len(str) == 2:
                if str[0].startswith('rz'):
                    angle = float(str[0][3:len(str[0]) - 1])
                    g.control = -1
                    g.target = int(str[1][2:len(str[1]) - 2])
                    g.type = 'rz'
                    g.angle = angle
                elif str[0].startswith('ry'):
                    angle = float(str[0][3:len(str[0]) - 1])
                    g.control = -1
                    g.target = int(str[1][2:len(str[1]) - 2])
                    g.type = 'ry'
                    g.angle = angle
                elif str[0].startswith('rx'):
                    angle = float(str[0][3:len(str[0]) - 1])
                    g.control = -1
                    g.target = int(str[1][2:len(str[1]) - 2])
                    g.type = 'rx'
                    g.angle = angle
                else:
                    g.type = str[0]
                    g.control = -1
                    g.target = int(str[1][2:len(str[1]) - 2])
                    layer = last_layer[g.target] + 1
                    last_layer[g.target] = layer
            else:
                print("ERROR: could not read gate: " + line)
                sys.exit(-1)
            ngates += 1
            if len(layers) <= layer:
                layers.append([])
            layers[layer].append(g)
        results.ngates = ngates
        results.n2gates = n2gates
        return results
