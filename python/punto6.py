# escribir un algoritmo que determine el area y el volumen de un cilindro
radio = float(input("por facvor Ingresa el valor del radio: "))
altura = float(input("ahora Ingresa el valor de la altura: "))

# Calcula el área de la base del cilindro
area_base = 3.14 * radio ** 2

# formula para Calcula el área lateral del cilindro
area_lateral = 2 * 3.14 * radio * altura

# formula Calcula el área total del cilindro
area_total = area_base + area_lateral

# formula para Calcula el volumen del cilindro
volumen = area_base * altura

print(f"El área total del cilindro es: {area_total:.2f} unidades cuadradas.")
print(f"El volumen del cilindro es: {volumen:.2f} unidades cúbicas.")