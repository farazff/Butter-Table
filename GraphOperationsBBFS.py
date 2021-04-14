from copy import copy, deepcopy
from NodeBBFS import NodeBBFS
from State import State


class GraphOperationsBBFS:
    def __init__(self, blocks, persons, butters):

        self.blocks = blocks
        self.__persons = persons
        self.__butters = butters

    # if  robotOrButter  ==  True : successor method act as robots successor if  robotOrButter  ==  False:
    # successor method act as butters successor and you should enter whichButterNumber

    def successorAlone(self, currentNodeBBFS, robotOrButter, whichButterNumber):

        #   |_1_|_2_|_3_|
        #   |_8_|___|_4_|
        #   |_7_|_6_|_5_|

        successorList = []

        if robotOrButter:

            robotsLocation = currentNodeBBFS.getState().getRobot().getLocation()

            for i in range(1, 9):
                if i % 2 == 0:
                    if self.blocks[self.neighbourProducer(i, robotsLocation)[0]][
                        self.neighbourProducer(i, robotsLocation)[1]].getHaveObstacle() or \
                            self.blocks[self.neighbourProducer(i, robotsLocation)[0]][
                                self.neighbourProducer(i, robotsLocation)[1]].getHaveButter():
                        continue
                        # print(self.neighbourProducer(i, robotsLocation)[0], end="  ")
                        # print(self.neighbourProducer(i, robotsLocation)[1])
                    robotTemp = copy(currentNodeBBFS.getState().getRobot())
                    robotTemp.setLocation(self.neighbourProducer(i, robotsLocation))
                    # print(robotTemp.getLocation())
                    successorList.append(
                        NodeBBFS(State(robotTemp, currentNodeBBFS.getState().getButters()), currentNodeBBFS))
        else:
            buttersLocation = currentNodeBBFS.getState().getButters()[whichButterNumber].getLocation()

            for i in range(1, 9):
                if i % 2 == 0:
                    if self.blocks[self.neighbourProducer(i, buttersLocation)[0]][
                        self.neighbourProducer(i, buttersLocation)[1]].getHaveObstacle() or \
                            self.blocks[self.neighbourProducer(i, buttersLocation)[0]][
                                self.neighbourProducer(i, buttersLocation)[1]].getHaveButter():
                        continue
                    # for t in successorList:
                    #     print((t.getState().getRobot().getLocation()))
                    # print(self.neighbourProducer(i, buttersLocation)[0], end="  ")
                    # print(self.neighbourProducer(i, buttersLocation)[1])
                    buttersTemp = []
                    for j in currentNodeBBFS.getState().getButters():
                        buttersTemp.append(copy(j))
                    buttersTemp[whichButterNumber].setLocation(self.neighbourProducer(i, buttersLocation))
                    successorList.append(
                        NodeBBFS(State(copy(currentNodeBBFS.getState().getRobot()), buttersTemp), currentNodeBBFS))

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

    def BBFSAlone(self, state, wantedButter, side):
        fringe_robot = []
        fringe_butter = []
        state_temp = deepcopy(state)
        height = wantedButter.getLocation()[0]
        length = wantedButter.getLocation()[1]
        if side == 1:
            state_temp.getButters()[wantedButter.getNum()].setLocation((height, length - 1))
        if side == 2:
            state_temp.getButters()[wantedButter.getNum()].setLocation((height - 1, length))
        if side == 3:
            state_temp.getButters()[wantedButter.getNum()].setLocation((height, length + 1))
        if side == 4:
            state_temp.getButters()[wantedButter.getNum()].setLocation((height + 1, length))
        visited_robot = {state.getRobot().getLocation(): 1}
        visited_butter = {wantedButter.getLocation(): 1,
                          state_temp.getButters()[wantedButter.getNum()].getLocation(): 1}
        fringe_robot.append(NodeBBFS(state, None))
        fringe_butter.append(NodeBBFS(state_temp, None))
        for phase in range(1, 8):
            if len(fringe_butter) == 0 or len(fringe_robot) == 0:
                return None
            if len(fringe_robot) != 0:
                while True:
                    n = fringe_robot[0]
                    temp = copy(n)
                    now_depth = int(0)
                    while temp is not None:
                        temp = temp.getParent()
                        now_depth = now_depth + int(1)
                    if now_depth > int(phase):
                        # print("Robot - finished phase {}".format(phase))
                        break
                    fringe_robot.pop(0)
                    successor = self.successorAlone(n, True, wantedButter.getNum())
                    # print("Robot - Successor of {}: ".format(n.getState().getRobot().getLocation()))
                    for i in successor:
                        newN = NodeBBFS(i.getState(), copy(n))
                        if visited_robot.get(newN.getState().getRobot().getLocation()) == 1:
                            continue
                        visited_robot[newN.getState().getRobot().getLocation()] = 1
                        # print(i.getState().getRobot().getLocation())
                        # if self.goal(wantedButter.getNum(), newN.getState()):
                        #     t = copy(newN)
                        #     print("Answer:")
                        #     while t is not None:
                        #         print(t.getState().getRobot().getLocation())
                        #         t = t.getParent()
                        #     return True
                        fringe_robot.append(newN)
            for r in fringe_robot:
                for b in fringe_butter:
                    if r.getState().getRobot().getLocation() == b.getState().getButters()[
                        wantedButter.getNum()].getLocation():
                        ans = []
                        temp_NodeBBFS = copy(r)
                        while temp_NodeBBFS is not None:
                            ans.insert(0, temp_NodeBBFS.getState().getRobot().getLocation())
                            temp_NodeBBFS = temp_NodeBBFS.getParent()
                        temp_NodeBBFS = copy(b)
                        while temp_NodeBBFS is not None:
                            ans.append(temp_NodeBBFS.getState().getButters()[wantedButter.getNum()].getLocation())
                            temp_NodeBBFS = temp_NodeBBFS.getParent()
                        print("Answer:")
                        for q in ans:
                            print(q)
                        return True

            if len(fringe_butter) != 0:
                while True:
                    n = fringe_butter[0]
                    temp = copy(n)
                    now_depth = int(0)
                    while temp is not None:
                        temp = temp.getParent()
                        now_depth = now_depth + int(1)
                    if now_depth > int(phase):
                        # print("Butter - finished phase {}".format(phase))
                        break
                    fringe_butter.pop(0)
                    successor = self.successorAlone(n, False, wantedButter.getNum())
                    # print("Butter - Successor of {}: ".format(n.getState().getButters()[0].getLocation()))
                    for i in successor:
                        newN = NodeBBFS(i.getState(), n)
                        if visited_butter.get(newN.getState().getButters()[0].getLocation()) == 1:
                            continue
                        visited_butter[newN.getState().getButters()[0].getLocation()] = 1
                        # print(i.getState().getButters()[0].getLocation())
                        # if self.goal(wantedButter.getNum(), newN.getState()):
                        #     t = copy(newN)
                        #     print("answer:")
                        #     while t is not None:
                        #         print(t.getState().getButters()[0].getLocation())
                        #         t = t.getParent()
                        #     return True
                        fringe_butter.append(newN)
            for r in fringe_robot:
                for b in fringe_butter:
                    if r.getState().getRobot().getLocation() == b.getState().getButters()[
                            wantedButter.getNum()].getLocation():
                        ans = []
                        temp_NodeBBFS = copy(r)
                        while temp_NodeBBFS is not None:
                            ans.insert(0, temp_NodeBBFS.getState().getRobot().getLocation())
                            temp_NodeBBFS = temp_NodeBBFS.getParent()
                        temp_NodeBBFS = copy(b)
                        while temp_NodeBBFS is not None:
                            ans.append(temp_NodeBBFS.getState().getButters()[wantedButter.getNum()].getLocation())
                            temp_NodeBBFS = temp_NodeBBFS.getParent()
                        print("Answer:")
                        for q in ans:
                            print(q)
                        return True

    def successorPush(self, currentNode, whichButterNumber):
        robotsLocation = currentNode.getState().getRobot().getLocation()
        wantedButtersLocation = currentNode.getState().getButters()[whichButterNumber].getLocation()
        whichNeighbours = []
        pushList = []
        successorList = []

        if self.neighbourProducer(1, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(2)
            whichNeighbours.append(8)
        elif self.neighbourProducer(2, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(1)
            whichNeighbours.append(3)
            pushList.append(6)
        elif self.neighbourProducer(3, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(2)
            whichNeighbours.append(4)
        elif self.neighbourProducer(4, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(3)
            whichNeighbours.append(5)
            pushList.append(8)
        elif self.neighbourProducer(5, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(4)
            whichNeighbours.append(6)
        elif self.neighbourProducer(6, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(5)
            whichNeighbours.append(7)
            pushList.append(2)
        elif self.neighbourProducer(7, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(6)
            whichNeighbours.append(8)
        elif self.neighbourProducer(8, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(1)
            whichNeighbours.append(7)
            pushList.append(4)

        for i in whichNeighbours:
            if not self.blocks[self.neighbourProducer(i, wantedButtersLocation)[0]][
                self.neighbourProducer(i, wantedButtersLocation)[1]].getHaveObstacle() or \
                    self.blocks[self.neighbourProducer(i, wantedButtersLocation)[0]][
                        self.neighbourProducer(i, wantedButtersLocation)[1]].getHaveButter():
                robotTemp = copy(currentNode.getState().getRobot())
                robotTemp.setLocation(self.neighbourProducer(i, wantedButtersLocation))
                successorList.append(NodeBBFS(State(robotTemp, copy(currentNode.getState().getButters())), currentNode))

        for i in pushList:
            if not self.blocks[self.neighbourProducer(i, wantedButtersLocation)[0]][
                self.neighbourProducer(i, wantedButtersLocation)[1]].getHaveObstacle() or \
                    self.blocks[self.neighbourProducer(i, wantedButtersLocation)[0]][
                        self.neighbourProducer(i, wantedButtersLocation)[1]].getHaveButter():
                robotTemp = copy(currentNode.getState().getRobot())
                robotTemp.setLocation(wantedButtersLocation)

                buttersTemp = []
                for j in currentNode.getState().getButters():
                    buttersTemp.append(copy(j))
                buttersTemp[whichButterNumber].setLocation(self.neighbourProducer(i, wantedButtersLocation))
                successorList.append(NodeBBFS(State(robotTemp, buttersTemp), currentNode))

        return successorList

    def successorTemp(self, currentNode, butterNum):  # goal test must be on expansion time
        robotsLocation = currentNode.getState().getRobot().getLocation()
        blocksTemp = deepcopy(self.blocks)
        blocksTemp[self.__butters[butterNum].getLocation()[0]][
            self.__butters[butterNum].getLocation()[1]].setHaveButter(False)

        blocksTemp[currentNode.getState().getButters()[butterNum].getLocation()[0]][
            currentNode.getState().getButters()[butterNum].getLocation()[1]].setHaveButter(True)
        #   |_1_|_2_|_3_|
        #   |_8_|___|_4_|
        #   |_7_|_6_|_5_|
        successorList = []
        for i in range(1, 9):
            if i == 2 or i == 4 or i == 6 or i == 8:
                if blocksTemp[self.neighbourProducer(i, robotsLocation)[0]][
                    self.neighbourProducer(i, robotsLocation)[1]].getHaveObstacle() or \
                        blocksTemp[self.neighbourProducer(i, robotsLocation)[0]][
                            self.neighbourProducer(i, robotsLocation)[1]].getHaveButter():
                    continue
                robotTemp = copy(currentNode.getState().getRobot())
                robotTemp.setLocation(self.neighbourProducer(i, robotsLocation))
                successorList.append(
                    NodeBBFS(State(robotTemp, deepcopy(currentNode.getState().getButters())), currentNode))
        return successorList

    def successorPull(self, currentNode, whichButterNumber):
        robotsLocation = currentNode.getState().getRobot().getLocation()
        wantedButtersLocation = currentNode.getState().getButters()[whichButterNumber].getLocation()
        whichNeighbours = []
        pullList = []
        successorList = []

        if self.neighbourProducer(1, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(2)
            whichNeighbours.append(8)
        elif self.neighbourProducer(2, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(1)
            whichNeighbours.append(3)
            pullList.append(2)
        elif self.neighbourProducer(3, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(2)
            whichNeighbours.append(4)
        elif self.neighbourProducer(4, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(3)
            whichNeighbours.append(5)
            pullList.append(4)
        elif self.neighbourProducer(5, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(4)
            whichNeighbours.append(6)
        elif self.neighbourProducer(6, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(5)
            whichNeighbours.append(7)
            pullList.append(6)
        elif self.neighbourProducer(7, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(6)
            whichNeighbours.append(8)
        elif self.neighbourProducer(8, wantedButtersLocation) == robotsLocation:
            whichNeighbours.append(1)
            whichNeighbours.append(7)
            pullList.append(8)

        for i in whichNeighbours:
            if not self.blocks[self.neighbourProducer(i, wantedButtersLocation)[0]][
                self.neighbourProducer(i, wantedButtersLocation)[1]].getHaveObstacle() or \
                    self.blocks[self.neighbourProducer(i, wantedButtersLocation)[0]][
                        self.neighbourProducer(i, wantedButtersLocation)[1]].getHaveButter():
                robotTemp = copy(currentNode.getState().getRobot())
                robotTemp.setLocation(self.neighbourProducer(i, wantedButtersLocation))
                successorList.append(NodeBBFS(State(robotTemp, copy(currentNode.getState().getButters())), currentNode))

        for i in pullList:
            if not self.blocks[self.neighbourProducer(i, robotsLocation)[0]][
                self.neighbourProducer(i, robotsLocation)[1]].getHaveObstacle() or \
                    self.blocks[self.neighbourProducer(i, robotsLocation)[0]][
                        self.neighbourProducer(i, robotsLocation)[1]].getHaveButter():
                robotTemp = copy(currentNode.getState().getRobot())
                robotTemp.setLocation(self.neighbourProducer(i, robotsLocation))

                buttersTemp = []
                for j in currentNode.getState().getButters():
                    buttersTemp.append(copy(j))
                buttersTemp[whichButterNumber].setLocation(robotsLocation)

                successorList.append(NodeBBFS(State(robotTemp, buttersTemp), currentNode))

        return successorList

    def BBFSBoth(self, state, wantedButter, side, wantedPerson):
        fringe_robot = []
        # fringe_butter = []
        # state_temp = deepcopy(state)
        # height = wantedButter.getLocation()[0]
        # length = wantedButter.getLocation()[1]
        # if side == 1:
        #     state_temp.getButters()[wantedButter.getNum()].setLocation((height, length - 1))
        # if side == 2:
        #     state_temp.getButters()[wantedButter.getNum()].setLocation((height - 1, length))
        # if side == 3:
        #     state_temp.getButters()[wantedButter.getNum()].setLocation((height, length + 1))
        # if side == 4:
        #     state_temp.getButters()[wantedButter.getNum()].setLocation((height + 1, length))
        visited_robot = {(state.getRobot().getLocation(), state.getButters()[wantedButter.getNum()].getLocation()): 1}
        # visited_butter = {wantedButter.getLocation(): 1,
        #                   state_temp.getButters()[wantedButter.getNum()].getLocation(): 1}
        fringe_robot.append(NodeBBFS(state, None))
        # fringe_butter.append(NodeBBFS(state_temp, None))
        for phase in range(1, 15):
            # if len(fringe_butter) == 0 or len(fringe_robot) == 0:
            if len(fringe_robot) == 0:
                return None
            if len(fringe_robot) != 0:
                while True:
                    n = fringe_robot[0]
                    temp = copy(n)
                    now_depth = int(0)
                    while temp is not None:
                        temp = temp.getParent()
                        now_depth = now_depth + int(1)
                    if now_depth > int(phase):
                        print("Robot - finished phase {}".format(phase))
                        break
                    fringe_robot.pop(0)
                    successor = self.successorPush(n, wantedButter.getNum())
                    # print("Robot - Successor of {}: ".format(n.getState().getRobot().getLocation()))
                    for i in successor:
                        newN = NodeBBFS(i.getState(), copy(n))
                        if visited_robot.get((newN.getState().getRobot().getLocation(),
                                              newN.getState().getButters()[wantedButter.getNum()].getLocation())) == 1:
                            continue
                        visited_robot[(newN.getState().getRobot().getLocation(),
                                       newN.getState().getButters()[wantedButter.getNum()].getLocation())] = 1
                        print(i.getState().getRobot().getLocation(), " ",
                              i.getState().getButters()[wantedButter.getNum()].getLocation())
                        if newN.getState().getButters()[
                                wantedButter.getNum()].getLocation() == wantedPerson.getLocation():
                            t = copy(newN)
                            print("Answer:")
                            while t is not None:
                                print(t.getState().getRobot().getLocation())
                                t = t.getParent()
                            return True
                        fringe_robot.append(newN)

            # for r in fringe_robot:
            #     for b in fringe_butter:
            #         if r.getState().getRobot().getLocation() == b.getState().getButters()[
            #                 wantedButter.getNum()].getLocation():
            #             ans = []
            #             temp_NodeBBFS = copy(r)
            #             while temp_NodeBBFS is not None:
            #                 ans.insert(0, temp_NodeBBFS.getState().getRobot().getLocation())
            #                 temp_NodeBBFS = temp_NodeBBFS.getParent()
            #             temp_NodeBBFS = copy(b)
            #             while temp_NodeBBFS is not None:
            #                 ans.append(temp_NodeBBFS.getState().getButters()[wantedButter.getNum()].getLocation())
            #                 temp_NodeBBFS = temp_NodeBBFS.getParent()
            #             print("Answer:")
            #             for q in ans:
            #                 print(q)
            #             return True

            # if len(fringe_butter) != 0:
            #     while True:
            #         n = fringe_butter[0]
            #         temp = copy(n)
            #         now_depth = int(0)
            #         while temp is not None:
            #             temp = temp.getParent()
            #             now_depth = now_depth + int(1)
            #         if now_depth > int(phase):
            #             # print("Butter - finished phase {}".format(phase))
            #             break
            #         fringe_butter.pop(0)
            #         successor = self.successorAlone(n, False, wantedButter.getNum())
            #         # print("Butter - Successor of {}: ".format(n.getState().getButters()[0].getLocation()))
            #         for i in successor:
            #             newN = NodeBBFS(i.getState(), n)
            #             if visited_butter.get(newN.getState().getButters()[0].getLocation()) == 1:
            #                 continue
            #             visited_butter[newN.getState().getButters()[0].getLocation()] = 1
            #             # print(i.getState().getButters()[0].getLocation())
            #             # if self.goal(wantedButter.getNum(), newN.getState()):
            #             #     t = copy(newN)
            #             #     print("answer:")
            #             #     while t is not None:
            #             #         print(t.getState().getButters()[0].getLocation())
            #             #         t = t.getParent()
            #             #     return True
            #             fringe_butter.append(newN)
            # for r in fringe_robot:
            #     for b in fringe_butter:
            #         if r.getState().getRobot().getLocation() == b.getState().getButters()[
            #                 wantedButter.getNum()].getLocation():
            #             ans = []
            #             temp_NodeBBFS = copy(r)
            #             while temp_NodeBBFS is not None:
            #                 ans.insert(0, temp_NodeBBFS.getState().getRobot().getLocation())
            #                 temp_NodeBBFS = temp_NodeBBFS.getParent()
            #             temp_NodeBBFS = copy(b)
            #             while temp_NodeBBFS is not None:
            #                 ans.append(temp_NodeBBFS.getState().getButters()[wantedButter.getNum()].getLocation())
            #                 temp_NodeBBFS = temp_NodeBBFS.getParent()
            #             print("Answer:")
            #             for q in ans:
            #                 print(q)
            #             return True
