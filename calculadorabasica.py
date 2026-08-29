# Programacion y desarrolo de calculadora basica
# entrada de datos
# operaciones basicas = sumar, restar, multiplicar, dividir.
# salida de resultados
# limpiar datos con cada nueva operacion

# Librerias
import customtkinter as ctk

# ==================== BLOQUE BACKEND ====================

# Funciones de operaciones basicas
def calcular(operacion):
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
    except ValueError:
        label_resultado.configure(text="Error: Ingrese números válidos")
        return

    if operacion == "sumar":
        resultado = num1 + num2
    elif operacion == "restar":
        resultado = num1 - num2
    elif operacion == "multiplicar":
        resultado = num1 * num2
    elif operacion == "dividir":
        if num2 == 0:
            label_resultado.configure(text="Error: División por cero")
            return
        resultado = num1 / num2
    else:
        label_resultado.configure(text="Error: Operación no válida")
        return

    label_resultado.configure(text=f"Resultado: {resultado}")
        
def clear():
    num1_entry.delete(0, ctk.END)
    num2_entry.delete(0, ctk.END)
    label_resultado.configure(text="")

# ==================== BLOQUE FRONTEND ====================

# temas y apariencia 
ctk.set_appearance_mode("Dark")

# Configuracion de la ventana
app = ctk.CTk()
app.title("Calculadora Basica")
app.resizable(False, False)
app.geometry("300x300")
app.columnconfigure((0,1), weight=1)

label_resultado = ctk.CTkLabel(app,
                               text="",
                               fg_color="gray",
                               corner_radius=10,
                               height=50,
                               font=("Arial", 20, "bold"))
label_resultado.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Configuracion de las entrada de datos
num1_entry = ctk.CTkEntry(app, placeholder_text="Número 1", height=40, font=("Arial", 16))
num1_entry.grid(row=1, column=0, padx=(10,2), pady=10, sticky="ew")
num2_entry = ctk.CTkEntry(app, placeholder_text="Número 2", height=40, font=("Arial", 16))
num2_entry.grid(row=1, column=1, padx=(2,10), pady=10, sticky="ew")

# Configuracion de los botones de operaciones matemáticas
btn_sumar = ctk.CTkButton(app, height=40, text="Sumar ( + )", fg_color="#6366f1", hover_color="#818cf8", command=lambda: calcular("sumar"))
btn_sumar.grid(row=2, column=0, padx=(10,2), pady=(10,2))
btn_restar= ctk.CTkButton(app, height=40, text="Restar ( - )", fg_color="#6366f1", hover_color="#818cf8", command=lambda: calcular("restar"))
btn_restar.grid(row=2, column=1, padx=(2,10), pady=(10,2))
btn_multiplicar = ctk.CTkButton(app, height=40, text="Multiplicar ( x )", fg_color="#6366f1", hover_color="#818cf8", command=lambda: calcular("multiplicar"))
btn_multiplicar.grid(row=3, column=0, padx=(10,2), pady=(2,2))
btn_dividir = ctk.CTkButton(app, height=40, text="Dividir ( ÷ )", fg_color="#6366f1", hover_color="#818cf8", command=lambda: calcular("dividir"))
btn_dividir.grid(row=3, column=1, padx=(2,10), pady=(2,2))

# Configuracion del boton C (clear) para limpiar los datos de entrada y el resultado
btn_limpiar = ctk.CTkButton(app, height=40, text="Limpiar", fg_color="#6366f1", hover_color="#818cf8", command=lambda: clear())
btn_limpiar.grid(row=4, column=0, columnspan=2, padx=10, pady=(2,10), sticky="ew")

if __name__ == "__main__":
    app.mainloop()