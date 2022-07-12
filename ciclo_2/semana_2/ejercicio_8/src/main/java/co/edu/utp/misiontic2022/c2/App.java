package co.edu.utp.misiontic2022.c2;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Colas en java con Queue
 * 
 * Métodos a tener en cuenta
 * 
 * para insertar:
 * - add(e)
 * - offer(e)
 * 
 * para extraer
 * - remove()
 * - poll()
 * 
 * para consultar el frente
 * - element()
 * - peek()
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        // Creamos la Cola indicando el tipo de dato
        Queue<Integer> cola = new LinkedList<>();

        cola.offer(3);      // insertar un elemento (mejor método)
        cola.add(14);       // insertar un elemento (lanza excepciones)
        cola.offer(12);
        cola.add(7);
        cola.offer(10);

        // Imprimir Cola llena de datos
        System.out.println("Cola llena: " + cola);

        while(cola.poll() != null){ // recupera el primer elemento, si es null = vacio
            System.out.println(cola.peek()); // muestra el primer elemento de la cola
        }
    }
}
