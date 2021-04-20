import multiprocessing
import os
from copy import copy, deepcopy

from GraphOperationsAStar import GraphOperationsAStar
from PathNode import PathNode
from State import State


def calculateEmptyAroundOfButter(butter, table):
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


class SolutionTreeAStar:

    def __init__(self, table, robot, butters, persons, doTemp):
        self.__robot = robot
        self.__butters = butters
        self.__persons = persons
        self.doTemp = doTemp
        self.haveSolution = False
        self.__startingNodes = [
            PathNode(table, State(copy(robot), copy(butters)), None, None, "", 0, copy(self.__butters),
                     copy(self.__persons))]

    def startMultiprocessing2(self, currentNode, b, p):
        jobs = []
        for side in calculateEmptyAroundOfButter(b, currentNode.table):

            graph = GraphOperationsAStar(currentNode.table, self.__butters,
                                         deepcopy(currentNode.getState().getRobot()), self.__persons)
            tup1 = graph.AStar(currentNode.getState(), b, side)
            if tup1 is None:
                continue
            new_node = tup1[0]
            self.updateDataAfterSimpleIDS(new_node, currentNode.table, graph)

            tup2 = graph.AStarWithButter(new_node.getState(), b.getNum(), p, self.doTemp)
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

            # self.__startingNodes.append(
            tmp = [
                PathNode(blocksTemp, new_node2.getState(), b.getNum(), p.getNum(),
                         currentNode.getPathString() + tup1[1] + tup2[1],
                         currentNode.getCost() + new_node.cost + new_node2.cost, copy(unvisited_butters),
                         copy(unvisited_persons))]
            jobs.append(multiprocessing.Process(target=self.startMultiprocessing1, args=(tmp,)))

            # self.startThread(tmp)   # 5.20  min

        for q in jobs:
            q.start()
        for q in jobs:
            q.join()
        # self.startMultiprocessing1(tmp)

    def start(self):
        jobs = []
        currentNode = self.__startingNodes.pop()

        for b in currentNode.getUnvisitedButters():
            for p in currentNode.getUnvisitedPersons():
                jobs.append(multiprocessing.Process(target=self.startMultiprocessing2, args=(currentNode, b, p,)))

        for q in jobs:
            q.start()
        for q in jobs:
            q.join()
        try:
            f = open("temporaryFile.txt", "r")
            allPath = f.read()
            f.close()
            os.remove("temporaryFile.txt")
            allPathList = allPath.split("\n")

            minL = 99
            for i in allPathList:
              if "Impossible" not in i:
                # if len(i.split(" ")[0]) < minL and i != "":
                if i != "" and  int(i.split(" ")[1]) < minL :
                    minL = len(i.split(" ")[0])
            minC = 0
            for i in allPathList:
                if len(i.split(" ")[0]) == minL:
                    minL = i.split(" ")[0]
                    minC = i.split(" ")[1]
                    break

            if "Impossible" in allPath:
                self.haveSolution = False
                f = open("output_files/outputs_AStar.txt", "w")
                f.write("Impossible")
                print("--------------------------------------------- \nimpossible")
                f.close()
            else:
                self.haveSolution = True
                f = open("output_files/outputs_AStar.txt", "w")
                f.write(minL + "\n" + str(len(minL)) + "\n" + str(minC))
                print("--------------------------------------------- \nResult : ",
                      minL + "\n" + str(len(minL)) + "\n" + str(minC))
                f.close()
        except:
            self.haveSolution = False
            f = open("output_files/outputs_AStar.txt", "w")
            f.write("Impossible")
            print("--------------------------------------------- \nimpossible")
            f.close()

    def startMultiprocessing1(self, startingNodes):
        finalList = []
        while len(startingNodes) > 0:
            currentNode = startingNodes.pop()
            if len(currentNode.getUnvisitedButters()) == 0:
                finalList.append(copy(currentNode))
                continue
            for b in currentNode.getUnvisitedButters():
                for p in currentNode.getUnvisitedPersons():
                    for side in calculateEmptyAroundOfButter(b, currentNode.table):

                        graph = GraphOperationsAStar(currentNode.table, self.__butters,
                                                     deepcopy(currentNode.getState().getRobot()), self.__persons)
                        tup1 = graph.AStar(currentNode.getState(), b, side)
                        if tup1 is None:
                            continue
                        new_node = tup1[0]
                        self.updateDataAfterSimpleIDS(new_node, currentNode.table, graph)

                        tup2 = graph.AStarWithButter(new_node.getState(), b.getNum(), p, self.doTemp)
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
                            PathNode(blocksTemp, new_node2.getState(), b.getNum(), p.getNum(),
                                     currentNode.getPathString() + tup1[1] + tup2[1],
                                     currentNode.getCost() + new_node.cost + new_node2.cost,
                                     copy(unvisited_butters),
                                     copy(unvisited_persons)))
        for i in finalList:
            print("Path = {}".format(i.getPathString()), "cost = ", i.getCost())
        print()

        if len(finalList) == 0:
            # f = open("temporaryFile.txt", "a")
            # f.write("impossible\n")
            #
            # f.close()
            pass
        else:
            minLen = min(i.getCost() for i in finalList)
            for i in finalList:
                if i.getCost() == minLen:
                    minPath = i.getPathString()
                    # print("minPath : ", minPath)
                    f = open("temporaryFile.txt", "a")
                    st = str(str(i.getCost()))
                    f.write(str(minPath) + " " + st + "\n")

                    f.close()
                    break

    def updateDataAfterSimpleIDS(self, new_node, table, graph):
        table[self.__robot.getLocation()[0]][self.__robot.getLocation()[1]].setHaveRobot(False)
        table[new_node.getState().getRobot().getLocation()[0]][
            new_node.getState().getRobot().getLocation()[1]].setHaveRobot(True)
        graph.blocks = table
        graph.robot.setLocation((new_node.getState().getRobot().getLocation()[0],
                                 new_node.getState().getRobot().getLocation()[1]))
