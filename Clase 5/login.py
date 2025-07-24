from flask import Blueprint, Flask, jsonify, request


login= Blueprint('login', __name__)

@login.route('/login', methods=['POST'])

def llamarServicioSet():
    user= request.json.get('user')
    password= request.json.get('password')
    print("User enviado:", user, "Pass enviado:", password)

    codRes, menRes, accion, rol = inicializarVariables(user, password)

    #si hubo error en el login
    if codRes == 'ERROR':
        user = "N/A"

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'usuario': user,
        'accion': accion,
        'rol': rol
    }

    return jsonify(salida)


def inicializarVariables(user, password):
    codRes = 'SIN_ERROR'
    menRes = "OK"
    accion = "login exitoso"
    rol= "admin"
    userlocar = "gray"
    passwordlocal= "unida2025"

    try:
        if user == userlocar and password == passwordlocal:
            print("Login exitoso")
            accion = "login exitoso"
        else:
            codRes = 'ERROR'
            menRes = "Usuario o contraseña incorrectos"
            accion = "login fallido"
            rol = "N/A"
    except Exception as e:
        print("Error en el login:", e)
        codRes = 'ERROR'
        menRes = "Error en el login"
        accion = "error en el login"
        rol = "N/A"
        return codRes, menRes, accion, rol,
    
    
    
    return codRes, menRes, accion, rol,