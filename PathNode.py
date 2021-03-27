class PatchNode:
    def __init__(self, whichButter, whichPerson, pathString, cost,unvisitedButters,unvisitedPersons):
        self.__whichButter = whichButter
        self.__whichPerson = whichPerson
        self.__pathString = pathString
        self.__cost = cost
        self.__unvisitedButters = unvisitedButters
        self.__unvisitedPersons = unvisitedPersons

    def getWhichButter(self):
        return self.__whichButter

    def setWhichButter(self, whichButter):
        self.__whichButter = whichButter

    def getUnvisitedButters(self):
        return self.__unvisitedButters

    def setUnvisitedButters(self, unvisitedButters):
        self.__unvisitedButters = unvisitedButters

    def getUnvisitedPersons(self):
        return self.__unvisitedButters

    def setUnvisitedPersons(self, unvisitedPersons):
        self.unvisitedPersons = unvisitedPersons

    def getWhichPerson(self):
        return self.__whichPerson

    def setWhichPerson(self, whichPerson):
        self.__whichPerson = whichPerson

    def getCost(self):
        return self.__cost

    def setCost(self, cost):
        self.__cost = cost

    def getPathString(self):
        return self.__pathString

    def setPathString(self, pathString):
        self.__pathString = pathString
