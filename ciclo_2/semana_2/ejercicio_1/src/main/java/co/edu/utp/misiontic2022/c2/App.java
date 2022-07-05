package co.edu.utp.misiontic2022.c2;

import java.util.Scanner;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        /*
           MiPrimerClase mpc = new MiPrimerClase();
           MiPrimerClase mpc2 = new MiPrimerClase(50);
           MiPrimerClase mpc3 = new MiPrimerClase(12,24);
           
           mpc.incrementarContador(5);
           System.out.println("Valor atributo contador : " + mpc.getContador());
           mpc.setContador(20);
           System.out.println("Valor atributo contador : " + mpc.getContador());

           System.out.println("mpc2 atributo : " + mpc2.getContador());
           mpc2.incrementarContador(50);
           System.out.println("mpc2 atributo : " + mpc2.getContador());

           System.out.println("mpc3 atributo : " +mpc3.getContador());
           System.out.println("mpc3 atributo numero Horas : " + mpc3.getNumHoras());
        */

        // Declarar variables

        /* 
            String colorTriangulo;
            Double baseTriangulo;
            Double alturaTriangulo;

            Scanner sc = new Scanner(System.in);

            System.out.print("Ingrese el color del triángulo: ");
            colorTriangulo = sc.nextLine();

            System.out.print("Ingrese la base del triángulo: ");
            baseTriangulo = sc.nextDouble();

            System.out.print("Ingrese la altura del triángulo: ");
            alturaTriangulo = sc.nextDouble();

            Triangulo triangulo = new Triangulo(colorTriangulo, baseTriangulo, alturaTriangulo);

            System.out.printf("El área del triángulo %s es : %f",triangulo.getColor(), triangulo.calcularArea());

            sc.close();
        */


        // Declarar variables
        String colorCua;
        Double ladoCua;

        Scanner sc = new Scanner(System.in);

        System.out.print("Introduzca el color del cuadrado: ");
        colorCua = sc.nextLine();

        System.out.print("Introduzca el lado del cuadrado: ");
        ladoCua = sc.nextDouble();

        Cuadrado cuadrado = new Cuadrado(colorCua, ladoCua);

        System.out.printf("El área del cuadrado %s es: %f", cuadrado.getColor(),cuadrado.calcularArea());

        sc.close();

    }
}
