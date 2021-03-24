from Block import Block
from Butter import Butter
from Robot import Robot
from Person import Person
def main():
    butters=[]
    persons=[]
    robot = None
    height, length = input().split()
    height = int(height)
    length = int(length)
    print(height,length)
    table = []
    temp = None

    for i in range(height+1):
        row = []
        x = list(map(str, input().split()))
        print(x)
        for j in range(length+1) :

            if i==0 or j==0 or i==height or j==length:
                temp = Block((i, j), 0, False, False, True, False)

            else:

                if x[j-1][len(x[j-1])-1].isdigit():
                     temp = Block((i, j), int(x[j-1]), False, False, False, False)

                if x[j-1][len(x[j-1]) - 1] == 'r':
                    temp = Block((i, j), int(x[j-1][:len(x[j-1])-1]), False, True, False, False)
                    robot = Robot((i,j))

                if x[j-1][len(x[j-1]) - 1] == 'b':
                    temp = Block((i, j), int(x[j-1][:len(x[j-1])-1]), True, False, False, False)
                    butters.append(Butter((i,j)))


                if x[j-1][len(x[j-1]) - 1] == 'p':
                    temp = Block((i, j), int(x[j-1][:len(x[j-1])-1]), False, False, False, True)
                    persons.append(Person((i,j)))


                if x[j-1][len(x[j-1]) - 1] == 'x':
                    temp = Block((i, j), 0, False, False, True, False)

            row.append(temp)
        table.append(row)





    for i in range(height+1):
        for j in range(length+1):
            print(table[i][j].getLocation(),"butter:",table[i][j].getHaveButter(),"person:",table[i][j].getHavePerson(),"robot:",table[i][j].getHaveRobot(),"obstacle:",table[i][j].getHaveObstacle(), end="    ")

        print()


if __name__ == "__main__":
    main()
