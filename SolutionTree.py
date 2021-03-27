from copy import copy
from GraphOperations import GraphOperations
from PathNode import PathNode
from State import State


class SolutionTree:

    def __init__(self, table, robot, butters, persons):
        self.__table = table
        self.__robot = robot
        self.__butters = butters
        self.__persons = persons
        self.__graph = GraphOperations(self.__table, self.__butters, self.__robot, self.__persons)
        self.__startingNodes = [
            PathNode(State(copy(robot), copy(butters)), None, None, "", 0, copy(self.__butters), copy(self.__persons))]

    def start(self):
        for b in self.__startingNodes[len(self.__startingNodes) - 1].getUnvisitedButters():
            for p in self.__startingNodes[len(self.__startingNodes) - 1].getUnvisitedPersons():
                for side in self.calculateEmptyAroundOfButter(b):
                    print("butter = {} side = {}, person = {}".format(b.getLocation(), side, p.getLocation()))
                    new_node = self.__graph.IDS(self.__startingNodes[len(self.__startingNodes) - 1].getState(), b, side)
                    self.updateDataAfterSimpleIDS(new_node)
                    print()
                    self.__graph.IDSWithButter(new_node.getState(), b.getNum(), p)
                    print("\n")

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
