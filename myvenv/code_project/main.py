import variables

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
