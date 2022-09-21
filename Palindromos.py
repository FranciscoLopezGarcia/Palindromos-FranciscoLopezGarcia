import unittest


def Palindromo(palabras):
    palabras = palabras.lower() and palabras.replace(" ","") and palabras.replace('é','e') and palabras.replace('í','i') and palabras.replace('ó','o') and palabras.replace('ú','u')

    if palabras == palabras[::-1]:
        return True
    else:
       return False



if __name__ == '__main__':
    unittest.main()