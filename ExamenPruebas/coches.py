import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Ventana principal
root = tk.Tk()
root.title("App de coches")
root.geometry("500x600")

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

# Aqui añadimos los botones y area de texto para cada categoría
botones_frame = tk.Frame(root)
botones_frame.pack(pady=10)

# Colocamos los botones y el campo de texto por cada categoría
for categoria in informacion_vehiculos.keys():
    frame_categoria = tk.Frame(botones_frame)
    frame_categoria.pack(side="left", padx=10)
    
    # Botón de categoría
    boton = ttk.Button(frame_categoria, text=categoria, command=lambda c=categoria: mostrar_categoria(c))
    boton.pack()
    
    # Campo de texto para escribir información adicional
    text_area = tk.Text(frame_categoria, height=3, width=20, wrap="word")
    text_area.insert("end", f"Escribe aquí detalles sobre {categoria}")
    text_area.pack(pady=5)

# Mostramos la descripción
descripcion_label = tk.Label(root, text="Selecciona una categoría para ver la información", font=("Arial", 12))
descripcion_label.pack(pady=10)

# Mostrar la imagen
imagen_label = tk.Label(root)
imagen_label.pack(pady=10)

# Iniciamos la aplicación
root.mainloop()
