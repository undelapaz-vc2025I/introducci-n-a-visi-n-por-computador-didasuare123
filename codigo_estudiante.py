# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:00:25 2024

@author: jfrui
"""

# Completa las funciones de abajo de acuerdo a la descripción de los parámetros de entrada y salida

# test_visión_por_computador.py

from PIL import Image
import numpy as np

# Importamos nuestras funciones
from codigo_estudiante import (
    leer_imagen,
    obtener_info_imagen,
    imagen_a_arreglo,
    estadisticas_intensidad,
    estadisticas_por_canal
)

# Ruta de la imagen
ruta = 'imagen0.png'

# Paso 1: Leer la imagen
img = leer_imagen(ruta)
print("Imagen cargada correctamente.")

# Paso 2: Obtener información
num_canales, dimensiones = obtener_info_imagen(img)
print(f"Número de canales: {num_canales}")
print(f"Dimensiones (ancho x alto): {dimensiones}")

# Paso 3: Convertir a arreglo
arreglo = imagen_a_arreglo(img)
print(f"Tipo de arreglo: {type(arreglo)}")
print(f"Forma del arreglo: {arreglo.shape}")

# Paso 4: Estadísticas globales
promedio, desviacion = estadisticas_intensidad(arreglo)
print(f"Promedio de intensidad: {promedio:.2f}")
print(f"Desviación estándar: {desviacion:.2f}")

# Paso 5: Estadísticas por canal
estadisticas = estadisticas_por_canal(arreglo)
print("\nEstadísticas por canal:")
for canal, valores in estadisticas.items():
    print(f"{canal}: Promedio = {valores['Promedio']:.2f}, Desviación = {valores['Desviación Estándar']:.2f}")
else:
        raise ValueError("El arreglo de imagen debe tener 2 o 3 dimensiones.")
    
    return resultados
