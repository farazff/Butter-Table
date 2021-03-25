from copy import copy
from Node import Node
from State import State


class GraphOperations:
    def __init__(self, blocks, butters, robot, persons):
        self.__blocks = blocks
        self.__butters = butters
        self.__robot = robot
        self.__persons = persons

    def goal(self, wantedButter, whichSide, currentState):  # which side ->   1:left   2:up   3:right    4:down
        whichSide = int(whichSide)
        robotsLocation = currentState.get_robot().get_location()
        wantedButtersLocation = wantedButter.getLocation()
        print('wanted: {} , current: {}'.format(wantedButtersLocation, robotsLocation))
        if whichSide == 1:
            if robotsLocation[0] == wantedButtersLocation[0] and \
                    robotsLocation[1] + 1 == wantedButtersLocation[1]:
                return True
        elif whichSide == 2:
            if int(int(robotsLocation[0]) + 1) == int(wantedButtersLocation[0]) and \
                    int(robotsLocation[1]) == int(wantedButtersLocation[1]):
                return True
        elif whichSide == 3:
            if robotsLocation[0] == wantedButtersLocation[0] and \
                    robotsLocation[1] - 1 == wantedButtersLocation[1]:
                return True
        elif whichSide == 4:
            if robotsLocation[0] - 1 == wantedButtersLocation[0] and \
                    robotsLocation[1] == wantedButtersLocation[1]:
                return True
        return False

    def successor(self, currentNode):  # goal test must be on expansion time

        robotsLocation = currentNode.getState().get_robot().get_location()

        #   |_1_|_2_|_3_|
        #   |_8_|___|_4_|
        #   |_7_|_6_|_5_|
        successorList = []
        for i in range(1, 9):
            if i == 2 or i == 4 or i == 6 or i == 8:
                if not self.__blocks[self.neighbourProducer(i, robotsLocation)[0]][
                    self.neighbourProducer(i, robotsLocation)[1]].getHaveObstacle() or \
                        self.__blocks[self.neighbourProducer(i, robotsLocation)[0]][
                            self.neighbourProducer(i, robotsLocation)[1]].getHaveButter():
                    # print(self.neighbourProducer(i, robotsLocation)[0], end="  ")
                    # print(self.neighbourProducer(i, robotsLocation)[1])
                    robotTemp = copy(self.__robot)
                    robotTemp.set_location(self.neighbourProducer(i, robotsLocation))
                    # print(robotTemp.get_location())
                    successorList.append(
                        Node(State(robotTemp, self.__butters), currentNode))
        return successorList

    def neighbourProducer(self, whichSide, robotsLocation):
        xStep = yStep = 0
        if whichSide == 1:
            xStep = -1
            yStep = -1
        elif whichSide == 2:
            yStep = -1
        elif whichSide == 3:
            xStep = 1
            yStep = -1
        elif whichSide == 4:
            xStep = 1
        elif whichSide == 5:
            xStep = 1
            yStep = 1
        elif whichSide == 6:
            yStep = 1
        elif whichSide == 7:
            xStep = -1
            yStep = 1
        elif whichSide == 8:
            xStep = -1

        return robotsLocation[0] + yStep, robotsLocation[1] + xStep

    def IDS(self, state, wantedButter, whichSide):
        for limit in range(6):
            fringe = [Node(state, None)]
            if self.DLS(limit, fringe, wantedButter, whichSide):
                return True

    def DLS(self, limit, fringe, wantedButter, whichSide):

        visited = {}
        n = list(fringe)[0]
        if self.goal(wantedButter, whichSide, n.getState()):
            return True

        while True:
            if len(fringe) == 0:
                print("finished\n\n\n")
                return False
            print("fringe: ", end="  ")
            for i in range(len(fringe)):
                print(fringe[i].getState().get_robot().get_location(), end=", ")
            print()
            n = fringe.pop()
            visited[n.getState().get_robot().get_location()] = 1
            print('selected : {}'.format(n.getState().get_robot().get_location()))
            level = int(-1)
            t = n
            while t is not None:
                t = t.getParent()
                level = level + 1
            if level > int(limit):
                continue
            successor = self.successor(n)
            for i in range(len(successor)):
                newN = Node(successor[i].getState(), n)
                if visited.get(newN.getState().get_robot().get_location()) == 1:
                    continue
                if self.goal(wantedButter, whichSide, newN.getState()):
                    t = newN
                    while t is not None:
                        print(t.getState().get_robot().get_location())
                        t = t.getParent()
                    return True
                fringe.append(newN)
