class PatchNode:
    def __init__(self, whichButter, whichPerson, pathString, cost):
        self.__whichButter = whichButter
        self.__whichPerson = whichPerson
        self.__pathString  = pathString
        self.__cost        = cost

    def getWhichButter(self):
        return self.__whichButter

    def setWhichButter(self, whichButter):
        self.__whichButter = whichButter

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
