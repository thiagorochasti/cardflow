package EstruturaCondicional;

import java.util.Scanner;

public class Exercicio2 {
    public static void main(String[] args){
//      Fazer um programa para ler um número inteiro e dizer se este número é par ou ímpar

        int A,B;


        Scanner sc = new Scanner(System.in);
        A = sc.nextInt();
        B = sc.nextInt();
//        if (A > B){
//            if (A % B == 0) {
//
//                System.out.println("São multiplos");
//
//            }
//            else{
//                System.out.println("Não são multiplos");
//            }
//        } else if (A < B){
//            if (B % A == 0) {
//
//                System.out.println("São multiplos");
//
//            }
//            else{
//                System.out.println("Não são multiplos");
//            }
//        }
        if (A % B == 0 || B % A == 0) {
            System.out.println("Sao Multiplos");
        }
        else {
            System.out.println("Nao sao Multiplos");
        }




        sc.close();

    }
}
