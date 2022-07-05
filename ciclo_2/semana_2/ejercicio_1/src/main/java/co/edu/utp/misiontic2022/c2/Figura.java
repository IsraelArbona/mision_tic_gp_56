package co.edu.utp.misiontic2022.c2;

public abstract class Figura {

    private String color;

    // Constructor: definir el atributo "color" con un "this" haciendo las veces de setter(mutación)
    public Figura(String color){
        this.color = color;
    }

    // Método vacio para ser implementado desde las subclases
    public abstract Double calcularArea();

    // getter, para acceder al color
    public String getColor(){
        return color;
    }
    
}
