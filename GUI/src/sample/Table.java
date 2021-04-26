package sample;


public class Table
{
    public House[][] house;
    public Table()
    {
        house = new House[5 + 2][5 + 2];
        house[1][1] = new House(1, false, false, false, false);
        house[1][2] = new House(1, false, false, false, false);
        house[1][3] = new House(1, false, false, false, false);
        house[1][4] = new House(1, false, false, false, false);
        house[1][5] = new House(1, false, false, false, false);
        house[2][1] = new House(1, false, false, false, false);
        house[2][2] = new House(1, false, false, false, false);
        house[2][3] = new House(1, false, false, false, false);
        house[2][4] = new House(1, false, false, false, false);
        house[2][5] = new House(1, false, false, false, false);
        house[3][1] = new House(1, false, false, false, false);
        house[3][2] = new House(1, false, false, false, false);
        house[3][3] = new House(1, true, false, false, false);
        house[3][4] = new House(1, false, true, false, false);
        house[3][5] = new House(1, false, false, false, false);
        house[4][1] = new House(1, false, false, false, false);
        house[4][2] = new House(1, false, false, false, false);
        house[4][3] = new House(1, false, false, false, false);
        house[4][4] = new House(1, false, false, false, false);
        house[4][5] = new House(1, false, false, false, false);
        house[5][1] = new House(1, false, false, false, false);
        house[5][2] = new House(1, false, false, false, false);
        house[5][3] = new House(1, false, false, false, false);
        house[5][4] = new House(1, false, false, false, false);
        house[5][5] = new House(1, false, false, false, false);
    }
}
