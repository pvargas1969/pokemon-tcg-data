import os, json, pandas as pd

archivos = os.listdir('cards\\en')

LArchivos = len(archivos)

#for i in range(LArchivos):
#    print(i, archivos[i])

TotalKeys = []

for archivo in archivos:
    #print(archivo)
    with open("cards\\en\\" + archivo, encoding="utf8") as ArchivoJson:
        datos = json.load(ArchivoJson)

    L1 = len(datos)
    for i in range(0, L1):
        Keys = list(datos[i].keys())
        TotalKeys.extend(Keys)
        #print(TotalKeys)
        TotalKeys = list(pd.unique(TotalKeys))

print(TotalKeys)
