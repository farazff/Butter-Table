package sample;


public class Table
{
    public House[][] house;
    public Table()
    {
        house = new House[5 + 2][5 + 2];
        house[0][0] = new House(1, false, false, false, true);
        house[0][1] = new House(1, false, false, false, true);
        house[0][2] = new House(1, false, false, false, true);
        house[0][3] = new House(1, false, false, false, true);
        house[0][4] = new House(1, false, false, false, true);
        house[0][5] = new House(1, false, false, false, true);
        house[0][6] = new House(1, false, false, false, true);

        house[1][0] = new House(1, false, false, false, true);
        house[1][1] = new House(1, false, false, false, false);
        house[1][2] = new House(1, false, false, false, false);
        house[1][3] = new House(1, false, false, false, true);
        house[1][4] = new House(1, false, false, false, false);
        house[1][5] = new House(1, false, false, false, false);
        house[1][6] = new House(1, false, false, false, true);

        house[2][0] = new House(1, false, false, false, true);
        house[2][1] = new House(1, false, false, false, false);
        house[2][2] = new House(1, false, false, false, true);
        house[2][3] = new House(1, false, false, false, false);
        house[2][4] = new House(1, false, false, false, false);
        house[2][5] = new House(1, false, false, false, false);
        house[2][6] = new House(1, false, false, false, true);

        house[3][0] = new House(1, false, false, false, true);
        house[3][1] = new House(1, false, false, false, false);
        house[3][2] = new House(1, false, false, false, false);
        house[3][3] = new House(1, true, false, false, false);
        house[3][4] = new House(1, false, true, false, false);
        house[3][5] = new House(1, false, false, false, false);
        house[3][6] = new House(1, false, false, false, true);

        house[4][0] = new House(1, false, false, false, true);
        house[4][1] = new House(1, false, false, false, false);
        house[4][2] = new House(1, false, false, false, false);
        house[4][3] = new House(1, false, false, false, false);
        house[4][4] = new House(1, false, false, true, false);
        house[4][5] = new House(1, false, false, false, false);
        house[4][6] = new House(1, false, false, false, true);

        house[5][0] = new House(1, false, false, false, true);
        house[5][1] = new House(1, false, false, false, false);
        house[5][2] = new House(1, false, false, false, false);
        house[5][3] = new House(1, false, false, false, false);
        house[5][4] = new House(1, false, false, false, false);
        house[5][5] = new House(1, false, false, false, false);
        house[5][6] = new House(1, false, false, false, true);

        house[6][0] = new House(1, false, false, false, true);
        house[6][1] = new House(1, false, false, false, true);
        house[6][2] = new House(1, false, false, false, true);
        house[6][3] = new House(1, false, false, false, true);
        house[6][4] = new House(1, false, false, false, true);
        house[6][5] = new House(1, false, false, false, true);
        house[6][6] = new House(1, false, false, false, true);
    }
}
