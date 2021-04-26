package sample;

import java.net.URL;
import java.util.ResourceBundle;
import com.jfoenix.controls.JFXButton;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.image.ImageView;
import javafx.scene.layout.GridPane;

public class Controller implements Initializable
{
    @FXML
    private GridPane gridPane;

    @FXML
    private JFXButton next;

    @FXML
    private JFXButton last;


    int[] HRobot = {3};
    int[] LRobot = {3};
    Table table = new Table();
    String pathReal = "URD";
    int start = 0;

    public void UpdateTableNext(int row, int column, char m)
    {
        if (m == 'L')
        {
            if (table.house[HRobot[0]][LRobot[0] - 1].butter)
            {
                table.house[HRobot[0]][LRobot[0] - 1].butter = false;
                table.house[HRobot[0]][LRobot[0] - 2].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0]][LRobot[0] - 1].robot = true;
            LRobot[0]--;
        }

        if (m == 'R')
        {
            if (table.house[HRobot[0]][LRobot[0] + 1].butter)
            {
                table.house[HRobot[0]][LRobot[0] + 1].butter = false;
                table.house[HRobot[0]][LRobot[0] + 2].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0]][LRobot[0] + 1].robot = true;
            LRobot[0]++;
        }

        if (m == 'U')
        {
            if (table.house[HRobot[0] - 1][LRobot[0]].butter)
            {
                table.house[HRobot[0] - 1][LRobot[0]].butter = false;
                table.house[HRobot[0] - 2][LRobot[0]].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0] - 1][LRobot[0]].robot = true;
            HRobot[0]--;
        }

        if (m == 'D')
        {
            if (table.house[HRobot[0] + 1][LRobot[0]].butter)
            {
                table.house[HRobot[0] + 1][LRobot[0]].butter = false;
                table.house[HRobot[0] + 2][LRobot[0]].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0] + 1][LRobot[0]].robot = true;
            HRobot[0]++;
        }

        updateGUI(row, column);
    }

    public void UpdateTableLast(int row, int column, char m)
    {
        if (m == 'L')
        {
            if (table.house[HRobot[0]][LRobot[0] + 1].butter)
            {
                table.house[HRobot[0]][LRobot[0] + 1].butter = false;
                table.house[HRobot[0]][LRobot[0]].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0]][LRobot[0] - 1].robot = true;
            LRobot[0]--;
        }

        if (m == 'R')
        {
            if (table.house[HRobot[0]][LRobot[0] - 1].butter)
            {
                table.house[HRobot[0]][LRobot[0] - 1].butter = false;
                table.house[HRobot[0]][LRobot[0]].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0]][LRobot[0] + 1].robot = true;
            LRobot[0]++;
        }

        if (m == 'U')
        {
            if (table.house[HRobot[0] + 1][LRobot[0]].butter)
            {
                table.house[HRobot[0] + 1][LRobot[0]].butter = false;
                table.house[HRobot[0]][LRobot[0]].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0] - 1][LRobot[0]].robot = true;
            HRobot[0]--;
        }

        if (m == 'D')
        {
            if (table.house[HRobot[0] - 1][LRobot[0]].butter)
            {
                table.house[HRobot[0] - 1][LRobot[0]].butter = false;
                table.house[HRobot[0]][LRobot[0]].butter = true;
            }
            table.house[HRobot[0]][LRobot[0]].robot = false;
            table.house[HRobot[0] + 1][LRobot[0]].robot = true;
            HRobot[0]++;
        }
        updateGUI(row, column);
    }

    public void updateGUI(int row, int column)
    {
        for (Node node : gridPane.getChildren())
        {
            if (GridPane.getColumnIndex(node) != null)
            {
                node.setVisible(false);
            }
        }

        for (Node node : gridPane.getChildren())
        {
            if (GridPane.getColumnIndex(node) != null)
            {
                if (((ImageView) node).getImage().getUrl().contains("part"))
                    node.setVisible(true);
            }
        }

        for (int i = 1; i <= row; i++)
        {
            for (int j = 1; j <= column; j++)
            {
                for (Node node : gridPane.getChildren())
                {
                    if (GridPane.getColumnIndex(node) != null)
                    {
                        if (GridPane.getColumnIndex(node) == j && GridPane.getRowIndex(node) == i)
                        {
                            if (table.house[i][j].butter && table.house[i][j].person)
                            {
                                if (((ImageView) node).getImage().getUrl().endsWith("nh.png"))
                                    node.setVisible(true);
                            }
                            else if (table.house[i][j].butter)
                            {
                                if (((ImageView) node).getImage().getUrl().endsWith("b.png"))
                                    node.setVisible(true);
                            }
                            else if (table.house[i][j].robot)
                            {
                                if (((ImageView) node).getImage().getUrl().endsWith("r.png"))
                                    node.setVisible(true);
                            }
                            else if (table.house[i][j].person)
                            {
                                if (((ImageView) node).getImage().getUrl().endsWith("h.png") && !((ImageView) node).getImage().getUrl().endsWith("nh.png"))
                                    node.setVisible(true);
                            }
                            else if (table.house[i][j].obstacle)
                            {
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
    void drawNext(ActionEvent event)
    {
        int row = 5;
        int column = 5;
        char path = pathReal.charAt(start);
        start++;

        UpdateTableNext(row, column, path);
        drawTableInConsole(row, column);

        if(start == pathReal.length())
        {
            next.setDisable(true);
        }
        if(start > 0)
        {
            last.setDisable(false);
        }
    }

    @FXML
    void drawLast(ActionEvent event)
    {
        int row = 5;
        int column = 5;
        start--;
        char path = pathReal.charAt(start);
        if(path == 'U')
            path = 'D';
        else if(path == 'D')
            path = 'U';
        else if(path == 'L')
            path = 'R';
        else if(path == 'R')
            path = 'L';

        UpdateTableLast(row, column, path);
        drawTableInConsole(row, column);

        if(start == 0)
        {
            last.setDisable(true);
        }
        if(start < pathReal.length())
        {
            next.setDisable(false);
        }
    }

    public void drawTableInConsole(int row, int column)
    {
        for(int i = 1; i <= row; i++)
        {
            for(int j = 1; j <= column; j++)
            {
                if(table.house[i][j].robot)
                {
                    System.out.print("R ");
                    continue;
                }
                if(table.house[i][j].butter)
                {
                    System.out.print("B ");
                    continue;
                }
                if(table.house[i][j].person)
                {
                    System.out.print("P ");
                    continue;
                }
                if(table.house[i][j].obstacle)
                {
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
    public void initialize(URL location, ResourceBundle resources)
    {
        updateGUI(5, 5);
    }
}
