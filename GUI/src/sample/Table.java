package sample;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;


public class Table {

    public House[][] house;

    public Table(String mapPath) throws FileNotFoundException {

        File mapFile = new File("../input_files/test" + mapPath+".txt");
        Scanner myReader = new Scanner(mapFile);
        String dimS=myReader.nextLine();
        System.out.println(dimS);
        String[] dimension = dimS.split("\t", 2);

        String[] mapInput;
        house = new House[5 + 2][5 + 2];
        for(int i = 0; i < 7; i++)
            for (int j = 0; j < 7; j++)
                house[i][j] = new House(1, false, false, false, false,false);

        for (int i = 0; i < Integer.parseInt(dimension[0]); i++) {
            System.out.println("--------------------");
            mapInput = myReader.nextLine().split("\t", Integer.parseInt(dimension[1]));
            for (int k=0;k<Integer.parseInt(dimension[1]);k++)
               System.out.print(mapInput[k]);
               System.out.println();
            for (int j = 0; j < Integer.parseInt(dimension[1]); j++) {
                System.out.println("--"+mapInput[j]);
                if (mapInput[j].contains("x"))
                    house[i][j] = new House(1, false, false, true, true, true);
                else if(mapInput[j].contains("r"))
                    house[i][j] = new House(Integer.parseInt(mapInput[j].substring(0,mapInput[j].length()-1)), true, false, true, false, true);
                else if(mapInput[j].contains("b"))
                    house[i][j] = new House(Integer.parseInt(mapInput[j].substring(0,mapInput[j].length()-1)), false, true, false, false, true);
                else if(mapInput[j].contains("p"))
                    house[i][j] = new House(Integer.parseInt(mapInput[j].substring(0,mapInput[j].length()-1)), false, false, true, false, true);
                else
                    house[i][j] = new House(Integer.parseInt(mapInput[j]), false, false, false, false, true);

            }
        }
//        house = new House[5 + 2][5 + 2];
//        house[0][0] = new House(1, false, false, true, true);
//        house[0][1] = new House(1, false, false, false, true);
//        house[0][2] = new House(1, false, false, false, true);
//        house[0][3] = new House(1, false, false, false, true);
//        house[0][4] = new House(1, false, false, false, true);
//        house[0][5] = new House(1, false, false, false, true);
//        house[0][6] = new House(1, false, false, false, true);
//
//        house[1][0] = new House(1, false, false, false, true);
//        house[1][1] = new House(1, false, false, false, false);
//        house[1][2] = new House(1, false, false, false, false);
//        house[1][3] = new House(1, false, false, false, true);
//        house[1][4] = new House(1, false, false, false, false);
//        house[1][5] = new House(1, false, false, false, false);
//        house[1][6] = new House(1, false, false, false, true);
//
//        house[2][0] = new House(1, false, false, false, true);
//        house[2][1] = new House(1, false, false, false, false);
//        house[2][2] = new House(1, false, false, false, true);
//        house[2][3] = new House(1, false, false, false, false);
//        house[2][4] = new House(1, false, false, false, false);
//        house[2][5] = new House(1, false, false, false, false);
//        house[2][6] = new House(1, false, false, false, true);
//
//        house[3][0] = new House(1, false, false, false, true);
//        house[3][1] = new House(1, false, false, false, false);
//        house[3][2] = new House(1, false, false, false, false);
//        house[3][3] = new House(1, true, false, false, false);
//        house[3][4] = new House(1, false, true, false, false);
//        house[3][5] = new House(1, false, false, false, false);
//        house[3][6] = new House(1, false, false, false, true);
//
//        house[4][0] = new House(1, false, false, false, true);
//        house[4][1] = new House(1, false, false, false, false);
//        house[4][2] = new House(1, false, false, false, false);
//        house[4][3] = new House(1, false, false, false, false);
//        house[4][4] = new House(1, false, false, true, false);
//        house[4][5] = new House(1, false, false, false, false);
//        house[4][6] = new House(1, false, false, false, true);
//
//        house[5][0] = new House(1, false, false, false, true);
//        house[5][1] = new House(1, false, false, false, false);
//        house[5][2] = new House(1, false, false, false, false);
//        house[5][3] = new House(1, false, false, false, false);
//        house[5][4] = new House(1, false, false, false, false);
//        house[5][5] = new House(1, false, false, false, false);
//        house[5][6] = new House(1, false, false, false, true);
//
//        house[6][0] = new House(1, false, false, false, true);
//        house[6][1] = new House(1, false, false, false, true);
//        house[6][2] = new House(1, false, false, false, true);
//        house[6][3] = new House(1, false, false, false, true);
//        house[6][4] = new House(1, false, false, false, true);
//        house[6][5] = new House(1, false, false, false, true);
//        house[6][6] = new House(1, false, false, false, true);

    }
}
