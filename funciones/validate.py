'''
Validate.py
    validate_number()
    validate_length()
'''
def validate_number(numero: int | float, mensaje_error: str) -> int:
    '''
    La función valida si el dato ingresado es un número entero o decimal (float). En caso negativo, devuelve un mensaje de error.
    Args:
        mensaje_error: str
    Returns: 
        numero: int | float
    '''
    while True:
        if "." in numero:
            print("El número es decimal")
        else:
            print("El número es entero")

def validate_length(cadena: str, mensaje_error: str, long: int) -> str|int:
    
    while cadena.isalpha() == False or len(cadena) != long:
        cadena = input(mensaje_error)
    
    print("La cadena ingresada coincide con la longitud establecida")