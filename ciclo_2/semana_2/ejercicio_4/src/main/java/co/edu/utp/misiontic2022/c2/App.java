package co.edu.utp.misiontic2022.c2;

/**
 * Enum
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        // System.out.println(Color.BLANCO);

        Transporte tp;

        
        tp = Transporte.Tren;
        // System.out.println("El valor de tp: " + tp);
        tp = Transporte.Barco;

        /* 
            if (tp == Transporte.Camion)
                System.out.println("tp tiene el valor de Camion");
            else
                System.out.println("tp tiene el valor de " + tp);
        */
        
        //Enum para control de secuencia switch
        switch(tp){
            case Coche:
                System.out.println("Respuesta es Coche");
                break;
            case Camion:
                System.out.println("Respuesta es Camion");
                break;
            case Avion:
                System.out.println("Respuesta es Avion");
                break;
            case Tren:
                System.out.println("Respuesta es Tren");
                break;
            default:
                System.out.print("Respuesta es Barco");
        }

    }
}
