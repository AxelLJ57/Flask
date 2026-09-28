from flask import Flask, jsonify
import json

with open("API.json", "r") as json_api:
    datos_json = json.load(json_api)

app = Flask(__name__)


# Endpoint HTML
@app.route('/')
def inicio():
    print("Cambio")
    return datos_json["1A:35:ED:0F:54:63"]


@app.route('/json/<mac>')
def json_data(mac):
    # .get() para evitar errores si algún dispositivo no tiene el campo
    print(datos_json[mac].get("Name"))
    print(datos_json[mac].get("Protocolos"))
    print(datos_json[mac].get("status"))
    print(datos_json[mac].get("VLANs"))
    return datos_json[mac]["Name"]


# ---------- Endpoints JSON: 10 servidores ----------
@app.route('/servidor_1')
def servidor_1():
    return jsonify({
    "0001": {
        "ip": "192.168.0.1",
        "divice": "Router",
        "policy": ["Ro", "Not Allowed", [0.2, 0.3, 0.5] ],
        "status": True,
    }
})


@app.route('/servidor_2')
def servidor_2():  # AP3
    return jsonify({
    "0002": {
        "ip": "192.168.36.122",
        "divice": "Access Point",
        "policy": ["AP3", "Not Allowed", [0.2, 0.3, 0.5] ],
        "status": True,
    }
})


@app.route('/servidor_3')
def servidor_3():  # GW4
    return jsonify({
    "0003": {
        "ip": "192.168.40.11",
        "divice": "Gateway",
        "policy": ["GW4", "Allowed", [0.2, 0.3, 0.5] ],
        "status": True,
    }
})


@app.route('/servidor_4')
def servidor_4():  # R5
    return jsonify({
    "0004": {
        "ip": "192.168.48.211",
        "divice": "Router",
        "policy": ["R5", "Allowed", [0.2, 0.3, 0.5] ],
        "status": True,
    }
})


@app.route('/servidor_5')
def servidor_5():  # FW6
    return jsonify({
    "0005": {
        "ip": "192.168.22.128",
        "divice": "Firewall",
        "policy": ["FW6", "Allowed", [0.2, 0.3, 0.5] ],
        "status": True,
    }
})


@app.route('/servidor_6')
def servidor_6():  # R7
    return jsonify({
    "0006": {
        "ip": "192.168.7.60",
        "divice": "Router",
        "policy": ["R7", "Allowed", [0.2, 0.3, 0.5] ],
        "status": True,
    }
})


@app.route('/servidor_7')
def servidor_7():  # SW8
    return jsonify({
    "0007": {
        "ip": "192.168.38.16",
        "divice": "Switch",
        "policy": ["SW8", "Not Allowed", [0.2, 0.3, 0.5] ],
        "status": True,
    }
})


@app.route('/servidor_8')
def servidor_8():  # GW9
    return jsonify({
    "0008": {
        "ip": "192.168.37.149",
        "divice": "Gateway",
        "policy": ["GW9", "Not Allowed", [0.2, 0.3, 0.5] ],
        "status": True,
    }
})


@app.route('/servidor_9')
def servidor_9():  # SW10
    return jsonify({
    "0009": {
        "ip": "192.168.43.117",
        "divice": "Switch",
        "policy": ["SW10", "Allowed", [0.2, 0.3, 0.5] ],
        "status": True,
    }
})


@app.route('/servidor_10')
def servidor_10():  # GW11
    return jsonify({
    "0010": {
        "ip": "192.168.24.243",
        "divice": "Gateway",
        "policy": ["GW11", "Not Allowed", [0.2, 0.3, 0.5] ],
        "status": True,
    }
})


if __name__ == '__main__':
    app.run(debug=True)