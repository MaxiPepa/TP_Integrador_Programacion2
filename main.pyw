from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from unittest import TestCase
from class_alumno import *
from class_directivo import *
from class_docente import *
from class_personal import *

#-----Funciones-----#

def close_frame(frame):
    frame.destroy()

#-----Funciones-----#

#-----Ventana-----#

root = Tk()
root.geometry("850x600")
root.resizable(0,0)
root.title("Sist. de organización Colegio Chester")

#-----Ventana-----#

#-----Título-----#

title_text = Label(root, text = "Bienvenid@, seleccione una opción", font = (20))
title_text.pack(pady=10)

#-----Título-----#

#-----Pestañas-----#

panel = ttk.Notebook(root)
panel.pack(fill = "both", expand = "yes")

tab1 = ttk.Frame(panel)
panel.add(tab1, text = "Incorporar alumno")

tab2 = ttk.Frame(panel)
panel.add(tab2, text = "Incorporar directivo")

tab3 = ttk.Frame(panel)
panel.add(tab3, text = "Incorporar docente")

tab4 = ttk.Frame(panel)
panel.add(tab4, text = "Incorporar personal")

tab5 = ttk.Frame(panel)
panel.add(tab5, text = "Mostrar alumnos")

tab6 = ttk.Frame(panel)
panel.add(tab6, text = "Mostrar directivos")

tab7 = ttk.Frame(panel)
panel.add(tab7, text = "Mostrar docentes")

tab8 = ttk.Frame(panel)
panel.add(tab8, text = "Mostrar personal")

#-----Pestañas-----#

#-----Incorporar alumno-----#

label_nombre_alumno = ttk.Label(tab1, text="Nombre:")
label_nombre_alumno.grid(row=0, column=0, padx=10, pady=10)
entry_nombre_alumno = ttk.Entry(tab1)
entry_nombre_alumno.grid(row=0, column=1, padx=10, pady=10)

label_apellido_alumno = ttk.Label(tab1, text="Apellido:")
label_apellido_alumno.grid(row=1, column=0, padx=10, pady=10)
entry_apellido_alumno = ttk.Entry(tab1)
entry_apellido_alumno.grid(row=1, column=1, padx=10, pady=10)

label_dni_alumno = ttk.Label(tab1, text="DNI:")
label_dni_alumno.grid(row=2, column=0, padx=10, pady=10)
entry_dni_alumno = ttk.Entry(tab1)
entry_dni_alumno.grid(row=2, column=1, padx=10, pady=10)

label_direccion_alumno = ttk.Label(tab1, text="Direccion:")
label_direccion_alumno.grid(row=3, column=0, padx=10, pady=10)
entry_direccion_alumno = ttk.Entry(tab1)
entry_direccion_alumno.grid(row=3, column=1, padx=10, pady=10)

label_telefono_alumno = ttk.Label(tab1, text="Teléfono:")
label_telefono_alumno.grid(row=4, column=0, padx=10, pady=10)
entry_telefono_alumno = ttk.Entry(tab1)
entry_telefono_alumno.grid(row=4, column=1, padx=10, pady=10)

label_email_alumno = ttk.Label(tab1, text="Email:")
label_email_alumno.grid(row=5, column=0, padx=10, pady=10)
entry_email_alumno = ttk.Entry(tab1)
entry_email_alumno.grid(row=5, column=1, padx=10, pady=10)

label_nacionalidad_alumno = ttk.Label(tab1, text="Nacionalidad:")
label_nacionalidad_alumno.grid(row=6, column=0, padx=10, pady=10)
entry_nacionalidad_alumno = ttk.Entry(tab1)
entry_nacionalidad_alumno.grid(row=6, column=1, padx=10, pady=10)

label_residencia_alumno = ttk.Label(tab1, text="Residencia:")
label_residencia_alumno.grid(row=7, column=0, padx=10, pady=10)
entry_residencia_alumno = ttk.Entry(tab1)
entry_residencia_alumno.grid(row=7, column=1, padx=10, pady=10)

label_cant_hermanos_alumno = ttk.Label(tab1, text="Cantidad de hermanos insciptos al colegio:")
label_cant_hermanos_alumno.grid(row=8, column=0, padx=10, pady=10)
entry_cant_hermanos_alumno = ttk.Entry(tab1)
entry_cant_hermanos_alumno.grid(row=8, column=1, padx=10, pady=10)

