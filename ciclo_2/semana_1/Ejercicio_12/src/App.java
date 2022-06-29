public class App {
    public static void main(String[] args) throws Exception {
        Persona persona = new Persona();

        persona.impNombre();
    }
}

class Persona {
    String nombre;
    int edad;

    public void impNombre(){
        System.out.println("Nombre de la persona");
    }
}
