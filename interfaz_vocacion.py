import tkinter as tk
from PIL import Image, ImageTk  # Asegúrate de tener Pillow instalado
from tkinter import messagebox
import clips  # Asegúrate de tener instalada la biblioteca `clipspy`

# Configurar el entorno CLIPS
env = clips.Environment()
env.load("orientacionvocacional.clp")  # Asegúrate de que el archivo `orientacionvocacional.clp` esté en la misma carpeta

# Función para ejecutar CLIPS y determinar el diagnóstico
def ejecutar_clips_vocacional(respuestas):
    env.reset()  # Restablece el entorno

    # Agrega hechos según las respuestas del usuario
    for respuesta in respuestas:
        if respuestas[respuesta]:  # Solo agrega los hechos afirmativos
            env.assert_string(f"({respuesta})")

    env.run()  # Ejecuta las reglas en CLIPS
    
    # Mostrar todos los hechos generados por CLIPS para depuración
    for fact in env.facts():
        print(fact)  # Esto imprime todos los hechos generados

    # Obtener y mostrar los hechos resultantes relacionados con la vocación
    resultados = []  # Lista para almacenar múltiples resultados
    for fact in env.facts():
        if "es-" in str(fact):  # Busca el hecho que indica el diagnóstico
            resultado = str(fact).replace("(es-", "").replace(")", "")  # Formato limpio
            resultados.append(resultado.capitalize())

    if resultados:
        # Mostrar los resultados en un mensaje
        messagebox.showinfo("Resultado", "Los resultados de la orientación vocacional son:\n" + "\n".join(resultados))
    else:
        # Si no se pudo determinar ninguna vocación
        messagebox.showinfo("Resultado", "No se pudo determinar su vocación.")

# Función para manejar la recopilación de respuestas
def iniciar_diagnostico_vocacional():
    respuestas = {
        "habilidades-matematicas": habilidades_matematicas_var.get(),
        "resolucion-de-problemas": resolucion_de_problemas_var.get(),
        "disenio-construccion": disenio_construccion_var.get(),
        "mejora-de-procesos": mejora_de_procesos_var.get(),

        "cuidado-de-la-salud": cuidado_de_la_salud_var.get(),
        "biologia-humana": biologia_humana_var.get(),
        "servicio-a-los-demas": servicio_a_los_demas_var.get(),
        "investigacion-medica": investigacion_medica_var.get(),

        "finanzas": finanzas_var.get(),
        "administracion": administracion_var.get(),
        "comercio": comercio_var.get(),
        "emprendimiento": emprendimiento_var.get(),
        "liderazgo": liderazgo_var.get(),

        "expresion-artistica": expresion_artistica_var.get(),
        "creatividad": creatividad_var.get(),
        "comunicacion-visual": comunicacion_visual_var.get(),
        "medios-audiovisuales": medios_audiovisuales_var.get(),

        "ensenianza": ensenianza_var.get(),
        "comunicacion": comunicacion_var.get(),
        "pedagogia": pedagogia_var.get(),
        "trabajo-con-personas": trabajo_con_personas_var.get(),
        "desarrollo-humano": desarrollo_humano_var.get(),

        "actividad-fisica": actividad_fisica_var.get(),
        "deporte": deporte_var.get(),
        "salud": salud_var.get(),
        "anatomia-humana": anatomia_humana_var.get(),
        "motivacion": motivacion_var.get(),

        "agricultura": agricultura_var.get(),
        "ecologia": ecologia_var.get(),
        "sostenibilidad": sostenibilidad_var.get(),
        "trabajo-al-aire-libre": trabajo_al_aire_libre_var.get()
    }
    
    ejecutar_clips_vocacional(respuestas)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Sistema Experto de Orientacion Vocacional")
ventana.geometry("1000x900")
ventana.configure(bg="#f0f8ff")

# Cargar y mostrar la imagen en la interfaz
image = Image.open("vocacion.jpeg")  # Asegúrate de que la imagen exista
image = image.resize((300, 200))  # Ajusta el tamaño según tus necesidades
photo = ImageTk.PhotoImage(image)  
image_label = tk.Label(ventana, image=photo, bg="#f0f8ff")
image_label.image = photo  
image_label.pack(pady=10)

