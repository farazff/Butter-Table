from copy import copy, deepcopy

from NodeAStar import NodeAStar
from State import State


def heuristicWithoutButter(state, butterNum, side):
    buttersLoc = state.getButters()[butterNum].getLocation()
    b0 = buttersLoc[0]
    b1 = buttersLoc[1]
    if side == 1:
        b1 = b1 - 1
    if side == 2:
        b0 = b0 - 1
    if side == 3:
        b1 = b1 + 1
    if side == 4:
        b0 = b0 + 1
    robotsLoc = state.getRobot().getLocation()
    return abs(b0 - robotsLoc[0]) + abs(b1 - robotsLoc[1])


class GraphOperationsAStar:
    def __init__(self, blocks, butters, robot, persons):
        self.blocks = blocks
        self.__butters = butters
        self.robot = robot
        self.__persons = persons
        self.__canPush = False

    def goal(self, wantedButter, whichSide, currentState):  # which side ->   1:left   2:up   3:right    4:down
        whichSide = int(whichSide)
        robotsLocation = currentState.getRobot().getLocation()
        wantedButtersLocation = wantedButter.getLocation()
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

        robotsLocation = currentNode.getState().getRobot().getLocation()

        #   |_1_|_2_|_3_|
        #   |_8_|___|_4_|
        #   |_7_|_6_|_5_|
        successorList = []
        for i in range(1, 9):
            if i == 2 or i == 4 or i == 6 or i == 8:
                if self.blocks[self.neighbourProducer(i, robotsLocation)[0]][
                    self.neighbourProducer(i, robotsLocation)[1]].getHaveObstacle() or \
                        self.blocks[self.neighbourProducer(i, robotsLocation)[0]][
                            self.neighbourProducer(i, robotsLocation)[1]].getHaveButter():
                    continue
                robotTemp = copy(self.robot)
                robotTemp.setLocation(self.neighbourProducer(i, robotsLocation))
                cost = self.blocks[robotTemp.getLocation()[0]][robotTemp.getLocation()[1]].getCost()
                successorList.append(
                    NodeAStar(State(robotTemp, self.__butters), currentNode, currentNode.cost + cost))
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

    def AStar(self, state, wantedButter, whichSide):
        explored = {state.getRobot().getLocation(): 1}
        fringe = [NodeAStar(copy(state), None, 0)]
        n = fringe[0]
        if self.goal(wantedButter, whichSide, n.getState()):
            returnAns = (copy(n), "")
            return returnAns

        while True:
            if len(fringe) == 0:
                return None
            bestPath = min(i.cost + heuristicWithoutButter(i.getState(), wantedButter.getNum(), whichSide) for i in fringe)
            for i in range(len(fringe)):
                now = fringe[i]
                temp = now.cost + heuristicWithoutButter(now.getState(), wantedButter.getNum(), whichSide)
                if temp == bestPath:
                    n = fringe.pop(i)
                    break

            if self.goal(wantedButter, whichSide, n.getState()):
                t = n
                ans = ""
                now = t.getState().getRobot().getLocation()
                t = t.getParent()
                while t is not None:
                    past = t.getState().getRobot().getLocation()
                    if now[1] - past[1] == 1:
                        ans = "R" + ans
                    if now[1] - past[1] == -1:
                        ans = "L" + ans
                    if now[0] - past[0] == 1:
                        ans = "D" + ans
                    if now[0] - past[0] == -1:
                        ans = "U" + ans
                    now = copy(past)
                    t = t.getParent()
                print(ans)
                returnAns = (copy(n), ans)
                return returnAns
            explored[n.getState().getRobot().getLocation()] = 1

            successor = self.successor(n)
            for i in range(len(successor)):
                newN = deepcopy(successor[i])
                t = copy(n)
                isOK = True
                while t is not None:
                    if t.getState().getRobot().getLocation() == newN.getState().getRobot().getLocation():
                        isOK = False
                        break
                    t = copy(t.getParent())
                if explored.get(newN.getState().getRobot().getLocation()) == 1:
                    isOK = False
                if isOK:
                    fringe.append(newN)

    # def heuristicWithButter(self, state, butterNum, personNum, side):
    #     buttersLoc = state.getButters()[butterNum].getLocation()
    #     personsLoc = self.__persons[personNum].getLocation()
    #     return abs(buttersLoc[0] - personsLoc[0]) + abs(buttersLoc[1] - personsLoc[1])


    # def goalWithButter(self, whichPerson, wantedButter):
    #     personsLocation = whichPerson.getLocation()
    #     wantedButtersLocation = wantedButter.getLocation()
    #     if personsLocation[0] == wantedButtersLocation[0] and personsLocation[1] == wantedButtersLocation[1]:
    #         return True
    #     return False
    #
    # def successorWithButter(self, currentNode, wantedButterNumber):
    #     robotsLocation = currentNode.getState().getRobot().getLocation()
    #     wantedButtersLocation = currentNode.getState().getButters()[wantedButterNumber].getLocation()
    #     # wantedButtersLocation = wantedButter.getLocation()
    #     whichNeighbours = []
    #     pushList = []
    #     successorList = []
    #
    #     if self.neighbourProducer(1, wantedButtersLocation) == robotsLocation:
    #         self.__canPush = True
    #         whichNeighbours.append(2)
    #         whichNeighbours.append(8)
    #     elif self.neighbourProducer(2, wantedButtersLocation) == robotsLocation:
    #         whichNeighbours.append(1)
    #         whichNeighbours.append(3)
    #         pushList.append(6)
    #     elif self.neighbourProducer(3, wantedButtersLocation) == robotsLocation:
    #         self.__canPush = True
    #         whichNeighbours.append(2)
    #         whichNeighbours.append(4)
    #     elif self.neighbourProducer(4, wantedButtersLocation) == robotsLocation:
    #         whichNeighbours.append(3)
    #         whichNeighbours.append(5)
    #         pushList.append(8)
    #     elif self.neighbourProducer(5, wantedButtersLocation) == robotsLocation:
    #         self.__canPush = True
    #         whichNeighbours.append(4)
    #         whichNeighbours.append(6)
    #     elif self.neighbourProducer(6, wantedButtersLocation) == robotsLocation:
    #         whichNeighbours.append(5)
    #         whichNeighbours.append(7)
    #         pushList.append(2)
    #     elif self.neighbourProducer(7, wantedButtersLocation) == robotsLocation:
    #         self.__canPush = True
    #         whichNeighbours.append(6)
    #         whichNeighbours.append(8)
    #     elif self.neighbourProducer(8, wantedButtersLocation) == robotsLocation:
    #         whichNeighbours.append(1)
    #         whichNeighbours.append(7)
    #         pushList.append(4)
    #
    #     for i in whichNeighbours:
    #         if not self.blocks[self.neighbourProducer(i, wantedButtersLocation)[0]][
    #             self.neighbourProducer(i, wantedButtersLocation)[1]].getHaveObstacle() or \
    #                 self.blocks[self.neighbourProducer(i, wantedButtersLocation)[0]][
    #                     self.neighbourProducer(i, wantedButtersLocation)[1]].getHaveButter():
    #             robotTemp = copy(self.robot)
    #             robotTemp.setLocation(self.neighbourProducer(i, wantedButtersLocation))
    #             successorList.append(Node(State(robotTemp, copy(currentNode.getState().getButters())), currentNode, 0))
    #
    #     for i in pushList:
    #         if not self.blocks[self.neighbourProducer(i, wantedButtersLocation)[0]][
    #             self.neighbourProducer(i, wantedButtersLocation)[1]].getHaveObstacle() or \
    #                 self.blocks[self.neighbourProducer(i, wantedButtersLocation)[0]][
    #                     self.neighbourProducer(i, wantedButtersLocation)[1]].getHaveButter():
    #             robotTemp = copy(self.robot)
    #             robotTemp.setLocation(wantedButtersLocation)
    #             buttersTemp = []
    #             for j in currentNode.getState().getButters():
    #                 buttersTemp.append(copy(j))
    #             buttersTemp[wantedButterNumber].setLocation(self.neighbourProducer(i, wantedButtersLocation))
    #             successorList.append(Node(State(robotTemp, buttersTemp), currentNode, 0))
    #
    #     return successorList  # this list contains the nodes required for rotation and the nodes for pushing
    #     # wantedButter

    # def IDSWithButter(self, state, butterNUM, person):
    #     for limit in range(15):
    #         # print("__________________________________________",limit)
    #         fringe = [Node(state, None, 0)]
    #         ans = self.DLSWithButter(limit, fringe, butterNUM, person)
    #         if ans is not None:
    #             return ans
    #     return None
    #
    # def DLSWithButter(self, limit, fringe, butterNUM, person):
    #     n = fringe[0]
    #     if self.goalWithButter(person, n.getState().getButters()[butterNUM]):
    #         returnAns = (copy(n), "ans")
    #         return returnAns
    #     visited = {(n.getState().getRobot().getLocation(), n.getState().getButters()[butterNUM].getLocation()): 1}
    #     while True:
    #         if len(fringe) == 0:
    #             return None
    #         # print(end="\n\n")
    #         # print("fringe: ", end="  ")
    #         # for i in range(len(fringe)):
    #         #     print(fringe[i].getState().getRobot().getLocation(), end=", ")
    #         # print()
    #         n = fringe.pop(0)
    #
    #         # print('selected : {}'.format(n.getState().getRobot().getLocation()))
    #         # print(n.getState().getRobot().getLocation(),
    #         #       n.getState().getButters()[butterNUM].getLocation())
    #         level = n.depth
    #         if level > int(limit):
    #             continue
    #         self.__canPush = False
    #         successor = self.successorWithButter(copy(n), butterNUM)
    #         # if not self.__canPush:
    #         #      successor.extend(self.successorTemp(n, butterNUM))
    #         for i in range(len(successor)):
    #             isOK = True
    #             newN = Node(successor[i].getState(), n, n.depth + 1)
    #
    #             if visited.get((newN.getState().getRobot().getLocation(),
    #                             newN.getState().getButters()[butterNUM].getLocation())) == 1:
    #                 continue
    #             visited[(newN.getState().getRobot().getLocation(),
    #                      newN.getState().getButters()[butterNUM].getLocation())] = 1
    #             # print(newN.getState().getRobot().getLocation(),
    #             #       newN.getState().getButters()[butterNUM].getLocation())
    #             # print(newN.getState().getRobot().getLocation(), " ",
    #             #       newN.getState().getButters()[butterNUM].getLocation())
    #             if isOK:
    #                 if self.goalWithButter(person, newN.getState().getButters()[butterNUM]):
    #                     t = newN
    #                     ans = ""
    #                     now = t.getState().getRobot().getLocation()
    #                     # print(now)
    #                     t = t.getParent()
    #                     while t is not None:
    #                         # print(t.getState().getRobot().getLocation())
    #                         past = t.getState().getRobot().getLocation()
    #                         if now[1] - past[1] == 1:
    #                             ans = "R" + ans
    #                         if now[1] - past[1] == -1:
    #                             ans = "L" + ans
    #                         if now[0] - past[0] == 1:
    #                             ans = "D" + ans
    #                         if now[0] - past[0] == -1:
    #                             ans = "U" + ans
    #                         now = copy(past)
    #                         t = t.getParent()
    #                     returnAns = (copy(newN), ans)
    #                     return returnAns
    #                 fringe.append(newN)
    #
    # def successorTemp(self, currentNode, butterNum):  # goal test must be on expansion time
    #
    #     robotsLocation = currentNode.getState().getRobot().getLocation()
    #     blocksTemp = deepcopy(self.blocks)
    #
    #     blocksTemp[self.__butters[butterNum].getLocation()[0]][
    #         self.__butters[butterNum].getLocation()[1]].setHaveButter(False)
    #
    #     blocksTemp[currentNode.getState().getButters()[butterNum].getLocation()[0]][
    #         currentNode.getState().getButters()[butterNum].getLocation()[1]].setHaveButter(True)
    #     #   |_1_|_2_|_3_|
    #     #   |_8_|___|_4_|
    #     #   |_7_|_6_|_5_|
    #     successorList = []
    #     for i in range(1, 9):
    #         if i == 2 or i == 4 or i == 6 or i == 8:
    #             if blocksTemp[self.neighbourProducer(i, robotsLocation)[0]][
    #                 self.neighbourProducer(i, robotsLocation)[1]].getHaveObstacle() or \
    #                     blocksTemp[self.neighbourProducer(i, robotsLocation)[0]][
    #                         self.neighbourProducer(i, robotsLocation)[1]].getHaveButter():
    #                 continue
    #             robotTemp = copy(self.robot)
    #             robotTemp.setLocation(self.neighbourProducer(i, robotsLocation))
    #             successorList.append(
    #                 Node(State(robotTemp, deepcopy(currentNode.getState().getButters())), currentNode, 0))
    #     return successorList