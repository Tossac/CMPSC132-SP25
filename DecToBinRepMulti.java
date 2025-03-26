/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package dectobinrepmulti;

/**
 *
 * @author mbswo
 */
public class DecToBinRepMulti {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        double i = 0.14159;
        //double carry;
        String iInBinary = "1.";
        
        do{
           i = i * 2;
           if (i >= 1){
               iInBinary = iInBinary + "1";
               i--;
               //System.out.println(carry);
           }
           else
               iInBinary = iInBinary + "0";
           System.out.println(i);
           
        }while (i > 0);
        
        System.out.println(iInBinary);
        System.out.println(iInBinary.length());
    }
    
}
