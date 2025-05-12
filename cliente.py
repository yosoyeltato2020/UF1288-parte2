import requests

def comprobar_estado():
    """
    Realiza una petición GET a https://api.ejemplo.com/estado y verifica el estado de la conexión.

    Returns:
        str: "O.K" si el código de respuesta es 200, de lo contrario "FALLO DE CONEXION".
    """
    url = "https://api.ejemplo.com/estado"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "O.K"
        else:
            return "FALLO DE CONEXION"
    except requests.exceptions.RequestException:
        return "FALLO DE CONEXION"