package co.edu.utp.misiontic2022.c2;

public class Cuadrado extends Figura {

    // Se define el atributo "lado" de la clase
    private Double lado;

    public Cuadrado(String color, Double lado) {
        // Toma de la clase abtracta "Figura" (super) el (metodo) constructor "color"
        super(color);
        this.lado = lado;
    }

    // Método que fue definido en la clase abstracta "Figura"
    public Double calcularArea() {
        return lado * lado;
    }


    
}