# Título y descripción
titulo_label = tk.Label(ventana, text="Identificador de Intereses Vocacionales", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#004d00")
titulo_label.pack(pady=10)

descripcion_label = tk.Label(ventana, text="Selecciona tus principales intereses y presiona 'Determinar Vocacion'.", 
                             font=("Arial", 10), bg="#f0f8ff", fg="#333333")
descripcion_label.pack(pady=5)

# Variables para almacenar las respuestas del usuario
habilidades_matematicas_var = tk.BooleanVar()
resolucion_de_problemas_var = tk.BooleanVar()
disenio_construccion_var = tk.BooleanVar()
mejora_de_procesos_var = tk.BooleanVar()

cuidado_de_la_salud_var = tk.BooleanVar()
biologia_humana_var = tk.BooleanVar()
servicio_a_los_demas_var = tk.BooleanVar()
investigacion_medica_var = tk.BooleanVar()

finanzas_var = tk.BooleanVar()
administracion_var = tk.BooleanVar()
comercio_var = tk.BooleanVar()
emprendimiento_var = tk.BooleanVar()
liderazgo_var = tk.BooleanVar()

expresion_artistica_var = tk.BooleanVar()
creatividad_var = tk.BooleanVar()
comunicacion_visual_var = tk.BooleanVar()
medios_audiovisuales_var = tk.BooleanVar()

ensenianza_var = tk.BooleanVar()
comunicacion_var = tk.BooleanVar()
pedagogia_var = tk.BooleanVar()
trabajo_con_personas_var = tk.BooleanVar()
desarrollo_humano_var = tk.BooleanVar()

actividad_fisica_var = tk.BooleanVar()
deporte_var = tk.BooleanVar()
salud_var = tk.BooleanVar()
anatomia_humana_var = tk.BooleanVar()
motivacion_var = tk.BooleanVar()

agricultura_var = tk.BooleanVar()
ecologia_var = tk.BooleanVar()
sostenibilidad_var = tk.BooleanVar()
trabajo_al_aire_libre_var = tk.BooleanVar()

# Preguntas al usuario
tk.Label(ventana, text="Selecciona tus principales intereses:", font=("Arial", 12), bg="#f0f8ff", fg="#333333").pack(pady=10)

# Marco donde se colocarán los checkbuttons
checkbutton_frame = tk.Frame(ventana, bg="#f0f8ff")
checkbutton_frame.pack()

# Crear los checkbuttons en una cuadrícula de 4 columnas
checkbutton_texts = [
    ("Habilidades matemáticas", habilidades_matematicas_var),
    ("Resolución de problemas", resolucion_de_problemas_var),
    ("Diseño y construcción", disenio_construccion_var),
    ("Mejora de procesos", mejora_de_procesos_var),
    
    ("Cuidado de la salud", cuidado_de_la_salud_var),
    ("Biología humana", biologia_humana_var),
    ("Servicio a los demás", servicio_a_los_demas_var),
    ("Investigación médica", investigacion_medica_var),
    
    ("Finanzas", finanzas_var),
    ("Administración", administracion_var),
    ("Comercio", comercio_var),
    ("Emprendimiento", emprendimiento_var),
    
    ("Expresión artística", expresion_artistica_var),
    ("Creatividad", creatividad_var),
    ("Comunicación visual", comunicacion_visual_var),
    ("Medios audiovisuales", medios_audiovisuales_var),
    
    ("Enseñanza", ensenianza_var),
    ("Comunicación", comunicacion_var),
    ("Pedagogía", pedagogia_var),
    ("Trabajo con personas", trabajo_con_personas_var),
    
    ("Actividad física", actividad_fisica_var),
    ("Deporte", deporte_var),
    ("Salud", salud_var),
    ("Anatomía humana", anatomia_humana_var),
    
    ("Agricultura", agricultura_var),
    ("Ecología", ecologia_var),
    ("Sostenibilidad", sostenibilidad_var),
    ("Trabajo al aire libre", trabajo_al_aire_libre_var)
]

# Crear los checkbuttons
for i, (text, var) in enumerate(checkbutton_texts):
    tk.Checkbutton(checkbutton_frame, text=text, variable=var, font=("Arial", 10), bg="#f0f8ff").grid(row=i//4, column=i%4, padx=10, pady=5)

# Botón para iniciar diagnóstico
tk.Button(ventana, text="Determinar Vocación", font=("Arial", 14, "bold"), command=iniciar_diagnostico_vocacional).pack(pady=20)

# Ejecutar la interfaz
ventana.mainloop()
