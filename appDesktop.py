import socket
import tkinter as tk
from datetime import date
from tkinter import scrolledtext

import requests
from flask import Flask

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

def getInfo(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza un error si la solicitud falla
        datos = respuesta.json()  # Convierte la respuesta JSON en un objeto

        return datos if isinstance(datos, dict) else {'resultados': datos}

    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error: {e}")
        return None


def izquierda90():
    actualizar_label("Giro a la izquierda de 90°")
    sendInfo("giro_izquierda_90")


def avanzar():
    actualizar_label("Avanzar")
    sendInfo("avanzar")

def derecha90():
    actualizar_label("Giro a la derecha de 90°")
    sendInfo("giro_derecha_90")

def izquierda():
    actualizar_label("Giro a la izquierda")
    sendInfo("giro_izquierda")

def detener():
    actualizar_label("Detener")
    sendInfo("detener")

def derecha():
    actualizar_label("Giro a la derecha")
    sendInfo("giro_derecha")

def izquierda360():
    actualizar_label("Giro a la izquierda de 360°")
    sendInfo("giro_izquierda_360")


def historial():
    # Hacer la consulta API
    resultados = getInfo("http://127.0.0.1:5000/cars/latest")
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Datos de Coches")

    # Crear un área de texto desplazable
    textarea = scrolledtext.ScrolledText(nueva_ventana, wrap=tk.WORD, width=60, height=20)
    textarea.pack(padx=10, pady=10)

    # Formatear y añadir los datos al área de texto
    for coche in resultados['resultados']:
        textarea.insert(tk.END, f"ID: {coche['id']}\n")
        textarea.insert(tk.END, f"Nombre: {coche['name']}\n")
        textarea.insert(tk.END, f"Estado: {coche['status']}\n")
        textarea.insert(tk.END, f"Fecha: {coche['date']}\n")
        textarea.insert(tk.END, f"IP del Cliente: {coche['ipClient']}\n")
        textarea.insert(tk.END, "----------------------\n")

    # Hacer que el área de texto sea de solo lectura
    textarea.config(state=tk.DISABLED)

def derecha360():
    actualizar_label("Giro a la derecha de 360°")
    sendInfo("giro_derecha_360")

def actualizar_label(nuevo_texto):
    labelResult.config(text=nuevo_texto)

# Crear la ventana principal
root = tk.Tk()
root.title("Controlador del carrito")

# Configurar el tamaño de la ventana
root.geometry("300x350")

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

label = tk.Label(root, text="Acción seleccionada:", font=("Arial", 14))
    # Colocar la etiqueta en la parte superior (fila 0)
label.grid(row=4, column=0, columnspan=3, pady=10)

labelResult = tk.Label(root, text="", font=("Arial", 12))
    # Colocar la etiqueta en la parte superior (fila 0)
labelResult.grid(row=5, column=0, columnspan=3, pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()
