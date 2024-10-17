import string

caracteres_ascii = string.ascii_letters
print(caracteres_ascii)

def verificar(cadena):
    #caracter de la cadena
    for caracter in cadena:
        #Devolvemos False
        if caracter not in caracteres_ascii:
            return False
    #Devolvemos True
    return True

cadena1 = "Esto es un a cadena$"
print(verificar(cadena1))  #False

cadena2 = "SoloLetrasASCII"
print(verificar(cadena2))  #True
