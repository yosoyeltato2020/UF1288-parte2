import requests

def comprobar_estado():
    url = "https://api.ejemplo.com/estado"
    
    try:
        respuesta = requests.get(url)
    except requests.RequestException:
        return "FALLO DE CONEXION"

    if respuesta.status_code == 200:
        return "O.K"
    else:
        return "error"