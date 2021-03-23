from Block import Block


def main():
    height, length = input().split()
    height = int(height)
    length = int(length)

    table = []
    temp = None

    for i in range(height):
        row = []
        x = list(map(str, input().split()))
        for j in range(length):

            if x[j][len(x[j])-1].isdigit():
                temp = Block(i, j, int(x[j]), False, False, False, False)
            else:
                if x[j][len(x[j]) - 1] == 'r':
                    temp = Block(i, j, int(x[j][:len(x[j])-1]), False, True, False, False)

                if x[j][len(x[j]) - 1] == 'b':
                    temp = Block(i, j, int(x[j][:len(x[j])-1]), True, False, False, False)

                if x[j][len(x[j]) - 1] == 'p':
                    temp = Block(i, j, int(x[j][:len(x[j])-1]), False, False, False, True)

                if x[j][len(x[j]) - 1] == 'x':
                    temp = Block(i, j, 0, False, False, True, False)

            row.append(temp)
        table.append(row)

    for i in range(height):
        for j in range(length):
            print(table[i][j].getX(), end=" ")
        print()


if __name__ == "__main__":
    main()
