# -*- coding: utf-8 -*-
#Calculo de calorias
#Menus
#Alimentos convenientes para cada plato
print("\n")
print("\n BIENVENIDO AL CALCULO DE LA COMIDA SALUDABLE")
print("\n ")
print("Como sabras la cantidad de \"Calorias\" depende del tipo de actividad que realices aqui te dejo una lista con las proporciones y actividades")
print("\n")
print("Trabajo Muy Liviano 2500cal ") 
print(" Cuando no hay Trabajo Muscular ( Personas que trabajan bajo Techo y Ambientes Templados )")
print("\n")
print("Trabajo Liviano 2700cal ")
print(" Poco Trabajo Muscular ( Sentados y en Ambientes cerrados )")
print("\n")
print("Trabajo Mediano 3000cal ")
print(" Intervalos de Trabajo Muscular ( Momentos parados de momentos de pie )")
print("\n")
print("Trabajo Intenso 4000cal ")
print(" Mayor ezfuerzo Muscular ( Aire libre y lugares Cerrados- generalmente niños de 10 a 15 años )")
print("\n")
print("Trabajo Muy Intenso 4500cal ")
print(" Deportistas ( Aire libre y Ambientes muy calidos )")
print("\n")
#Calculos
print("\n")
print("Para Calclar el IMC - Indice de Masa Muscular coloque   1 ")
print("\n")
print("Para calculos de calorias Presione   2 ")
print("\n")
print("Para salir Presone cualquier tecla")
print("\n")
print("")
#variables
lipidos = 0
glucidos = 0
proteinas = 0
test = int(input(" Ingrese:   "))
x = 0
#funciones
def desicion(a):
    if a == 2:
        global lipidos, glucidos, proteinas   
        calorias = int(input("\n Ingrese la cantidad de Calorias: "))
        lipidos = calorias * 32 / 100
        glucidos = calorias * 55 / 100
        proteinas = calorias * 13 / 100
        print("\n")
        print("  Neccesitaras estas cantidades de calorias en un plato")
        print("\n")
        print("    Hidratos de Carbono  " + str(glucidos) + "cal")
        print("\n")
        print("    Lipidos  " + str(lipidos) + " cal")
        print("\n")
        print("    Proteinas  " + str(proteinas) + " cal")

    elif a == 1:
        imc = float(input("\n Ingrese su peso:  "))
        altura = float(input("\n Ingrese su altura:  "))
        calculo_imc = imc / altura
        print("\n Su IMC es de:  "+ str(calculo_imc))
    else: 
        print("\n")
        print("\nAdios..")
        print("\n")
        exit()
desicion(test)
#COLOCAR UN OS.SYS() PARA LIMPIAR LA TERMINAL Y NO CONFUNDIR AL USUARIO
Z = input(" \n    PRESIONE ENTER PARA CONTINUAR  ")
#funcion proteica
def proteica():
    global proteinas, x
    dic_1 = {"carne magra": 20, "huevo": 10, "leche": 13}
    print(" \nLa lista corresponde a CALORIAS X cada 100 Grs") 
    print("\n Para agregar 200 Grs debera volver a colocar el nombre luego de sumar el primer dato. ")
    print("UNICAMENTE COLOQUE EL NOMBRE")
    print("\n Puede ver la suma acumulada por encima de la lista ")    
    if x <= proteinas :
        print("\n") 
        print("         "+ str (dic_1))
        b = input(" \nAgrege una proteina de la lista:  ")
#xxx
        x += dic_1[b]
        print("\n SU PLATO VA SUMANDO:   " + str(x) + " CAL" ) 
        z = input("  \n PRESIONE ENTER PARA CONTINUAR ")
        return proteica()
    else: 
        print("\n  Por favor ingrese unicamente el NOMBRE contenido en la lista")
        return proteica()
    print("\nLa suma final es de:  " + str(x))

proteica()
