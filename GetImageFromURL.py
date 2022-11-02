import requests

url_imagen = "https://images.pokemontcg.io/swsh9/13_hires.png"      # El link de la imagen
nombre_local_imagen = "swsh9-13.png"                                      # El nombre con el que queremos guardarla
imagen = requests.get(url_imagen).content
with open(nombre_local_imagen, 'wb') as handler:
	handler.write(imagen)