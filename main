package individual.project;

import java.io.File;
import java.io.FileNotFoundException; import java.io.IOException;
import java.sql.*;
import java.util.ArrayList;
import java.util.NoSuchElementException; import java.util.Scanner;


public static int main_menu() {

  System.out.println ();
  System.out.println("\t\tMenu"); 
  System.out.print("=====================================\n"); 
  System.out.println ("Select one of the following: ");
  System.out.println ("1. Enter department name to display budget");
  System.out.println ("2. Enter department name and new budget amount to update their budget");
  System.out.println ("3. Insert a new department in the department table"); System.out.println ("4. Exit");
  Scanner input = new Scanner (System.in);
  System.out.print ("Enter Your Selection: ");
  int option = input.nextInt();
  
  while (option < 1 || option > 4){ 
    System.out.println ("Invalid Input. Try Again"); 
    option = input.nextInt();
  }

  if (option == 4){
    System.out.println ("Thank you and good bye!"); System.exit(0);
  }
  return option; 
 }
