# Función para obtener un valor de entrada con un valor predeterminado
def obtener_valor(prompt, valor_predeterminado):
    valor = input(prompt)
    return float(valor) if valor else valor_predeterminado


# Solicitar al usuario la presión atmosférica, la gravedad y el ancho del tanque
Patm = obtener_valor(
    "Ingrese la presión atmosférica en Pascales (por defecto 101325): ", 101325)
g = obtener_valor(
    "Ingrese la aceleración debida a la gravedad en m/s^2 (por defecto 9.81): ", 9.81)
ancho_tanque = obtener_valor(
    "Ingrese el ancho del tanque en metros (por defecto 5): ", 5)

# Inicializar la lista de fluidos
fluidos = []

# Solicitar al usuario que ingrese la cantidad de fluidos
n_fluids = int(obtener_valor(
    "Ingrese el número de fluidos en el tanque (por defecto 3): ", 3))

# Recopilar datos de cada fluido
for i in range(n_fluids):
    nombre = input(f"Ingrese el nombre del fluido {
                   i + 1} (por defecto 'Fluido{i+1}'): ") or f"Fluido{i+1}"
    densidad = obtener_valor(f"Ingrese la densidad del fluido {
                             nombre} en kg/m^3 (por defecto 1000): ", 1000)
    altura = obtener_valor(f"Ingrese la altura de la capa de {
                           nombre} en metros (por defecto 2): ", 2)
    fluidos.append({"nombre": nombre, "densidad": densidad, "altura": altura})

# Variables para almacenar los resultados acumulados
presion_absoluta_total = Patm
fuerza_total = 0
momento_total = 0
altura_acumulada = 0

# Iterar sobre cada fluido para calcular presión, fuerza y centro de presión
for fluido in fluidos:
    densidad = fluido["densidad"]
    altura = fluido["altura"]
    nombre = fluido["nombre"]

    # Calcular presión debido al fluido actual
    presion_fluido = densidad * g * altura
    presion_absoluta_total += presion_fluido

    # Área de la sección del fluido (frontal)
    area_fluido = altura * ancho_tanque

    # Presión media y fuerza ejercida por el fluido
    presion_media_fluido = presion_fluido / 2
    fuerza_fluido = presion_media_fluido * area_fluido

    # Sumar a la fuerza total
    fuerza_total += fuerza_fluido

    # Calcular el centro de presión para el fluido
    altura_centro_presion_fluido = (2 / 3) * altura + altura_acumulada
    momento_fluido = altura_centro_presion_fluido * fuerza_fluido
    momento_total += momento_fluido

    # Actualizar altura acumulada con la altura del fluido actual
    altura_acumulada += altura

    print(f'\nPresión absoluta {nombre}: {presion_fluido} Pascales')
    print(f'Fuerza ejercida por el {nombre}: {fuerza_fluido} N')
    print(f'Momento debido al {nombre}: {momento_fluido} N*m')

# Altura del centro de presión total desde la base del tanque
altura_centro_presion_total = momento_total / fuerza_total

print(f'\nPresión absoluta total en el fondo del tanque: {
      presion_absoluta_total} Pascales')
print(f'Fuerza total en la cara frontal del tanque: {fuerza_total} N')
print(f'La altura del centro de presión desde la base del tanque es: {
      altura_centro_presion_total} metros')

print('end')
