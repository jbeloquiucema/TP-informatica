class Remera:

    def __init__(self, remera_code, color,tamaño_letra, price, cantidad, frase, talle) -> None:
        self.remera_code = remera_code
        self.color = color
        self.tamaño_letra = tamaño_letra
        self.price = price
        self.cantidad = cantidad
        self.frase = frase
        self.talle = talle


    def serialize(self):
        return {
            'remera_code': self.remera_code,
            'color': self.color,
            'talle': self.talle,
            'price': self.price
        }

    def serialize_details(self):
        return {
            'remera_code': self.remera_code,
            'color': self.color,
            'tamaño_letra': self.tamaño_letra,
            'price': self.price,
            'cantidad': self.cantidad,
            'frase': self.frase,
            'talle': self.talle
        }
