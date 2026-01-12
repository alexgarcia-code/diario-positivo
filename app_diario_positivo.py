## APP diario cosas positivas ##

import tkinter as tk
from datetime import date, timedelta
import json

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("3 cosas buenas del día")
ventana.geometry("400x400")
ventana.configure(bg="#53ED77")
                   
# Obtener la fecha de hoy
dia_actual = date.today()

# Mostrar la fecha
label_fecha = tk.Label(ventana, text="", font=("Segoe UI", 14, "bold"))
label_fecha.configure(bg="#B6EBC2")
label_fecha.pack(pady=10)

# Agrupar entradas
frame_entradas = tk.Frame(ventana, bg="#f2f2f2")
frame_entradas.pack(pady=10)

# Botones cambio de dia
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# Campo 1
entrada1 = tk.Entry(frame_entradas, width=40, font=("Segoe UI", 10))
entrada1.configure(bg="#f2f2f2")
entrada1.pack(pady=5)

# Campo 2
entrada2 = tk.Entry(frame_entradas, width=40, font=("Segoe UI", 10))
entrada2.configure(bg="#f2f2f2")
entrada2.pack(pady=5)

# Campo 3
entrada3 = tk.Entry(frame_entradas, width=40, font=("Segoe UI", 10))
entrada3.configure(bg="#f2f2f2")
entrada3.pack(pady=5)

# Función actualizar fecha
def actualizar_fecha():
    label_fecha.config(text=f"Fecha: {dia_actual}")

# Función dia anterior
def dia_anterior():
    global dia_actual
    dia_actual = dia_actual - timedelta(days=1)
    actualizar_fecha()
    cargar_dia()
    limpiar_mensaje()

# Función dia siguiente
def dia_siguiente():
    global dia_actual
    dia_actual = dia_actual + timedelta(days=1)
    actualizar_fecha()
    cargar_dia()
    limpiar_mensaje()

# Función de guardar
def guardar():
    texto1 = entrada1.get()
    texto2 = entrada2.get()
    texto3 = entrada3.get()

    datos_dia = [texto1, texto2, texto3]
    fecha_str = str(dia_actual)

    if not texto1 or not texto2 or not texto3:
        label_mensaje.config(text="⚠️ Debes escribir 3 cosas positivas", fg="red")
        return

    try:
        with open("diario.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = {}
    
    datos[fecha_str] = datos_dia

    with open("diario.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)
    
    label_mensaje.config(text="✅ Guardado correctamente", fg="green")

    print("Guardado correctamente")

# Función Cargar día
def cargar_dia():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    entrada3.delete(0, tk.END)

    fecha_str = str(dia_actual)

    try:
        with open("diario.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        
        if fecha_str in datos:
            entrada1.insert(0, datos[fecha_str][0])
            entrada2.insert(0, datos[fecha_str][1])
            entrada3.insert(0, datos[fecha_str][2])
    
    except FileNotFoundError:
        pass

actualizar_fecha()

# Función limpiar mensaje
def limpiar_mensaje():
    label_mensaje.config(text="")

# Botón Guardar
boton_guardar = tk.Button(ventana, text="Guardar", bg="#2E89F0", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", padx=10, pady=5, command=guardar)
boton_guardar.pack(pady=15)

# Mensaje guardado
label_mensaje = tk.Label(ventana, text="", font=("Segoe UI", 10), bg="#f2f2f2")
label_mensaje.pack()

# Botones cambio de dia
btn_anterior = tk.Button(frame_botones, text="⬅ Día anterior", command=dia_anterior, bg="#dddddd", relief="flat")
btn_anterior.pack(side="left", padx=8)

btn_siguiente = tk.Button(frame_botones, text="Día siguiente ➡", command=dia_siguiente, bg="#dddddd", relief="flat")
btn_siguiente.pack(side="left", padx=8)

cargar_dia()

# Ejecutar la app
ventana.mainloop()