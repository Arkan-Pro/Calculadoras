# Programacion y Desarrollo de Calculadoara con teclado numérico.
# operaciones basicas = sumar, restar, dividir, Multiplicar.
# salida de resultados en pantalla.
# limpiar datos con cada nueva operacion. 

# Librerias
import customtkinter as ctk

# ==================== BLOQUE BACKEND ==================== #

numero_anterior = None
operacion_pendiente = None
esperando_numero = True

# Funciones de operaciones basicas
def actualizar_pantalla(texto):
    label_resultado.configure(text=texto)

# Funcion para insertar numeros en la pantalla
def insertar_numero(numero):
    global esperando_numero

    pantalla = label_resultado.cget("text")
    if esperando_numero or pantalla.startswith("Error"):
        pantalla = ""
        esperando_numero = False
    actualizar_pantalla(pantalla + str(numero))

# Función para realizar operaciones matemáticas
def realizar_operacion(numero1, numero2, operacion):
    if operacion == "+":
        return numero1 + numero2
    if operacion == "-":
        return numero1 - numero2
    if operacion == "x":
        return numero1 * numero2
    if operacion == "÷":
        if numero2 == 0:
            raise ZeroDivisionError
        return numero1 / numero2
    if operacion == "%":
        return numero1 * numero2 / 100
    raise ValueError

# Función para seleccionar la operación y manejar el flujo de cálculo
def seleccionar_operacion(operacion):
    global numero_anterior, operacion_pendiente, esperando_numero

    try:
        numero_actual = float(label_resultado.cget("text"))

        if numero_anterior is not None and operacion_pendiente is not None:
            if not esperando_numero:
                numero_anterior = realizar_operacion(
                    numero_anterior,
                    numero_actual,
                    operacion_pendiente
                )
        else:
            numero_anterior = numero_actual

        operacion_pendiente = operacion
        esperando_numero = True
        actualizar_pantalla(f"{numero_anterior:g} {operacion}")
    except ZeroDivisionError:
        actualizar_pantalla("Error")
        clear()
    except ValueError:
        actualizar_pantalla("Error")

# Función para calcular el resultado de la operación pendiente
def calcular():
    global numero_anterior, operacion_pendiente, esperando_numero

    if numero_anterior is None or operacion_pendiente is None or esperando_numero:
        actualizar_pantalla("Error")
        return

    texto_actual = label_resultado.cget("text")
    try:
        numero_actual = float(texto_actual)
        resultado = realizar_operacion(
            numero_anterior,
            numero_actual,
            operacion_pendiente
        )

        numero_anterior = resultado
        operacion_pendiente = None
        esperando_numero = True
        actualizar_pantalla(f"{resultado:g}")
    except ZeroDivisionError:
        actualizar_pantalla("Error")
    except ValueError:
        actualizar_pantalla("Error")

# Función para limpiar la pantalla y reiniciar el estado de la calculadora
def clear():
    global numero_anterior, operacion_pendiente, esperando_numero
    numero_anterior = None
    operacion_pendiente = None
    esperando_numero = True
    actualizar_pantalla("")
    

# ==================== BLOQUE FRONTEND ==================== #

# temas de apariencia de la app
ctk.set_appearance_mode("dark") # Modos: "light", "dark", "system"
ctk.set_default_color_theme("blue") # Temas: "blue", "green", "dark-blue"

# Configuracion de la ventana principal
app = ctk.CTk()
app.title("Calculadora CTk")
app.resizable(False, False) 
app.geometry("320x390")
app.columnconfigure((0, 1, 2, 3), weight=1)


# Pantalla de resultados    
label_resultado = ctk.CTkLabel(app, 
                               text="",
                               anchor="e",
                               fg_color="gray",
                               corner_radius=10,
                               height=60, 
                               font=("Arial", 24, "bold"))
