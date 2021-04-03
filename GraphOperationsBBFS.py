from copy import copy
from Node import Node
from State import State


class GraphOperationsBBFS:
    def __init__(self, blocks, persons):

        self.blocks = blocks
        self.__persons = persons

    def goalAlone(self, whichButterNumber, currentState):
        if currentState.getButters()[whichButterNumber].getLocation() == currentState.getRobot().getLocation():
            return True
        return False

    # if  robotOrButter  ==  True : successor method act as robots successor if  robotOrButter  ==  False:
    # successor method act as butters successor and you should enter whichButterNumber

    def successorAlone(self, currentNode, robotOrButter, whichButterNumber):

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
                    # for t in successorList:
                    #     print((t.getState().getRobot().getLocation()))
                    # print(self.neighbourProducer(i, buttersLocation)[0], end="  ")
                    # print(self.neighbourProducer(i, buttersLocation)[1])
                    buttersTemp = []
                    for j in currentNode.getState().getButters():
                        buttersTemp.append(copy(j))
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

    def BBFSAlone(self, state, wantedButter, side):
        fringe_robot = []
        fringe_butter = []
        state_temp = copy(state)
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
        fringe_robot.append(Node(state, None))
        fringe_butter.append(Node(state_temp, None))
        # TODO: check if first state is goal :)
        for round in range(1, 4):
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
                    if now_depth > int(round):
                        # print("Robot - finished round {}".format(round))
                        break
                    fringe_robot.pop(0)
                    successor = self.successorAlone(n, True, wantedButter.getNum())
                    # print("Robot - Successor of {}: ".format(n.getState().getRobot().getLocation()))
                    for i in successor:
                        newN = Node(i.getState(), copy(n))
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
                        temp_node = copy(r)
                        while temp_node is not None:
                            ans.insert(0, temp_node.getState().getRobot().getLocation())
                            temp_node = temp_node.getParent()
                        temp_node = copy(b)
                        while temp_node is not None:
                            ans.append(temp_node.getState().getButters()[wantedButter.getNum()].getLocation())
                            temp_node = temp_node.getParent()
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
                    if now_depth > int(round):
                        # print("Butter - finished round {}".format(round))
                        break
                    fringe_butter.pop(0)
                    successor = self.successorAlone(n, False, wantedButter.getNum())
                    # print("Butter - Successor of {}: ".format(n.getState().getButters()[0].getLocation()))
                    for i in successor:
                        newN = Node(i.getState(), n)
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
                        temp_node = copy(r)
                        while temp_node is not None:
                            ans.insert(0, temp_node.getState().getRobot().getLocation())
                            temp_node = temp_node.getParent()
                        temp_node = copy(b)
                        while temp_node is not None:
                            ans.append(temp_node.getState().getButters()[wantedButter.getNum()].getLocation())
                            temp_node = temp_node.getParent()
                        print("Answer:")
                        for q in ans:
                            print(q)
                        return True

    def goal_Both(self):
        pass
        # TODO: goal function when butter is with robot

    def successorPush(self):
        pass
        # TODO: successor function when robot is pushing butter

    def successorPull(self):
        pass
        # TODO: successor function when robot is pulling butter
