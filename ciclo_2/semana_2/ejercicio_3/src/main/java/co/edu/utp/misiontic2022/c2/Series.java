package co.edu.utp.misiontic2022.c2;

/**
 * Interfases
 * 
 * Define métodos sin cuerpo
 * Implementados por subclases
 * 
 * <(modificador) "public" o "default"> interfase <nombre> (<tipo parametros>)
 * 
 * Donde:
 *      public: para todos los paquetes.
 *      default: No se coloca y solo es vista desde otros miembros del mismo paquete.
 * 
 * Las variable declaradas en un interfaz no son variable de instancia. En cambio, 
 * son implícitamente public, final y static, y deben inicializar. 
 * Por lo tanto, sin esencialmente constantes.
 */

public interface Series {

    int getSiguiente();             // Retorna el siguiente número de la serie
    void reiniciar();               // Reiniciar
    void setComenzar(int x);        // Establecer un valor inicial
    
}
