from flask import Flask, jsonify, request
import remera_controller_poo
from db_remeras import create_tables
from exchange_rate import get_xr

app = Flask(__name__)


@app.route('/remeras', methods=["GET"])
def get_remeras():
    remeras = remera_controller_poo.get_remeras()
    remeras_list=[]
    for remera in remeras:
        elem = remera.serialize()
        remeras_list.append(elem)
    return jsonify(remeras_list)

@app.route("/remera/create", methods=["POST"])
def insert_remera():
    remera_details = request.get_json()
    remera_code = remera_details["remera_code"]
    color = remera_details["color"]
    tamaño_letra =remera_details["tamaño_letra"]
    price = remera_details["price"]
    cantidad= remera_details["cantidad"]
    frase= remera_details["frase"]
    talle = remera_details["talle"]
    result = remera_controller_poo.insert_remera(remera_code, color, tamaño_letra, price, cantidad, frase, talle)
    return jsonify(result)


@app.route("/game/modify", methods=["PUT"])
def update_remera():
    remera_details = request.get_json()
    remera_code = remera_details["remera_code"]
    color = remera_details["color"]
    tamaño_letra =remera_details["tamaño_letra"]
    price = remera_details["price"]
    cantidad= remera_details["cantidad"]
    frase= remera_details["frase"]
    talle = remera_details["talle"]
    result = remera_controller_poo.update_remera(remera_code, color, tamaño_letra, price, cantidad, frase, talle)
    return jsonify(result)



@app.route("/remera/eliminate/<remera_code>", methods=["DELETE"])
def delete_remera(remera_code):
    result = remera_controller_poo.delete_remera(remera_code)
    return jsonify(result)


@app.route("/remera/<remera_code>", methods=["GET"])
def get_remera_by_id(remera_code):
    remera = remera_controller_poo.get_by_id(remera_code)
    return jsonify(remera)

@app.route("/remera/usd/<remera_code>", methods=["GET"])
def get_remera_by_id_usd(remera_code):
    remera = remera_controller_poo.get_by_id(remera_code)
    xr = get_xr()
    price_usd = remera['price']/xr
    remera['price'] = round(price_usd,2)
    return jsonify(remera)

create_tables()

app.run()

if __name__ == '__main__':
    app.run()
