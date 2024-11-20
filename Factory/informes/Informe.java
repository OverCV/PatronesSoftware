package informes;

import java.time.LocalDate;

/**
 * Reporte con información consolidada de una actividad realizada.
 */
public abstract class Informe {
    private LocalDate fecha;
    private String contenido;

    public Informe(String contenido) {
        this.fecha = LocalDate.now();
        this.contenido = contenido;
    }

    public LocalDate getFecha() {
        return fecha;
    }

    public String getContenido() {
        return contenido;
    }

    public abstract void imprimir();
}
