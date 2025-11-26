package EstruturaCondicional;

import java.util.Scanner;

public class Exercicio1 {
    public static void main(String[] args){
//      Fazer um programa para ler um número inteiro, e depois dizer se este número é negativo ou não

        int A;


        Scanner sc = new Scanner(System.in);
        A = sc.nextInt();

        if (A > 0) {
            System.out.printf("NÃO NEGATIVO",A);
        }
        else{
            System.out.printf("NEGATIVO",A);
        }


        sc.close();

    }
}
