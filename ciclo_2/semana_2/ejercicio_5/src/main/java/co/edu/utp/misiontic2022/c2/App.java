package co.edu.utp.misiontic2022.c2;

/**
 * Arrays
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        /* 
            // Declarar el array
            int[] miArray;

            // Inicializar el array
            miArray = new int[5];

            int[] intArray = {1,2,3,4,5,6,7,8,9,10};

            int[] intArray2 = new int[2];

            intArray2[0] = 10;
            intArray2[1] = 11;

            for(int i = 0; i < intArray2.length; i++){
                System.out.println("Elemento en el indice i : " + i + " es: " + intArray2[i]);
            }

            int[][] matrizCuadrada = new int[3][3];
            int[][] matrizIrregular = new int[3][];

            matrizIrregular[0] = new int[3];
            matrizIrregular[1] = new int[20];
            matrizIrregular[2] = new int[1];

            matrizCuadrada[2][1] = 10;
            matrizIrregular[1][18] = 21;
        */

        ImpresoraTinta[] impresoraTintas = new ImpresoraTinta[3];

        impresoraTintas[0] = new ImpresoraTinta(10);
        impresoraTintas[1] = new ImpresoraTinta(20);
        impresoraTintas[2] = new ImpresoraTinta(30);

        for(int j = 0; j < impresoraTintas.length; j++){
            System.out.println("Velocidad : " + impresoraTintas[j].getVelocidad());
            System.out.println(impresoraTintas[j].toString());
        }
        
    }
}
