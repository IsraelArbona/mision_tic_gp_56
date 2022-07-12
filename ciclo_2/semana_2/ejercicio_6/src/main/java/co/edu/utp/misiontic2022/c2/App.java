package co.edu.utp.misiontic2022.c2;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * List
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        ArrayList<Integer> listaEntero = new ArrayList<>();
        // var ArrayList<Integer> lista = new ArrayList<>();

        listaEntero.add(4);
        listaEntero.add(5);
        listaEntero.add(7);
        listaEntero.add(3,6);

        System.out.println("La longitud de la lista es de: " + listaEntero.size());

        Scanner sc = new Scanner(System.in);
        System.out.println("Introduzca el número a buscar: ");
        int buscar = sc.nextInt();


        if(!listaEntero.isEmpty()){
            if (listaEntero.contains(buscar) == true){
                System.out.println(buscar + " Si esta");
                System.out.println(buscar + " Esta en la posición: " + listaEntero.indexOf(buscar));
            } else {
                System.out.println(buscar + " No esta");
            }
    
            for(int i = 0; i < listaEntero.size(); i++){
                if(listaEntero.get(i) == buscar){
                    System.out.println(buscar + " Si esta y su posición es: " + listaEntero.indexOf(buscar));
                }
            }
        } else {
            System.out.println("La lista esta vacia");
        }




        /*
            for(Integer entero: listaEntero){
                System.out.println(entero);
            }
        */

    }
}
