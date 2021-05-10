from Block import Block
from Butter import Butter
from ClientForGraphic import ClientForGraphic
from Person import Person
from Robot import Robot
from SolutionTreeIDS import SolutionTreeIDS
from SolutionTreeBBFS import SolutionTreeBBFS
from SolutionTreeAStar import SolutionTreeAStar
import datetime

path = []


def main():
    whichInputFile = 5
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

    # start_time = datetime.datetime.now()
    # solutionTreeIDS = SolutionTreeIDS(table, robot, butters, persons, False)
    # whichMethod = 1
    # solutionTreeIDS.start()
    # if not solutionTreeIDS.haveSolution:
    #     solutionTreeIDS1 = SolutionTreeIDS(table, robot, butters, persons, True)
    #     solutionTreeIDS1.start()
    # end_time = datetime.datetime.now()
    # time_diff = (end_time - start_time)
    # execution_time = time_diff.total_seconds() * 1000
    # print("Execution Time in millisecond: ", execution_time)

    start_time = datetime.datetime.now()
    solutionTreeBBFS = SolutionTreeBBFS(table, robot, butters, persons, False)
    whichMethod = 2
    solutionTreeBBFS.start()
    if not solutionTreeBBFS.haveSolution:
        solutionTreeBBFS1 = SolutionTreeBBFS(table, robot, butters, persons, True)
        solutionTreeBBFS1.start()
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    print("Execution Time in millisecond: ", execution_time)

    # start_time = datetime.datetime.now()
    # solutionTreeAStar = SolutionTreeAStar(table, robot, butters, persons, False)
    # whichMethod = 3
    # solutionTreeAStar.start()
    # if not solutionTreeAStar.haveSolution:
    #     solutionTreeAStar1 = SolutionTreeAStar(table, robot, butters, persons, True)
    #     solutionTreeAStar1.start()
    # end_time = datetime.datetime.now()
    # time_diff = (end_time - start_time)
    # execution_time = time_diff.total_seconds() * 1000
    # print("Execution Time in millisecond: ", execution_time)

    clientForGraphic.send(whichInputFile=whichInputFile, whichMethod=whichMethod)


if __name__ == "__main__":
    main()
