from dis import Instruction

from base.BooleanResult import BooleanResult
from base.Qubit import Qubit
from base.StringResult import StringResult


class Instruction:
    Operation = 0
    Measure = 1
    Decline = 2

    def getSubStr(self, pos) -> StringResult:
        start = pos
        result = StringResult()
        result.start = pos
        result.str = self.code
        while pos < len(self.code) and self.code[pos] != ' ' and self.code[pos] != ',' and self.code[pos] != ';':
            pos += 1
        end = pos
        pos+=1
        while pos < len(self.code) and self.code[pos] == ' ':
            pos += 1
        result.pos = pos
        result.end = end
        result.subStr = self.code[start: end]
        return result

    def __init__(self):
        self.is_operation = False
        self.is_void = False
        self.qubits = []
        self.prefix = []
        self.code = ''
        self.line = 0
        self.mark = 0
        self.next = None

    def isEnd(self):
        return self.code == 'end'

    def printCode(self, writer):
        if self.is_void:
            return
        writer.write(self.code)
        writer.write('\n')
        writer.flush()

    def judge(self, prefix):
        if prefix == 'qreg' or prefix == 'creg' or prefix == 'OPENQASM' or prefix == 'include':
            return Instruction.Decline
        elif prefix == 'measure':
            return Instruction.Measure
        else:
            return Instruction.Operation

    def judgeQubits(self,qubits1:list):
        for id in self.qubits:
            p=None
            for i in range(len(qubits1)):
                if qubits1[i].id==id:
                    p=qubits1[i]
            if p==None:
                print('no qubit called:',id)
                continue
            if p.mark==0:
                return False
        return True

    def isEmpty(self):
        for i in range(len(self.code)):
            if self.code[i] != ' ':
                return False
        return True

    def input(self, u, line, qubits: list, pw):
        result = BooleanResult()
        result.index = line
        result.total_qubits = u
        self.code = pw.readline().strip()
        if self.code == None or len(self.code)==0 or self.isEnd():
            result.flag = False
            return result
        if self.isEmpty():
            result.flag = True
            return result
        self.line = line
        line += 1
        result.index = line
        pos = 0
        strResult = self.getSubStr(pos)
        prefix = strResult.subStr
        pos = strResult.pos
        if self.judge(prefix) != self.Operation:
            self.is_operation = False
            result.flag = True
            return result
        self.is_operation = True
        while pos < len(self.code):
            result1 = self.getSubStr(pos)
            qub = result1.subStr
            pos = result1.pos
            tmp = self.hashi(qubits, qub)
            if qubits[tmp].sign == 0:
                qubits[tmp].name = qub
                qubits[tmp].sign = 1
                u += 1
                result.total_qubits = u
            qubits[tmp].insertInstr(self)
            self.insertQubit(qubits[tmp])
        result.flag=True
        return result

    def insertQubit(self, q: Qubit):
        self.qubits.append(q.id)

    def hashi(self, qubits, name):
        i = 0
        sum = 0
        while qubits[i].sign != 0:
            if name == qubits[i].name:
                return i
            i += 1
        return i

    def setQubitsState(self, state: int, qubits1: list):
        for id in self.qubits:
            p=None
            for i in range(len(qubits1)):
                if qubits1[i].id == id:
                    p = qubits1[i]
            if p == None:
                print('no qubit called: ', id)
                continue
            p.mark = state

