from Block import Block
from Butter import Butter
from ClientForGraphic import ClientForGraphic
from Person import Person
from Robot import Robot
from SolutionTreeAStar import SolutionTreeAStar
from SolutionTreeIDS import SolutionTreeIDS

path = []


def main():
    whichInputFile = 12
    file = open("input_files/test" + str(whichInputFile) + ".txt", "r")
    clientForGraphic = ClientForGraphic()

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

    solutionTreeIDS = SolutionTreeIDS(table, robot, butters, persons, False)
    whichMethod = 1
    solutionTreeIDS.start()
    if not solutionTreeIDS.haveSolution:
        solutionTreeIDS1 = SolutionTreeIDS(table, robot, butters, persons, True)
        solutionTreeIDS1.start()

    # solutionTreeAStar = SolutionTreeAStar(table, robot, butters, persons, False)
    # whichMethod = 3
    # solutionTreeAStar.start()
    # if not solutionTreeAStar.haveSolution:
    #     solutionTreeAStar1 = SolutionTreeAStar(table, robot, butters, persons, True)
    #     solutionTreeAStar1.start()

    # solutionTreeBBFS = SolutionTreeBBFS(table, robot, butters, persons, False)
    # whichMethod = 2
    # solutionTreeBBFS.start()
    # if not solutionTreeBBFS.haveSolution:
    #     solutionTreeBBFS1 = SolutionTreeBBFS(table, robot, butters, persons, True)
    #     solutionTreeBBFS1.start()

    clientForGraphic.send(whichInputFile=whichInputFile, whichMethod=whichMethod)

    # graph = GraphOperationsBBFS(table, persons, butters)
    # tableTemp = deepcopy(table)
    # print(graph.BBFSBoth(State(robot, butters), butters[0], 4, persons[0]))
    # robot.setLocation((butters[0].getLocation()[0], butters[0].getLocation()[1] + 1))
    # print(graph.BBFSBoth(State(robot, butters), butters[0], 4, persons[0]))
    # successor = graph.successorPull(NodeBBFS(State(robot, butters), None), 0)
    # for i in successor:
    #     print(i.getState().getRobot().getLocation(), " ", i.getState().getButters()[0].getLocation())


if __name__ == "__main__":
    main()
