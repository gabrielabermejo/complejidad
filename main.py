import tkinter as tk
from tkinter import filedialog

def abrir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, 'r') as archivo_txt:
            contenido = archivo_txt.read()
            mostrar_contenido(contenido)

def mostrar_contenido(contenido):
    ventana_dialogo = tk.Toplevel(root)
    ventana_dialogo.title("Contenido del archivo")
    label_contenido = tk.Label(ventana_dialogo, text=contenido)
    label_contenido.pack(padx=10, pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("Ejecutar archivo de texto")

# Botón para abrir archivo
boton_abrir = tk.Button(root, text="Abrir archivo", command=abrir_archivo)
boton_abrir.pack(padx=10, pady=10)

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
 
