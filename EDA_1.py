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
data.dropna(inplace = True) 
#data.info()

#Columnas irrelevenates
#Coneteo de los niveles en columnas categoricas
#cols_cat = ['job', 'marital', 'education','default'
 #           , 'housing', 'loan', 'contact', 'month','poutcome','y']
#for col in cols_cat:
   # print(f'Columna{col} : {data[col].nunique()} subniveles')

#Todas las categoricas tienen mas de 1 subnivel

#Columnas  numericas
#print(data.describe())
#No hay columnas con std igual a cero por lo que todas son relevantes 

#Filas repetidas

#print(f'tamaño del set antes de eliminar filas repetidas: {data.shape}')
data.drop_duplicates(inplace=True)
#print(f'tamaño del set despues de eliminar filas repetidas: {data.shape}')

#      VARIABLES NUMERICAS
#Valores extremos (Outliers)
cols_num = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']

fig, ax = plt.subplots(nrows=7, ncols=1, figsize=(8,30))
fig.subplots_adjust(hspace=0.5)

for i, col in enumerate(cols_num):
    sns.boxplot(x=col, data=data, ax=ax[i])
    ax[i].set_title(col)

#Nos enfocamos en age , duration y previous

#age
data = data[data['age']<=100]
#duration
data = data[data['duration']>0]
data = data[data['previous']<=100]

#print(data.shape)
#Finalmente tenemos 45.189 filas

#    VARIABLES CATEGORICAS
cols_cat = ['job','marital', 'education','default','housing','loan','contact','month','poutcome','y']

fig , ax = plt.subplots(nrows=10 , ncols=  1 , figsize =(10,30))
fig.subplots_adjust(hspace=1)

for i, col in enumerate(cols_cat):
    sns.countplot(x=col,data=data,ax=ax[i])
    ax[i].set_title(col)
    ax[i].set_xticklabels(ax[i].get_xticklabels(),rotation=30)

#todo a minuscula
for column in data.columns:
    if column in cols_cat:
        data[column] = data[column].str.lower()

#Graficamos nuevamente

fig , ax = plt.subplots(nrows=10 , ncols=  1 , figsize =(10,30))
fig.subplots_adjust(hspace=1)

for i, col in enumerate(cols_cat):
    sns.countplot(x=col,data=data,ax=ax[i])
    ax[i].set_title(col)
    ax[i].set_xticklabels(ax[i].get_xticklabels(),rotation=30)
   
#unificamos para cada categoria
#job: admin. y administrative
data['job']= data['job'].str.replace('admin.', 'administrative', regex= False)
#marital : div. y divorced
data['marital']=data['marital'].str.replace('div.', 'divorced', regex=False)
#education 
data['education']=data['education'].str.replace('sec.', 'secondary', regex=False)
data['education']=data['education'].str.replace('unk', 'unknown', regex=False)
data['education']=data['education'].str.replace('unknownnown', 'unknown', regex=False)
#contact
data['contact']=data['contact'].str.replace('phone', 'telephone', regex=False)
data['contact']=data['contact'].str.replace('teletelephone', 'telephone', regex=False)
data['contact']=data['contact'].str.replace('mobile', 'telephone', regex=False)

#poutcome
data['poutcome']=data['poutcome'].str.replace('unk', 'unknown', regex=False)
data['poutcome']=data['poutcome'].str.replace('unknownnown', 'unknown', regex=False)
#Graficamos una ultima vez


fig , ax = plt.subplots(nrows=10 , ncols=  1 , figsize =(10,30))
fig.subplots_adjust(hspace=1)

for i, col in enumerate(cols_cat):
    sns.countplot(x=col,data=data,ax=ax[i])
    ax[i].set_title(col)
    ax[i].set_xticklabels(ax[i].get_xticklabels(),rotation=30)
   
#   LISTO TENEMOS LOS DATOS LIMPIOS

#Eliminamos variables que no son relevnatnes para nuestro objetivo 

data.drop(columns=['contact','month','day','duration', 'campaign', 'pdays', 'previous'],inplace=True)
#data.describe()

col_num = ['age', 'balance']

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,5))
fig.subplots_adjust(hspace=0.5)

for i, col in enumerate(col_num):
    if col == 'age':
        nbins = 10
    else:
        nbins = 50
    sns.histplot(x=col, data=data, ax=ax[i], bins=nbins, kde = True)
    ax[i].set_title(col)

data['balance'].describe()

#El 75% de la poblacion tiene un balance de al rededor 1500
#La edad se encuentra entre 25 y 40 años

#analisis univariado
#Variable a predecir de forma binaria 'y' ( ¿el cliente se suscribió a un depósito a término?)

diccionario = {'yes':1, 'no':0}
binario = data['y'].map(diccionario)
data['y_bin']= binario

fig , ax = plt.subplots(nrows=1,ncols=2, figsize=(15,5))
fig.subplots_adjust(hspace=0.5)

for i, col in enumerate(col_num):
    bplt = sns.boxplot(x='y_bin',y=col,data=data,ax=ax[i])
    ax[i].set_xlabel('y_bin (1:yes, 0:no)')
    ax[i].set_title(col)
    # Al observar el grafico de edad y balance no s eobserva una evidencia significatica para que sean relevantes

print(diccionario)
