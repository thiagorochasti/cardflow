package Modulo1;

import java.util.Locale;
import java.util.Scanner;

public class Exercicios4 {
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        int numFunc;
        int horasTrab;
        double salario;
        double calc;

        Scanner sc = new Scanner(System.in);
        numFunc = sc.nextInt();
        horasTrab = sc.nextInt();
        salario = sc.nextFloat();


        calc = horasTrab * salario;
        System.out.printf("NUMBER = %d",numFunc);
        System.out.printf("%n");
        System.out.printf("SALARY = U$ %.2f",calc);

        sc.close();

    }
}
