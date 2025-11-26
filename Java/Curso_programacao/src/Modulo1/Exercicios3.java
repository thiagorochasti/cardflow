package Modulo1;

import java.util.Locale;
import java.util.Scanner;

public class Exercicios3 {
    public static void main(String[] args){

        int A;
        int B;
        int C;
        int D;

        int calc;

        Scanner sc = new Scanner(System.in);
        A = sc.nextInt();
        B = sc.nextInt();
        C = sc.nextInt();
        D = sc.nextInt();

        calc = A * B - C * D;
        System.out.printf("Diferença = %d",calc);

        sc.close();

    }
}
