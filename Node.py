class Node:
    def __init__(self, state, parent):
        self.__state = state
        self.__parent = parent

    def setstate(self, state):
        self.__state = state

    def setParent(self, parent):
        self.__parent = parent

    def getState(self):
        return self.__state

    def getParent(self):
        return self.__parent
