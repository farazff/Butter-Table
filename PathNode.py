class PathNode:
    def __init__(self, state, ButterNUM, PersonNUM, pathString, cost, unvisitedButters, unvisitedPersons):
        self.__state = state
        self.__ButterNUM = ButterNUM
        self.__PersonNUM = PersonNUM
        self.__pathString = pathString
        self.__cost = cost
        self.__unvisitedButters = unvisitedButters
        self.__unvisitedPersons = unvisitedPersons

    def getState(self):
        return self.__state

    def setState(self, state):
        self.__state = state

    def getButterNUM(self):
        return self.__ButterNUM

    def setButterNUM(self, ButterNUM):
        self.__ButterNUM = ButterNUM

    def getUnvisitedButters(self):
        return self.__unvisitedButters

    def setUnvisitedButters(self, unvisitedButters):
        self.__unvisitedButters = unvisitedButters

    def getUnvisitedPersons(self):
        return self.__unvisitedPersons

    def setUnvisitedPersons(self, unvisitedPersons):
        self.__unvisitedPersons = unvisitedPersons

    def getPersonNUM(self):
        return self.__PersonNUM

    def setPersonNUM(self, whichPerson):
        self.__PersonNUM = whichPerson

    def getCost(self):
        return self.__cost

    def setCost(self, cost):
        self.__cost = cost

    def getPathString(self):
        return self.__pathString

    def setPathString(self, pathString):
        self.__pathString = pathString
