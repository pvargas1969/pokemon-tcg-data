import os, json, pandas

#TotalKeys = []

#Campos = ['id', 'name', 'supertype', 'subtypes', 'level', 'hp', 'types', 'evolvesFrom', 
#            'abilities', 'attacks', 'weaknesses', 'retreatCost', 'convertedRetreatCost', 
#            'number', 'artist', 'rarity', 'flavorText', 'nationalPokedexNumbers', 'legalities', 
#            'images', 'evolvesTo', 'resistances', 'rules', 'ancientTrait', 'regulationMark']

Campos = ['id', 'name', 'supertype', 'subtypes', 'level', 'hp', 'types', 'evolvesFrom', 
            'abilities', 'attacks', 'weaknesses', 'retreatCost', 'convertedRetreatCost', 
            'number', 'artist', 'rarity', 'flavorText', 'nationalPokedexNumbers', 'legalities', 
            'images', 'evolvesTo', 'resistances'] #, 'rules', 'ancientTrait', 'regulationMark']

Contador = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

LCampos = len(Campos)

archivos = os.listdir('cards\\en')

fCartas = open("Cartas.sql", "w", encoding='utf-8')
fSubTipos = open("SubTipos.sql", "w", encoding='utf-8')
fTipos = open("Tipos.sql", "w", encoding='utf-8')
fHabilidades = open("Habilidades.sql", "w", encoding='utf-8')
fAtaques = open("Ataques.sql", "w", encoding='utf-8')
fDebilidades = open("Debilidades.sql", "w", encoding='utf-8')
fRetidara = open("Retirada.sql", "w", encoding='utf-8')
fFlavorText = open("FlavorText.sql", "w", encoding='utf-8')
fNatPdexNum = open("NatPdexNum.sql", "w", encoding='utf-8')
fLegalidad = open("Legalidad.sql", "w", encoding='utf-8')
fImagenes = open("Imagenes.sql", "w", encoding='utf-8')
fResistencias = open("Resistencias.sql", "w", encoding='utf-8')

for archivo in archivos:
    with open("cards\\en\\" + archivo, encoding="utf8") as ArchivoJson:
        datos = json.load(ArchivoJson)
        NReg = len(datos)
        for i in range(0, NReg):
            print("--", "=" * 120)
            Keys = list(datos[i].keys())

            for j in range(LCampos):
                if (Campos[j] in Keys):
            #        print(Campos[j], " : ", datos[i][Campos[j]])
                    Contador[j] += 1
            #    else:
            #        print(Campos[j], " : ")

            stSql = ""
            stSql += "INSERT CARTA VALUES ("
            stSql += "'" + datos[i]["id"] + "', "
            stSql += datos[i]["number"] + ", "
            stSql += "'" + datos[i]["name"].replace("'", "''") + "', "
            stSql += "'" + datos[i]["supertype"] + "', "

            #Level
            if ("level" in Keys):
                stSql += "'" + datos[i]["level"] + "', "
            else:
                stSql += "''" + ", "

            #Hp
            if ("hp" in Keys):
                stSql += datos[i]["hp"] + ", "
            else:
                stSql += "0" + ", "

            #artist
            if ("artist" in Keys):
                stSql += "'" + datos[i]["artist"] + "', "
            else:
                stSql += "''" + ", "

            #rarity
            if ("rarity" in Keys):
                stSql += "'" + datos[i]["rarity"] + "', "
            else:
                stSql += "''" + ", "

            #evolvesFrom
            if ("evolvesFrom" in Keys):
                stSql += "'" + datos[i]["evolvesFrom"].replace("'", "''") + "', "
            else:
                stSql += "'', "

            #evolvesTo
            if ("evolvesTo" in Keys):
                stSql += "'" + str(datos[i]["evolvesTo"]).replace("[", "").replace("]", "").replace("'", "").replace(", ", ",") + "'"
            else:
                stSql += "''"

            stSql += ")"
##            print("/* Carta     : */ ", stSql)
            fCartas.write(stSql + "\n")

            #subtypes
            if ("subtypes" in Keys):
                L = datos[i]["subtypes"]
                for k in range(len(L)):
                    stSql = "INSERT SUBTIPO VALUES ('" + datos[i]["id"] + "', '" + L[k].replace("'", "''") + "')"
##                    print("/* Subtipo   : */ ", stSql)
                    fSubTipos.write(stSql + "\n")

            #types
            if ("types" in Keys):
                L = datos[i]["types"]
                for k in range(len(L)):
                    stSql = "INSERT TIPO VALUES ('" + datos[i]["id"] + "', '" + L[k] + "')"
##                    print("/* Tipo      : */ ", stSql)
                    fTipos.write(stSql + "\n")

            #abilities
            if ("abilities" in Keys):
                Lista = datos[i]["abilities"]
                L = len(Lista)
                for k in range(L):
                    stSql = "INSERT HABILIDAD VALUES ("
                    stSql += "'" + datos[i]["id"] + "', "
                    stSql += "'" + Lista[k]["name"].replace("'", "''") + "', "
                    stSql += "'" + Lista[k]["type"] + "', "
                    stSql += "'" + Lista[k]["text"].replace("'", "''") + "')"
