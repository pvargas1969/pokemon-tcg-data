import json

#with open("cards\\en\\base1.json") as archivo:
with open("cards\\en\\swsh9.json") as archivo:
    datos = json.load(archivo)

#print(len(datos))

L1 = len(datos)

for i in range(0, L1):
    #print (datos[i].keys())
    Keys = list(datos[i].keys())
    if ("nationalPokedexNumbers" in Keys):
        print(datos[i]["number"], datos[i]["id"], datos[i]["supertype"], datos[i]["name"], datos[i]["nationalPokedexNumbers"])
    else:
        print(datos[i]["number"], datos[i]["id"], datos[i]["supertype"], datos[i]["name"])

    #L2 = len(Keys)
    #for j in range(0, L2):
    #    print(Keys[j], datos[i][Keys[j]])



    #print(i, datos[i]["id"], datos[i]["abilities"])

#cliente_JSON = json.dumps(datos, indent=4)

#print(cliente_JSON)
#print(datos[0])

#P = json.dumps(datos[0], indent=4)

#print(P)
#print(datos[0]["id"])
#print(datos[0]["abilities"])
#print(P[1])

