meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "AGUACATE": "tambien conocido como palta",
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
            
if word in meme_dict.keys():            
                    
    print(meme_dict[word])
else:
    
    print("la palabra no existe aun en nuestro diccionario")        