##                    print("/* Habilidad : */ ", stSql)
                    fHabilidades.write(stSql + "\n")

            #attacks
            if ("attacks" in Keys):
                #['name', 'cost', 'convertedEnergyCost', 'damage', 'text']
                Lista = datos[i]["attacks"]
                L = len(Lista)
                for k in range(L):
                    #print(Lista[k])
                    #AtkKeys = list(Lista[k].keys())
                    #TotalKeys.extend(AtkKeys)
                    #TotalKeys = list(pandas.unique(TotalKeys))
                    stCosto = str(Lista[k]["cost"]).replace("[", "").replace("]", "").replace("'", "")
                    #print(datos[i]["id"], Lista[k]["name"], stCosto, Lista[k]["convertedEnergyCost"], Lista[k]["damage"], Lista[k]["text"].replace("'", "''"))
                    stSql = "INSERT ATAQUE VALUES ("
                    stSql += "'" + datos[i]["id"] + "', "
                    stSql += "'" + Lista[k]["name"].replace("'", "''") + "', "
                    stSql += "'" + stCosto + "', "
                    stSql += str(Lista[k]["convertedEnergyCost"]) + ", "
                    if (Lista[k]["damage"].strip() == "" ):
                        stSql += "'0', "
                    else:
                        stSql += "'" + Lista[k]["damage"] + "', "
                    stSql += "'" + Lista[k]["text"].replace("'", "''") + "')"
##                    print("/* Ataque    : */", stSql)
                    fAtaques.write(stSql + "\n")

            #weaknesses
            if ("weaknesses" in Keys):
                Lista = datos[i]["weaknesses"]
                L = len(Lista)
                for k in range(L):
                    #Keys = list(Lista[k].keys())
                    #print(Keys, Lista[k]["type"], Lista[k]["value"])
                    stSql = "INSERT DEBILIDAD VALUES ("
                    stSql += "'" + datos[i]["id"] + "', "
                    stSql += "'" + Lista[k]["type"] + "', "
                    stSql += "'" + Lista[k]["value"] + "')"
##                    print(stSql)
                    fDebilidades.write(stSql + "\n")

            #retreatCost y convertedRetreatCost
            if (("retreatCost" in Keys) and ("convertedRetreatCost" in Keys)):
                stCostoRet = str(datos[i]["retreatCost"]).replace("[", "").replace("]", "").replace("'", "")
                stSql = "INSERT RETIRADA VALUES ("
                stSql += "'" + datos[i]["id"] + "', "
                stSql += str(datos[i]["convertedRetreatCost"]) + ", "
                stSql += "'" + stCostoRet + "')"
##              #  print(stSql)
                fRetidara.write(stSql + "\n")
            elif (("retreatCost" in Keys)):
                print("NOOK...!!!")
            elif (("convertedRetreatCost" in Keys)):
                print("NOOK...!!!")

            #flavorText
            if ("flavorText" in Keys):
                stflavorText = str(datos[i]["flavorText"]).replace("'", "''")
                stSql = "INSERT FLAVORTEXT VALUES ("
                stSql += "'" + datos[i]["id"] + "', "
                stSql += "'" + stflavorText + "')"
##                print(stSql)
                fFlavorText.write(stSql + "\n")

            #nationalPokedexNumbers
            if ("nationalPokedexNumbers" in Keys):
                stNatPdexNum = str(datos[i]["nationalPokedexNumbers"]).replace("[", "").replace("]", "").replace(" ", "")
                stSql = "INSERT NATPDEXNUM VALUES ("
                stSql += "'" + datos[i]["id"] + "', "
                stSql += "'" + stNatPdexNum + "')"
                #print(stNatPdexNum)
                fNatPdexNum.write(stSql + "\n")

            #legalities
            if ("legalities" in Keys):
                LglKeys = datos[i]["legalities"].keys()
                #TotalKeys.extend(LglKeys)
                #TotalKeys = list(pandas.unique(TotalKeys))
                stLglStd, stLglExp, stLglUnl = "", "", ""
                if ("standard" in LglKeys):
                    stLglStd = datos[i]["legalities"]["standard"]
                if ("expanded" in LglKeys):
                    stLglExp = datos[i]["legalities"]["expanded"]
                if ("unlimited" in LglKeys):
                    stLglUnl = datos[i]["legalities"]["unlimited"]
##                print(datos[i]["id"], stLglStd, stLglExp, stLglUnl)
                stSql = ""
                stSql += "INSERT LEGALIDAD VALUES ("
                stSql += "'" + datos[i]["id"] + "', "
                stSql += "'" + stLglStd + "', "
                stSql += "'" + stLglExp + "', "
                stSql += "'" + stLglUnl + "')"
                fLegalidad.write(stSql + "\n")

            #images
            if ("images" in Keys):
##                print(datos[i]["id"], datos[i]["images"]["small"], datos[i]["images"]["large"])
                stSql = ""
                stSql += "INSERT IMAGEN VALUES ("
                stSql += "'" + datos[i]["id"] + "', "
                stSql += "'" + datos[i]["images"]["small"] + "', "
                stSql += "'" + datos[i]["images"]["large"] + "')"
                #print(stSql)
                fImagenes.write(stSql + "\n")

            #resistances
            if ("resistances" in Keys):
                Lista = datos[i]["resistances"]
                L = len(Lista)
                for k in range(L):
                    #Keys = list(Lista[k].keys())
                    #print(Keys, Lista[k]["type"], Lista[k]["value"])
                    stSql = "INSERT RESISTENCIA VALUES ("
                    stSql += "'" + datos[i]["id"] + "', "
                    stSql += "'" + Lista[k]["type"] + "', "
                    stSql += "'" + Lista[k]["value"] + "')"
##                    print(stSql)
                    fResistencias.write(stSql + "\n")

print("--", "=" * 120)

print(Contador)
## print(TotalKeys)

fCartas.close()
fSubTipos.close()
fTipos.close()
fHabilidades.close()
fAtaques.close()
fDebilidades.close()
fRetidara.close()
fFlavorText.close()
fNatPdexNum.close()
fLegalidad.close()
fImagenes.close()
fResistencias.close()
