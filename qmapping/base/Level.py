from base.Instruction import Instruction
from base.Qubit import Qubit


class Level:
    N = 999999

    def __init__(self, id):
        self.id = id
        self.level_head = Instruction()
        self.head = self.level_head
        self.line = 0
        self.length = 0
        self.is_operation = True
        self.tail = self.head

    def insertInstr(self, a: Instruction):
        self.tail.next = a
        a.next = None
        self.tail = a

    def levelize(self, tower: list, codes: list, qubits: list):
        i = 2
        lastline = 1
        newline = 1
        while codes[lastline].line != 0:
            j = lastline
            # print('last ',lastline,' ',i)
            tower[newline].is_operation = codes[lastline].is_operation
            while j < i:
                if self.overlap(codes[i], codes[j], qubits):
                    break
                j+=1
            if j < i or codes[i].line == 0:
                j = lastline
                while j < i:
                    tower[newline].insertInstr(codes[j])
                    codes[j].line = newline
                    j += 1
                lastline = i
                tower[newline].line = newline
                newline += 1
            i+=1
        print('...')
        return newline - 1

    def overlap(self, a: Instruction, b: Instruction, qubits: list):
        if not a.is_operation or not b.is_operation:
            return True
        p=None
        for id in a.qubits:
            for i in range(len(qubits)):
                if qubits[i].id == id:
                    p = qubits[i]
            if p == None:
                print('no qubit called: ', id)
                return False
            for id1 in b.qubits:
                for i in range(len(qubits)):
                    if qubits[i].id == id1:
                        q = qubits[i]
                if q == None:
                    print('no qubit called: ', id)
                    return False
                if p == q:
                    return True
        return False

    def delInstr(self, a: Instruction):
        p = self.head
        while p.next != None:
            if p.next == a:
                break
            p = p.next
        if p.next == None:
            return
        if p.next == self.tail:
            self.tail = p
        p.next = p.next.next

    def find_overlap_instruction(self, Q: set, qubits: list) -> Instruction:
        p = self.head.next
        while p != None:
            for id in p.qubits:
                q=None
                for i in range(len(qubits)):
                    if qubits[i].id == id:
                        q = qubits[i]
                if q == None:
                    print('no qubit called: ', id)
                if q in Q:
                    return p
            p = p.next
        return None

    def printcode(self, writer):
        p = self.head.next
        print(self.line, ' : ')
        while p != None:
            p.printcode()
            print(' ')
            p = p.next
