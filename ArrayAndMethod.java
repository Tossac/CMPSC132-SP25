/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/**
 *
 * @author Alex Hall
 * CMPSC 132 - Spring 2025
 * Assignment 2
 * 
 * Program for intuitive Array Addition
 */

//Write a Java class called ArrayAndMethod that has two functions:
//the main function and a function called array_addition.

import java.util.Scanner;

public class ArrayAndMethod {
    //You should use a static variable to define the maximum array length for the two arrays.
    static int MAX_LENGTH = 5;
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        
        //Please make sure to allocate all the arrays using "new" inside the main function before you populate the array with values.
        int[] firstArray = new int[MAX_LENGTH];
        int[] secondArray = new int[MAX_LENGTH];
        Scanner in;
        
        //Next, you should ask the user to input values for each array element and populate the arrays A and B.
        System.out.println("Please enter " + MAX_LENGTH + " integer values for each array, A and B.");
        
        //You need to read the two arrays from inside the main function.
        System.out.println("Array A:");
        for (int i=0; i<MAX_LENGTH; i++){
            
            in = new Scanner(System.in);
            //While reading input, please make sure to check if all the numbers are integers.
            //If there is a double value provided, then your program should send an appropriate message to the user and allow him/her to re-enter another value.
            while (!in.hasNextInt()){
                System.out.println("That is not a valid integer.");
                in = new Scanner(System.in);
            }
            firstArray[i] = in.nextInt();
        }
        
        //You need to read the two arrays from inside the main function.
        System.out.println("Array B:");
        for (int i=0; i<MAX_LENGTH; i++){
            
            in = new Scanner(System.in);
            //While reading input, please make sure to check if all the numbers are integers.
            //If there is a double value provided, then your program should send an appropriate message to the user and allow him/her to re-enter another value.
            while (!in.hasNextInt()){
                System.out.println("That is not a valid integer.");
                in = new Scanner(System.in);
            }
            secondArray[i] = in.nextInt();
        }
        
        firstArray = array_addition(firstArray, secondArray);
        
        //Once you return from the array_addition to main, inside the main, you need to
        //print the values array returned from the function array_addition
        System.out.println("The addition of these Arrays is:");
        for (int i=0; i<MAX_LENGTH; i++)
            System.out.print(firstArray[i] + " ");
        

        
        
        
        //All the arrays will be equal in length.
    }
    
    //The purpose of the function array_addition is to take two integer arrays as arguments,
    //add them item by item, and then return the result in one of the two arrays.
    //A = {1,2,3,4,5} and array B ={5,6,7,8,9} should equal "C" = {6,8,10,12,14}
    public static int[] array_addition(int[] ArrayOne, int[] ArrayTwo){
        for (int i=0; i<MAX_LENGTH; i++){
            ArrayOne[i] = ArrayOne[i] + ArrayTwo[i];
        }
        return ArrayOne;
    }
    
/*    
Write a Java class called ArrayAndMethod that has two functions: the main function and a function called array_addition. The purpose of the function array_addition is to take two integer arrays as arguments, add them item by item, and then return the result in one of the two arrays.

You need to read the two arrays from inside the main function. All the arrays will be equal in length. Let's say you have an array A = {1,2,3,4,5} and array B ={5,6,7,8,9} where the array length is equal or 5 in this case

If you call the function from main A=array_addition(A, B) then A would have the values [Please note you can also call the function like B=array_addition(A, B) in that case, B array would have the results] 

A[0] = A[0]+ B[0] = 1+5 =6

A[1]= A[1]+ B[1] = 2+6 =8

A[2]= A[2]+ B[2] = 3+7=10

A[3]= A[3]+ B[3] = 4+8 =12

A[4]= A[4]+ B[4] = 5+9= 14






 (array A in the case of the above example).
*/
}
