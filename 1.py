# Script para calcular el costo total de una compra en una tienda

# Solicitar al usuario el nombre del producto
nombre_producto = input("Ingrese el nombre del producto: ")

# Validar que el nombre del producto no esté vacío
while not nombre_producto.strip():
    print("El nombre del producto no puede estar vacío.")
    nombre_producto = input("Ingrese el nombre del producto: ")

# Solicitar el precio unitario del producto
while True:
    try:
        precio_unitario = float(input("Ingrese el precio unitario del producto: "))
        if precio_unitario <= 0:
            print("El precio debe ser mayor a cero.")
        else:
            break
    except ValueError:
        print("Por favor ingrese un valor numérico válido para el precio.")

# Solicitar la cantidad de productos adquiridos
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de productos adquiridos: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
        else:
            break
    except ValueError:
        print("Por favor ingrese un valor entero válido para la cantidad.")

# Solicitar el porcentaje de descuento
while True:
    try:
        descuento = float(input("Ingrese el porcentaje de descuento (si no hay descuento ingrese 0): "))
        if descuento < 0:
            print("El descuento no puede ser negativo.")
        else:
            break
    except ValueError:
        print("Por favor ingrese un valor numérico válido para el descuento.")

# Calcular el costo total sin aplicar descuento
costo_sin_descuento = precio_unitario * cantidad

# Calcular el monto de descuento
monto_descuento = costo_sin_descuento * (descuento / 100)

# Calcular el costo total después de aplicar el descuento
costo_total = costo_sin_descuento - monto_descuento

# Mostrar el resultado final con los valores formateados a dos decimales
print(f"\nResumen de la compra:")
print(f"Producto: {nombre_producto}")
print(f"Costo sin descuento: ${costo_sin_descuento:.2f}")
print(f"Descuento aplicado: ${monto_descuento:.2f}")
print(f"Costo total a pagar: ${costo_total:.2f}")

