from Butter import Butter
from Node import Node
from Robot import Robot
from State import State


class GraphOperations:
    def __init__(self, blocks, butters, robot, persons):
        self.__blocks = blocks
        self.__butters = butters
        self.__robot = robot
        self.__persons = persons

    def goal(self, wantedButter, whichSide, currentState):  # which side ->   1:left   2:up   3:right    4:down
        robotsLocation = currentState.get_robot().get_location()
        wantedButtersLocation = Butter(wantedButter).getLocation()[0]
        if whichSide == 1:
            if robotsLocation[0] == wantedButtersLocation[0] and \
                    robotsLocation[1] + 1 == wantedButtersLocation[1]:
                return True
        elif whichSide == 2:
            if robotsLocation[0] + 1 == wantedButtersLocation[0] and \
                    robotsLocation[1] == wantedButtersLocation[1]:
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
            if not self.__blocks[self.neighbourProducer(i, robotsLocation)[0]][
                self.neighbourProducer(i, robotsLocation)[1]].getHaveObstacle() or \
                    self.__blocks[self.neighbourProducer(i, robotsLocation)[0]][
                        self.neighbourProducer(i, robotsLocation)[1]].getHaveButter():
                print(self.neighbourProducer(i, robotsLocation)[0], end="  ")
                print(self.neighbourProducer(i, robotsLocation)[1])
                robotTemp = self.__robot
                robotTemp.set_location(self.neighbourProducer(i, robotsLocation))
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
        limit = int(0)

        while True:
            fringe = [Node(state, None)]
            if self.DLS(limit, fringe, wantedButter, whichSide):
                return True
            limit = limit + 1

    # def DLS(self, limit, fringe, wantedButter, whichSide):
    #     n = Node(list(fringe).pop())
    #     if self.goal(wantedButter, whichSide, n.getState()):
    #         return True
    #     while True:
    #         if len(fringe) == 0:
    #             return False
    #         n = Node(list(fringe).pop())
    #         s = State(n.getState())
    #         level = int(0)
    #         t = n
    #         while t is not None:
    #             t = t.getParent()
    #             level = level + 1
    #         if t >= limit:
    #             continue
    #         successor = self.successor(n)
    #         for i in range(len(successor)):
    #             newN = Node(successor[i].getState(), n)
    #             if self.goal(wantedButter, whichSide, newN.getState()):
    #                 return True
    #             fringe.append(newN)
