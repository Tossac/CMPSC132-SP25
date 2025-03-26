/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
import java.util.Scanner;
/**
 *
 * @author mbswo
 */
public class Randos {
    public Randos(){
        
        /*
        System.out.println("Would you like a random (N)umber or (L)etter?");
        Scanner in = new Scanner(System.in);
        String type = in.next();
        
        if ("n".equals(type) || "N".equals(type)){
            System.out.println("Enter the max range.");
            int max_range = in.nextInt();
            System.out.println((int)(Math.random()*max_range));
        }
        
        if ("l".equals(type) || "L".equals(type)){
            
        }*/
    }
    //max_range 
    
    public static void getRandom(){
        System.out.println("Would you like a random (N)umber or (L)etter?");
        Scanner in = new Scanner(System.in);
        String type = in.next();
        System.out.println("How many would you like to generate?");
        int iterations = in.nextInt();
        
        Randomize(type, iterations);
        
        /*
        if ("n".equals(type) || "N".equals(type)){
            System.out.println("Enter the max range.");
            int max_range = in.nextInt();
            System.out.println((int)(Math.random()*max_range));
        }
        
        else if ("l".equals(type) || "L".equals(type)){
            //"00" + str(random.randint(1,27)+64)
            System.out.println((char)(Math.random()*26+64));
        }*/
    }
    
    public static void Randomize(String type, int iterations){
        int max_range=0;
        Scanner in = new Scanner(System.in);
        
        if ("n".equals(type) || "N".equals(type)){
            System.out.println("Enter the max range.");
            max_range = in.nextInt();
            
        }
        
        else if ("l".equals(type) || "L".equals(type)){
            max_range = 26+64;
        }
        
        for(int i=0; i<iterations; i++)
                System.out.println((int)(Math.random()*max_range));
    }
}

