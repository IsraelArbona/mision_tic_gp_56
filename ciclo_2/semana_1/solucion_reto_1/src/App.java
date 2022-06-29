public class App {
    public static void main(String[] args) throws Exception {

        BecaUniversitaria becaUniversitaria = new BecaUniversitaria();
        System.out.println(becaUniversitaria.calcularInteresSimple());
        System.out.println(becaUniversitaria.calcularInteresCompuesto());
        System.out.println(becaUniversitaria.compararInversion(60, 13000, 1.4));

        System.out.println(becaUniversitaria.calcularInteresSimple());
        System.out.println(becaUniversitaria.calcularInteresCompuesto());
        System.out.println(becaUniversitaria.compararInversion(48, 10000, 2.0));

    }
}



class BecaUniversitaria {

    //----------------------------------
    // Atributos
    //----------------------------------

    /**
     * valor del tiempo
     */
    private int tiempo;

    /**
     * Valor de la Beca Universitaria
     */
    private double monto;

    /**
     * Tasa de interés efectiva mensual del proyecto
     */
    private double interes;

    // -------------------------------------------------
    // Métodos
    // -------------------------------------------------

    /**
     * Contruye el proyecto
     * Se crea un nuevo proyecto de los siguientes valores.
     */
    public BecaUniversitaria(){
        tiempo = 0;
        monto = 0;
        interes = 0;
    }

    public BecaUniversitaria(int pTiempo, double pMonto, double pInteres){
        this.tiempo = pTiempo;
        this.monto = pMonto;
        this.interes = pInteres;
    }

    /**
     * Retorna el interes simple
     * @return el total de intere simple generado en número
     */
    public double calcularInteresSimple() {
        double interesSimple = monto * (interes / 100) * tiempo;
        return Math.round(interesSimple);
    }

    /**
     * Retorna el interes compuesto
     * @return El total de interes compuesto generado en número.
     */
    public double calcularInteresCompuesto() {
        double interesCompuesto = monto * ( Math.pow(1 + interes / 100, tiempo) -1 );
        return Math.round(interesCompuesto);
    }


    /**
     * Método para comparar la diferencia en el total de interes generados para el proyecto.
     * @param pTiempo
     * @param pMonto
     * @param pInteres
     * @return respuesta al reto 1
     */
    public String compararInversion(int pTiempo, double pMonto, double pInteres){
        
        this.tiempo = pTiempo;
        this.monto = pMonto;
        this.interes = pInteres;

        // Cálculo de la diferencia entre tipos de intereses
        double diferencia = calcularInteresCompuesto() - calcularInteresSimple();

        if (diferencia != 0) {
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;
        } else {
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }
    }

    public String compararInversion(){
        double diferencia = 0;

        // Cálculo de la diferencia entre los tipos de intereses
        diferencia = calcularInteresCompuesto() - calcularInteresSimple();

        // Revisar la diferencia obtenida
        if (diferencia != 0){
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;
        } else {
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }
    }

}
