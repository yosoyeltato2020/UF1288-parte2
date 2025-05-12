import requests

def comprobar_estado():
    """
    Estoy haciendo una funcion que haga una  petición GET  y verifica el estado de la conexión.

    Devuelve:
        Un string: "O.K" si el código de respuesta es 200, de lo contrario si es un erro 404 o 500 da "error".
    """
    url = "https://api.ejemplo.com/estado"
    try:
        # Realiza la petición GET.
        respuesta = requests.get(url)
               
        codigo_respuesta = respuesta.status_code
                
        # Verifica si el código de respuesta es 200.
        if codigo_respuesta == 200:
            resultado = "O.K"
        else:
            resultado = "error"
    except requests.exceptions.Timeout:
        
        return "FALLO DE CONEXION"
    except requests.exceptions.ConnectionError:
        
        return "FALLO DE CONEXION"
    except requests.exceptions.RequestException:
        
        resultado = "FALLO DE CONEXION"
    
    
    return resultado