label_resultado.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Botones de numeros
btn_1 = ctk.CTkButton(app, height=60, text="1", font=("Arial", 20, "bold"), command=lambda: insertar_numero(1))
btn_1.grid(row=1, column=0, padx=(10,2), pady=3, sticky="ew")
btn_2 = ctk.CTkButton(app, height=60, text="2", font=("Arial", 20, "bold"), command=lambda: insertar_numero(2))
btn_2.grid(row=1, column=1, padx=(2,2), pady=3, sticky="ew")
btn_3 = ctk.CTkButton(app, height=60, text="3", font=("Arial", 20, "bold"), command=lambda: insertar_numero(3))
btn_3.grid(row=1, column=2, padx=(2,2), pady=3, sticky="ew")
btn_4 = ctk.CTkButton(app, height=60, text="4", font=("Arial", 20, "bold"), command=lambda: insertar_numero(4))
btn_4.grid(row=2, column=0, padx=(10,2), pady=3, sticky="ew")
btn_5 = ctk.CTkButton(app, height=60, text="5", font=("Arial", 20, "bold"), command=lambda: insertar_numero(5))
btn_5.grid(row=2, column=1, padx=(2,2), pady=3, sticky="ew")
btn_6 = ctk.CTkButton(app, height=60, text="6", font=("Arial", 20, "bold"), command=lambda: insertar_numero(6))
btn_6.grid(row=2, column=2, padx=(2,2), pady=3, sticky="ew")
btn_7 = ctk.CTkButton(app, height=60, text="7", font=("Arial", 20, "bold"), command=lambda: insertar_numero(7))
btn_7.grid(row=3, column=0, padx=(10,2), pady=3, sticky="ew")
btn_8 = ctk.CTkButton(app, height=60, text="8", font=("Arial", 20, "bold"), command=lambda: insertar_numero(8))
btn_8.grid(row=3, column=1, padx=(2,2), pady=3, sticky="ew")
btn_9 = ctk.CTkButton(app, height=60, text="9", font=("Arial", 20, "bold"), command=lambda: insertar_numero(9))
btn_9.grid(row=3, column=2, padx=(2,2), pady=3, sticky="ew")
btn_0 = ctk.CTkButton(app, height=60, text="0", font=("Arial", 20, "bold"), command=lambda: insertar_numero(0))
btn_0.grid(row=4, column=1, padx=(2,2), pady=3, sticky="ew")

# Botones de operaciones
btn_sumar = ctk.CTkButton(app, fg_color="#008080", height=60, text="+", font=("Arial", 20, "bold"), command=lambda: seleccionar_operacion("+"))
btn_sumar.grid(row=1, column=3, padx=(2,10), pady=(3), sticky="ew")
btn_restar = ctk.CTkButton(app, fg_color="#008080", height=60, text="-", font=("Arial", 20, "bold"), command=lambda: seleccionar_operacion("-"))
btn_restar.grid(row=2, column=3, padx=(2,10), pady=(3), sticky="ew")
btn_multiplicar = ctk.CTkButton(app, fg_color="#008080", height=60, text="x", font=("Arial", 20, "bold"), command=lambda: seleccionar_operacion("x"))
btn_multiplicar.grid(row=3, column=3, padx=(2,10), pady=(3), sticky="ew")
btn_dividir = ctk.CTkButton(app, fg_color="#008080", height=60, text="÷", font=("Arial", 20, "bold"), command=lambda: seleccionar_operacion("÷"))
btn_dividir.grid(row=4, column=3, padx=(2,10), pady=(3), sticky="ew")
btn_resultado = ctk.CTkButton(app, height=60, text="=", font=("Arial", 20, "bold"), fg_color="green", command=calcular)
btn_resultado.grid(row=4, column=2, padx=(2, 2), pady=(3), sticky="ew")
btn_clear = ctk.CTkButton(app, height=60, text="C", font=("Arial", 20, "bold"), fg_color="red", command=lambda: clear())   
btn_clear.grid(row=4, column=0, padx=(10,2), pady=(3), sticky="ew")

# Inicialización de la app
if __name__ == "__main__":
    app.mainloop()