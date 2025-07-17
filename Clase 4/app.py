#-*- coding: utf-8 -*-
# Caracteres especiales


from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods=['GET'])

def unida():
    return 'Hola soy Goku'

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
# Ejecutar el servidor con: python app.py