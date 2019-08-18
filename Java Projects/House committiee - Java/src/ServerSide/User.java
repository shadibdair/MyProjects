package ServerSide;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.net.Socket;
import java.sql.PreparedStatement;
import java.sql.SQLException;

//abstract class 
public abstract class User {

 // Attributes:
 protected ObjectInputStream inObject;
 BufferedReader inFromClient;
 DataOutputStream outToClient;
 Socket incoming;
 String username;
	
 // Constructor:
 public User(ObjectInputStream inObject, BufferedReader inFromClient, DataOutputStream outToClient, Socket incoming, String username) {
     this.inObject = inObject;
     this.inFromClient = inFromClient;
     this.outToClient = outToClient;
     this.incoming = incoming;
     this.username = username;

     PreparedStatement statement;
 }
 
 // Menu: 
 public abstract void menu() throws IOException, SQLException;
}