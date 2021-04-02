from copy import copy
from Node import Node
from State import State




class GraphOperations_BBFS:
    def __init__(self, blocks, persons):

        self.blocks = blocks
        self.__persons = persons



    def goal(self, whichButterNumber, currentState):
        if currentState.getButters()[whichButterNumber].getLocation() == currentState.getRobot().getLocation():
            return True
        return False



    #  if  robotOrButter  ==  True     : successor method act as  robots successor
    #  if  robotOrButter  ==  False    : successor method act as butters successor and you should enter whichButterNumber

    def successor(self, currentNode, robotOrButter, whichButterNumber):

        #   |_1_|_2_|_3_|
        #   |_8_|___|_4_|
        #   |_7_|_6_|_5_|

        successorList = []

        if robotOrButter:

            robotsLocation = currentNode.getState().getRobot().getLocation()

            for i in range(1, 9):
                if i % 2 == 0:
                    if self.blocks[self.neighbourProducer(i, robotsLocation)[0]][
                        self.neighbourProducer(i, robotsLocation)[1]].getHaveObstacle() or \
                            self.blocks[self.neighbourProducer(i, robotsLocation)[0]][
                                self.neighbourProducer(i, robotsLocation)[1]].getHaveButter():
                        continue
                        # print(self.neighbourProducer(i, robotsLocation)[0], end="  ")
                        # print(self.neighbourProducer(i, robotsLocation)[1])
                    robotTemp = copy(currentNode.getState().getRobot())
                    robotTemp.setLocation(self.neighbourProducer(i, robotsLocation))
                    # print(robotTemp.getLocation())
                    successorList.append(
                        Node(State(robotTemp, currentNode.getState().getButters()), currentNode))



        else:
            buttersLocation = currentNode.getState().getButters()[whichButterNumber].getLocation()

            for i in range(1, 9):
                if i % 2 == 0:
                    if self.blocks[self.neighbourProducer(i, buttersLocation)[0]][
                        self.neighbourProducer(i, buttersLocation)[1]].getHaveObstacle() or \
                            self.blocks[self.neighbourProducer(i, buttersLocation)[0]][
                                self.neighbourProducer(i, buttersLocation)[1]].getHaveButter():
                        continue
                        # print(self.neighbourProducer(i, buttersLocation)[0], end="  ")
                        # print(self.neighbourProducer(i, buttersLocation)[1])
                    buttersTemp=copy(currentNode.getState().getButters())
                    buttersTemp[whichButterNumber].setLocation(self.neighbourProducer(i, buttersLocation))
                    successorList.append(
                        Node(State(copy(currentNode.getState().getRobot()), buttersTemp), currentNode))

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
