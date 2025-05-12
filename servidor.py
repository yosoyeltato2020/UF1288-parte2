from flask import Flask, jsonify
from cliente import comprobar_estado

app = Flask(__name__)

@app.route('/estado', methods=['GET'])
def estado_servidor():
    """
    verifica el estado del servidor llamando a la función comprobar_estado.
    
       
    """
    estado = comprobar_estado()
    return jsonify({"estado": estado})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)