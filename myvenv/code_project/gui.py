import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import variables
from main import mostrar_detalle_y_calcular_total



def crear_ventana_principal():
    root = tk.Tk()
    root.iconbitmap('D:\\Proyecto\\myvenv\\iconos\\pago_mensual_WeR_icon.ico')
    root.title("Calculadora de Facturas")
    root.geometry("440x680")
    root.resizable(0,0)

    # Fuente predeterminada para toda la ventana
    root.option_add("*Font", "Bookman 9")
    # -----------------Frame para el botón de tema-----------------

    # frame para el botón de tema


    # ---------------Tipo de plan---------------
    lbl_tipo_plan = tk.Label(root, text="-Seleccione el tipo de plan:")
    lbl_tipo_plan.place(relx=0.05, rely=0.03, anchor="w")
    lbl_tipo_plan.config(font=("Bookman", 10, "bold"))

    var_tipo_plan = tk.IntVar(value=1)
    radio_combo = tk.Radiobutton(root, text="Combo", variable=var_tipo_plan, value=1)
    radio_combo.place(relx=0.07, rely=0.06, anchor="w")

    radio_combo_skinny = tk.Radiobutton(root, text="Combo Skinny", variable=var_tipo_plan, value=2)
    radio_combo_skinny.place(relx=0.07, rely=0.09, anchor="w")

    # ---------------Planes de pago mensual---------------
    lbl_seleccion = tk.Label(root, text="-Planes de pago mensual:")
    lbl_seleccion.place(relx=0.05, rely=0.13, anchor="w")
    lbl_seleccion.config(font=("Bookman", 10, "bold"))

    var_seleccion = tk.StringVar()
    var_seleccion.set("Select")
    options = list(variables.precios_combo.keys())
 

    for plan, option in enumerate(options):
        radio_plan = tk.Radiobutton(root, text=option, variable=var_seleccion, value=option)
        radio_plan.place(relx=0.07, rely=0.16 + plan*0.03, anchor="w")


    #--------------------Descuento web-----------------
    check_descuento = tk.Label(root, text='-Descuento WEB & AFFINITY')
    check_descuento.place(relx=0.05, rely=0.32, anchor="w")
    check_descuento.config(font=("Bookman", 10, "bold"))

    descuento_var = tk.BooleanVar()
    descuento_checkbox = tk.Checkbutton(root, text="Aplicar descuento", variable=descuento_var)
    descuento_checkbox.place(relx=0.05, rely=0.34, x=20, y=5, anchor="nw")  # Coordenadas relativas con respecto al frame

    # --------------- Selección Decodificador-------------
    caja_adicional_var = tk.IntVar()  # Definir variable para checkbox de caja adicional
    lbl_seleccion = tk.Label(root, text="-Cajas adicionales:")
    lbl_seleccion.config(font=("Bookman", 10, "bold"))
    lbl_seleccion.place(relx=0.05, rely=0.4, anchor="w")

    decos_combobox = ttk.Combobox(root, width=10, font=("Arial", 12), foreground="blue", background="white", state="readonly")
    decos_combobox.place(relx=0.05, rely=0.44, x=20, y=5, anchor="w")
    decos = list(variables.caja_adicional.keys())
    decos_combobox["values"] = decos

    #--------------- invoice----------------
    lbl_servicios = tk.Label(root, text="-Payment invoice:")
    lbl_servicios.place(relx=0.05, rely=0.49, anchor="w")
    lbl_servicios.config(font=("Bookman", 10, "bold"))

    invoice_var = tk.BooleanVar()
    invoice_checkbox = tk.Checkbutton(root, text="Invoice", variable=invoice_var)
    invoice_checkbox.place(relx=0.05, rely=0.52, x=20, y=5, anchor="w")

    #--------------- servicios premium----------------
    lbl_servicios = tk.Label(root, text="-Servicios adicionales:")
    lbl_servicios.place(relx=0.05, rely=0.57, anchor="w")
    lbl_servicios.config(font=("Bookman", 10, "bold"))

    servicios_vars = []
    for prem, servicio in enumerate(variables.premium.keys()):
        var = tk.BooleanVar()
        servicios_vars.append(var)
        checkbox = tk.Checkbutton(root, text=servicio, variable=var)
        checkbox.place(relx=0.07 + prem*0.15, rely=0.60, anchor="w")


    # Cuadro de texto para mostrar la selección y el total
    texto_resultado = tk.Label(root, text="Resumen pago mensual")
    texto_resultado.place(relx=0.05, rely=0.65, anchor="w")
    texto_resultado.config(font=("Bookman", 10, "bold"))
    texto_resultado = tk.Text(root, height=13, width=55, wrap="word", bg="lightblue", fg="black", padx=10)
    texto_resultado.place(relx=0.02, rely=0.82, x=10, anchor="w")
    texto_resultado.config(state=tk.DISABLED)
    # Vincular la función mostrar_detalle_y_calcular_total a la selección del plan
    var_seleccion.trace_add("write", mostrar_detalle_y_calcular_total)


    # Ejecutar la aplicación
    root.mainloop()
