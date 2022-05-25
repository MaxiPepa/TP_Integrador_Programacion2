from tkinter import *
from cProfile import label
from tkinter import messagebox
from tkinter import ttk
from class_alumno import *
from class_directivo import *
from class_docente import *
from class_personal import *


def mensaje_prueba():
    print("Pueba")

#-----Ventana-----#
root = Tk()
root.geometry("510x500")
root.resizable(0,0)
root.title("Sist. de organización Colegio Chester")
#-----Ventana-----#

#-----Pestañas-----#
notebook = ttk.Notebook(root)
notebook.grid()

pes1 =ttk.Frame(notebook)
pes2 =ttk.Frame(notebook)
pes3 =ttk.Frame(notebook)
pes4 =ttk.Frame(notebook)
pes5 =ttk.Frame(notebook)
notebook.add(pes1, text = "Mostrar alumnos")
notebook.add(pes2, text = "Mostrar directivos")
notebook.add(pes3, text = "Mostrar docentes")
notebook.add(pes4, text = "Mostrar personal")
notebook.add(pes5, text = "Incorporar persona")
#-----Pestañas-----#

#-----Pestaña Alumnos-----#



#-----Pestaña Alumnos-----#

"""
#-----Título-----#
title_text = Label(root, text = "Bienvenid@, seleccione una opción", font = (20))
title_text.pack(pady=10)
#-----Título-----#

#-----Botones-----#
btn_mostrar_alumnos = Button(root, text = "Mostrar alumnos", command = mensaje_prueba)
btn_mostrar_alumnos.pack(pady=10)

btn_mostrar_directivos = Button(root, text = "Mostrar directivos", command = mensaje_prueba)
btn_mostrar_directivos.pack(pady=10)

btn_mostrar_docentes = Button(root, text = "Mostrar docentes", command = mensaje_prueba)
btn_mostrar_docentes.pack(pady=10)

btn_mostrar_personal = Button(root, text = "Mostrar personal", command = mensaje_prueba)
btn_mostrar_personal.pack(pady=10)

btn_incorporar_persona = Button(root, text = "Incorporar persona", command = mensaje_prueba)
btn_incorporar_persona.pack(pady=10)
#-----Botones-----#
"""

root.mainloop()