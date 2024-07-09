import tkinter as tk
#import variables as vars
from tkinter import messagebox
from tkinter import ttk
#from code_project.variables import config
#rom code_project.gui import create_window
precios_combo = {
        "SELECT":48.61,
        "SELECT COMBO": 55,
        "ENTERTAINMENT COMBO": 66,
        "COMBO CHOICE": 95,
        "COMBO XTRA": 99
    }
precios_skinny = {
        "SELECT":48.61,
        "SELECT COMBO": 51.14,
        "ENTERTAINMENT COMBO": 62.15,
        "COMBO CHOICE": 91.14,
        "COMBO XTRA": 95.14
    }
premium = {
        "MAX": 19.88,
        "Cmax": 15.46,
        "Starz": 15.46,
        "Pmount+Show": 15.46
    }


caja_adicional = {
        "default":0,
        "3th deco":7.72,
        "4th deco":15.44,
        "5th deco":23.16
    }

invoice = {
        "invoice":6.08,
        "invoice_select":3.87
    }

descuento = {
        "ENTERTAINMENT COMBO":6,
        "COMBO XTRA":4
    }

    # Definir las descripciones de los planes
descripciones = {
        "SELECT":"incluye paquete de programación, 1 equipo principal SD. No aplica servicio HDDVR.",
        "SELECT COMBO":"Incluye paquete de programación, hasta 2 equipos HD, transferencia de señal y tarifa de mantenimiento. No aplica servicio DVR.",
        "ENTERTAINMENT COMBO": "Incluye paquete de programación, 1 equipo principal HDDVR, equipo adicional HD, transferencia de señal y tarifa de mantenimiento.",
        "COMBO CHOICE": "Incluye paquete de programación, 1 equipo principal HDDVR, equipo adicional HD, transferencia de señal y tarifa de mantenimiento.",
        "COMBO XTRA": "Incluye paquete de programación, 1 equipo principal HDDVR, equipo adicional HD, transferencia de señal y tarifa de mantenimiento."
    }

# Función para mostrar los planes disponibles y calcular el total
def mostrar_detalle_y_calcular_total(*args):
    seleccion = var_seleccion.get()
    tipo_plan = "Combo" if var_tipo_plan.get() == 1 else "Combo Skinny"
    
    if var_tipo_plan.get() == 1:  # Combo
        precios = precios_combo
    elif var_tipo_plan.get() == 2:  # Combo Skinny
        precios = precios_skinny
    else:
        messagebox.showerror("Error", "Seleccione un tipo de plan.")
        return

    descuento_checkbox.config(state='normal' if seleccion in descuento else 'disabled')# Habilita el checkbox de descuento solo si el plan seleccionado tiene descuento

    #precios pagos mensual
    if seleccion in precios:
        descripcion = descripciones[seleccion]
        pago_plan = precios[seleccion]
        total = precios[seleccion]
        total = round(total, 2)
        

        # Verificar si el checkbox de descuento está seleccionado
        if descuento_var.get():
            if seleccion in descuento:
                total -=  descuento[seleccion]
                total = round(total, 2)

            elif seleccion == "ENTERTAINMENT COMBO" or seleccion == "COMBO XTRA":
                total = precios[seleccion] - descuento[seleccion]
                total = round(total, 2)
                            
        else:
            total = precios[seleccion]
            total = round(total, 2)

        
            #Descuento aplicado    
        if descuento_var.get():  # Verificar si el checkbox está seleccionado
            try:
                descuento_aplicado = descuento[seleccion]
            
                if descuento_aplicado > 0:
                    pago_plan  -= descuento_aplicado
            except KeyError:
                descuento_aplicado = 0
        else:
            descuento_aplicado = 0
            
        # Agregar costo de caja adicional
        caja_adicional_seleccionada = decos_combobox.get()
        if caja_adicional_seleccionada in caja_adicional:
            total += caja_adicional[caja_adicional_seleccionada]
            total = round(total, 2)
        
        #Subtotl Caja adicional
        if caja_adicional_seleccionada:
            subtotal_caja_adicional = caja_adicional[caja_adicional_seleccionada]
        else:
            subtotal_caja_adicional = 0

        # Agregar costo de servicios premium
        servicios_premium_seleccionados = [servicio for servicio, var in zip(premium.keys(), servicios_vars) if var.get()]
        for servicio in servicios_premium_seleccionados:
            total += premium[servicio]
            total = round(total, 2)

            #subtotal premium
        if servicios_premium_seleccionados:  # Verificar si hay algún servicio premium seleccionado
            subtotal_servicios_premium = sum(premium[servicio] for servicio in servicios_premium_seleccionados)
        else:
            subtotal_servicios_premium = 0

        # Agregar costo de invoice
        if seleccion in ["SELECT", "SELECT COMBO"]:
            invoice_valor = invoice["invoice_select"] if seleccion == "SELECT" else invoice["invoice_select"]
        else:
            invoice_valor = invoice["invoice"]
        if invoice_var.get():
            total += invoice_valor
            total = round(total, 2)

            #subtotal invoice    
        if invoice_var.get():  # Verificar si el checkbox está seleccionado
            subtotal_invoice = invoice_valor
        else:
            subtotal_invoice = 0
    
        texto_resultado.config(state=tk.NORMAL)
        texto_resultado.delete("1.0", tk.END)
        texto_resultado.insert(tk.END, f"Descripción:\n{descripcion}\n\n")
        texto_resultado.insert(tk.END, f"Tipo de Plan: {tipo_plan}\n")
        texto_resultado.insert(tk.END, f"Plan Seleccionado: {seleccion}\n")
        if descuento_var.get():
            texto_resultado.insert(tk.END, f"Descuento WEB & AFFINITY: $ {descuento_aplicado}\n")
        texto_resultado.insert(tk.END, f"Costo del plan: ${pago_plan}\n")
        if invoice_var.get():  # Verificar si el checkbox está seleccionado
            texto_resultado.insert(tk.END, f"Costo Invoice: ${invoice_valor}\n")
        if servicios_premium_seleccionados:#verifica cuantos hay marcados
            texto_resultado.insert(tk.END, f"Costos Servicios Premium: ${subtotal_servicios_premium:.2f}\n")
        if subtotal_caja_adicional >0:
            texto_resultado.insert(tk.END, f"Costo decodificador: ${subtotal_caja_adicional:.2f}\n")
        texto_resultado.insert(tk.END, f"Total a pagar: ${total}\n")
        texto_resultado.config(state=tk.DISABLED)
    else:
        messagebox.showerror("Error", "Selección no válida. Por favor, seleccione uno de los planes disponibles.")
# Funcion para mostrar la ventana cread con tkinter

#mostrar_detalle_y_calcular_total()

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
var_seleccion.set("SELECT")
options = list(precios_combo.keys())

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
decos = list(caja_adicional.keys())
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
for prem, servicio in enumerate(premium.keys()):
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


