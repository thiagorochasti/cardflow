package Modulo1;

import java.util.Locale;
import java.util.Scanner;

public class Exercicios2 {

    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        double pi = 3.14159;
        double A;
        double result;
        //System.out.printf("O valor de PI é %f: ",pi);
        //System.out.printf("%n");


        Scanner sc = new Scanner(System.in);
        A = sc.nextDouble();
        result = pi * Math.pow(A, 2.0);
        System.out.printf("Área =%.4f",result);

        sc.close();

    }
}
