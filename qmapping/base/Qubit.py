from base.Instruction import Instruction


class Qubit:
    def __init__(self, id):
        self.name = ''
        self.id = id
        self.sign = 0
        self.mark = 0
        self.instructions = []

    def insertInstr(self, n: Instruction):
        self.instructions.append(n)
