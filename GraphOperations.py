from Butter import Butter
from Person import Person
from Node import Node
from State import State
from Robot import Robot
from Block import Block


class GraphOperations:
    def __init__(self, blocks, butters, robot, persons):
        self.__blocks = blocks
        self.__butters = butters
        self.__robot = robot
        self.__persons = persons

    def goal(self, wantedButter, whichSide, currentState):  # which side ->   1:left   2:up   3:right    4:down
        robotsLocation = Robot(State(currentState).get_robot()).get_location()
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
        robotsLocation = Robot(State(Node(currentNode).getState()).get_robot()).get_location()

        #   |_1_|_2_|_3_|
        #   |_8_|___|_4_|
        #   |_7_|_6_|_5_|
        successorList = []
        for i in range(1, 9):
            if not Block(self.__blocks[self.neighbourProducer(i, robotsLocation)]).getHaveObstacle() or \
                    Block(self.__blocks[self.neighbourProducer(i, robotsLocation)]).getHaveButter():
                successorList.append(
                    Node(State(Robot(self.__robot).set_location(self.neighbourProducer(i)), self.__butters),
                         Node(currentNode)))
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

            return (robotsLocation[0] + yStep, robotsLocation[1] + xStep)
