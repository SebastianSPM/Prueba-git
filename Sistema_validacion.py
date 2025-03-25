print("****************************************************")
print("***BIENVENID@S SISTEMA DE VALIDACION DE PRODUCTOS***")
print("****************************************************")

# Entrada de datos
nombreProducto = input("Ingrese el nombre del producto: ")

#Pidiendo al usuario precio unitario
while True:
    try:
        precioUnitario = float(input("Ingrese el precio unitario del producto: "))
        if precioUnitario <= 0:
            print("El precio debe ser mayor a cero.")
        else:
            break
    except ValueError:
        print("Por favor ingrese un valor numérico válido para el precio.")

#Pidiendo al usuario cantidad de productos adquiridos
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de productos adquiridos: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
        else:
            break
    except ValueError:
        print("Por favor ingrese un valor entero válido para la cantidad.")

#Pidiendo al usuario porcentaje de descuento
while True:
    try:
        descuento = float(input("Ingrese el porcentaje de descuento (si no hay descuento ingrese 0): "))
        if descuento < 0:
            print("El descuento no puede ser negativo.")
        else:
            break
    except ValueError:
        print("Por favor ingrese un valor numérico válido para el descuento.")

# Proceso
#Calculando
sinDescuento = precioUnitario * cantidad
montoDescuento = sinDescuento * (descuento / 100)
totalPagar = sinDescuento - montoDescuento

# Mostrar resumen de la compra
#Salida de datos
print(f"\nResumen de la compra:")
print(f"Producto: {nombreProducto}")
print(f"Costo sin descuento: ${sinDescuento:.2f}")
print(f"Descuento aplicado: ${montoDescuento:.2f}")
print(f"Costo total a pagar: ${totalPagar:.2f}")
