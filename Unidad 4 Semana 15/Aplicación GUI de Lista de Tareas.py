"""Objetivo: Desarrollar una aplicación GUI simple para gestionar una lista de tareas,
permitiendo al usuario añadir nuevas tareas, marcarlas como completadas y eliminarlas.
La aplicación deberá responder adecuadamente a los eventos del usuario,
como clics del ratón y pulsaciones del teclado."""
import tkinter as tk
from tkinter import ttk, messagebox

#función para agregar una tarea, para marcar como completo y eliminar tarea.
def agregar_tarea():
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tarea.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Ingrese una tarea")

def marcar_completado():
    try:
        seleccion = lista_tarea.curselection()
        if seleccion:
            indice = seleccion[0]
            lista_tarea.delete(indice)
            messagebox.showinfo("Tarea Completada", "Tarea marcada como completada.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def eliminar_tarea():
    try:
        seleccion = lista_tarea.curselection()
        if seleccion:
            indice = seleccion[0]
            lista_tarea.delete(indice)
            messagebox.showinfo("Tarea Eliminada", "Tarea eliminada.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def salir():
    if messagebox.askyesno("Salir", "¿Está seguro que desea salir?"):
        ventana.destroy()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x300")  # Ancho x Alto

# Entrada para agregar tareas
entrada_tarea = tk.Entry(ventana)
entrada_tarea.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew") #columnspan para ocupar dos columnas y sticky para que se expanda

# Botón para agregar tareas
boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.grid(row=0, column=2, padx=5, pady=10)

# Lista de tareas
lista_tarea = tk.Listbox(ventana)
lista_tarea.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Botón para marcar tarea como completada
boton_completado = tk.Button(ventana, text="Marcar Completado", command=marcar_completado)
boton_completado.grid(row=2, column=0, padx=5, pady=5)

# Botón para eliminar tarea
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.grid(row=2, column=1, padx=5, pady=5)

# Botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.grid(row=2, column=2, padx=5, pady=5)

ventana.grid_rowconfigure(1, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)

ventana.mainloop()