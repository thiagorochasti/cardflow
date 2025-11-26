package Modulo1;

import java.util.Locale;
import java.util.Scanner;

public class Exercicios1 {
    public static void main(String[] args){

        int A;
        int B;
        int calc;
        //System.out.printf("O valor de PI é %f: ",pi);
        //System.out.printf("%n");


        Scanner sc = new Scanner(System.in);
        A = sc.nextInt();
        B = sc.nextInt();
        calc = A + B;
        System.out.printf("Soma = %d",calc);

        sc.close();

    }
}
