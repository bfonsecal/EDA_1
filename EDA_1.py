import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#importo libreria
ruta = '/Users/56966/Desktop/Analisis de datos/VSC/dataset_banco.csv'
data = pd.read_csv(ruta)
#print(data)

#print(data.shape)

#data.head()

#Variables categoricas y numericas
#data.info() 

#Eliminamos fila completa en la que faltan datos
#data.dropna(inplace = True) 
#data.info()

#Columnas irrelevenates
#Coneteo de los niveles en columnas categoricas
#cols_cat = ['job', 'marital', 'education','default'
 #           , 'housing', 'loan', 'contact', 'month','poutcome','y']
#for col in cols_cat:
   # print(f'Columna{col} : {data[col].nunique()} subniveles')

#Todas las categoricas tienen mas de 1 subnivel

#Columnas  numericas
print(data.describe())
#No hay columnas con std igual a cero por lo que todas son relevantes

#Filas repetidas
