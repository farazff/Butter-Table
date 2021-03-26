from Block import Block
from Butter import Butter
from GraphOperations import GraphOperations
from Node import Node
from Robot import Robot
from Person import Person
from State import State


def main():
    butters = []
    persons = []
    robot = None
    height, length = input().split()
    height = int(height)
    length = int(length)
    table = []
    temp = None
    x = []

    for i in range(height + 2):
        row = []
        if i != 0 and i != height + 1:
            x = list(map(str, input().split()))

        for j in range(length + 2):
            if i == 0 or j == 0 or i == height + 1 or j == length + 1:
                temp = Block((i, j), 0, False, False, True, False)

            else:

                if x[j - 1][len(x[j - 1]) - 1].isdigit():
                    temp = Block((i, j), int(x[j - 1]), False, False, False, False)

                if x[j - 1][len(x[j - 1]) - 1] == 'r':
                    temp = Block((i, j), int(x[j - 1][:len(x[j - 1]) - 1]), False, True, False, False)
                    robot = Robot((i, j))

                if x[j - 1][len(x[j - 1]) - 1] == 'b':
                    temp = Block((i, j), int(x[j - 1][:len(x[j - 1]) - 1]), True, False, False, False)
                    butters.append(Butter((i, j)))

                if x[j - 1][len(x[j - 1]) - 1] == 'p':
                    temp = Block((i, j), int(x[j - 1][:len(x[j - 1]) - 1]), False, False, False, True)
                    persons.append(Person((i, j)))

                if x[j - 1][len(x[j - 1]) - 1] == 'x':
                    temp = Block((i, j), 0, False, False, True, False)

            row.append(temp)
        table.append(row)

    for i in range(height + 2):
        for j in range(length + 2):
            # print(table[i][j].getLocation(),"butter:",table[i][j].getHaveButter(),"person:",table[i][
            # j].getHavePerson(),"robot:",table[i][j].getHaveRobot(),"obstacle:",table[i][j].getHaveObstacle(),
            # end="    ")
            if table[i][j].getHaveObstacle():
                print("  x ", end="")
            elif table[i][j].getHaveButter():
                print("  B ", end="")
            elif table[i][j].getHavePerson():
                print("  P ", end="")
            elif table[i][j].getHaveRobot():
                print("  R ", end="")
            else:
                print("  - ", end="")
        print()

    graph = GraphOperations(table, butters, robot, persons)
    # successor = graph.successor(Node(State(robot, butters), None))
    #
    # for i in range(len(successor)):
    #     print((successor[i].getState().get_robot().get_location()))
    # graph.IDS(State(robot, butters), butters[0], 2)

    # successor = graph.successor_withButter(Node(State(robot, butters), None), 0)
    #
    # for i in range(len(successor)):
    #     print(successor[i].getState().get_robot().get_location(),
    #           successor[i].getState().get_butters()[0].getLocation())

    graph.IDS_withButter(State(robot, butters), 0, persons[0])


if __name__ == "__main__":
    main()
