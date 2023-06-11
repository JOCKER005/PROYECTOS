# -*- coding: utf-8 -*-
#PROYECTO DE COSTEO DE PASTELERIA EN PYTHON
from typing import OrderedDict
import os
os.system("figlet  BIENVENIDO  AL  PROGRAMA  DEL  COSTEO PASTELERO ")
print("\n")
print("\n")
print("PARA EMPEZAR TE PEDIRE LA CANTIDAD DE KG QUE DEBES COCINAR DE CADA INGREDIENTE")
print("Nota la escencia de vainilla no se costea")
print("\n")
print(" \n AL FINAL DEL PROGRAMA TE DIRE EL VALOR DEL ALIMENTO CON SU RESPECTIVA GANANCIA ")
#variables y diccionarios
kilogramos = 0
def calculo():
    global kilogramos
    nombre_ingrediente = input("\n NOMBRE DEL INGREDIENTE:  ")
    kilogramos = float(input("\n Cuantos Kg desea cocinar:  "))
    precio = float(input("\n ¿Que precio tiene el ingrediente? :  " ))
    nombre_receta = input("\n¿QUE ESTA POR COCINAR ? :  ")    
    precio_sganancia = kilogramos * precio 
    precio_cganancia = precio_sganancia * 25 / 100
    precio_publico = precio_cganancia + precio_sganancia
    
calculo()
def calculo_precioxkg():
    paquete = int(input("  ¿De cuantos gramos biene el Paquete?  : "))
    precioxpaquete = float(input(" ¿Cual es el Valor del Paquete?  :  "))
    precio_100grs = precioxpaquete * 100 / paquete
#tiene que tomar el valoor de precio cada 100grs y almacenarlo en un dic con e nombre del ingrediente de esa forma ya se sabra de cuanto es el preecio cada 100grs de dicho ingrediente 