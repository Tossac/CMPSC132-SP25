/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
import java.util.Arrays;
import java.util.Scanner;
/**
 *
 * @author mbswo
 */
public class Selfies {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Randos.getRandom();
        //summonTwosComp();
    }
    
    public static void summonTwosComp(){
        Scanner in = new Scanner(System.in);
        
        System.out.println("Please enter the first binary number");
        String firstBinary = in.next();
        System.out.println("Please enter the second binary number");
        String secondBinary = in.next();
        
        //System.out.println("The Twos Complement Sum of them is:");
        System.out.println("The Twos Complement Sum of them is:\n" + Arrays.toString(TwosComp.addition(firstBinary, secondBinary)));
    }
}
