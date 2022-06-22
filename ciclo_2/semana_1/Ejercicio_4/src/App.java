public class App {
    public static void main(String[] args) throws Exception {

        // Ciclo de for

        /*
            for (inicializacion; condicion; incremento) {
                instrucciones
            }
        */

        /* 
        for (int i = 0; i < 100; i++) {
            System.out.println("Número es : " + i);
        }
        */

        // Ciclo del while

        /*
        var numero = 0;
        while (numero < 100){
            if (numero == 10){
                break;
            }
            System.out.println("Número while es : " + numero);
            numero++;
        }
        */

        // Ciclo del do while
        // Quiero solo imprimir desde el número 100 hasta el número 120.

        /* 
        var numero2 = 0;
        do {
            if ((numero2 >= 100) && (numero2 <= 120)){
                System.out.println("Número do while es : " + numero2);
            }
            numero2++;
        } while (numero2 <= 200);
        */


        var a = 5;
        var b = a++;

        System.out.println("valor de a : " + a);
        System.out.println("valor de b : " + b);

        var c = 5;
        var d = ++c;

        System.out.println("valor de c : " + c);
        System.out.println("valor de d : " + d);

    }
}
