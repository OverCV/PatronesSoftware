package informes;

import java.time.LocalDate;

/**
 * Informe de una actividad de visión.
 */
public class Planeacion extends Informe {
    public Planeacion(String contenido) {
        super(contenido);
    }

    @Override
    public void imprimir() {
        System.out.println("Informe de PLANEACIÓN ");
        System.out.println("Fecha: "+getFecha());
        System.out.println(getContenido());
    }
}
