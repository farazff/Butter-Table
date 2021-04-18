from Block import Block
from Butter import Butter
from GraphOperationsAStar import GraphOperationsAStar
from Robot import Robot
from Person import Person
from SolutionTreeAStar import SolutionTreeAStar
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

    # solutionTreeIDS = SolutionTreeIDS(table, robot, butters, persons)
    # solutionTreeIDS.start()

    # solutionTreeBBFS = SolutionTreeBBFS(table, robot, butters, persons)
    # solutionTreeBBFS.start()

    solutionTreeAStar = SolutionTreeAStar(table, robot, butters, persons)
    solutionTreeAStar.start()

    # graph = GraphOperationsBBFS(table, persons, butters)
    # tableTemp = deepcopy(table)
    # print(graph.BBFSBoth(State(robot, butters), butters[0], 4, persons[0]))
    # robot.setLocation((butters[0].getLocation()[0], butters[0].getLocation()[1] + 1))
    # print(graph.BBFSBoth(State(robot, butters), butters[0], 4, persons[0]))
    # successor = graph.successorPull(NodeBBFS(State(robot, butters), None), 0)
    # for i in successor:
    #     print(i.getState().getRobot().getLocation(), " ", i.getState().getButters()[0].getLocation())

    # graph = GraphOperationsAStar(table, butters, robot, persons)
    # graph.AStar(State(robot, butters), butters[0], 3)
    # graph.AStarWithButter(State(robot, butters), 0, persons[0])


if __name__ == "__main__":
    main()
