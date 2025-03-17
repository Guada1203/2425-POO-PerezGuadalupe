"""Objetivo:
Desarrollar una aplicación de interfaz gráfica de usuario (GUI) que permita a los usuarios
interactuar con datos de manera visual, utilizando los conceptos aprendidos sobre GUI."""

import tkinter as tk
from tkinter import messagebox

def Abrir_mensaje():
    print("se muestra un mensaje en pantalla")
    messagebox.showinfo("Mensaje", "Mensaje enviado con éxito")
    print("Mostrar mensaje en la pantalla")

def agregar_datos():
    dato = entrada_dato.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_dato.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Introduzca su información.")

def limpiar_datos():
    lista_datos.delete(0, tk.END)

# Ventana principal
ventana = tk.Tk()
ventana.title("Tarea de GUI con Tkinter")
ventana.geometry("400x500")

# Botones principales
boton1 = tk.Button(ventana, text="Abrir mensaje", command=Abrir_mensaje)
boton1.pack(pady=15)

boton2 = tk.Button(ventana, text="Agregar datos", command=agregar_datos)
boton2.pack(pady=15)

# Sección de entrada de datos y lista
frame_datos = tk.Frame(ventana) #Agregamos un frame para organizar los widgets
frame_datos.pack(pady=20)

etiqueta_titulo = tk.Label(frame_datos, text="Ingrese un dato:")
etiqueta_titulo.grid(row=0, column=0, padx=5, pady=5)

entrada_dato = tk.Entry(frame_datos)
entrada_dato.grid(row=0, column=1, padx=5, pady=5)

boton_agregar = tk.Button(frame_datos, text="Agregar", command=agregar_datos)
boton_agregar.grid(row=1, column=0, padx=5, pady=5)

boton_limpiar = tk.Button(frame_datos, text="Limpiar", command=limpiar_datos)
boton_limpiar.grid(row=1, column=1, padx=5, pady=5)

lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=15)

# Bucle de eventos
ventana.mainloop()