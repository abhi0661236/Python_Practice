// Demo of instance variable

import java.io.*;

public class instanceVar{
    // This variable will be visible to any child class.
    public String name;
    // Salary variable is visible in instanceVar class only.
    private double salary;

    // The name variable is assigned in the constructor
    // A constructor is the function that have same name as the name of class.

    public instanceVar(String empName){
        name = empName;
    }

    // The salary variable is assigned a value

    public void setSalary(double empSal){
        salary = empSal;
    }

    public void printEmp(){
        System.out.println("name" + name);
        System.out.println("salary" + salary);
    }

    public static void main(String[]args){
        instanceVar object1 = new instanceVar("Shashikant");
        object1.setSalary(34000);
        object1.printEmp();

    }

}