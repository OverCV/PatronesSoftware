package informes;

public class ControlProyectos {

    public static void main(String[] args) {
        Proyecto proyecto = new Proyecto();
        proyecto.adicionarActividad(new Actividad("Visión",'v',4));
        proyecto.adicionarActividad(new Actividad("Entrevista usuario",'i',2));
        proyecto.adicionarActividad(new Actividad("Especificar ítems",'i',2));
        proyecto.adicionarActividad(new Actividad("Retrospectiva",'r',2));

        Actividad actividad = proyecto.getActividad("Entrevista usuario");
        Informe informe = actividad.generarInforme();
        informe.imprimir();

    }
}
