# Definición de constantes
Patm = 101325  # Presión atmosférica en Pascales
g = 9.81  # Aceleración debida a la gravedad en m/s^2
ancho_tanque = 5  # Ancho del tanque en metros

# Lista de fluidos en el tanque
# Cada fluido es un diccionario con sus propiedades: densidad y altura
fluidos = [
    {"nombre": "Aceite", "densidad": 920, "altura": 3},
    {"nombre": "Agua", "densidad": 1000, "altura": 3},
    {"nombre": "Mercurio", "densidad": 13600, "altura": 2}
]

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

    print(f'Presión absoluta {nombre}: {presion_fluido} Pascales')
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
