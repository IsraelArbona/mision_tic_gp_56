package co.edu.utp.misiontic2022.c2;

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * try
 * catch
 * finally
 */
public class App {
    public static void main(String[] args) throws Exception {
        /*
            try {
                System.out.println("Intentamos ejecutar el bloque de instrucciones: ");
                System.out.println("Instruccion 1.");
                System.out.println("Instruccion 2.");

            } catch (Exception e) {
                System.out.println("Instruccion que se ejecuta cuando se produce un error");
            } finally{
                System.out.println("Instuccion que se ejecuta finalmente tanto si se produce un error o no.");
            }
        */

        /* 
            int[] array = new int[20];

            try{
                array[-2] = 18;
                int b = 0;
                int a = 18/b;
            } catch(ArrayIndexOutOfBoundsException | ArithmeticException ex){
                System.out.println("Operación invalida: " + ex.getMessage());

            }
        */
        Matematicas matematicas = new Matematicas();
        double c = matematicas.dividir(24, 2);
        System.out.println("El resultado es: " + c);

        Scanner sc = new Scanner(System.in);
        int numero;

        try{
            System.out.println("Ingrese un valor entero");
            numero = sc.nextInt();
            int cuadrado = numero * numero;
            System.out.println("El cuadrado de " + numero + " es: " + cuadrado);
        } catch(InputMismatchException ex){
            System.out.println("Debe ingresar obligatoriamente un número entero.");

        }

    }
}
