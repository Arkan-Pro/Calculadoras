# Librerias
import customtkinter as ctk

from calculadorabasica import calcular

# ==================== BLOQUE BACKEND =====================



# ==================== BLOQUE FRONTEND ====================

# temas y apariencia 
ctk.set_appearance_mode("Dark")

# Configuracion de la ventana
app = ctk.CTk()
app.title("Calculadora Alfanumerica")
app.resizable(False, False)
app.geometry("300x360")
app.columnconfigure((0,1,2,3), weight=1)

label_resultado = ctk.CTkLabel(app,
                               text="",
                               fg_color="gray",
                               corner_radius=10,
                               height=50,
                               font=("Arial", 20, "bold"))
label_resultado.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

btn_limpiar = ctk.CTkButton(app, height=50, width=50, text="C", fg_color="#FF0000", hover_color="#CC0000", command=lambda: clear())
btn_limpiar.grid(row=1, column=0, padx=(10,2), pady=(3), sticky="ew")
btn_borrar = ctk.CTkButton(app, height=50, width=50, text="⌫", fg_color="#6366f1", hover_color="#818cf8", command=lambda: clear())
btn_borrar.grid(row=1, column=1, padx=(2,2), pady=(3), sticky="ew")
btn_porciento = ctk.CTkButton(app, height=50, width=50, text="%", fg_color="#6366f1", hover_color="#818cf8", command=lambda: calcular("sumar"))
btn_porciento.grid(row=1, column=2, padx=(2,2), pady=(3), sticky="ew")
btn_dividir = ctk.CTkButton(app, height=50, width=50, text="÷", fg_color="#6366f1", hover_color="#818cf8", command=lambda: calcular("dividir"))
btn_dividir.grid(row=1, column=3, padx=(2,10), pady=(3), sticky="ew")

btn_7 = ctk.CTkButton(app, height=50, width=50, text="7", fg_color="#6366f1", hover_color="#818cf8")
btn_7.grid(row=2, column=0, padx=(10,2), pady=(3), sticky="ew")
btn_8 = ctk.CTkButton(app, height=50, width=50, text="8", fg_color="#6366f1", hover_color="#818cf8")
btn_8.grid(row=2, column=1, padx=(2,2), pady=(3), sticky="ew")
btn_9 = ctk.CTkButton(app, height=50, width=50, text="9", fg_color="#6366f1", hover_color="#818cf8")
btn_9.grid(row=2, column=2, padx=(2,2), pady=(3), sticky="ew")
btn_multiplicar = ctk.CTkButton(app, height=50, width=50, text="x", fg_color="#6366f1", hover_color="#818cf8", command=lambda: calcular("multiplicar"))
btn_multiplicar.grid(row=2, column=3, padx=(2,10), pady=(3), sticky="ew")

btn_4 = ctk.CTkButton(app, height=50, width=50, text="4", fg_color="#6366f1", hover_color="#818cf8")
btn_4.grid(row=3, column=0, padx=(10,2), pady=(3), sticky="ew")
btn_5 = ctk.CTkButton(app, height=50, width=50, text="5", fg_color="#6366f1", hover_color="#818cf8")
btn_5.grid(row=3, column=1, padx=(2,2), pady=(3), sticky="ew")
btn_6 = ctk.CTkButton(app, height=50, width=50, text="6", fg_color="#6366f1", hover_color="#818cf8")
btn_6.grid(row=3, column=2, padx=(2,2), pady=(3), sticky="ew")
btn_restar= ctk.CTkButton(app, height=50, width=50, text="-", fg_color="#6366f1", hover_color="#818cf8", command=lambda: calcular("restar"))
btn_restar.grid(row=3, column=3, padx=(2,10), pady=(3), sticky="ew")

btn_1 = ctk.CTkButton(app, height=50, width=50, text="1", fg_color="#6366f1", hover_color="#818cf8")
btn_1.grid(row=4, column=0, padx=(10,2), pady=(3), sticky="ew")
btn_2 = ctk.CTkButton(app, height=50, width=50, text="2", fg_color="#6366f1", hover_color="#818cf8")
btn_2.grid(row=4, column=1, padx=(2,2), pady=(3), sticky="ew")
btn_3 = ctk.CTkButton(app, height=50, width=50, text="3", fg_color="#6366f1", hover_color="#818cf8")
btn_3.grid(row=4, column=2, padx=(2,2), pady=(3), sticky="ew")
btn_sumar = ctk.CTkButton(app, height=50, width=50, text="+", fg_color="#6366f1", hover_color="#818cf8", command=lambda: calcular("sumar"))
btn_sumar.grid(row=4, column=3, padx=(2,10), pady=(3), sticky="ew")

btn_0 = ctk.CTkButton(app, height=50, width=50, text="0", fg_color="#6366f1", hover_color="#818cf8")
btn_0.grid(row=5, column=0, padx=(10,2), pady=(3), sticky="ew")
btn_coma = ctk.CTkButton(app, height=50, width=50, text=",", fg_color="#6366f1", hover_color="#818cf8")
btn_coma.grid(row=5, column=1, padx=(2,2), pady=(3), sticky="ew")
btn_punto = ctk.CTkButton(app, height=50, width=50, text=".", fg_color="#6366f1", hover_color="#818cf8")
btn_punto.grid(row=5, column=2, padx=(2,2), pady=(3), sticky="ew")
btn_igual = ctk.CTkButton(app, height=50, width=50, text="=", fg_color="#36dd30", hover_color="#6ce967")
btn_igual.grid(row=5, column=3, padx=(2,10), pady=(3), sticky="ew")

# Iniializacion de la app
if __name__ == "__main__":
    app.mainloop()