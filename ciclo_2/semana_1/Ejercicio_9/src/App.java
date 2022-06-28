public class App {
    public static void main(String[] args) throws Exception {
        String cadena = "        EstoesunaCadenaDeCaracteres      ";

        int longitud = 0;
        longitud = cadena.length();

        System.out.println("La longitud de la cadena es : " + longitud);
        System.out.println("Indice de caracter t: " + cadena.indexOf('t'));
        System.out.println("Posición de caracter '2': " + cadena.charAt(2));

        System.out.println("Devolver una sub-cadena desde la posición 1 hasta la 10: " + cadena.substring(1, 10));
        System.out.println("Devolver la cadena convertida a mayúsculas: " + cadena.toUpperCase());
        System.out.println("Devolver la cadena convertida a minúsculas: " + cadena.toLowerCase());

        System.out.println("Elimina los espacios en blanco al inicio y final de la cadena: " + cadena.trim());
    }
}
