package individual.project;

import java.io.File;
import java.io.FileNotFoundException; import java.io.IOException;
import java.sql.*;
import java.util.ArrayList;
import java.util.NoSuchElementException; import java.util.Scanner;

public class TestProject {
  
  public static void main(String[] args) throws SQLException, ClassNotFoundException,FileNotFoundException, IOException {

    ArrayList <Department> department = new ArrayList <>(); 
    ArrayList <Instructor> instructor = new ArrayList <>();

    Database();
    Read_Department(department); 
    Read_Instructor(instructor); 
    main_menu_functions (department, instructor);
   }
   
   public static void Database() throws SQLException, ClassNotFoundException, FileNotFoundException{
       Class.forName("com.mysql.cj.jdbc.Driver");
       Connection connection = DriverManager.getConnection("jdbc:mysql://localhost/", "root", "f7aaa8re9s");
       Statement statement = connection.createStatement();
       statement.executeUpdate("drop database if exists university;"); statement.executeUpdate("create database university;"); statement.executeUpdate("use university;");
       statement.executeUpdate("create table department(dept_name varchar(20),location varchar(10),budget numeric (8,2),primary key (dept_name))"); 
       statement.executeUpdate("create table instructor(id varchar(5),name varchar(20) not null, dept_name varchar(20),primary key (ID),foreign key (dept_name) references department (dept_name) on delete set null)");
       connection.close(); 
   }
   
   // Creating connection to the database for the department using department class
   public static void Read_Department (ArrayList <Department> department) throws SQLException, ClassNotFoundException, FileNotFoundException, IOException {
       Connection connection = DriverManager.getConnection("jdbc:mysql://localhost/", "root", "f7aaa8re9s");
       Statement statement = connection.createStatement(); statement.executeUpdate("use university");

       File file1 = new File("/Users/faresmohamed7/Desktop/department.txt/"); 
       Scanner scanner = new Scanner(file1);
       
       scanner.useDelimiter(",|\\n");
        
       //Scanning the file using try and catch
       while (scanner.hasNext()){
         try {
           String [] Line = scanner.nextLine().split(","); 
           Department department1 = new Department (Line[0], Line[1], Line[2]); 
           
           String deptname = Line[0]; 
           String location = Line[1]; 
           String budget = Line[2];

           //inserting all file contents to department table in database university
           int insert_department = statement.executeUpdate("insert into department values ('"+deptname+"','"+location+"','"+budget+"')");
           department.add(department1); //add file content to arraylist department 
          }

          catch (NoSuchElementException error){ 
             System.out.print ("Error");
             break; 
          }
        }
        scanner.close(); //close file
        connection.close(); //close connection 
    }
      
     // Creating connection to the database for instructor using its class
    public static void Read_Instructor (ArrayList <Instructor> instructor) throws SQLException, ClassNotFoundException, FileNotFoundException, IOException {
        Connection connection = DriverManager.getConnection("jdbc:mysql://localhost/", "root", "f7aaa8re9s");
        Statement statement = connection.createStatement(); statement.executeUpdate("use university");

        File file1 = new File("/Users/faresmohamed7/Desktop/instructor.txt/"); 
        Scanner scanner = new Scanner(file1);
        
        scanner.useDelimiter(",|\\n");

       //Scanning the file using try and catch 
        while (scanner.hasNext()){
        try {
            String [] line = scanner.nextLine().split(","); //split the each line by ","
            Instructor instructor1 = new Instructor (line[0], line[1], line[2]); 
            
            String id = line [0];
            String name = line [1]; 
            String deptname = line [2];

            int insert_instructor = statement.executeUpdate("insert into instructor values ('"+id+"','"+name+"','"+deptname+"')");
            instructor.add(instructor1); //add file content to arraylist instructor 
           }
           
           catch (NoSuchElementException error){ 
              System.out.print ("Error");
              break;
            }
          }
          scanner.close(); //close file
          connection.close(); //close connection 
      }
