# Determinar presion absoluta enm el fondo del tranque
# La fuerza sobre la cara fronmtal
# Centro de Presion
Patm = 101325  # Pascales
Ancho = 5  # Ancho
H = 8  # Altura total

# Aceite
rhoAceite = 920
hAceite = 3
AnchoAceite = 5
AreaAceite = hAceite*AnchoAceite
g = 9.81
PAceite = rhoAceite*g*hAceite
print(f'Presion absoluta Aceite {PAceite} Pascales ')

# Agua
rhoAgua = 1000
hAgua = 3
AnchoAgua = 5
Aagua = AnchoAgua*hAgua
Pagua = rhoAgua*g*hAgua
print(f'Presion absoluta Agua {Pagua} Pascales')

# Mercurio
rhoMercurio = 13600
hMercurio = 2
AnchoMercuio = 5
AreaMercurio = AnchoMercuio*hMercurio
PMercurio = rhoMercurio*g*hMercurio
print(f'Presion absoluta Mercurio {PMercurio} Pascales ')


# Calculo de Presion Absoluta
Pabs = PMercurio+Pagua+PAceite+Patm
print(f'Presion absoluta total en el tanque {Pabs} Pascales ')


# Calculando Fuerza sobre la cara frontal
P_MediaAceite = PAceite/2
P_MediaAgua = Pagua/2
P_MediaMercurio = PMercurio/2


# Calculando presion en el fondo
f_ac = P_MediaAceite * AreaAceite
print(f'fuerza ejercida por el aceite {f_ac} N ')

f_H20 = (PAceite + P_MediaAgua) * Aagua
print(f'fuerza ejercida por el Agua y Aceite {f_H20} N ')


f_Mer = (PAceite + Pagua + P_MediaMercurio) * AreaMercurio
print(f'fuerza ejercida por el Mercurio,Agua y Aceite {f_Mer} N ')

# Calculo de fuerza total
f_total = f_ac+f_H20+f_Mer
print(f'La fuerza total en la cara fronta es:  {f_total}')

# Calculando el centro de Presion
# ACEITE
hp1 = (2/3)*hAceite
hf1 = hp1*f_ac
print(hf1)

# AGUA
hp2 = ((2/3)*hAgua)+hAceite
hf2 = hp2*f_H20
print(hf2)

# MERCURIO
hp3 = ((2/3)*hMercurio)+hAceite+hAgua
hf3 = hp3 * f_Mer
print(hf3)

# CALCULADO ALTURA DE PRESION TOTAL
hpt = (hf1+hf2+hf3)/f_total
print(f'La altura de la presion se cuentra en: {hpt} ')
