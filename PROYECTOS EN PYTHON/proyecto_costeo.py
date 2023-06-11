# -*- coding: utf-8 -*-
#PROYECTO DE COSTEO DE UN PLATO EN PTHON
from typing import OrderedDict
import os
os.system("figlet  BIENVENIDO  AL  PROGRAMA  DE  COSTEO")
print("\n")
print("\n")
print("PARA EMPEZAR TE PEDIRE LA CANTIDAD DE KG QUE DEBES COCINAR DE CADA INGREDIENTE")
print("Nota ¿sabes que el agua no se costea verdad?")
print("\n")

#variables
bruto = 0
#listas y diccionarios
lista_monoprecios = []
coeficiente_carnes = {"lomo":1.70, "cerdo costilla":1.51, "cerdo magro":1.22, "ganso":1.69, "cordero paleta":1.25, "cordero costilla":1.31, "liebre":1.62, "pato":1.19, "pavo":1.64, "pollo":1.88, "gallina":1.72, "puchero":1.37, "tira de asado":1.26, "nalga":1.19, "lengua":1.30, "abadejo":2.20, "almeja":3.12, "anguila":1.31}
coeficiente_verduras = {"acelga":1.66, "chicori":1.12, "ajo":1.29, "puerro":1.92, "alcaucil":2.08, "arbeja":2.22, "apio":1.58, "batata":1.23, "verejena":1.15, "puerro":1.96, "brocoli":2.0, "cebolla":1.17, "cebolla de verdeo":2.44, "chaucha":1.11, "coliflor":2.22, "col crespa":2.22, "esparrago":3.03, "espinaca":1.30, "lechuga":1.33, "choclo":2.63, "mandioca":1.33, "papa":1.18, "pimiento":1.35, "remolacha":1.33, "tomate":1.05, "zanahoria":1.59, "zapallo":1.45, "zapallito":1.38 }
coeficiente_frutas = {"anana":1.61, "banana":1.54, "cereza":1.09, "ciruela":1.05, "damasco":1.16, "durazno":1.23, "frutilla":1.04, "manzana":1.16}
#intro
print("""
    \nPara Verduras Presione - 1 -
    \nPara Frutas Presionne  - 2 -
    \nPara Carnes Presione   - 3 -
    \n
    \n Para conocer la Lista de Alimentos con sus respectivo Coeficiente de Desperdicio \nPresione el Numero del alimento 2 veces sin espacios.
    \nPara SALIR Presione 0
    """)
#vamos con las funciones


def calculo_costeo(c):
    global bruto
    if c == 1 : 
        print("\nUsted esta en el Costeo de ")
        os.system("figlet VERDURAS")
        dic = coeficiente_verduras
    elif c == 2 :
        print("\nUsted esta en el Costeo de ")
        os.system("figlet FRUTAS")
        dic = coeficiente_frutas
    elif c == 3 : 
        print("\nUsted esta en el Costeo de ")
        os.system("figlet CARNES")
        dic = coeficiente_carnes
    elif c == 11 :
        print("\n" + str(coeficiente_verduras))
        alimento()
    elif c == 22 :
        print("\n" + str(coeficiente_frutas))
        alimento()    
    elif c == 33 :
        print("\n" + str(coeficiente_carnes))
        alimento()
    elif c == 4 :
        print("SELECCIONA DE NUEVO")
        alimento()
    elif c == 0 :
        os.system("figlet VUELVE PRONTO!")
        exit()
        
    else:
        print("INGRESE UNA OPCION VALIDA")
        return alimento()

    
    def clave_1():

        global ingrediente

        ingrediente = input("\nNombre del ingrediente: ")    
        
        metodo_in = ingrediente in dic 
    
        if ingrediente == "11" :
            calculo_costeo(11)
        elif ingrediente == "22":
            calculo_costeo(22)
        elif ingrediente == "33":
            calculo_costeo(33)
        elif ingrediente == "4":
            calculo_costeo(4)
        elif ingrediente == "0":
            calculo_costeo(0)
        
        true_numerico = ingrediente.isdigit()
        if  true_numerico  == True :
            print("EN ESTE CAMPO NO SE PERMITEN NUMEROS, EXCEPTO LOS DE LAS LISTAS")
            print("\nPARA VOLVER AL MENU PRINCIPAL PRESIONA 4")
            print(" \n Para salir 0")
            clave_1()

        if metodo_in == False:
            print("NO PUDE ENCONTRAR TU INGREDIENTE, INTENTA CON OTRO")
            clave_1()
    clave_1()
    
    
    print("\n")
    def true_de_peso():

        try:
            global peso
            peso = float(input("Ingrese los Gramos: "))
        except:
            print("SOLO COLOCA EL NRO EN GRAMOS SIN LA ABREVIACION DE KG O GRS, ETC.")
            true_de_peso()
    
    true_de_peso()

    print("\n")
    bruto = peso * dic.get(ingrediente)
    print("El Peso BRUTO de " + ingrediente + " es: " + str(bruto))
    print("\n")

    precio = int(input("Ingrese el precio por KG: "))

    global lista_monoprecios
    monoprecio = precio * bruto / 1000
    lista_monoprecios.append(monoprecio)   
    print("\n")
    print("El Precio Bruto es de: " + str(monoprecio))
    print("Precio Bruto = costo de prodcucion ")
    print("\n")
    a = int(input("¿Tiene algun otro ingrediente a sumar? 1 si o 2 no: "))
    print("\n")
    if a == 1:
        return alimento()
    else: 
        print("Gracias por utilizarme")

def alimento():
    try:
        b = int(input("\nIngrese el Numero del Alimento:  "))
    except:
        print("EN ESTE CAMPO NO SE PERMITEN LETRAS")
        alimento()
    
    calculo_costeo(b)
alimento()

print("\n")
#
total_suma = sum(lista_monoprecios)
print("\n El Costo del Plato sera de: " + str(total_suma))
print("\n")
print(" ¿Para cuantas raciones es el plato? ")
print("\n")
plato = int(input(":"))
xplato = total_suma / plato
print("\n")
print("Precio por plato sin sumar ganancias: " + str(xplato))
