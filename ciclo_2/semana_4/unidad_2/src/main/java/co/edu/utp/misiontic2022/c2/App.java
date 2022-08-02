package co.edu.utp.misiontic2022.c2;

import static java.nio.file.StandardOpenOption.*;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.*;

public class App 
{
    public static void main( String[] args )
    {
        
        /* 
        var f = new File("prueba.txt");

        System.out.println("pathSeparator : " + File.pathSeparator);
        System.out.println("separator : " + File.separator);
        System.out.println("separatorChar : " + File.separatorChar);

        try {
            System.out.println("canRead : " + f.canRead());
            System.out.println("canWrite : " + f.canWrite());
            System.out.println("exists : " + f.exists());
            System.out.println("getName : " + f.getName());

            System.out.println("getParent : " + f.getParent());
            System.out.println("isDirectory : " + f.isDirectory());
            System.out.println("isFile : " + f.isFile());
            System.out.println("length : " + f.length());
        } catch (Exception e) {
            e.printStackTrace();
        }

        */

        
        try {
            File archivo = new File("Numeros.txt");

            if (archivo.createNewFile()){
                System.out.println("Archivo creado: " + archivo.getName());
            } else {
                System.out.println("El archivo ya existe!");
            }

        } catch (Exception e) {
            System.out.println(e);
        }

        




        /* 
        // Convertir de String a byte array
        String s = "Grupo 56";

        byte datos[] = s.getBytes();
        Path p = Paths.get("./prueba_2.txt");

        // Un archivo bytes a bytes desde el BufferedOutputStream quien los convierte de caracteres a bytes
        try (OutputStream out = new BufferedOutputStream(
            // anexar a un archivo existente, crear un archivo si no existe inicialmente
            Files.newOutputStream(p, CREATE,APPEND))){

                out.write(datos,0, datos.length);
                System.out.println("Archivo creado");

            } 
            catch (IOException e) {
            System.out.println(e);
        }

        */

        /* 
        int[][] numeros = { 
            { 1, 2, 3, 4, 5},
            { 6, 7, 8, 9, 10},
            {11, 12, 13, 14, 15},
            {16, 17, 18, 19, 20},
            {21, 22, 23, 24, 25}
        };

        try {
            File numeroArc = new File("Numeros.txt");
            PrintWriter salida = new PrintWriter(numeroArc);

            for(int i = 0; i < numeros.length; i++){
                for(int j = 0; j < numeros[i].length; j++){
                    salida.print(numeros[i][j] + ",");
                }
                salida.println("");
            }
            System.out.println("Archivo escrito.");
            salida.close();
        } catch (Exception e) {
            System.out.println("Errores encontrados: ");
            e.printStackTrace();
        }

        */

        File archivoEli = new File("prueba.txt");

        if (!archivoEli.exists()){
            System.out.println("El archivo no existe");
        } else {
            archivoEli.delete();
            System.out.println("El archivo ha sido eliminado");
        }
    }
}
