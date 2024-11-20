package informes;

import java.time.LocalDate;

/**
 * Informe de una actividad de ingeniería.
 */
public class Ejecucion extends Informe{
    public Ejecucion(String contenido) {
        super(contenido);
    }

    @Override
    public void imprimir() {
        System.out.println("Informe de EJECUCIÓN");
        System.out.println("Fecha: "+getFecha());
        System.out.println(getContenido());
    }
}
