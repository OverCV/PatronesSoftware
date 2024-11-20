package informes;

import java.util.ArrayList;
import java.util.List;

/**
 * Un proyecto de desarrollo de software, con actividades.
 */
public class Proyecto {
    List<Actividad> actividades;

    public Proyecto (){
        this.actividades = new ArrayList<>();
    }

    public void adicionarActividad(Actividad actividad){
        this.actividades.add(actividad);
    }

    public Actividad getActividad(String nombre) {
        for (Actividad actividad: actividades){
            if (actividad.getNombre().equals(nombre)){
                return actividad;
            }
        }
        return  null;
    }
}
