package co.edu.utp.misiontic2022.c2;

import javax.swing.JButton;
import javax.swing.JFrame;

/**
 * Swing
 * Ejemplo de Swing por asociación dentro del contructor
 *
 */
public class App 
{
    JFrame f;

    App() {
        f = new JFrame();

        JButton b = new JButton("Click");
        b.setBounds(130, 100, 100, 40);

        f.add(b);

        f.setSize(400, 500);
        f.setLayout(null);
        f.setVisible(true);
    }
    public static void main( String[] args )
    {
        new App();
    }
}
