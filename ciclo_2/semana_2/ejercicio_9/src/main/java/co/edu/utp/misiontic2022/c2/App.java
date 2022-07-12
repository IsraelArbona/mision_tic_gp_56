package co.edu.utp.misiontic2022.c2;

import java.util.HashMap;
import java.util.Map;

/**
 * HashMap
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        HashMap<Integer,String> m = new HashMap<>();

        m.put(924,"Amilia Núñez");
        m.put(921,"Jose Diaz");
        m.put(700,"Cesar Ramirez");
        m.put(219,"Juan Brito");
        m.put(605,"Esteban Quito");
        m.put(921,"Cindy Trillo");
        m.put(537,"Alan Marquez");

        System.out.println("Los elementos de m son: \n" + m);
        System.out.println(m.get(921));
        System.out.println(m.get(605));

        System.out.println(m.entrySet());

        for(Map.Entry pareja: m.entrySet()){
            System.out.println(pareja);
        }
    }
}
