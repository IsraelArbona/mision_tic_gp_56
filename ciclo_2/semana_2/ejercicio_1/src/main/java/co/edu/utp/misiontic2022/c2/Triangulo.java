package co.edu.utp.misiontic2022.c2;

public class Triangulo extends Figura {

    // Se definen los atributos: "base" y "altura" 
    private Double base;
    private Double altura;

    // Constructor de la clase "Triangulo"
    public Triangulo(String color, Double base, Double altura){
        // Toma de la clase abtracta "Figura" (super) el (metodo) constructor "color"
        super(color);
        this.base = base;
        this.altura = altura;
    }

    // Método que fue definido en la clase abstracta "Figura"

    public Double calcularArea(){
        return (base * altura) / 2;
    }
    
}
