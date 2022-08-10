package individual.project;

import java.io.File;
import java.io.FileNotFoundException; import java.io.IOException;
import java.sql.*;
import java.util.ArrayList;
import java.util.NoSuchElementException; import java.util.Scanner;

// Instructor Class

public class Instructor {

  private String instructor_id; 
  private String instructor_name; 
  private String department;


  public Instructor (){ 
  }
  
  public Instructor (String instructor_id, String instructor_name, String department){
     this.instructor_id = instructor_id; 
     this.instructor_name = instructor_name; 
     this.department = department;
   }
  
  public String getinstructor_id (){
     return instructor_id; 
   }

  public String getinstructor_name (){ 
     return instructor_name;
   }

  public String getdepartment (){
     return department; 
   }
  
  public void setinstructor_id (String Id){
     instructor_id = Id; 
   }

  public void setinstructor_name (String Name){ 
     instructor_name = Name;
   }
  
  public void setdepartment (String dep){
     department = dep; 
   } 
}
  
  public class Department{
     private String dept_name; 
     private String location;
     private String budget;

  public Department(){ 
  
   }
  
  public Department(String dept_name, String location, String budget){
      this.dept_name = dept_name; 
      this.location = location; 
      this.budget = budget;
   }
   
   public String getdept_name(){
      return dept_name; 
   }
   
   public String getlocation(){ 
      return location;
   }
   
   public String getbudget(){ 
      return budget;
   }
   
   public void setdept_name(String name){
      dept_name = name; 
   }

   public void setlocation(String Location){ 
      location = Location;
   }
   
   public void setbudget(String Budget){
      budget = Budget; 
   }
}
