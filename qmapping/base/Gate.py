class Gate:
    target = -1
    control = -1
    type = ""
    angle = 0.0
    last_subscore = 9999999
    subscore = 0.0

    def Gate(self):
        pass

    def Gate(self, g: Gate):
        self.target = g.target
        self.control = g.control
        self.type = g.type
        self.angle = g.angle