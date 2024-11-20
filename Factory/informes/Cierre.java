package informes;

import java.time.LocalDate;

/**
 * Informe de una actividad de retrospectiva.
 */
public class Cierre extends Informe{
    public Cierre(String contenido) {
        super(contenido);
    }

    @Override
    public void imprimir() {
        System.out.println("Informe de CIEERE");
        System.out.println("Fecha: "+getFecha());
        System.out.println(getContenido());
    }
}
