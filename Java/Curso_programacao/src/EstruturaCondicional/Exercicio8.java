package EstruturaCondicional;
import java.util.Locale;
import java.util.Scanner;

public class Exercicio8 {
    public static void main(String[] args){
//        Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem
//        que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, sem
//        qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.
//        Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e
//        mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double salario = sc.nextDouble();
        double imposto;

        if (salario <= 2000.0) {
            imposto = 0.0;
        }
        else if (salario <= 3000.0) {
            imposto = (salario - 2000.0) * 0.08;
        }
        else if (salario <= 4500.0) {
            imposto = (salario - 3000.0) * 0.18 + 1000.0 * 0.08;
        }
        else {
            imposto = (salario - 4500.0) * 0.28 + 1500.0 * 0.18 + 1000.0 * 0.08;
        }

        if (imposto == 0.0) {
            System.out.println("Isento");
        }
        else {
            System.out.printf("R$ %.2f%n", imposto);
        }

        sc.close();
    }
}