label_telf_madre_alumno = ttk.Label(tab1, text="Teléfono de la madre:")
label_telf_madre_alumno.grid(row=9, column=0, padx=10, pady=10)
entry_telf_madre_alumno = ttk.Entry(tab1)
entry_telf_madre_alumno.grid(row=9, column=1, padx=10, pady=10)

label_telf_padre_alumno = ttk.Label(tab1, text="Teléfono del padre:")
label_telf_padre_alumno.grid(row=10, column=0, padx=10, pady=10)
entry_telf_padre_alumno = ttk.Entry(tab1)
entry_telf_padre_alumno.grid(row=10, column=1, padx=10, pady=10)

label_telf_adicional_alumno = ttk.Label(tab1, text="Teléfono adicional:")
label_telf_adicional_alumno.grid(row=11, column=0, padx=10, pady=10)
entry_telf_adicional_alumno = ttk.Entry(tab1)
entry_telf_adicional_alumno.grid(row=11, column=1, padx=10, pady=10)

button_agregar_alumno = ttk.Button(tab1, text = "Agregar")
button_agregar_alumno.grid(row=12)

#-----Incorporar alumno-----#

#-----Incorporar directivo-----#

label_nombre_directivo = ttk.Label(tab2, text="Nombre:")
label_nombre_directivo.grid(row=0, column=0, padx=10, pady=10)
entry_nombre_directivo = ttk.Entry(tab2)
entry_nombre_directivo.grid(row=0, column=1, padx=10, pady=10)

label_apellido_directivo = ttk.Label(tab2, text="Apellido:")
label_apellido_directivo.grid(row=1, column=0, padx=10, pady=10)
entry_apellido_directivo = ttk.Entry(tab2)
entry_apellido_directivo.grid(row=1, column=1, padx=10, pady=10)

label_direccion_directivo = ttk.Label(tab2, text="Direccion:")
label_direccion_directivo.grid(row=2, column=0, padx=10, pady=10)
entry_direccion_directivo = ttk.Entry(tab2)
entry_direccion_directivo.grid(row=2, column=1, padx=10, pady=10)

label_dni_directivo = ttk.Label(tab2, text="DNI:")
label_dni_directivo.grid(row=3, column=0, padx=10, pady=10)
entry_dni_directivo = ttk.Entry(tab2)
entry_dni_directivo.grid(row=3, column=1, padx=10, pady=10)

label_telefono_directivo = ttk.Label(tab2, text="Teléfono:")
label_telefono_directivo.grid(row=4, column=0, padx=10, pady=10)
entry_telefono_directivo = ttk.Entry(tab2)
entry_telefono_directivo.grid(row=4, column=1, padx=10, pady=10)

label_telf_urgencia_directivo = ttk.Label(tab2, text="Teléfono urgencia:")
label_telf_urgencia_directivo.grid(row=5, column=0, padx=10, pady=10)
entry_telf_urgencia_directivo = ttk.Entry(tab2)
entry_telf_urgencia_directivo.grid(row=5, column=1, padx=10, pady=10)

es_docente = bool()
label_es_docente_directivo = ttk.Label(tab2, text="¿Es docente?:")
label_es_docente_directivo.grid(row=6, column=0, padx=10, pady=10)
radiobutton1_es_docente_directivo = Radiobutton(tab2, text = "Si", variable=es_docente, value=True)
radiobutton1_es_docente_directivo.grid(row=6, column=1, padx=10, pady=10)
radiobutton2_es_docente_directivo = Radiobutton(tab2, text = "No", variable=es_docente, value=False)
radiobutton2_es_docente_directivo.grid(row=6, column=2, padx=10, pady=10)

button_agregar_directivo = ttk.Button(tab2, text = "Agregar")
button_agregar_directivo.grid(row=7)

#-----Incorporar directivo-----#

#-----Incorporar docente-----#

label_nombre_docente = ttk.Label(tab3, text="Nombre:")
label_nombre_docente.grid(row=0, column=0, padx=10, pady=10)
entry_nombre_docente = ttk.Entry(tab3)
entry_nombre_docente.grid(row=0, column=1, padx=10, pady=10)

