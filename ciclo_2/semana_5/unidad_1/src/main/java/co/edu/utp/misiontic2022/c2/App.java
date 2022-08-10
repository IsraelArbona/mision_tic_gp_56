package co.edu.utp.misiontic2022.c2;

import javax.swing.*;

/**
 * Swing
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        JFrame ventana = new JFrame(); // creamos una instancia con jframe

        JButton boton = new JButton("Click"); // creamos una instancia con jbutton
        boton.setBounds(130, 100, 100, 40); // x axis, y axis, width, height

        ventana.add(boton); // agregamos el boton dentro del jframe

        ventana.setSize(400, 500); // 400 de width, 500 de height
        ventana.setLayout(null); // asignamos null el managerLayout
        ventana.setVisible(true); // mostrar el jframe

    }
}
