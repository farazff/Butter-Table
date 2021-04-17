from copy import copy, deepcopy
from GraphOperations import GraphOperations
from PathNode import PathNode
from State import State

import _thread


class SolutionTreeIDS:

    def __init__(self, table, robot, butters, persons):
        self.__robot = robot
        self.__butters = butters
        self.__persons = persons
        self.__startingNodes = [
            PathNode(table, State(copy(robot), copy(butters)), None, None, "", 0, copy(self.__butters),
                     copy(self.__persons))]

    def start(self):
        finalList = []
        currentNode = self.__startingNodes.pop(0)
        for b in currentNode.getUnvisitedButters():
            for p in currentNode.getUnvisitedPersons():
                for side in self.calculateEmptyAroundOfButter(b, currentNode.table):
                    print(b.getNum(), " ", p.getNum(), " ", side)
                    # print(b.getLocation())

                    graph = GraphOperations(currentNode.table, self.__butters,
                                            deepcopy(currentNode.getState().getRobot()), self.__persons)
                    print("Start")
                    tup1 = graph.IDS(currentNode.getState(), b, side)
                    print("end")
                    if tup1 is None:
                        continue
                    new_node = tup1[0]
                    self.updateDataAfterSimpleIDS(new_node, currentNode.table, graph , currentNode)

                    tup2 = graph.IDSWithButter(new_node.getState(), b.getNum(), p)
                    if tup2 is None:
                        continue
                    new_node2 = tup2[0]
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

                    blocksTemp[new_node.getState().getRobot().getLocation()[0]][
                        new_node.getState().getRobot().getLocation()[1]].setHaveRobot(False)

                    tmp=[PathNode(blocksTemp, new_node2.getState(), b.getNum, p.getNum,
                                 currentNode.getPathString() + tup1[1] + tup2[1], 0, copy(unvisited_butters),
                                 copy(unvisited_persons))]


                    _thread.start_new_thread(self.startThread,(deepcopy(tmp),))
                    # self.startThread(tmp)   # 5.20  min


        # for q in finalList:
        #     print(q.getPathString())

        if len(finalList) != 0:
            minPath = minLen = min(len(i.getPathString()) for i in finalList)
            for i in finalList:
                if len(i.getPathString()) == minLen:
                    minPath = i.getPathString()
                    break

            f = open("output_files/outputs_IDS.txt", "w")
            f.write(minPath + "\n" + str(minLen) + "\n" + str(minLen))
            f.close()
        else:
            f = open("output_files/outputs_IDS.txt", "w")
            f.write("Impossible")
            f.close()

        for i in finalList:
            print("Path = {}".format(i.getPathString()))


    def startThread(self,startingNodes1):
        startingNodes=deepcopy(startingNodes1)
        finalList = []
        while len(startingNodes) > 0:
            currentNode = startingNodes.pop(0)
            if len(currentNode.getUnvisitedButters()) == 0:
                finalList.append(copy(currentNode))
                continue
            for b in currentNode.getUnvisitedButters():
                for p in currentNode.getUnvisitedPersons():
                    for side in self.calculateEmptyAroundOfButter(b, currentNode.table):
                        print(b.getNum(), " ", p.getNum(), " ", side)
                        # print(b.getLocation())

                        graph = GraphOperations(currentNode.table,deepcopy( self.__butters),
                                                deepcopy(currentNode.getState().getRobot()), self.__persons)
                        print("Start")
                        tup1 = graph.IDS(currentNode.getState(), b, side)
                        print("end")
                        if tup1 is None:
                            continue
                        new_node = tup1[0]
                        self.updateDataAfterSimpleIDS(new_node, currentNode.table, graph,currentNode)


                        tup2 = graph.IDSWithButter(new_node.getState(), b.getNum(), p)
                        if tup2 is None:
                            continue
                        new_node2 = tup2[0]
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

                        blocksTemp[new_node.getState().getRobot().getLocation()[0]][
                            new_node.getState().getRobot().getLocation()[1]].setHaveRobot(False)

                        startingNodes.append(
                            PathNode(blocksTemp, new_node2.getState(), b.getNum, p.getNum,
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

            f = open("output_files/outputs_IDS.txt", "w")
            f.write(minPath + "\n" + str(minLen) + "\n" + str(minLen))
            f.close()
        else:
            f = open("output_files/outputs_IDS.txt", "w")
            f.write("Impossible")
            f.close()

        for i in finalList:
            print("Path = {}".format(i.getPathString()))


    def updateDataAfterSimpleIDS(self, new_node, table, graph, parent):
        table[parent.getState().getRobot().getLocation()[0]][parent.getState().getRobot().getLocation()[1]].setHaveRobot(False)
        table[new_node.getState().getRobot().getLocation()[0]][
            new_node.getState().getRobot().getLocation()[1]].setHaveRobot(True)
        graph.blocks = table
        graph.robot.setLocation((new_node.getState().getRobot().getLocation()[0],
                                 new_node.getState().getRobot().getLocation()[1]))


    def calculateEmptyAroundOfButter(self, butter, table):
        ans = []
        length = butter.getLocation()[1]
        height = butter.getLocation()[0]
        if table[height][length - 1].getHaveButter() or table[height][length - 1].getHaveObstacle():
            pass
        else:
            ans.append(1)
        if table[height - 1][length].getHaveButter() or table[height - 1][length].getHaveObstacle():
            pass
        else:
            ans.append(2)
        if table[height][length + 1].getHaveButter() or table[height][length + 1].getHaveObstacle():
            pass
        else:
            ans.append(3)
        if table[height + 1][length].getHaveButter() or table[height + 1][length].getHaveObstacle():
            pass
        else:
            ans.append(4)
        return ans
