class Edge:
    source = -1
    target = -1
    weight = 1.0
    degree = 0
    choosed_weight = 1

    def Edge(self, e):
        self.source = e.source
        self.target = e.target
        self.weight = e.weight
        self.degree = e.degree

    def Edge(self):
        print(" Edge()")

    def toString(self):
        return "Edge{source=%s, target=%s , weight=%s, degree=%s }"%(self.source, self.target,self.weight,self.degree)

    def equals(self, o):
        if (self == o):
            return True
        if o == None or self.__class__ != o.__class__:
            return False
        return self.source == o.source and self.target == o.target

    def compareTo(self, o):
        res = self.source + self.target - (o.source + o.target)
        if res == 0:
            x = self.source - o.source
            if x == 0:
                return self.target - o.target
            return x
        return res
