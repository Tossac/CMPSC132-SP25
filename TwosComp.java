/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
import java.util.Scanner;
/**
 *
 * @author mbswo
 */
public class TwosComp {
    
    public static char[] addition(String firstBinary, String secondBinary){
        //find which one is longer
        int length = secondBinary.length();
        
        //first is longer
        if (firstBinary.length() > length){
            length = firstBinary.length();
            secondBinary = embiggen(secondBinary, length);
            
        }
        
        //second is longer
        else{
            firstBinary = embiggen(firstBinary, length);
        }
        
        System.out.println("The decimal sum is:");
        System.out.println(binToDec(firstBinary)+binToDec(secondBinary));
        
        //Twos Comp addition (finally!)
        int carry = 0;
        char[] binarySum = new char[length];
        for (int i=0; i<length; i++)
            binarySum[i]='0';
        
        for (int i=length-1; i>=0; i--){
            //if 0, 0, 0 = 0, 0
            //do nothing, no updates needed
          
            //if 0, 0, 1 = 1, 0
            if (firstBinary.charAt(i) == '0'){
                if (secondBinary.charAt(i) == '0'){
                    if (carry==1){
                        carry=0;
                        binarySum[i]='1';
                    }  
                }
                //0, 1, 0 = 1,0
                else{ //(secondBinary.charAt(i) == '1'){
                    if (carry==0){
                        binarySum[i]='1';
                    }
                    //0, 1, 1 = 0, 1
                    //no updates needed
                }
            }    
            //if 1, 0, 0 = 1, 0
            else{ //(firstBinary.charAt(i) == '1'){
                if (secondBinary.charAt(i) == '0'){
                    if (carry==0){
                        binarySum[i]='1';
                    }
                    //1,0,1 = 0, 1
                    //no update need, carry already 1
                }
                
                else{ //(secondBinary.charAt(i) == '1'){
                    if (carry==0){
                        carry=1;
                    }
                    else{ //carry is 1
                        binarySum[i]='1';
                    }
                    //no updates needed
                }
            
            //if 1, 1, 0 = 0, 1
            //if 1, 1, 1 = 1, 1
            }
        }
        
        //check for overflow
        //if the initial leading digits are the same,
        //but the leading digit of the sum is not,
        //there was an overflow, signified by 'E'RROR at position 0.
        if (firstBinary.charAt(0)==secondBinary.charAt(0)){
            if (firstBinary.charAt(0)!=binarySum[0])
                binarySum[0]='E';
        }
        
        return (binarySum);
    }
    
    private static String embiggen(String binary, int length){
        String converted="";
        
        //initialize leading 0s for positive number, 1s for negative
        for (int i=0; i<length-binary.length(); i++){
            converted+=binary.charAt(0);
        }
        
        //add binary number to leading 0s or 1s        
        return converted+=binary;
    }
    
    
    public static double binToDec(String binary){
        double decimal=0;
        if(binary.charAt(0) == '1')
            decimal-=Math.pow(2, binary.length()-1);
        
        for (int i=1; i<binary.length(); i++){
            //System.out.println(decimal);
            if (binary.charAt(i)=='1'){
                decimal+=Math.pow(2, binary.length()-i-1);
            }
        }
        System.out.println(decimal);
        return decimal;
    }
}
