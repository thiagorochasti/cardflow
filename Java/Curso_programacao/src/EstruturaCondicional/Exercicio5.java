package EstruturaCondicional;
import java.util.Locale;
import java.util.Scanner;

public class Exercicio5 {
    public static void main(String[] args){
//        Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A
//        seguir, calcule e mostre o valor da conta a pagar.
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int cod = sc.nextInt();
        int qtd = sc.nextInt();
        double total,preco;


        if (cod == 1) {
            preco = 4.00;
            total = preco * qtd;
            System.out.printf("Total: R$ %.2f",total);
        }
        else if(cod == 2){
            preco = 4.50;
            total = preco * qtd;
            System.out.printf("Total: R$ %.2f",total);
        }
        else if(cod == 3){
            preco = 5.00;
            total = preco * qtd;
            System.out.printf("Total: R$ %.2f",total);
        }
        else if(cod == 4){
            preco = 2.00;
            total = preco * qtd;
            System.out.printf("Total: R$ %.2f",total);
        }
        else {
            preco = 1.50;
            total = preco * qtd;
            System.out.printf("Total: R$ %.2f",total);
        }



        sc.close();
    }
}
