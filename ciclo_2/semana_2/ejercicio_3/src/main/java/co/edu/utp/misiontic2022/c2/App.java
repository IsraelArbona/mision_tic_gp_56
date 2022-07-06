package co.edu.utp.misiontic2022.c2;

/**
 * Interfases
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        DeDos objeto = new DeDos();

        for(int i = 0; i < 5; i++)
            System.out.println("El siguiente valor es: " + objeto.getSiguiente());
            System.out.println("El valor anterior a " +objeto.getSiguiente() + " es " + objeto.getAnterior());
        
        System.out.println("\nReiniciando...");
        objeto.reiniciar();

        for(int i = 0; i < 5; i++)
            System.out.println("El siguiente valor es: " + objeto.getSiguiente());
            System.out.println("El valor anterior a " + objeto.getSiguiente() + " es " + objeto.getAnterior());
            System.out.println("\nIniciando en 1000...");

        objeto.setComenzar(1000);

        for(int i = 0; i < 5; i++)
            System.out.println("El siguiente valor es: " + objeto.getSiguiente());
            System.out.println("El valor anterior a " + objeto.getSiguiente() + " es " + objeto.getAnterior());

    }
}
