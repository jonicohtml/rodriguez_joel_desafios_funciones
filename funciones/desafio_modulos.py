'''
1 - Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:

En donde:
mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
mínimo: valor mínimo admitido (inclusive)
máximo: valor máximo admitido (inclusive)
reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.

En caso de que la función no haya podido conseguir un número válido, la misma retorna None.

Repetir el mismo procedimiento para un dato de tipo float.

'''

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int| None:
    
    cont = 0
    numero = input(f"{mensaje}")
    
    while numero.isdigit() == False:
        cont += 1
        if cont > reintentos:
            return None
        else:
            numero = input(f"{mensaje_error}")
    numero = int(numero)
    
    while numero > maximo or numero < minimo:
        numero = input(f"{mensaje_error}")
        numero = int(numero)
        cont += 1
        if cont > reintentos:
            return None
        
print(get_int("Ingese un número entero: ", f"ERROR. Vuelva a ingresar un número entero válido: ", 3, 6, 2))
'''

'''
def get_float(mensaje: str, mensaje_error: str, minimo: float | int, maximo: float | int, reintentos: int) -> float | None:
    
    cont = 0
    numero = input(f"{mensaje}")
    
    while "." not in numero:
        cont += 1
        if cont > reintentos:
            return None
        else:
            numero = input(f"{mensaje_error}")
    numero = float(numero)
    
    while numero > maximo or numero < minimo:
        numero = input(f"{mensaje_error}")
        numero = float(numero)
        cont += 1
        if cont > reintentos:
            return None
    
print(get_float("Ingese un número decimal: ", f"ERROR. Vuelva a ingresar un número entero válido: ", 3, 6, 2))

'''
Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud de la cadena ingresada dado el parámetro recibido. El siguiente prototipo es la base para realizar el ejercicio (se puede extender):

Nota: utilizar la función len.
'''

def get_string(longitud: int, reintentos: int, mensaje: str, mensaje_error: str) -> str | None:
    
    cont = 0
    cadena = input(mensaje)
    
    while cadena.isalpha() == False or len(cadena) != longitud:
        cont += 1
        if cont > reintentos:
            return None
        else:
            cadena = input(mensaje_error)
    
    
print(get_string(5, 3, "Ingrese un texto: ", "ERROR. Ingrese una texto válido: "))


'''
3 - Realizar los siguientes módulos:

Input.py
    get_int()
    get_float()
    get_string()

Validate.py
    validate_number()
    validate_length()

Nota: estas funciones las tendrán que desarrollar en el módulo Validate y utilizar en el módulo Input.py para realizar las validaciones necesarias.

Crear un repositorio en github con su apellido y nombre junto con el texto funciones_input:
Por ejemplo: scarafilo_german_funciones_input
Dicho repositorio deberá ser privado. Agregar a sus profesores como colaboradores.
'''