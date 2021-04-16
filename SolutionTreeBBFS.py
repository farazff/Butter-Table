from copy import copy, deepcopy
from GraphOperationsBBFS import GraphOperationsBBFS
from PathNode import PathNode
from State import State


class SolutionTreeBBFS:

    def __init__(self, table, robot, butters, persons):
        self.__table = table
        self.__robot = robot
        self.__butters = butters
        self.__persons = persons
        self.__startingNodes = [
            PathNode(table, State(copy(robot), copy(butters)), None, None, "", 0, copy(self.__butters),
                     copy(self.__persons))]

    def start(self):
        finalList = []
        while len(self.__startingNodes) > 0:
            currentNode = self.__startingNodes.pop()
            if len(currentNode.getUnvisitedButters()) == 0:
                finalList.append(copy(currentNode))
                continue
            for b in currentNode.getUnvisitedButters():
                for p in currentNode.getUnvisitedPersons():
                    for sideButter in self.calculateEmptyAroundOfButter(b):
                        for sidePerson in self.calculateEmptyAroundOfPerson(p):

                            # sideButter = 3
                            # sidePerson = 4
                            graph = GraphOperationsBBFS(currentNode.table, self.__persons,
                                                        currentNode.getState().getButters())

                            part1 = graph.BBFSAlone(currentNode.getState(), b, sideButter)
                            if part1 is None:
                                continue
                            new_node1 = deepcopy(currentNode)
                            if sideButter == 1:
                                new_node1.getState().getRobot().setLocation(
                                    (b.getLocation()[0], b.getLocation()[1] - 1))
                            if sideButter == 2:
                                new_node1.getState().getRobot().setLocation(
                                    (b.getLocation()[0] - 1, b.getLocation()[1]))
                            if sideButter == 3:
                                new_node1.getState().getRobot().setLocation(
                                    (b.getLocation()[0], b.getLocation()[1] + 1))
                            if sideButter == 4:
                                new_node1.getState().getRobot().setLocation(
                                    (b.getLocation()[0] + 1, b.getLocation()[1]))

                            self.updateDataAfterSimpleBBFS(new_node1, currentNode.table, graph)

                            part2 = graph.BBFSBoth(new_node1.getState(), deepcopy(b), sidePerson, deepcopy(p))
                            if part2 is None:
                                continue
                            new_node2 = deepcopy(new_node1)

                            new_node2.getState().getButters()[b.getNum()].setLocation((p.getLocation()[0],
                                                                                       p.getLocation()[1]))
                            if sidePerson == 1:
                                new_node2.getState().getRobot().setLocation((p.getLocation()[0], p.getLocation()[1] - 1))
                            if sidePerson == 2:
                                new_node2.getState().getRobot().setLocation((p.getLocation()[0] - 1, p.getLocation()[1]))
                            if sidePerson == 3:
                                new_node2.getState().getRobot().setLocation((p.getLocation()[0], p.getLocation()[1] + 1))
                            if sidePerson == 4:
                                new_node2.getState().getRobot().setLocation((p.getLocation()[0] + 1, p.getLocation()[1]))

                            unvisited_butters = []
                            for i in currentNode.getUnvisitedButters():
                                if i != b:
                                    unvisited_butters.append(copy(i))
                            unvisited_persons = []
                            for i in currentNode.getUnvisitedPersons():
                                if i != p:
                                    unvisited_persons.append(copy(i))

                            blocksTemp = deepcopy(currentNode.table)
                            blocksTemp[b.getLocation()[0]][b.getLocation()[1]].setHaveButter(False)
                            blocksTemp[p.getLocation()[0]][p.getLocation()[1]].setHaveButter(True)

                            blocksTemp[new_node2.getState().getRobot().getLocation()[0]][
                                new_node2.getState().getRobot().getLocation()[1]].setHaveRobot(True)

                            blocksTemp[new_node1.getState().getRobot().getLocation()[0]][
                                new_node1.getState().getRobot().getLocation()[1]].setHaveRobot(False)

                            self.__startingNodes.append(
                                PathNode(blocksTemp, new_node2.getState(), b.getNum, p.getNum,
                                         currentNode.getPathString() + part1 + part2, 0, copy(unvisited_butters),
                                         copy(unvisited_persons)))
        # for i in finalList:
        #     print("Path = {}".format(i.getPathString()))

        if len(finalList) != 0:
            minPath = minLen = min(len(i.getPathString()) for i in finalList)
            for i in finalList:
                if len(i.getPathString()) == minLen:
                    minPath = i.getPathString()
                    print(minPath)
                    break

            f = open("output_files/outputs_BBFS.txt", "w")
            f.write(minPath + "\n" + str(minLen) + "\n" + str(minLen))
            f.close()
        else:
            f = open("output_files/outputs_BBFS.txt", "w")
            f.write("Impossible")
            f.close()

    def updateDataAfterSimpleBBFS(self, new_node1, table, graph):
        table[self.__robot.getLocation()[0]][self.__robot.getLocation()[1]].setHaveRobot(False)
        table[new_node1.getState().getRobot().getLocation()[0]][
            new_node1.getState().getRobot().getLocation()[1]].setHaveRobot(True)
        graph.blocks = deepcopy(self.__table)

    def calculateEmptyAroundOfButter(self, butter):
        ans = []
        length = butter.getLocation()[1]
        height = butter.getLocation()[0]
        if self.__table[height][length - 1].getHaveButter() or self.__table[height][length - 1].getHaveObstacle():
            pass
        else:
            ans.append(1)
        if self.__table[height - 1][length].getHaveButter() or self.__table[height - 1][length].getHaveObstacle():
            pass
        else:
            ans.append(2)
        if self.__table[height][length + 1].getHaveButter() or self.__table[height][length + 1].getHaveObstacle():
            pass
        else:
            ans.append(3)
        if self.__table[height + 1][length].getHaveButter() or self.__table[height + 1][length].getHaveObstacle():
            pass
        else:
            ans.append(4)
        return ans

    def calculateEmptyAroundOfPerson(self, person):
        ans = []
        length = person.getLocation()[1]
        height = person.getLocation()[0]
        if self.__table[height][length - 1].getHaveObstacle():
            pass
        else:
            ans.append(1)
        if self.__table[height - 1][length].getHaveObstacle():
            pass
        else:
            ans.append(2)
        if self.__table[height][length + 1].getHaveObstacle():
            pass
        else:
            ans.append(3)
        if self.__table[height + 1][length].getHaveObstacle():
            pass
        else:
            ans.append(4)
        return ans