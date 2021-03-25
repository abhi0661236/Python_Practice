// demo of static variable in Java.

import java.util.*;

public class StaticVar{
    // salary variable is private and a static variable.
    private static float salary;

    // department is a constant.
    public static final String DEPARTMENT = "Development"; // final keyword is used to make constant

    public static void main(String[]args){
        salary = 14000;
        System.out.println(salary);
    }
}