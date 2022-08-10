package co.edu.utp.misiontic2022.c2;

import java.awt.event.*;
import javax.swing.*;

/**
 * Swing
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        JFrame f = new JFrame("Ejemplo de componentes");

        JLabel lTf,lBima;

        lTf = new JLabel("Caja Texto");
        lTf.setBounds(50, 30, 150, 20);
        JTextField tf = new JTextField();
        tf.setBounds(50, 50, 150, 20);

        JButton b = new JButton("Click");
        b.setBounds(50, 100, 100, 30);
        b.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent arg0) {
                tf.setText("Grupo 56");
            }
        });

        lBima = new JLabel("Button Imagen");
        lBima.setBounds(50, 180, 250, 20);
        JButton bIma = new JButton(new ImageIcon("./mintic.png"));
        bIma.setBounds(50, 200, 250, 120);

        f.add(tf);
        f.add(b);
        f.add(bIma);
        f.add(lTf);
        f.add(lBima);
        f.setSize(500, 500);
        f.setLayout(null);
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    }
}
