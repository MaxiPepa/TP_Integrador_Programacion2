from tkinter import *
from tkinter import ttk
from turtle import clear
from class_alumno import *
from class_directivo import *
from class_docente import *
from class_personal import *

#-----Variables y Funciones-----#
agenda_alumnos = []
agenda_directivos = []
agenda_docentes = []
agenda_personal = []

def crear_alumno(nombre, apellido, dni, direccion, telefono, email, nacionalidad, residencia, cant_hermanos, telf_madre, telf_padre, telf_adicional):
    nuevo_alumno = Alumno(nombre, apellido, dni, direccion, telefono, email, nacionalidad, residencia, cant_hermanos, telf_madre, telf_padre, telf_adicional)
    agenda_alumnos.append(nuevo_alumno)

def crear_directivo(nombre, apellido, direccion, dni, telefono, telf_urgencia, es_docente):
    nuevo_directivo = Directivo(nombre, apellido, direccion, dni, telefono, telf_urgencia, es_docente)
    agenda_directivos.append(nuevo_directivo)

def crear_docente(nombre, apellido, direccion, dni, telefono, telf_urgencia, materia, titulo):
    nuevo_docente = Docente(nombre, apellido, direccion, dni, telefono, telf_urgencia, materia, titulo)
    agenda_docentes.append(nuevo_docente)

def crear_personal(nombre, apellido, telefono, direccion, dni, tarea):
    nuevo_personal = Personal(nombre, apellido, telefono, direccion, dni, tarea)
    agenda_personal.append(nuevo_personal)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

#-----Variables y Funciones-----#

#-----Ventana-----#

root = Tk()
root.geometry("1300x600")
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

button_agregar_alumno = ttk.Button(tab1, text = "Agregar", command=lambda: crear_alumno(entry_nombre_alumno.get(), entry_apellido_alumno.get(), entry_dni_alumno.get(), entry_direccion_alumno.get(), entry_telefono_alumno.get(), entry_email_alumno.get(), entry_nacionalidad_alumno.get(), entry_residencia_alumno.get(), entry_cant_hermanos_alumno.get(), entry_telf_madre_alumno.get(), entry_telf_padre_alumno.get(), entry_telf_adicional_alumno.get()))
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

es_docente = BooleanVar()
label_es_docente_directivo = ttk.Label(tab2, text="¿Es docente?:")
label_es_docente_directivo.grid(row=6, column=0, padx=10, pady=10)
radiobutton1_es_docente_directivo = Radiobutton(tab2, text = "Si", variable=es_docente, value=True)
radiobutton1_es_docente_directivo.grid(row=6, column=1, padx=10, pady=10)
radiobutton2_es_docente_directivo = Radiobutton(tab2, text = "No", variable=es_docente, value=False)
radiobutton2_es_docente_directivo.grid(row=6, column=2, padx=10, pady=10)

button_agregar_directivo = ttk.Button(tab2, text = "Agregar", command=lambda: crear_directivo(entry_nombre_directivo.get(), entry_apellido_directivo.get(), entry_direccion_directivo.get(), entry_dni_directivo.get(), entry_telefono_directivo.get(), entry_telf_urgencia_directivo.get(), es_docente.get()))
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

button_agregar_docente = ttk.Button(tab3, text = "Agregar", command=lambda: crear_docente(entry_nombre_docente.get(), entry_apellido_docente.get(), entry_direccion_docente.get(), entry_dni_docente.get(), entry_telefono_docente.get(), entry_telf_urgencia_docente.get(), entry_materia_docente.get(), entry_titulo_docente.get()))
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
entry_direccion_personal = ttk.Entry(tab4)
entry_direccion_personal.grid(row=3, column=1, padx=10, pady=10)

label_dni_personal = ttk.Label(tab4, text="DNI:")
label_dni_personal.grid(row=4, column=0, padx=10, pady=10)
entry_dni_personal = ttk.Entry(tab4)
entry_dni_personal.grid(row=4, column=1, padx=10, pady=10)

label_tarea_personal = ttk.Label(tab4, text="Tarea:")
label_tarea_personal.grid(row=5, column=0, padx=10, pady=10)
entry_tarea_personal = ttk.Entry(tab4)
entry_tarea_personal.grid(row=5, column=1, padx=10, pady=10)

button_agregar_personal = ttk.Button(tab4, text = "Agregar", command=lambda: crear_personal(entry_nombre_personal.get(), entry_apellido_personal.get(), entry_telefono_personal.get(), entry_direccion_personal.get(), entry_dni_personal.get(), entry_tarea_personal.get()))
button_agregar_personal.grid(row=6)

#-----Incorporar personal-----#

#-----Mostrar alumno-----#

def borrar_alumno(legajo):
    for alumno in agenda_alumnos:
        if alumno.legajo == legajo:
            agenda_alumnos.remove(alumno)
    mostrar_alumnos()

