from State import State


class Node:
    def __init__(self, state, parent):
        self.__parent = parent
        self.__state = state

    def setstate(self, state) -> State:
        self.__state = state

    def setParent(self, parent):
        self.__parent = parent

    def getState(self) -> State:
        return self.__state

    def getParent(self):
        return self.__parent
