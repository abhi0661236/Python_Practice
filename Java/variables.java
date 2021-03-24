import java.util.*;

public class Variables{
    int var2; // this variable is instance since it is in a class but outside a method.
    static int var3; // this variable is a static/class variable since it is declared with static keyword and is outside of method/block of code.
    public static void main(String[]args){
        // There are three types of variables in java based on their scope and accesibility.
        // Local variables
        // Instance variables
        // Class/static variables

        int var1 = 23; // variable var1 is local to main function
        System.out.println("var1 is holding the value: " + var1);
        

    }
}