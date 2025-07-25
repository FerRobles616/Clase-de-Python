from flask import Blueprint, Flask, jsonify, request


cliente= Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])

def llamarServicioSet():
    ci= request.json.get('ci')
    print("ci enviado:", ci)

    codRes, menRes, accion = inicializarVariables(ci)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'cedula': ci,
        'accion': accion,
    }

    return jsonify(salida)


def inicializarVariables(ci):
    accion = "Success"
    codRes = 'SIN_ERROR'
    menRes = "OK"
    cedula= "4133266"
    nombre = "Derlis"
    apellido= "Caballero Mendoza"

    try:
        if ci == cedula:
            print("Success")
            accion = "Success"
    except Exception as e:
        accion = "Cliente no está en el sistema"
        codRes = "ERROR"
        menRes = "Error cliente"
        ci = "4133267"
        return codRes, menRes, accion,
    
    
    
    return codRes, menRes, accion,