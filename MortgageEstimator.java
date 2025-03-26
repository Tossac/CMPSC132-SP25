/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/**
 *
 * @author Alex Hall
 * MortgageEstimator:
 * a program that computes the mortgage payment every OTHER month given:
 * the amount of the loan (principal), the interest rate, and the number of years required to repay the loan.
 */
import java.util.Scanner;
import java.lang.Math;

public class MortgageEstimator {

    /**
     * @param args the command line arguments
     */
    
    //Write a class called MortgageEstimator and add the main() method to it.
    public static void main(String[] args) {
        //While taking input from the user, make sure to print an error message
        //and exit if the user is entering an integer where the program prompts to enter a double and vice versa.
        //For that, you can use hasNextInt() or hasNextDouble() functions.
        
        //The first input will be the principal of the loan, which will be double.
        double principalOfLoan;
        System.out.println("Enter the Principal (total amount of loan) in 'double' format:");
        Scanner in = new Scanner(System.in);

        if (in.hasNextInt() || !in.hasNextDouble()){
            System.out.println("This is not a valid input");
            System.exit(0);            
        }
        principalOfLoan = in.nextDouble();
        //DEBUG System.out.println(principalOfLoan);
        
        //The second input will be the annual interest rate, which is double as well.
        double annualInterestRate;
        System.out.println("Enter the Annual Interest Rate in 'double' format:");
        in = new Scanner(System.in);

        if (in.hasNextInt() || !in.hasNextDouble()){
            System.out.println("This is not a valid input");
            System.exit(0);                        
        }
        annualInterestRate = in.nextDouble();
        //DEBUG System.out.println(annualInterestRate);
        
        //The third input is the number of years for the loan, which must be an integer.
        int numberOfYears;
        System.out.println("Enter the Number of Years in 'integer' format:");
        in = new Scanner(System.in);

        if (!in.hasNextInt()){
            System.out.println("This is not a valid input");
            System.exit(0);                        
        }
        numberOfYears = in.nextInt();            
        //DEBUG System.out.println(numberOfYears);
        
        //You now have all the data you need to compute the payment every OTHER month
        //and the total amount paid by the end of the mortgage tenure.
        //Use the following formulas to compute the mortgage,
        
        //Formulas for Payment Calculation:
        //N = years x 6 //Number of payments
        int numberOfPayments = numberOfYears * 6;
        
        //R = interest_rate / (6 x 100) //interest rate
        double bimonthlyInterestRate = annualInterestRate / (6 * 100);
        
        //Single payment = principal x (R / (1 – ((1 + R)^-N)))
        //Use pow(a, b) to compute the power of (1 + R) ^-N.
        double singlePayment = principalOfLoan * (bimonthlyInterestRate / (1 - (Math.pow((1 + bimonthlyInterestRate), -numberOfPayments))));
        
        //The total amount paid = Single Payment * N
        double totalAmountPaid = singlePayment * numberOfPayments;
        
        //and display the results (both total and single payment amount) using the println() method.
        System.out.println("The total amount paid by the end of the Mortgage Tenure is: " + totalAmountPaid);
        System.out.println("The single Bimonthly Payment Amount is: " + singlePayment);
        //17.65, 105.91, 100 principal, 10%, 1 year
    }
    
}