def mostrar_alumnos():
    clear_frame(tab5)

    row_alumnos = 1

    ttk.Label(tab5, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(tab5, text="Apellido").grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(tab5, text="DNI").grid(row=0, column=2, padx=5, pady=5)
    ttk.Label(tab5, text="Dirección").grid(row=0, column=3, padx=5, pady=5)
    ttk.Label(tab5, text="Teléfono").grid(row=0, column=4, padx=5, pady=5)
    ttk.Label(tab5, text="Email").grid(row=0, column=5, padx=5, pady=5)
    ttk.Label(tab5, text="Nacionalidad").grid(row=0, column=6, padx=5, pady=5)
    ttk.Label(tab5, text="Residencia").grid(row=0, column=7, padx=5, pady=5)
    ttk.Label(tab5, text="Cantidad Hermanos").grid(row=0, column=8, padx=5, pady=5)
    ttk.Label(tab5, text="Teléfono Madre").grid(row=0, column=9, padx=5, pady=5)
    ttk.Label(tab5, text="Teléfono Padre").grid(row=0, column=10, padx=5, pady=5)
    ttk.Label(tab5, text="Teléfono Adicional").grid(row=0, column=11, padx=5, pady=5)
    ttk.Label(tab5, text="Legajo").grid(row=0, column=12, padx=5, pady=5)

    ttk.Button(tab5, text="Actualizar", command=mostrar_alumnos).grid(row=0, column=13)
    ttk.Button(tab5, text="Borrar por legajo", command=lambda: borrar_alumno(entry_borrar_alumno.get())).grid(row=0, column=14)
    entry_borrar_alumno = ttk.Entry(tab5)
    entry_borrar_alumno.grid(row=0, column=15)

    for alumno in agenda_alumnos:
        ttk.Label(tab5, text=alumno.nombre).grid(row=row_alumnos, column=0)
        ttk.Label(tab5, text=alumno.apellido).grid(row=row_alumnos, column=1)
        ttk.Label(tab5, text=alumno.dni).grid(row=row_alumnos, column=2)
        ttk.Label(tab5, text=alumno.direccion).grid(row=row_alumnos, column=3)
        ttk.Label(tab5, text=alumno.telefono).grid(row=row_alumnos, column=4)
        ttk.Label(tab5, text=alumno.email).grid(row=row_alumnos, column=5)
        ttk.Label(tab5, text=alumno.nacionalidad).grid(row=row_alumnos, column=6)
        ttk.Label(tab5, text=alumno.residencia).grid(row=row_alumnos, column=7)
        ttk.Label(tab5, text=alumno.cant_hermanos).grid(row=row_alumnos, column=8)
        ttk.Label(tab5, text=alumno.telf_padre).grid(row=row_alumnos, column=9)
        ttk.Label(tab5, text=alumno.telf_madre).grid(row=row_alumnos, column=10)
        ttk.Label(tab5, text=alumno.telf_adicional).grid(row=row_alumnos, column=11)
        ttk.Label(tab5, text=alumno.legajo).grid(row=row_alumnos, column=12)
        row_alumnos += 1
    

mostrar_alumnos()

#-----Mostrar alumno-----#

#-----Mostrar directivo-----#

def borrar_directivo(legajo):
    for directivo in agenda_directivos:
        if directivo.legajo == legajo:
            agenda_directivos.remove(directivo)
    mostrar_directivos()

def mostrar_directivos():
    clear_frame(tab6)

    row_directivos = 1

    ttk.Label(tab6, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(tab6, text="Apellido").grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(tab6, text="Dirección").grid(row=0, column=2, padx=5, pady=5)
    ttk.Label(tab6, text="DNI").grid(row=0, column=3, padx=5, pady=5)
    ttk.Label(tab6, text="Teléfono").grid(row=0, column=4, padx=5, pady=5)
    ttk.Label(tab6, text="Teléfono de urgencia").grid(row=0, column=5, padx=5, pady=5)
    ttk.Label(tab6, text="Es docente").grid(row=0, column=6, padx=5, pady=5)
    ttk.Label(tab6, text="Legajo").grid(row=0, column=7, padx=5, pady=5)

    ttk.Button(tab6, text="Actualizar", command=mostrar_directivos).grid(row=0, column=8)
    ttk.Button(tab6, text="Borrar por legajo", command=lambda: borrar_directivo(entry_borrar_directivo.get())).grid(row=0, column=9)
    entry_borrar_directivo = ttk.Entry(tab6)
    entry_borrar_directivo.grid(row=0, column=10)

    for directivo in agenda_directivos:
        ttk.Label(tab6, text=directivo.nombre).grid(row=row_directivos, column=0)
        ttk.Label(tab6, text=directivo.apellido).grid(row=row_directivos, column=1)
        ttk.Label(tab6, text=directivo.direccion).grid(row=row_directivos, column=2)
        ttk.Label(tab6, text=directivo.dni).grid(row=row_directivos, column=3)
        ttk.Label(tab6, text=directivo.telefono).grid(row=row_directivos, column=4)
        ttk.Label(tab6, text=directivo.telf_urgencia).grid(row=row_directivos, column=5)
        ttk.Label(tab6, text=directivo.es_docente).grid(row=row_directivos, column=6)
        ttk.Label(tab6, text=directivo.legajo).grid(row=row_directivos, column=7)
        row_directivos += 1

mostrar_directivos()

#-----Mostrar directivo-----#

#-----Mostrar docente-----#

def borrar_docente(legajo):
    for docente in agenda_docentes:
        if docente.legajo == legajo:
            agenda_docentes.remove(docente)
    mostrar_docentes()

def mostrar_docentes():
    clear_frame(tab7)

    row_docentes = 1

    ttk.Label(tab7, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(tab7, text="Apellido").grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(tab7, text="Dirección").grid(row=0, column=2, padx=5, pady=5)
    ttk.Label(tab7, text="DNI").grid(row=0, column=3, padx=5, pady=5)
    ttk.Label(tab7, text="Teléfono").grid(row=0, column=4, padx=5, pady=5)
    ttk.Label(tab7, text="Teléfono de urgencia").grid(row=0, column=5, padx=5, pady=5)
    ttk.Label(tab7, text="Materia").grid(row=0, column=6, padx=5, pady=5)
    ttk.Label(tab7, text="Título").grid(row=0, column=7, padx=5, pady=5)
    ttk.Label(tab7, text="Legajo").grid(row=0, column=8, padx=5, pady=5)

    ttk.Button(tab7, text="Actualizar", command=mostrar_docentes).grid(row=0, column=9)
    ttk.Button(tab7, text="Borrar por legajo", command=lambda: borrar_docente(entry_borrar_docente.get())).grid(row=0, column=10)
    entry_borrar_docente = ttk.Entry(tab7)
    entry_borrar_docente.grid(row=0, column=11)

    for docente in agenda_docentes:
        ttk.Label(tab7, text=docente.nombre).grid(row=row_docentes, column=0)
        ttk.Label(tab7, text=docente.apellido).grid(row=row_docentes, column=1)
        ttk.Label(tab7, text=docente.direccion).grid(row=row_docentes, column=2)
        ttk.Label(tab7, text=docente.dni).grid(row=row_docentes, column=3)
        ttk.Label(tab7, text=docente.telefono).grid(row=row_docentes, column=4)
        ttk.Label(tab7, text=docente.telf_urgencia).grid(row=row_docentes, column=5)
        ttk.Label(tab7, text=docente.materia).grid(row=row_docentes, column=6)
        ttk.Label(tab7, text=docente.titulo).grid(row=row_docentes, column=7)
        ttk.Label(tab7, text=docente.legajo).grid(row=row_docentes, column=8)
        row_docentes += 1

mostrar_docentes()

#-----Mostrar docente-----#

#-----Mostrar personal-----#

def borrar_personal(legajo):
    for personal in agenda_personal:
        if personal.legajo == legajo:
            agenda_personal.remove(personal)
    mostrar_personal()

def mostrar_personal():
    clear_frame(tab8)

    row_personal = 1

    ttk.Label(tab8, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(tab8, text="Apellido").grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(tab8, text="Teléfono").grid(row=0, column=2, padx=5, pady=5)
    ttk.Label(tab8, text="Dirección").grid(row=0, column=3, padx=5, pady=5)
    ttk.Label(tab8, text="DNI").grid(row=0, column=4, padx=5, pady=5)
    ttk.Label(tab8, text="Tarea").grid(row=0, column=5, padx=5, pady=5)
    ttk.Label(tab8, text="Legajo").grid(row=0, column=6, padx=5, pady=5)

    ttk.Button(tab8, text="Actualizar", command=mostrar_personal).grid(row=0, column=7)
    ttk.Button(tab8, text="Borrar por legajo", command=lambda: borrar_personal(entry_borrar_personal.get())).grid(row=0, column=8)
    entry_borrar_personal = ttk.Entry(tab8)
    entry_borrar_personal.grid(row=0, column=9)

    for personal in agenda_personal:
        ttk.Label(tab8, text=personal.nombre).grid(row=row_personal, column=0)
        ttk.Label(tab8, text=personal.apellido).grid(row=row_personal, column=1)
        ttk.Label(tab8, text=personal.telefono).grid(row=row_personal, column=2)
        ttk.Label(tab8, text=personal.direccion).grid(row=row_personal, column=3)
        ttk.Label(tab8, text=personal.dni).grid(row=row_personal, column=4)
        ttk.Label(tab8, text=personal.tarea).grid(row=row_personal, column=5)
        ttk.Label(tab8, text=personal.legajo).grid(row=row_personal, column=6)
        row_personal += 1


mostrar_personal()

#-----Mostrar personal-----#

root.mainloop()