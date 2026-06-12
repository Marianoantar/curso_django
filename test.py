import requests

respuesta = requests.get("https://www.google.com", timeout=5)

contenido = respuesta.content.decode()

print(respuesta)
print(contenido)
