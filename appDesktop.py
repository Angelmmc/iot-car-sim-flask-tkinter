import tkinter as tk
from datetime import date
import socket
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
BASE_URL = 'http://127.0.0.1:5000/cars'

# Funciones que se ejecutarán al presionar los botones
def sendInfo(status):
    hostname = socket.gethostname()
    custom_car = {
        "status": status,
        "date": date.today().strftime("%d/%m/%Y"),
        "ipClient": socket.gethostbyname(hostname),
        "name": hostname
    }

    print(custom_car)
    response = requests.post(BASE_URL, json=custom_car)
    return response.json()


def izquierda90():
    print("Parar presionado")
    sendInfo("giro_izquierda_90")


def avanzar():
    print("Parar presionado")
    sendInfo("avanzar")

def derecha90():
    print("Reiniciar presionado")
    sendInfo("giro_derecha_90")

def izquierda():
    print("Guardar presionado")
    sendInfo("giro_izquierda")

def detener():
    print("Cargar presionado")
    sendInfo("detener")

def derecha():
    print("Salir presionado")
    sendInfo("giro_derecha")

def izquierda360():
    print("Ayuda presionado")
    sendInfo("giro_izquierda_360")

def historial():
    print("Configurar presionado")

def derecha360():
    print("Actualizar presionado")
    sendInfo("giro_derecha_360")

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
    izquierda90, avanzar, derecha90, izquierda, detener,
    derecha, izquierda360, historial, derecha360
]

# Crear y organizar los 9 botones en un layout de 3x3
for i in range(9):
    button = tk.Button(root, text=textos_botones[i], command=funciones_botones[i], width=10, height=2)
    # Usar grid para colocar los botones en un arreglo de 3 filas x 3 columnas
    button.grid(row=(i//3)+1, column=i%3, padx=10, pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()
