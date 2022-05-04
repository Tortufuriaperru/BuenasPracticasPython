"""Cálculo de medidas estadísticas y manipulacion de ficheros.

Description
-----------
En este documento se mostrará el código para:

- calcular medias de todas las columnas o de alguna en particular.

- mostrar los primero datos de un archivo y el número de columnas.

Libraries/Modules
-----------------
- pandas library (https://pandas.pydata.org/pandas-docs/stable/)
- Acceso a multitud de funciones.
    
Notes
-----
- Comments are Sphinx (reStructuredText) compatible.


Author(s)
---------
- Created by Eva Ruiz Macías on 04/27/2020.
- Modified by Eva Ruiz Macías on 04/27/2020.
- Copyright (c) 2020 Woolsey Workshop.  All rights reserved.

"""



import pandas as pd


class Resumen:
    """Generación datos estadisticos. Ejemplo de una de las funciones:

    >>>data = Resumen('data.csv')

    >>>print(data.mediacolumna('Age'))
    
    >>>Media Age: 25.122205745043114
    """

    def __init__(self, data):
        """Contructor de la clase
        
        :param pandas.DataFrame data: `dataframe`.
        :rtype: list
        
        :return: Se leerá nuestro archivo csv
        """
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        self.df = pd.read_csv(data)
        
    def primerosvalores(self, rows):
        """Esta función nos devolverá los 5 primeros valores del dataframe
        
        :return: 5 primeros valores del dataframe
        """
        return (self.df.head(rows))
        
    def columnas(self):
        """Esta función nos devolverá el numero de columnas del dataframe
        
        :return: Numero de columnas del dataframe
        """
        return(list(self.df.columns))
        
    def medidasestadisticas(self):
        """Esta función nos devolverá un resumen con las principales medidas estadisticas
        
        :return: Media, mediana, desviacion estandar, maximo, minimo y cuartiles
        """
        return(self.df.describe())
        
    def mediacolumna(self, column): 
        """Esta función nos devolverá la media de una columna en particular
        
        :return: Media de una columna en particular
        """
        print(f"Media {column}:", self.df[column].mean())
        
    def desestandarcolumna(self, column):
        """Esta función calcula la desviacion estandar de una columna
        
        :return: Desviación estadar de una columna en particular
        """
        print(f"STD {column}:", self.df[column].std())