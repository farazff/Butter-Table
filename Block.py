class Block:
    def __init__(self, location, cost, haveButter, haveRobot, haveObstacle, havePerson ) :
        self.__location=location
        self.__cost = cost
        self.__haveButter = haveButter
        self.__haveRobot = haveRobot
        self.__haveObstacle = haveObstacle
        self.__havePerson = havePerson

    def getLocation(self):
        return self.__location

    def getCost(self):
        return self.__cost

    def getHaveButter(self):
        return self.__haveButter

    def getHaveRobot(self):
        return self.__haveRobot

    def getHaveObstacle(self):
        return self.__haveObstacle

    def getHavePerson(self):
        return self.__havePerson

    def setHaveButter(self, temp):
        self.__haveButter = temp

    def setHaveRobot(self, temp):
        self.__haveRobot = temp

    def setHaveObstacle(self, temp):
        self.__haveObstacle = temp

    def setHavePerson(self, temp):
        self.__havePerson = temp
