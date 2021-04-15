from copy import copy
from GraphOperations import GraphOperations
from PathNode import PathNode
from State import State


class SolutionTreeIDS:

    def __init__(self, table, robot, butters, persons):
        self.__table = table
        self.__robot = robot
        self.__butters = butters
        self.__persons = persons
        self.__graph = GraphOperations(self.__table, self.__butters, self.__robot, self.__persons)
        self.__startingNodes = [
            PathNode(State(copy(robot), copy(butters)), None, None, "", 0, copy(self.__butters), copy(self.__persons))]

    def start(self):
        finalList = []
        while len(self.__startingNodes) > 0:
            currentNode = self.__startingNodes.pop()
            if len(currentNode.getUnvisitedButters()) == 0:
                finalList.append(copy(currentNode))
                continue
            for b in currentNode.getUnvisitedButters():
                for p in currentNode.getUnvisitedPersons():
                    for side in self.calculateEmptyAroundOfButter(b):
                        # print("butter = {} side = {}, person = {}".format(b.getLocation(), side, p.getLocation()))
                        # print("unvisited butters: ", end=" ")
                        # for i in currentNode.getUnvisitedButters():
                        #     print(i.getLocation(), end=",  ")
                        # print()
                        # print("unvisited persons: ", end=" ")
                        # for i in currentNode.getUnvisitedPersons():
                        #     print(i.getLocation(), end=",  ")
                        # print()
                        # print("Path = {}".format(currentNode.getPathString()))
                        # print("starting alone")
                        tup1 = self.__graph.IDS(currentNode.getState(), b, side)
                        # print("finish alone")
                        if tup1 is None:
                            continue
                        # print("hiii")
                        new_node = tup1[0]
                        self.updateDataAfterSimpleIDS(new_node)
                        # print("start both")
                        tup2 = self.__graph.IDSWithButter(new_node.getState(), b.getNum(), p)
                        # print("finish both")
                        if tup2 is None:
                            continue
                        new_node2 = tup2[0]
                        # print(tup1[1] + tup2[1])
                        # print("\n")

                        unvisited_butters = []
                        for i in currentNode.getUnvisitedButters():
                            if i != b:
                                unvisited_butters.append(copy(i))
                        unvisited_persons = []
                        for i in currentNode.getUnvisitedPersons():
                            if i != p:
                                unvisited_persons.append(copy(i))

                        self.__startingNodes.append(
                            PathNode(new_node2.getState(), b.getNum, p.getNum,
                                     currentNode.getPathString() + tup1[1] + tup2[1], 0, copy(unvisited_butters),
                                     copy(unvisited_persons)))
        # for q in finalList:
        #     print(q.getPathString())
        if len(finalList) != 0:
            minPath = minLen = min(len(i.getPathString()) for i in finalList)
            for i in finalList:
                if len(i.getPathString()) == minLen:
                    minPath = i.getPathString()
                    break

            f = open("output_files/outputs.txt", "w")
            f.write(minPath + "\n" + str(minLen) + "\n" + str(minLen))
            f.close()
        else:
            f = open("output_files/outputs.txt", "w")
            f.write("Impossible")
            f.close()

        # for i in finalList:
        #     print("Path = {}".format(i.getPathString()))

    def updateDataAfterSimpleIDS(self, new_node):
        self.__table[self.__robot.getLocation()[0]][self.__robot.getLocation()[1]].setHaveRobot(False)
        self.__table[new_node.getState().getRobot().getLocation()[0]][
            new_node.getState().getRobot().getLocation()[1]].setHaveRobot(True)
        self.__graph.blocks = self.__table
        self.__robot.setLocation(
            (new_node.getState().getRobot().getLocation()[0], new_node.getState().getRobot().getLocation()[1]))
        self.__graph.robot = self.__robot

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
