package sample;

import java.io.File;
import java.io.FileNotFoundException;
import java.net.URL;
import java.util.ResourceBundle;
import java.util.Scanner;
import com.jfoenix.controls.JFXButton;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.image.ImageView;
import javafx.scene.layout.GridPane;

public class Controller implements Initializable {
    @FXML
    private GridPane gridPane;

    @FXML
    private JFXButton next;

    @FXML
    private JFXButton last;


    int[] HRobot;
    int[] LRobot;
    Table table;
    String pathReal;
    int start = 0;
    int ro, col;

    public void UpdateTableNext(char m) {
        if (m == 'L') {
            if (table.house[HRobot[0]][LRobot[0] - 1].butter) {
                table.house[HRobot[0]][LRobot[0] - 1].butter = false;
                table.house[HRobot[0]][LRobot[0] - 2].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0]][LRobot[0] - 1].robot = true;
            LRobot[0]--;
        }

        if (m == 'R') {
            if (table.house[HRobot[0]][LRobot[0] + 1].butter) {
                table.house[HRobot[0]][LRobot[0] + 1].butter = false;
                table.house[HRobot[0]][LRobot[0] + 2].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0]][LRobot[0] + 1].robot = true;
            LRobot[0]++;
        }

        if (m == 'U') {
            if (table.house[HRobot[0] - 1][LRobot[0]].butter) {
                table.house[HRobot[0] - 1][LRobot[0]].butter = false;
                table.house[HRobot[0] - 2][LRobot[0]].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0] - 1][LRobot[0]].robot = true;
            HRobot[0]--;
        }

        if (m == 'D') {
            if (table.house[HRobot[0] + 1][LRobot[0]].butter) {
                table.house[HRobot[0] + 1][LRobot[0]].butter = false;
                table.house[HRobot[0] + 2][LRobot[0]].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0] + 1][LRobot[0]].robot = true;
            HRobot[0]++;
        }

        updateGUI();
    }

    public void UpdateTableLast(char m) {
        if (m == 'L') {
            if (LRobot[0] + 1 < col && table.house[HRobot[0]][LRobot[0] + 1].butter) {
                table.house[HRobot[0]][LRobot[0] + 1].butter = false;
                table.house[HRobot[0]][LRobot[0]].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0]][LRobot[0] - 1].robot = true;
            LRobot[0]--;
        }

        if (m == 'R') {
            if (LRobot[0] - 1 >= 0 && table.house[HRobot[0]][LRobot[0] - 1].butter) {
                table.house[HRobot[0]][LRobot[0] - 1].butter = false;
                table.house[HRobot[0]][LRobot[0]].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0]][LRobot[0] + 1].robot = true;
            LRobot[0]++;
        }

        if (m == 'U') {
            if (HRobot[0] + 1 < ro && table.house[HRobot[0] + 1][LRobot[0]].butter) {
                table.house[HRobot[0] + 1][LRobot[0]].butter = false;
                table.house[HRobot[0]][LRobot[0]].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0] - 1][LRobot[0]].robot = true;
            HRobot[0]--;
        }

        if (m == 'D') {
            if (HRobot[0] - 1 >=0 && table.house[HRobot[0] - 1][LRobot[0]].butter) {
                table.house[HRobot[0] - 1][LRobot[0]].butter = false;
                table.house[HRobot[0]][LRobot[0]].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0] + 1][LRobot[0]].robot = true;
            HRobot[0]++;
        }
        updateGUI();
    }

    public void updateGUI() {
        for (Node node : gridPane.getChildren()) {
            node.setVisible(false);
        }

        for (Node node : gridPane.getChildren()) {
            if (node instanceof ImageView) {
                if (((ImageView) node).getImage().getUrl().contains("part"))
                {
                    Integer CI = GridPane.getColumnIndex(node);
                    Integer RI = GridPane.getRowIndex(node);
                    if (CI == null)
                        CI = 0;
                    if (RI == null)
                        RI = 0;
                    if(CI < col && RI < ro)
                        node.setVisible(true);
                }
            }
        }

        for (int i = 0; i <= 6; i++) {
            for (int j = 0; j <= 6; j++) {
                for (Node node : gridPane.getChildren()) {
                    if (node instanceof ImageView) {
                        Integer CI = GridPane.getColumnIndex(node);
                        Integer RI = GridPane.getRowIndex(node);
                        if (CI == null)
                            CI = 0;
                        if (RI == null)
                            RI = 0;

                        if (CI == j && RI == i) {
                            if (table.house[i][j].butter && table.house[i][j].person) {
                                if (((ImageView) node).getImage().getUrl().endsWith("nh.png"))
                                    node.setVisible(true);
                            } else if (table.house[i][j].butter) {
                                if (((ImageView) node).getImage().getUrl().endsWith("b.png"))
                                    node.setVisible(true);
                            } else if (table.house[i][j].robot) {
                                if (((ImageView) node).getImage().getUrl().endsWith("r.png"))
                                    node.setVisible(true);
                            } else if (table.house[i][j].person) {
                                if (((ImageView) node).getImage().getUrl().endsWith("h.png") && !((ImageView) node).getImage().getUrl().endsWith("nh.png"))
                                    node.setVisible(true);
                            } else if (table.house[i][j].obstacle) {
                                if (((ImageView) node).getImage().getUrl().endsWith("o.png"))
                                    node.setVisible(true);
                            }
                        }

                    }
                }
            }
        }
    }

    @FXML
    void drawNext(ActionEvent event) {
        char path = pathReal.charAt(start);
        start++;

        UpdateTableNext(path);
        drawTableInConsole();

        if (start == pathReal.length()) {
            next.setDisable(true);
        }
        if (start > 0) {
            last.setDisable(false);
        }
    }

    @FXML
    void drawLast(ActionEvent event) {

        start--;
        char path = pathReal.charAt(start);
        if (path == 'U')
            path = 'D';
        else if (path == 'D')
            path = 'U';
        else if (path == 'L')
            path = 'R';
        else if (path == 'R')
            path = 'L';

        UpdateTableLast(path);
        drawTableInConsole();

        if (start == 0) {
            last.setDisable(true);
        }
        if (start < pathReal.length()) {
            next.setDisable(false);
        }
    }

    public void drawTableInConsole() {
        for (int i = 0; i < ro; i++) {
            for (int j = 0; j < col; j++) {
                if (table.house[i][j].robot) {
                    System.out.print("R ");
                    continue;
                }
                if (table.house[i][j].butter) {
                    System.out.print("B ");
                    continue;
                }
                if (table.house[i][j].person) {
                    System.out.print("P ");
                    continue;
                }
                if (table.house[i][j].obstacle) {
                    System.out.print("O ");
                    continue;
                }
                System.out.print("1 ");
            }
            System.out.println();
        }
        System.out.println("\n");
    }

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        ServerForGUI serverForGUI = new ServerForGUI();
        serverForGUI.run();
        String mapFileNumber = serverForGUI.mapFileNumber;
        String pathFileNumber = serverForGUI.pathFileNumber;
        if (pathFileNumber.equals("1"))
            pathFileNumber = "outputs_IDS.txt";
        if (pathFileNumber.equals("2"))
            pathFileNumber = "outputs_BBFS.txt";
        if (pathFileNumber.equals("3"))
            pathFileNumber = "outputs_AStar.txt";

        File pathFile = new File("../output_files/" + pathFileNumber);

        try {
            Scanner myReader = new Scanner(pathFile);
            pathReal = myReader.nextLine();

        } catch (Exception e) {
            e.printStackTrace();
        }
        try {
            table = new Table(mapFileNumber);
            HRobot = new int[]{table.h};
            LRobot = new int[]{table.l};
            ro = table.ro;
            col = table.col;
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        last.setDisable(true);
        int temp1 = (700-ro*95)/2;
        int temp2 = (900-col*95)/2;
        gridPane.setGridLinesVisible(true);
        gridPane.relocate(temp2, temp1);
        updateGUI();
    }
}
