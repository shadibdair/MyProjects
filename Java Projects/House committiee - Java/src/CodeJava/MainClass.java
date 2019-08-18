package CodeJava;

public class MainClass {
	
	public static void main(String[] args) {

		Sql sql = new Sql();
		sql.ConectingToSQL();			
	    sql.Login();
	    
		   /*
		      *  1 - Connect java code to MySql
	    	  *  2 - Go to Login() function - if user exists correctly - will move forward to menu (per ternant / manager) 
	       */
	}
}
