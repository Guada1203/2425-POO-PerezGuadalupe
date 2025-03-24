"""Objetivo: Desarrollar una aplicación GUI utilizando Tkinter en Python que funcione como agenda personal.
 La aplicación permitirá al usuario agregar, ver, y eliminar eventos o tareas programadas."""

#funcion para agregar un envento
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar

def agregar_evento():
#Agregar un evento a la tabla.
    fecha = cal.get_date()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        tree.insert('', 'end', values=(fecha, hora, descripcion))
        # Limpiar los campos después de agregar el evento
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        tk.messagebox.showerror("Error", "Por favor, complete todos los campos.")

#Funcion para eliminar un evento
def eliminar_evento():
    seleccionar = tree.selection()
    if seleccionar:
        if messagebox.askyesno("Confirme", "Seguro de eliminar eventos?"):
            tree.delete(seleccionar[0])
        else:
            messagebox.showwarning("Advertencia", "Seleccione el evento a eliminar")

def salir():
    ventana.destroy()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")

# Boton de eliminar.
btn_eliminar = tk.Button(ventana, text = "Eliminar Evento", command = eliminar_evento)
btn_eliminar.grid(row=5, column = 0, columnspan = 2, pady = 10)

#Boton para salir de la ventana
btn_salir = tk.Button(ventana, text="Salir", command=salir)
btn_salir.grid(row=6, column=0, columnspan=2, pady=10) # Ajusta la fila según tu diseño

# Calendario
cal = Calendar(ventana, selectmode='day', date_pattern='yyyy-mm-dd')
cal.grid(row=0, column=0, columnspan=2, padx=8, pady=10)

# Etiquetas y entradas
tk.Label(ventana, text="Hora:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry_hora = tk.Entry(ventana)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="Descripción:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
entry_descripcion = tk.Entry(ventana)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Botón para agregar evento
btn_agregar = tk.Button(ventana, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

# Tabla para mostrar eventos
tree = ttk.Treeview(ventana, columns=('Fecha', 'Hora', 'Descripción'), show='headings')
tree.heading('Fecha', text='Fecha')
tree.heading('Hora', text='Hora')
tree.heading('Descripción', text='Descripción')
tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()