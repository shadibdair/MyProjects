package Users;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.ObjectOutputStream;
import java.net.Socket;

public class ServerConnector {

    // Attributes:
    private static Socket clientSocket;
    private static DataOutputStream outToServer;
    private static BufferedReader inFromServer;
    private static ObjectOutputStream outToServerObject;

    // Create connection to local host:
    public static void create_connection() throws IOException {
        clientSocket = new Socket("localhost", 4000); //This new object contain a call server
        try {
            outToServer = new DataOutputStream(clientSocket.getOutputStream());
            inFromServer = new BufferedReader(new
                    InputStreamReader(clientSocket.getInputStream()));
            outToServerObject= new ObjectOutputStream(clientSocket.getOutputStream());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static DataOutputStream OutToServer() {
        return outToServer;
    }

    public static BufferedReader InFromServer() {
        return inFromServer;
    }

    public static ObjectOutputStream OutToServerObject(){
        return outToServerObject;
    }

    public static void closeSocket() throws IOException {clientSocket.close();}
}