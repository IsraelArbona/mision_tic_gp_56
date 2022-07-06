package co.edu.utp.misiontic2022.c2;

public class ImpresoraTinta implements Impresora {

    private int velocidad;

    public ImpresoraTinta(int velocidad){
        this.velocidad = velocidad;
    }

    public void imprimir(String texto){
        System.out.println("La impresora de tinta imprime: " + texto);
    }

    public int getVelocidad(){
        return velocidad;
    }

    public String toString(){
        return "[Velocidad = " + velocidad + "]";
    }
    
}
