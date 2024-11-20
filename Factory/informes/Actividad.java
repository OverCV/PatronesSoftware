package informes;

/**
 * Actividad o tarea que se realiza dentro de un proyecto
 */
public class Actividad {
    private String nombre;
    private char tipo;
    private int duracion;
    private Informe informe;

    public Actividad(String nombre, char tipo, int duración) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.duracion = duración;
    }

    public String getNombre() {
        return nombre;
    }

    /**
     * Dependiendo del tipo de actividad se genera un informe diferente.
     */
    public Informe generarInforme(){
        if (tipo == 'v'){
            this.informe = new Planeacion("Inicio del proyecto: " + nombre);
        } else if (tipo == 'r') {
            this.informe = new Cierre("Análisis del proyecto: " + nombre);
        }
        else {
            this.informe = new Ejecucion("Actividad realizada: " + nombre
                    + " - horas planeadas: " + duracion);
        }
        return this.informe;
    }
}
