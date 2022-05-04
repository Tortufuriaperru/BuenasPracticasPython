import pandas as pd
import numpy as np
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
import matplotlib.pyplot as plt

# Se probará si existe el archivo, en caso contrario, saltará la exceptción

try:
    finanzas = pd.read_csv('finanzas2020.csv' ,sep = '\t')
    # Se muestra la existencia del archivo
    # Se muestra la existencia de todas las columnas con el tipo de datos
    print(finanzas.info())
    print(finanzas.head())
    
    # Si hay variables no numericas forzaremos su conversion a numericas
    # y reemplazaremos por cero los valores no numéricos, aunque existen
    # otras técnicas como sustituir por la media, o eliminar las filas.
    # En caso de que todas las variables sean numéricas no será necesario
    # hacer nada.

    for col in finanzas:
        if not(is_numeric_dtype(col)):
            finanzas[col] = pd.to_numeric(finanzas[col], errors='coerce')
            finanzas = finanzas.replace(np.nan, 0, regex=True)
            finanzas[col] = finanzas[col].astype(int)
        else:
            raise Exception ("No es necesario cambiar el tipo de variable para continuar.")
            
    
    print("**************************************")
    print("**************************************")
    print("**************************************\n")
    

    # GASTO
    # sumaremos todos los gastos (negativos) de cada columna y luego se calculará el mínimo
    sumanegativos = finanzas[finanzas < 0].sum(axis = 0, skipna = True)
    gasto = sumanegativos.min()
    nombres = finanzas.columns.values
    list1 = list(zip(nombres, sumanegativos))
    df1= pd.DataFrame(list1)
    posic1=df1.loc[df1[1] == gasto]
    print("Se muestra el mes con mayor gasto junto con la cantidad gastada\n")
    print(posic1)

    print("**************************************")
    print("**************************************")
    print("**************************************\n")


    # AHORRO
    # sumaremos todos los números (ingresos) y estó nos dará el ahorro de cada mes
    sumas = finanzas.sum(axis = 0, skipna = True)
    print(sumas)
    ahorro = sumas.max()
    nombres = finanzas.columns.values
    list2 = list(zip(nombres, sumas))
    df2= pd.DataFrame(list2)
    posic2=df2.loc[df2[1] == ahorro]
    print("Se muestra el mes con mayor ahorro junto con la cantidad ahorrada\n")
    print(posic2)

    print("**************************************")
    print("**************************************")
    print("**************************************\n")

    # MEDIA DE GASTOS
    # Calcularemos la media entre los gastos de cada mes obtenidos anteriormente
    
    print("La media de los gastos ha sido:\n")
    mediagastos = sumanegativos.mean()
    print(abs(mediagastos))

    print("**************************************")
    print("**************************************")
    print("**************************************\n")

    # GASTO TOTAL ANUAL
    # Haremos la suma de todos los gastos (obtenidos anteriormente)
    print("El gasto Anual ha sido:\n")
    gastototal = sumanegativos.sum()
    print(abs(gastototal))

    print("**************************************")
    print("**************************************")
    print("**************************************\n")

    # INGRESO TOTAL ANUAL
    # Sumaremos todos los positivos de todas las columnas y a su vez sumaremos los resultados
    print("Los ingresos anuales han sido:\n")
    sumapositivos = finanzas[finanzas > 0].sum(axis = 0, skipna = True)
    #print(sumapositivos)
    ingresototal = sumapositivos.sum()
    print(ingresototal)
    
    print("**************************************")
    print("**************************************")
    print("**************************************\n")

    # Gráfica de los ingresos por mes durante todo el año con matplotlib
    
    print("Mostramos una gráfica con los ingresos mensuales\n")
    plt.bar(nombres, sumapositivos)
    plt.xlabel("Meses", size = 16,)
    plt.ylabel("Ingresos", size = 16)

    plt.title("Ingresos por mes", 
              fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 18})

    plt.show()
    
except IOError:
    print("Error:El archivo no existe o no se ha podido cargar")



