import tkinter as tk

# Funciones que se ejecutarán al presionar los botones
def iniciar():
    print("Iniciar presionado")

def parar():
    print("Parar presionado")

def reiniciar():
    print("Reiniciar presionado")

def guardar():
    print("Guardar presionado")

def cargar():
    print("Cargar presionado")

def salir():
    print("Salir presionado")

def ayuda():
    print("Ayuda presionado")

def configurar():
    print("Configurar presionado")

def actualizar():
    print("Actualizar presionado")

# Crear la ventana principal
root = tk.Tk()
root.title("Controlador del carrito")

# Configurar el tamaño de la ventana
root.geometry("300x300")

label = tk.Label(root, text="Seleccione una acción:", font=("Arial", 14))
# Colocar la etiqueta en la parte superior (fila 0)
label.grid(row=0, column=0, columnspan=3, pady=10)

# Lista de textos personalizados para cada botón
textos_botones = [
    "← 90°", "↑", "90° →", "←", "▄",
    "→", "← 360°", "Historial", "360° →"
]

# Lista de funciones para cada botón
funciones_botones = [
    iniciar, parar, reiniciar, guardar, cargar,
    salir, ayuda, configurar, actualizar
]

# Crear y organizar los 9 botones en un layout de 3x3
for i in range(9):
    button = tk.Button(root, text=textos_botones[i], command=funciones_botones[i], width=10, height=2)
    # Usar grid para colocar los botones en un arreglo de 3 filas x 3 columnas
    button.grid(row=(i//3)+1, column=i%3, padx=10, pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()
