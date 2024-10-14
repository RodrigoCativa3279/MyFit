import os

def calcular_barras(cantidad_hierro, barras_largas_stock=0, barras_medianas_stock=0, barras_cortas_stock=0):
    while True:
        barras_largas_deseadas = int(input("Ingrese la cantidad de barras de 6m que deseas: "))
        barras_medianas_deseadas = int(input("Ingrese la cantidad de barras de 2m que deseas: "))
        barras_cortas_deseadas = int(input("Ingrese la cantidad de barras de 1.2m que deseas: "))

        hierro_necesario = (barras_largas_deseadas * 6 + 
                            barras_medianas_deseadas * 2 + 
                            barras_cortas_deseadas * 1.2)

        if hierro_necesario <= cantidad_hierro:
            break  
        else:
            print("Error: No tienes suficiente hierro para producir la cantidad deseada de barras.")
            print("Por favor, ingresa nuevamente las cantidades.")

    hierro_sobrante = cantidad_hierro - hierro_necesario

    barras_largas_stock += barras_largas_deseadas
    barras_medianas_stock += barras_medianas_deseadas
    barras_cortas_stock += barras_cortas_deseadas

    print("Barras de 6m producidas:", barras_largas_deseadas)
    print("Barras de 2m producidas:", barras_medianas_deseadas)
    print("Barras de 1.2m producidas:", barras_cortas_deseadas)
    print("Hierro sobrante:", hierro_sobrante, "metros")

    return barras_largas_stock, barras_medianas_stock, barras_cortas_stock, hierro_sobrante

def armar_kit(cantidad_hierro, barras_largas_stock, barras_medianas_stock, barras_cortas_stock):
    barras_largas_kit = int(input("¿Cuántas barras de 6m quieres en tu kit?: "))
    barras_medianas_kit = int(input("¿Cuántas barras de 2m quieres en tu kit?: "))
    barras_cortas_kit = int(input("¿Cuántas barras de 1.2m quieres en tu kit?: "))
    discos = int(input("¿Cuántos discos quieres en tu kit?: "))

    hierro_necesario_para_fabricar = 0

    if barras_largas_kit > barras_largas_stock:
        hierro_necesario_para_fabricar += (barras_largas_kit - barras_largas_stock) * 6
    if barras_medianas_kit > barras_medianas_stock:
        hierro_necesario_para_fabricar += (barras_medianas_kit - barras_medianas_stock) * 2
    if barras_cortas_kit > barras_cortas_stock:
        hierro_necesario_para_fabricar += (barras_cortas_kit - barras_cortas_stock) * 1.2

    if hierro_necesario_para_fabricar > cantidad_hierro:
        print("Barras y hierro insuficiente para completar el kit.")
    else:
        cantidad_hierro -= hierro_necesario_para_fabricar
        barras_largas_stock = max(barras_largas_stock, barras_largas_kit)
        barras_medianas_stock = max(barras_medianas_stock, barras_medianas_kit)
        barras_cortas_stock = max(barras_cortas_stock, barras_cortas_kit)

        print(f"Kit armado con {barras_largas_kit} barras de 6m, {barras_medianas_kit} barras de 2m, {barras_cortas_kit} barras de 1.2m y {discos} discos.")
        print(f"Hierro restante: {cantidad_hierro} metros")

    return barras_largas_stock, barras_medianas_stock, barras_cortas_stock, cantidad_hierro

cantidad_hierro = float(input("Ingrese la cantidad de hierro disponible (en metros): "))

barras_largas_stock, barras_medianas_stock, barras_cortas_stock, cantidad_hierro = calcular_barras(cantidad_hierro)

barras_largas_stock, barras_medianas_stock, barras_cortas_stock, cantidad_hierro = armar_kit(
    cantidad_hierro, barras_largas_stock, barras_medianas_stock, barras_cortas_stock)

print("Producción finalizada. ¡Gracias por usar el sistema de Pechbar!")

os.system("pause")
