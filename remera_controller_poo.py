from db_remeras import get_db
from clase_remeras import Remera


def insert_remera(remera_code, color, tamaño_letra, price, cantidad, frase, talle):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO remeras (remera_code, color, tamaño_letra, price, cantidad, frase, talle) \
    VALUES ( ?, ?, ?, ? ,?, ?, ?)"
    cursor.execute(statement, [remera_code, color, tamaño_letra, price, cantidad, frase, talle])
    db.commit()
    return True

def update_remera(remera_code, color, tamaño_letra, price, cantidad, frase, talle):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE remeras SET color = ?, tamaño_letra = ?, cantidad= ?, frase= ?, talle= ? \
    WHERE remera_code = ?"
    cursor.execute(statement, [color, tamaño_letra, price, cantidad, frase, talle, remera_code])
    db.commit()
    return True


def delete_remera(remera_code):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM remeras WHERE remera_code = ?"
    cursor.execute(statement, [remera_code])
    db.commit()
    return True


def get_by_id(remera_code):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT remera_code, color, tamaño_letra, price, cantidad, frase, talle FROM remeras \
    WHERE remera_code = ?"
    cursor.execute(statement, [remera_code])
    single_remera = cursor.fetchone()
    remera_code = single_remera[0]
    color = single_remera[1]
    tamaño_letra = single_remera[2]
    price = single_remera[3]
    cantidad = single_remera[4]
    frase = single_remera[5]
    talle = single_remera[6]
    remera = Remera (remera_code, color, tamaño_letra, price, cantidad, frase, talle) 
    return game.serialize_details()


def get_remeras():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT remera_code, color, tamaño_letra, price, cantidad, frase, talle FROM remeras"
    cursor.execute(query)
    remera_list = cursor.fetchall()
    list_of_remeras=[]
    for remera in remera_list:
        remera_code = remera[0]
        color = remera[1]
        tamaño_letra = remera[2]
        price = remera[3]
        cantidad = remera[4]
        frase = remera[5]
        talle = remera[6]
        remera_to_add = Remera(remera_code, color, tamaño_letra, price, cantidad, frase, talle)
        list_of_remeras.append(remera_to_add)
    return list_of_remeras



