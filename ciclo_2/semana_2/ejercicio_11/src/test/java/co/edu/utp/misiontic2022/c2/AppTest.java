package co.edu.utp.misiontic2022.c2;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

/**
 * Unit test for simple App.
 */
public class AppTest 
{
    /**
     * Rigorous Test :-)
     */
    @Test
    public void shouldAnswerWithTrue()
    {
        Matematicas matematicas = new Matematicas();
        assertEquals("validad",10.0, matematicas.dividir(10.0, 2.0));
    }
}
