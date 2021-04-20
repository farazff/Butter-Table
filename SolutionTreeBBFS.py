import multiprocessing
import os
from copy import copy, deepcopy

from GraphOperationsBBFS import GraphOperationsBBFS
from PathNode import PathNode
from State import State


class SolutionTreeBBFS:

    def __init__(self, table, robot, butters, persons, doTemp):
        self.__table = table
        self.__robot = robot
        self.__butters = butters
        self.doTemp = doTemp
        self.__persons = persons
        self.haveSolution = False
        self.__startingNodes = [
            PathNode(table, State(copy(robot), copy(butters)), None, None, "", 0, copy(self.__butters),
                     copy(self.__persons))]
        global finalListt

    def startMultiprocessing2(self, currentNode, sideButter, b, p, pathList):
        print(end=".")
        jobs = []
        pathList2 = []
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

            part2 = graph.BBFSBoth(new_node1.getState(), deepcopy(b), sidePerson, deepcopy(p), self.doTemp)
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

            # self.__startingNodes.append(
            tmp = [
                PathNode(blocksTemp, new_node2.getState(), b.getNum(), p.getNum(),
                         currentNode.getPathString() + part1 + part2, 0, copy(unvisited_butters),
                         copy(unvisited_persons))]
            jobs.append(multiprocessing.Process(target=self.startMultiprocessing1, args=(tmp, pathList2,)))

        for q in jobs:
            q.start()
        for q in jobs:
            q.join()
        # print("_________=++++++++++--_____________________",pathList2)
        # self.start2(tmp)

    def start(self):
        jobs = []
        pathList = []
        currentNode = self.__startingNodes.pop()

        for b in currentNode.getUnvisitedButters():
            for p in currentNode.getUnvisitedPersons():
                for sideButter in self.calculateEmptyAroundOfButter(b):
                    jobs.append(multiprocessing.Process(target=self.startMultiprocessing2,
                                                        args=(currentNode, sideButter, b, p, pathList,)))

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
                f = open("output_files/outputs_BBFS.txt", "w")
                f.write("Impossible")
                print("--------------------------------------------- \nImpossible")
                f.close()
            else:
                self.haveSolution = True
                f = open("output_files/outputs_BBFS.txt", "w")
                f.write(minL + "\n" + str(len(minL)) + "\n" + str(len(minL)))
                print("--------------------------------------------- \nResult : ",
                      minL + "\n" + str(len(minL)) + "\n" + str(len(minL)))
                f.close()
        except:
            self.haveSolution = False
            f = open("output_files/outputs_BBFS.txt", "w")
            f.write("Impossible")
            print("--------------------------------------------- \nImpossible")
            f.close()

    def startMultiprocessing1(self, startingNodes, pathList):
        global finalList1
        finalList = []
        while len(startingNodes) > 0:
            currentNode = startingNodes.pop()
            if len(currentNode.getUnvisitedButters()) == 0:
                finalList.append(copy(currentNode))
                continue
            for b in currentNode.getUnvisitedButters():
                for p in currentNode.getUnvisitedPersons():
                    for sideButter in self.calculateEmptyAroundOfButter(b):
                        for sidePerson in self.calculateEmptyAroundOfPerson(p):

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

                            part2 = graph.BBFSBoth(new_node1.getState(), deepcopy(b), sidePerson, deepcopy(p),
                                                   self.doTemp)
                            if part2 is None:
                                continue
                            new_node2 = deepcopy(new_node1)

                            new_node2.getState().getButters()[b.getNum()].setLocation((p.getLocation()[0],
                                                                                       p.getLocation()[1]))
                            if sidePerson == 1:
                                new_node2.getState().getRobot().setLocation(
                                    (p.getLocation()[0], p.getLocation()[1] - 1))
                            if sidePerson == 2:
                                new_node2.getState().getRobot().setLocation(
                                    (p.getLocation()[0] - 1, p.getLocation()[1]))
                            if sidePerson == 3:
                                new_node2.getState().getRobot().setLocation(
                                    (p.getLocation()[0], p.getLocation()[1] + 1))
                            if sidePerson == 4:
                                new_node2.getState().getRobot().setLocation(
                                    (p.getLocation()[0] + 1, p.getLocation()[1]))

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

                            startingNodes.append(
                                PathNode(blocksTemp, new_node2.getState(), b.getNum(), p.getNum(),
                                         currentNode.getPathString() + part1 + part2, 0, copy(unvisited_butters),
                                         copy(unvisited_persons)))
        for i in finalList:
            print("Path = {}".format(i.getPathString()))
        print()

        if len(finalList) == 0:
            # f = open("temporaryFile.txt", "a")
            # f.write("impossible")
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
