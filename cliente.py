from flask import Blueprint, Flask, jsonify, request


cliente= Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])

def llamarServicioSet():
 ci= request.json.get('ci')
    print("ci enviado:", ci)

    codRes, menRes, accion, nombre, apellido = inicializarVariables(ci)

    if codRes == 'ERROR':
        ci = "4133267"

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'ci': ci,
        'accion': accion,
        'nombre': nombre,
        'apellido': apellido
    }

    return jsonify(salida)


def inicializarVariables(cedula):
    accion = "Success"
    codRes = 'SIN_ERROR'
    menRes = "OK"
    ci= "4133266"
    nombre = "Derlis"
    apellido= "Caballero Mendoza"

    try:
        if cedula == ci:
            print("Success")
            accion = "Success"
        else:
            codRes = 'ERROR'
            menRes = "Cliente no encontrado"
            accion = "Cliente no está en el sistema"
            ci = "4133267"
            nombre = ""
            apellido = ""
    except Exception as e:
        accion = "Cliente no está en el sistema"
        codRes = "ERROR"
        menRes = "Error cliente"
        ci = "4133267"
        return codRes, menRes, accion,

    return codRes, menRes, accion, nombre, apellido
