"""Objetivo: Desarrollar una aplicación GUI que permita a los usuarios gestionar una lista de tareas pendientes.
La aplicación deberá permitir añadir nuevas tareas, marcar tareas como completadas,
y eliminar tareas utilizando tanto la interfaz gráfica (clics de botón) como atajos de teclado."""
import tkinter as tk
from tkinter import messagebox

# Funcion para añadir tareas.
def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tarea.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Ingrese una tarea")

def marcar_completado(event=None):
    try:
        seleccion = lista_tarea.curselection()
        if seleccion:
            indice = seleccion[0]
            tarea = lista_tarea.get(indice)
            lista_tarea.delete(indice)
            lista_tarea.insert(tk.END, f"✔ {tarea}")
            lista_tarea.itemconfig(tk.END, fg="gray")  # Feedback visual: texto en gris
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def eliminar_tarea(event=None):
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

def cerrar_aplicacion(event=None):
    ventana.destroy()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title(" Gestión de Tareas")

# Campo de entrada para nuevas tareas
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_tarea)  # Atajo de teclado para agregar tarea (Enter)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack()

boton_agregar = tk.Button(frame_botones, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.grid(row=0, column=0, padx=6)

boton_completar = tk.Button(frame_botones, text="Marcar Completada", command=marcar_completado)
boton_completar.grid(row=0, column=2, padx=6)

boton_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.grid(row=0, column=3, padx=7)

# Lista de tareas
lista_tarea = tk.Listbox(ventana, width=50, height=10, selectmode=tk.SINGLE)
lista_tarea.pack(pady=15)

# Atajos de teclado
ventana.bind("c", marcar_completado)  # Atajo de teclado para marcar como completada (c)
ventana.bind("<Delete>", eliminar_tarea)  # Atajo de teclado para eliminar (Delete)
ventana.bind("d", eliminar_tarea)  # Atajo de teclado para eliminar (d)
ventana.bind("<Escape>", cerrar_aplicacion)  # Atajo de teclado para cerrar (Escape)
entrada_tarea.bind("<Return>", agregar_tarea)  # Atajo de teclado para agregar tarea (Enter)

ventana.mainloop()

