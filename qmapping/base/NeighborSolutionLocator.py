from queue import Queue
from operator import itemgetter, attrgetter


def compareKey(args):
    pass


def findBestNeighbor(neighborsSolutions: list, solutionsInTabu: list, type: int):
    for m in range(len(neighborsSolutions)):
        for n in range(len(solutionsInTabu)):
            if (neighborsSolutions[m].swapped_edge.source == solutionsInTabu[n].source and
                neighborsSolutions[m].swapped_edge.target == solutionsInTabu[n].target) \
                    or (neighborsSolutions[m].swapped_edge.target == solutionsInTabu[n].source \
                        and neighborsSolutions[m].swapped_edge.source == solutionsInTabu[n].target):
                neighborsSolutions[m].score += neighborsSolutions[len(neighborsSolutions) - 1].score
                neighborsSolutions[m].subscore += neighborsSolutions[len(neighborsSolutions) - 1].subscore
                # print(neighborsSolutions[m].swapped_edge.source,neighborsSolutions[m].swapped_edge.target)
    if neighborsSolutions == None or len(neighborsSolutions) <= 0:
        return None
    # for m in neighborsSolutions:
    #     print(m.swapped_edge.source,m.swapped_edge.target)
    neighborsSolutions = sorted(neighborsSolutions, key=lambda s: (s.score, s.subscore))
    # for m in neighborsSolutions:
    #     print(m.swapped_edge.source,m.swapped_edge.target)
    return neighborsSolutions[0]


def findAmnestyNeighbor(neighborsSolutions: list, solutionsInTabu: list, type: int):
    neighborsSolutions = sorted(neighborsSolutions, key=lambda s: (s.score, s.subscore))
    return neighborsSolutions[0]


def findCCABestNeighbor(neighborsSolutions: list, edgeInTabu: list):
    if neighborsSolutions == None or len(neighborsSolutions) <= 0:
        return None
    neighbors = [s for s in neighborsSolutions if s.swapped_edge in edgeInTabu]
    if neighbors == None or len(neighbors):
        return None
    neighbors = sorted(neighbors, key=lambda s: (s.score, s.subscore))

    return neighbors[0]


def findCCAAmnestyNeighbor(neighborsSolutions: list, edgesInTabu: Queue):
    neighborsSolutions = sorted(neighborsSolutions, key=lambda s: (s.score, s.subscore))
    return neighborsSolutions[0]
