from Block import Block
from Butter import Butter
from GraphOperationsBBFS import GraphOperationsBBFS
from Robot import Robot
from Person import Person
from State import State


def main():
    file = open("input_files/test6.txt", "r")
    butters = []
    persons = []
    robot = None
    # height, length = input().split()
    height, length = file.readline().split()
    height = int(height)
    length = int(length)
    table = []
    temp = None
    x = []
    butterCount = int(0)
    personCount = int(0)

    for i in range(height + 2):
        row = []
        if i != 0 and i != height + 1:
            # x = list(map(str, input().split()))
            x = file.readline().split()

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
                    butters.append(Butter((i, j), butterCount))
                    butterCount = butterCount + 1

                if x[j - 1][len(x[j - 1]) - 1] == 'p':
                    temp = Block((i, j), int(x[j - 1][:len(x[j - 1]) - 1]), False, False, False, True)
                    persons.append(Person((i, j), personCount))
                    personCount = personCount + 1

                if x[j - 1][len(x[j - 1]) - 1] == 'x':
                    temp = Block((i, j), 0, False, False, True, False)

            row.append(temp)
        table.append(row)

    for i in range(height + 2):
        for j in range(length + 2):
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

    # solutionTree = SolutionTree(table, robot, butters, persons)
    # solutionTree.start()

    graph = GraphOperationsBBFS(table, persons)
    # successor = graph.successor(Node(State(robot, butters), None), False, 0)
    #
    # for i in range(len(successor)):
    #     print((successor[i].getState().getRobot().getLocation()))
    #     for k in successor[i].getState().getButters():
    #         print(k.getLocation())
    graph.BBFSAlone(State(robot, butters), butters[0], 3)

    # graph = GraphOperations(table, butters, robot, persons)
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

    # graph.IDSWithButter(State(robot, butters), 0, persons[0])

    # node1 = graph.IDS(State(robot, butters), butters[0], 1)
    # table[1][1].setHaveRobot(False)
    # table[3][3].setHaveRobot(True)
    # graph.blocks = table
    # robot.setLocation((3, 2))
    # graph.robot = robot
    # print()
    # graph.IDSWithButter(node1.getState(), 0, persons[0])


if __name__ == "__main__":
    main()
