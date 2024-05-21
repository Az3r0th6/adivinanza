
import random
import tkinter as tk
from tkinter import messagebox

numero_secreto = random.randint(1, 100)
cant_max_intentos = 5
intentos_realizados = 0

def verificar_numero():
    global intentos_realizados
    intentos_realizados += 1
    try:
        numero = int(entrada.get())
        if numero == numero_secreto:
            messagebox.showinfo("Resultado", "¡Felicitaciones! Has adivinado el número secreto.")
            reiniciar_juego()
        elif numero < numero_secreto:
            messagebox.showinfo("Resultado", "El número secreto es mayor al ingresado.")
        else:
            messagebox.showinfo("Resultado", "El número secreto es menor al ingresado.")
        
        if intentos_realizados >= cant_max_intentos:
            messagebox.showinfo("¡Game Over!", "No has podido adivinar dentro de los 5 intentos.")
            reiniciar_juego()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

def reiniciar_juego():
    global numero_secreto, intentos_realizados
    numero_secreto = random.randint(1, 100)
    intentos_realizados = 0
    entrada.delete(0, tk.END)

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Adivina el número secreto")

# Etiqueta y entrada para el número
tk.Label(ventana, text="Introduce un número del 1 al 99:").pack()
entrada = tk.Entry(ventana)
entrada.pack()

# Botón para verificar el número
tk.Button(ventana, text="Verificar", command=verificar_numero).pack()

ventana.mainloop()
