'''
Input.py
    get_int()
    get_float()
    get_string()
'''

from validate import *

'''def get_int():
    
    int = input("Ingrese un número entero: ")
    
    validate_int(int, "ERROR. Ingrese un número válido: ")
    
get_int()'''

def get_float():
    
    flt = input("Ingrese un número decimal: ")
    
    validate_number(flt, "ERROR. Ingrese nuevamente un número: ")

print(get_float())
'''def get_string():
    
    cadena = input("Ingrese una cadena de texto: ")
    
    validate_length(cadena, "ERROR. No coincide la longitud o no es una cadena: ", 6)'''