(defrule vocacion-ingenieria
  (or (habilidades-matematicas) (resolucion-de-problemas) (disenio-construccion) (mejora-de-procesos))
  =>
  (assert (es-ingenieria))
  (assert (mensaje "Gusto por la resolución de problemas, el diseño y la mejora de procesos."))
)

(defrule vocacion-ciencias-de-la-salud
  (or (cuidado-de-la-salud) (biologia-humana) (servicio-a-los-demas) (investigacion-medica))
  =>
  (assert (es-ciencias-de-la-salud))
  (assert (mensaje "Gusto por la atención de la salud y el servicio a los demás."))
)

(defrule vocacion-ciencias-economicas
  (or (finanzas) (administracion) (comercio) (emprendimiento) (liderazgo))
  =>
  (assert (es-ciencias-economicas))
  (assert (mensaje "Interés por la administración, las finanzas y el emprendimiento."))
)

(defrule arte-disenio-y-comunicacion
  (or (expresion-artistica) (creatividad) (comunicacion-visual) (medios-audiovisuales))
  =>
  (assert (es-arte-disenio-y-comunicacion))
  (assert (mensaje "Gusto por la creación artística o la expresión visual y audiovisual."))
)

(defrule educacion-y-pedagogia
  (or (ensenianza) (comunicacion) (pedagogia) (trabajo-con-personas) (desarrollo-humano))
  =>
  (assert (es-educacion-y-pedagogia))
  (assert (mensaje "Pasión por la enseñanza y el trabajo con personas en el desarrollo humano."))
)

(defrule deporte-y-ciencias-del-ejercicio
  (or (actividad-fisica) (deporte) (salud) (anatomia-humana) (motivacion))
  =>
  (assert (es-deporte-y-ciencias-del-ejercicio))
  (assert (mensaje "Interés por la actividad física, el deporte y la salud."))
)

(defrule ciencias-del-medio-ambiente
  (or (agricultura) (ecologia) (sostenibilidad) (trabajo-al-aire-libre))
  =>
  (assert (es-ciencias-del-medio-ambiente))
  (assert (mensaje "Interés por la naturaleza, la ecología y la sostenibilidad."))
)
