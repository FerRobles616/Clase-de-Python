#-*- coding: utf-8 -*-
# Caracteres especiales


from flask import Flask, jsonify, request
from login import login
from logout import logout

app = Flask(__name__)

##Se expone el blueprint de login
app.register_blueprint(login)
##Se expone el blueprint de logout
app.register_blueprint(logout)
@app.route('/', methods=['GET'])

def unida():
    return 'Server flask is running on port 5000!'

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
# Ejecutar el servidor con: python app.py