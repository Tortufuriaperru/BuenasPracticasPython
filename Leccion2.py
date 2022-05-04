import pandas as pd
import numpy as np

finanzas = pd.read_csv('finanzas2020.csv' ,sep = '\t')

# Si hay variables no numericas forzaremos su conversion a numericas
# y reemplazaremos por cero los valores no numéricos, aunque existen
# otras técnicas como sustituir por la media, o eliminar las filas.
# En caso de que todas las variables sean numéricas no será necesario
# hacer nada.


for col in finanzas:
    finanzas[col] = pd.to_numeric(finanzas[col], errors='coerce')
    finanzas = finanzas.replace(np.nan, 0, regex=True)
    finanzas[col] = finanzas[col].astype(int)

# GASTO
# sumaremos todos los gastos (negativos) de cada columna y luego se calculará el mínimo

def gastos(archivo):
    sumanegativos = archivo[archivo < 0].sum(axis = 0, skipna = True)
    gasto = sumanegativos.min()
    return(gasto)

# AHORRO
# sumaremos todos los números (ingresos) y estó nos dará el ahorro de cada mes

def ahorro(archivo):
    sumas = archivo.sum(axis = 0, skipna = True)
    ahorros = sumas.max()
    return(ahorros)

# MEDIA DE GASTOS
# Calcularemos la media entre los gastos de cada mes obtenidos anteriormente

def mediagasto(archivo):
    sumanegativos = archivo[archivo < 0].sum(axis = 0, skipna = True)
    mediagastos = sumanegativos.mean()
    return(mediagastos)

# GASTO TOTAL ANUAL
# Haremos la suma de todos los gastos (obtenidos anteriormente)

def gastototanual(archivo):
    sumanegativos = archivo[archivo < 0].sum(axis = 0, skipna = True)
    gastototal = sumanegativos.sum()
    return(gastototal)

# INGRESO TOTAL ANUAL
# Sumaremos todos los positivos de todas las columnas y a su vez sumaremos los resultados

def ingresostotales(archivo):
    sumapositivos = archivo[archivo > 0].sum(axis = 0, skipna = True)
    ingresototal = sumapositivos.sum()
    return ingresototal