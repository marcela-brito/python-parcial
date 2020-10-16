import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 3 numeros
2+4+6 = 12
"""

    
   


# start-->
def suma():
    num1 = 2
    num2 = 4
    num3 = 6
    result = num1 + num2 + num3
    return result
    print(result.sum())



"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros impares del 1 al 1000
"""
# result = sumaImpares()
# if result == 250000:
#     print("ejercicio02: pass")
# else:
#     print("ejercicio02: fail")




# start-->
# def sumaImpares(listaNumeros):
#     result = 0
#     for i in listaNumeros
#         result  = result +i
#     return result



"""
***************************************************************
@@ ejercicio 3 @@
encontrar el perimetro, area y el volumen de un esfera
radio = 12 m

perimetro: 2*pi*r
area: 4*pi*r^2
volumen: (4/3)*pi*r^3
"""

# result = definicionEsfera()
# if result == {
#     "perimetro": 75.39822368615503,
#     "area": 1809.5573684677208,
#     "volumen": 7238.229473870882,
# }:
#     print("ejercicio03: pass")
# else:
#     print("ejercicio03: fail")


# start-->
def definicionEsfera():

    result = 0
    return result


def obtenerPerimetro():
    perimetro = 2*math.pi*12
    result = perimetro
    return result


def obtenerArea():
    area = 4*math.pi*12**2
    result = area
    return result


def obtenerVolumen():
    volumen = (4/3)*math.pi*12**3
    result = volumen
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Esfera:
    def definicionEsfera(self):
        return 0


"""
***************************************************************
@@ ejercicio 5 @@
Banco
Cliente
    nombre
    lugar
    numero de cuenta
    transaccion - retiro o abono
    monto
"""


class Banco:
    def procesar(self):
        return 0

    def abonosSanSalvador(self):
        return 0

    def abonosBalYRod(self):
        return 0


class Cliente:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
