from base.Instruction import Instruction
from base.IntegerResult import IntegerResult
from base.Level import Level
from base.Qubit import Qubit


class Translate:
    N = 9999
    INFINITE = 9999
    Visited = 1

    def __init__(self):
        self.level = Level(-1)

    def insert_codes_qubit(self, a: Instruction, Q: set, qubits: list):
        for id in a.qubits:
            p = None
            for i in range(len(qubits)):
                if qubits[i].id == id:
                    p = qubits[i]
            if p == None:
                print('no quibit called id: ', id)
                continue
            Q.add(p)

    def find_next_level(self, qubits_set: set, l):
        min = Translate.INFINITE
        for it in qubits_set:
            for i in range(len(it.instructions)):
                instruction = it.instructions[i]
                if instruction.line > l and instruction.line < min:
                    min = instruction.line
                    break
        return min

    def Lexer(self, codes: list, qubits: list, total_qubit: int, total_instruction: int, bf):
        j = 1
        integerResult = IntegerResult()
        integerResult.total_qubit = total_qubit
        integerResult.total_instruction = total_instruction
        u = 0
        flag = True
        while flag:
            booleanResult = codes[j].input(u, j, qubits, bf)
            if booleanResult == None:
                return integerResult
            flag = booleanResult.flag
            j = booleanResult.index
            u = booleanResult.total_qubits
        total_instruction = j - 1
        total_qubit = u
        integerResult.total_instruction = total_instruction
        integerResult.total_qubit = total_qubit
        return integerResult

    def translate(self, tower: list, bf,linecount):
        codes = []
        qubits = []

        for i in range(linecount):
            qubits.append(Qubit(i))
            codes.append(Instruction())
        total_qubits = 0
        total_ins = 0
        integerResult = self.Lexer(codes=codes, qubits=qubits, total_qubit=total_qubits, total_instruction=total_ins,
                                   bf=bf)

        total_qubits = integerResult.total_qubit
        total_ins = integerResult.total_instruction
        total_level = self.level.levelize(tower, codes, qubits)
        for i in range(total_level + 1):
            if tower[i].is_operation == False:
                continue
            p = tower[i].head.next
            while p != None:
                if p.judgeQubits(qubits) == True:
                    p = p.next
                    continue
                p.setQubitsState(Translate.Visited, qubits)
                if p.mark == Translate.Visited:
                    p = p.next
                    continue
                ins_unit = []
                for j in range(total_ins):
                    ins_unit.append(p)
                unit_begin = 1
                p.mark = Translate.Visited
                qubits_set = set()
                self.insert_codes_qubit(p, qubits_set, qubits)
                p = p.next
                cur_level = i
                while len(qubits_set) < total_qubits:
                    tmp_level = self.find_next_level(qubits_set, cur_level)
                    if tmp_level - self.INFINITE == 0:
                        break
                    cur_level = tmp_level
                    nex_instruction = tower[cur_level].find_overlap_instruction(qubits_set, qubits)
                    nex_instruction.mark = self.Visited

                    ins_unit[unit_begin] = nex_instruction
                    unit_begin += 1
                    self.insert_codes_qubit(nex_instruction, qubits_set, qubits)
                cur_level = ins_unit[unit_begin - 1].line
                unit_begin -= 1
                for u in range(unit_begin - 1, -1, -1):
                    ins = ins_unit[u]
                    l = ins.line
                    if l == cur_level - unit_begin + u:
                        continue
                    tower[l].delInstr(ins)
                    tower[cur_level - unit_begin + u].insertInstr(ins)
                    ins.line = cur_level - unit_begin + u
        return total_level
