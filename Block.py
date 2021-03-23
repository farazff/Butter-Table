class Block:
    def __init__(self, x, y, cost, haveButter, haveRobot, haveObstacle, havePerson):
        self.__x = x
        self.__y = y
        self.__cost = cost
        self.__haveButter = haveButter
        self.__haveRobot = haveRobot
        self.__haveObstacle = haveObstacle
        self.__havePerson = havePerson

    def getX(self):
        return self.__y

    def getY(self):
        return self.__y

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
