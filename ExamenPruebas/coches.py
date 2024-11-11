import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Ventana principal
root = tk.Tk()
root.title("App de coches")
root.geometry("500x500")

# Titulo
titulo = tk.Label(root, text="CATEGORIAS DE VEHICULOS A MOTOR", font=("Arial", 16))
titulo.pack(pady=10)

# Añadimos los textos y rutas de imagenes
informacion_vehiculos = {
    "Camiones": {
        "descripcion": "Vehículos pesados utilizados para transporte de carga.",
        "imagen": "camiones.jpg"
    },
    "Coches": {
        "descripcion": "Automóviles convencionales de uso diario.",
        "imagen": "coches.jpg"
    },
    "F1": {
        "descripcion": "Coches de alta velocidad usados en carreras de Fórmula 1.",
        "imagen": "f1.jpg"
    },
    "Motos": {
        "descripcion": "Vehículos de dos ruedas para transporte y deporte.",
        "imagen": "motos.jpg"
    },
    "Rally": {
        "descripcion": "Vehículos preparados para carreras en terrenos difíciles.",
        "imagen": "rally.jpg"
    }
}

# Función para mostrar información e imagen x categoría
def mostrar_categoria(categoria):
    descripcion_label.config(text=informacion_vehiculos[categoria]["descripcion"])
    imagen_path = informacion_vehiculos[categoria]["imagen"]
    try:
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((250, 200))  # Ajustamos los tamaño
        imagen_tk = ImageTk.PhotoImage(imagen)
        imagen_label.config(image=imagen_tk)
        imagen_label.image = imagen_tk  # Guardamos la foto pa no perderla
    except FileNotFoundError:
        messagebox.showerror("Error", f"No se encuentra la imagen: {imagen_path}")
        imagen_label.config(image='')

# Aqui añadimos los botones
botones_frame = tk.Frame(root)
botones_frame.pack(pady=5)

# Colocamos los botones en fila
categorias = ["Camiones", "Coches", "F1", "Motos", "Rally"]
for i, categoria in enumerate(categorias):
    boton = ttk.Button(botones_frame, text=categoria, command=lambda c=categoria: mostrar_categoria(c))
    boton.grid(row=0, column=i, padx=5, pady=5)  # Usamos el grid para organizarlos en una fila

# Mostramos la descripción
descripcion_label = tk.Label(root, text="Selecciona una categoría para ver la información", font=("Arial", 12))
descripcion_label.pack(pady=10)

# Mostrar la imagen
imagen_label = tk.Label(root)
imagen_label.pack(pady=10)

# Iniciamos la aplicación
root.mainloop()
