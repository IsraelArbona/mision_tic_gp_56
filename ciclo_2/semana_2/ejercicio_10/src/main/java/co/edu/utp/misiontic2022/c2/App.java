package co.edu.utp.misiontic2022.c2;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        // Crea una referencia Gen para Integers.
        Gen<Integer> iOb;

        // Crrea el objeto Gen<Integer> y asignamos su referencia a iOb.
        // vamos a encapsular el valor 25 dentro del objeto Integer
        iOb = new Gen<Integer>(25);

        // Mostramos el tipo de dato utilizado por iOb
        iOb.mostrarTipo();

        // Obtener el valor de iOb.
        // No se realiza la conversión
        int valor = iOb.getOb();
        System.out.println("Valor: " + valor);

        // Mostrar el tipo de dato utilizado por strOb
        Gen<String> strOb = new Gen<String>("Genericos");

        strOb.mostrarTipo();
        
        String str = strOb.getOb();
        System.out.println("Valor: "+ str);


    }
}


// T es un parámetro de tipo que será reemplazado por un tipo real cuando se crea un objeto de tipo Gen

class Gen<T> {
    // T es el parámetro de tipo generico
    T ob;

    Gen(T o){
        ob = o;
    }

    T getOb(){
        return ob;
    }

    // Muestra el tipo de T
    void mostrarTipo(){
        System.out.println("El tipo de T es: " + ob.getClass().getName());
    }
}