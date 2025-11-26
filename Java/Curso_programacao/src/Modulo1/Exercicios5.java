package Modulo1;

import java.util.Locale;
import java.util.Scanner;

public class Exercicios5 {
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        int peca1;
        int peca2;
        int qtdPeca1;
        int qtdPeca2;
        double valorPeca1;
        double valorPeca2;
        double calc;

        Scanner sc = new Scanner(System.in);
        peca1 = sc.nextInt();
        qtdPeca1 = sc.nextInt();
        valorPeca1 = sc.nextFloat();

        peca2 = sc.nextInt();
        qtdPeca2 = sc.nextInt();
        valorPeca2 = sc.nextFloat();


        calc = (valorPeca1 * qtdPeca1) + (valorPeca2 * qtdPeca2);
        System.out.printf("VALOR A PAGAR: = R$ %.2f",calc);

        sc.close();

    }
}
