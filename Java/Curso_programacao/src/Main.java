import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){

//        double y = 10000;
//        double x = 30000;
//        double media = (x + y) /2.0;

        //System.out.printf("A média é? ", String.valueOf(media));
        //System.out.printf("%n");
//        String nome = "Maria";
//        int idade = 31;
//        double renda = 4000.0;
        //System.out.printf("%s tem %d anos e ganha R$ %.2f reais%n", nome, idade, renda);

//        String product1 = "Computer";
//        String product2 = "Office Desk";
//
//        int age = 30;
//        int code = 5290;
//        char gender = 'F';
//
//        double price1 = 2100.0;
//        double price2 = 650.50;
//        double measure = 53.234567;

//        System.out.printf("Products:");
//        System.out.printf("%n");
//        System.out.printf("%s, wich price is $ %.2f",product1,price1);
//        System.out.printf("%n");
//        System.out.printf("%s, wich price is $ %.2f",product2,price2);
//        System.out.printf("%n");
//        System.out.printf("%n");
//        System.out.printf("Record: ");
//        System.out.printf("%d years old, code %d and gender: %s",age,code,gender);
//        System.out.printf("%n");
//        System.out.printf("%n");
//        System.out.printf("Measure with eight decimal places: %.8f",measure);
//        System.out.printf("%n");
//        System.out.printf("Rouded (three decimal places): %.3f",measure);
//        System.out.printf("%n");
//        Locale.setDefault(Locale.US);
//        System.out.printf("US decimal point: %.3f",measure);
//        System.out.printf("%n");
//        System.out.printf("%n");
//        System.out.printf("%n");


//        double a = 5.0;
//        int b;

//        b = (int) a; //casting

//        System.out.println(b);
//    Scanner sc = new Scanner(System.in);

//    String x;
//    int y;
//    double z;
//
//    x = sc.next();
//    y = sc.nextInt();
//    z = sc.nextDouble();
//    Locale.setDefault(Locale.US);
//    System.out.printf("Os dados digitados são: %n");
//        System.out.println(x);
//        System.out.println(y);
//        System.out.println(z);
//
//    sc.close();

//        int x;
//        String s1, s2, s3;
//        x = sc.nextInt();
//        sc.nextLine();
//        s1 = sc.nextLine();
//        s2 = sc.nextLine();
//        s3 = sc.nextLine();
//        System.out.println("DADOS DIGITADOS:");
//        System.out.println(x);
//        System.out.println(s1);
//        System.out.println(s2);
//        System.out.println(s3);
//        sc.close();

        //
        //Funções Matemáticas;

        double x = 3.0;
        double y = 4.0;
        double z = -5.0;
        double A, B, C;
        A = Math.sqrt(x);
        B = Math.sqrt(y);
        C = Math.sqrt(25.0);
        System.out.println("Raiz quadrada de " + x + " = " + A);
        System.out.println("Raiz quadrada de " + y + " = " + B);
        System.out.println("Raiz quadrada de 25 = " + C);
        A = Math.pow(x, y);
        B = Math.pow(x, 2.0);
        C = Math.pow(5.0, 2.0);
        System.out.println(x + " elevado a " + y + " = " + A);
        System.out.println(x + " elevado ao quadrado = " + B);
        System.out.println("5 elevado ao quadrado = " + C);
        A = Math.abs(y);
        B = Math.abs(z);
        System.out.println("Valor absoluto de " + y + " = " + A);
        System.out.println("Valor absoluto de " + z + " = " + B);


    }
}