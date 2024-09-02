# Definición de constantes
Patm = 101325  # Presión atmosférica en Pascales
g = 9.81  # Aceleración debida a la gravedad en m/s^2

# Dimensiones del tanque
ancho_tanque = 5  # Ancho del tanque en metros
altura_total = 8  # Altura total del tanque en metros

# Propiedades de los fluidos
# Aceite
densidad_aceite = 920  # Densidad del aceite en kg/m^3
altura_aceite = 3  # Altura de la capa de aceite en metros
area_aceite = altura_aceite * ancho_tanque
presion_aceite = densidad_aceite * g * altura_aceite

# Agua
densidad_agua = 1000  # Densidad del agua en kg/m^3
altura_agua = 3  # Altura de la capa de agua en metros
area_agua = altura_agua * ancho_tanque
presion_agua = densidad_agua * g * altura_agua

# Mercurio
densidad_mercurio = 13600  # Densidad del mercurio en kg/m^3
altura_mercurio = 2  # Altura de la capa de mercurio en metros
area_mercurio = altura_mercurio * ancho_tanque
presion_mercurio = densidad_mercurio * g * altura_mercurio

# Cálculo de la presión absoluta en el fondo del tanque
presion_absoluta_total = presion_aceite + \
    presion_agua + presion_mercurio + Patm
print(f'Presión absoluta total en el fondo del tanque: {
      presion_absoluta_total} Pascales')

# Cálculo de la fuerza sobre la cara frontal del tanque
# Presión media de cada fluido
presion_media_aceite = presion_aceite / 2
presion_media_agua = presion_agua / 2
presion_media_mercurio = presion_mercurio / 2

# Fuerzas ejercidas por cada fluido
fuerza_aceite = presion_media_aceite * area_aceite
fuerza_agua = (presion_aceite + presion_media_agua) * area_agua
fuerza_mercurio = (presion_aceite + presion_agua +
                   presion_media_mercurio) * area_mercurio

# Fuerza total sobre la cara frontal del tanque
fuerza_total = fuerza_aceite + fuerza_agua + fuerza_mercurio
print(f'Fuerza total en la cara frontal del tanque: {fuerza_total} N')

# Cálculo del centro de presión
# Momento de fuerza para cada fluido
altura_presion_aceite = (2 / 3) * altura_aceite
momento_aceite = altura_presion_aceite * fuerza_aceite

altura_presion_agua = ((2 / 3) * altura_agua) + altura_aceite
momento_agua = altura_presion_agua * fuerza_agua

altura_presion_mercurio = ((2 / 3) * altura_mercurio) + \
    altura_aceite + altura_agua
momento_mercurio = altura_presion_mercurio * fuerza_mercurio

# Altura del centro de presión total
altura_centro_presion = (momento_aceite + momento_agua +
                         momento_mercurio) / fuerza_total
print(f'La altura del centro de presión desde la base del tanque es: {
      altura_centro_presion} metros')
