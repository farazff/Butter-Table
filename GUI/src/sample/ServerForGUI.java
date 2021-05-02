package sample;


import java.net.Socket;
import java.net.*;
import java.io.*;

public class ServerForGUI {
    public  int port = 8080;
//    public  String ip = "127.0.0.1";
    public  String mapFileNumber ,pathFileNumber;


    public  void run() {
        try {
            ServerSocket server = new ServerSocket(port);
            System.out.println("GUI Server started\nWaiting for a client ...");
            Socket socket = server.accept();
            System.out.println("Python Client accepted");

            String inputStr=new String(socket.getInputStream().readAllBytes());

            String[] ar=inputStr.split("_",2);
            System.out.println(ar[0]  + "  "+ ar[1]);
             mapFileNumber=ar[0];
             pathFileNumber=ar[1];


            System.out.println("Closing connection");

            socket.close();

        } catch (IOException i) {
            System.out.println(i);
        }


    }
}
