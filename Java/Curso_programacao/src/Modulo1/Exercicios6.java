package Modulo1;

import java.util.Locale;
import java.util.Scanner;

public class Exercicios6 {
    public static void main(String[] args){
        Locale.setDefault(Locale.US);

        double A;
        double B;
        double C;
        double triangulo;
        double circulo;
        double trapezio;
        double quadrado;
        double retangulo;
        double pi = 3.14159;

        Scanner sc = new Scanner(System.in);
        A = sc.nextFloat();
        B = sc.nextFloat();
        C = sc.nextFloat();
        //A = b * h triangulo
        //A = π * r^2 circulo
        //A = (B1 + B2) * H / 2 trapezio
        //A = l² quadrado
        //A = b * h

        triangulo   = A * C;
        circulo     = pi * Math.pow(C, 2.0);
        trapezio    = (A + B) * C/2;
        quadrado    = Math.pow(B, 2.0);
        retangulo   = A * B;

        System.out.printf("TRIANGULO: %.3f",triangulo);
        System.out.printf("%nCIRCULO: %.3f",circulo);
        System.out.printf("%nTRAPEZIO: %.3f",trapezio);
        System.out.printf("%nQUADRADO: %.3f",quadrado);
        System.out.printf("%nRETANGULO: %.3f",retangulo);

        sc.close();

    }
}