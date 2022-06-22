import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        var sc = new Scanner(System.in);
        System.out.println("Ingrese el numero : ");
        var numero = sc.nextInt();

        var digitos = numeroDigito(numero);
        System.out.println("El número tiene : " + digitos + " cifras");
    }

    public static int numeroDigito(int numero){
        var cifras = 0;

        while (numero != 0){
            numero /= 10;
            cifras++;
        }
        return cifras;
    }
}