label_apellido_docente = ttk.Label(tab3, text="Apellido:")
label_apellido_docente.grid(row=1, column=0, padx=10, pady=10)
entry_apellido_docente = ttk.Entry(tab3)
entry_apellido_docente.grid(row=1, column=1, padx=10, pady=10)

label_direccion_docente = ttk.Label(tab3, text="Direccion:")
label_direccion_docente.grid(row=2, column=0, padx=10, pady=10)
entry_direccion_docente = ttk.Entry(tab3)
entry_direccion_docente.grid(row=2, column=1, padx=10, pady=10)

label_dni_docente = ttk.Label(tab3, text="DNI:")
label_dni_docente.grid(row=3, column=0, padx=10, pady=10)
entry_dni_docente = ttk.Entry(tab3)
entry_dni_docente.grid(row=3, column=1, padx=10, pady=10)

label_telefono_docente = ttk.Label(tab3, text="Teléfono:")
label_telefono_docente.grid(row=4, column=0, padx=10, pady=10)
entry_telefono_docente = ttk.Entry(tab3)
entry_telefono_docente.grid(row=4, column=1, padx=10, pady=10)

label_telf_urgencia_docente = ttk.Label(tab3, text="Teléfono urgencia:")
label_telf_urgencia_docente.grid(row=5, column=0, padx=10, pady=10)
entry_telf_urgencia_docente = ttk.Entry(tab3)
entry_telf_urgencia_docente.grid(row=5, column=1, padx=10, pady=10)

label_materia_docente = ttk.Label(tab3, text="Materia:")
label_materia_docente.grid(row=6, column=0, padx=10, pady=10)
entry_materia_docente = ttk.Entry(tab3)
entry_materia_docente.grid(row=6, column=1, padx=10, pady=10)

label_titulo_docente = ttk.Label(tab3, text="Título:")
label_titulo_docente.grid(row=7, column=0, padx=10, pady=10)
entry_titulo_docente = ttk.Entry(tab3)
entry_titulo_docente.grid(row=7, column=1, padx=10, pady=10)

button_agregar_docente = ttk.Button(tab3, text = "Agregar")
button_agregar_docente.grid(row=8)

#-----Incorporar docente-----#

#-----Incorporar personal-----#

label_nombre_personal = ttk.Label(tab4, text="Nombre:")
label_nombre_personal.grid(row=0, column=0, padx=10, pady=10)
entry_nombre_personal = ttk.Entry(tab4)
entry_nombre_personal.grid(row=0, column=1, padx=10, pady=10)

label_apellido_personal = ttk.Label(tab4, text="Apellido:")
label_apellido_personal.grid(row=1, column=0, padx=10, pady=10)
entry_apellido_personal = ttk.Entry(tab4)
entry_apellido_personal.grid(row=1, column=1, padx=10, pady=10)

label_telefono_personal = ttk.Label(tab4, text="Teléfono:")
label_telefono_personal.grid(row=2, column=0, padx=10, pady=10)
entry_telefono_personal = ttk.Entry(tab4)
entry_telefono_personal.grid(row=2, column=1, padx=10, pady=10)

label_direccion_personal = ttk.Label(tab4, text="Direccion:")
label_direccion_personal.grid(row=3, column=0, padx=10, pady=10)
entry_direccion = ttk.Entry(tab4)
entry_direccion.grid(row=3, column=1, padx=10, pady=10)

label_dni_personal = ttk.Label(tab4, text="DNI:")
label_dni_personal.grid(row=4, column=0, padx=10, pady=10)
entry_dni_personal = ttk.Entry(tab4)
entry_dni_personal.grid(row=4, column=1, padx=10, pady=10)

label_tarea_personal = ttk.Label(tab4, text="Teléfono urgencia:")
label_tarea_personal.grid(row=5, column=0, padx=10, pady=10)
entry_tarea_personal = ttk.Entry(tab4)
entry_tarea_personal.grid(row=5, column=1, padx=10, pady=10)

button_agregar_personal = ttk.Button(tab4, text = "Agregar")
button_agregar_personal.grid(row=6)

#-----Incorporar personal-----#

root.mainloop()