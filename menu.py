print("Bienvenido a Infinity!!! El lugar ideal para diseñar tu propia remera.")
print("Empecemos a diseñarla!")

# Función para validar si una cadena contiene solo letras
def es_cadena_letras(cadena):
    return cadena.isalpha()

# Función para validar si una cadena contiene solo números
def es_cadena_numeros(cadena):
    return cadena.isdigit()

# Función para calcular el precio de la compra
def calcular_precio(frase_remera, cantidad_remeras):
    precio_letras = len(frase_remera) * 100
    precio_total = precio_letras * cantidad_remeras
    return precio_total

# Solicitar todas las caracteristicas de la remera a los clientes
while True:
    color_remera = input("a) Ingresa el color de la remera: ")
    if not color_remera or not es_cadena_letras(color_remera):
        print("Valor incorrecto. Por favor, escribe el color con letras.")
    else:
        break

while True:
    tamanio_letra = input("b) Ingresa el tamaño de la letra (1-2-3): ")
    if not tamanio_letra or not es_cadena_numeros(tamanio_letra):
        print("Error. Por favor, responde con un número para el tamaño de la letra.")
    else:
        break

while True:
    talle_remera = input("c) Ingresa el talle de la remera(XS-S-M-L-XL): ")
    if not talle_remera or not es_cadena_letras(talle_remera):
        print("Valor incorrecto. Por favor, escribe el talle con palabras.")
    else:
        break

while True:
    frase_remera = input("d) Ingresa la frase que deseas escribir en la remera (hasta 5 palabras): ")
    palabras = frase_remera.split()
    if not frase_remera or len(palabras) > 5 or len(palabras) == 0:
        print("Error. Solo se pueden escribir hasta 5 palabras.")
    else:
        break


while True:
    cantidad_remeras = input("e) Ingresa la cantidad de remeras que deseas diseñar: ")
    if not cantidad_remeras or not es_cadena_numeros(cantidad_remeras):
        print("Error. Por favor, responde con un número para la cantidad de remeras.")
    else:
        break



# Verificar si se completaron todos los datos
datos_completos = True


if datos_completos:
    print("Genial, ¡ya completaste todos los datos!")

# Calcular el precio de la compra
precio_total = calcular_precio(frase_remera, int(cantidad_remeras))
print("El precio de su compra es de:", precio_total)

# Solicitar método de pago
while True:
    metodo_pago = input("¿Qué método desea utilizar para pagar? Opción A) Efectivo B) Transferencia Bancaria: ")
    if metodo_pago.lower() == "a" or metodo_pago.lower() == "b":
        break
    else:
        print("Opción inválida. Por favor, elige A) Efectivo o B) Transferencia Bancaria.")

if metodo_pago.lower() == "a":
    print("Genial, si deseas pagar en efectivo deberás abonar cuando recibas tu paquete!")
elif metodo_pago.lower() == "b":
    email = input("Por favor, ingresa tu dirección de correo electrónico para enviar la factura: ")
    print("¡Ya te hemos enviado un correo electrónico con la factura para que realices el pago!")
    
    while True:
        respuesta_email = input("¿Te ha llegado el correo electrónico? (Si/No): ")
        if respuesta_email.lower() == "si":
            print("¡Genial! Ya puedes realizar el pago.")
            break
        elif respuesta_email.lower() == "no":
            print("Hemos reenviado el correo electrónico. Por favor, revisa nuevamente.")
        else:
            print("Respuesta inválida. Por favor, responde con Si o No.")

direccion_casa = input("Por último, ingresa la dirección de tu casa: ")
print("Genial, en unos días estaremos enviando el paquete a", direccion_casa + ".")
print("¡Muchísimas gracias por confiar en nosotros! ¡Que tengas un buen día!")
