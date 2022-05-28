#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      client.py
#
import time
from socket import socket
import os
from turtle import clear
def menudatos():
    #os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    print("Selecciona una opción:")
    print("\n 1 - Crear un dato")
    print("\n 2 - Leer datos")
    print("\n 3 - Actualizar dato")
    print("\n 4 - Borrar dato")
    print("\n 9 - salir")

def menuarchivos():
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    print("\n Seleciona un archivo:")
    print("\n 1-Ford")
    print("\n 2-Nissan")
    print("\n 3-Honda")
    print("\n 4-Cualquier tecla para salir")

# Compatibilidad con Python 3
try:
    raw_input
except NameError:
    raw_input = input


def main():
    s = socket()
    s.connect(("localhost", 6030))
    a = 2  
    while a ==2:

        while True:
            # solicituamos una opción al usuario
            menuarchivos()
            opcionMenu = input("inserta un numero valor >> ")
            s.send(bytes(opcionMenu, "utf-8"))
            if opcionMenu == "1":
                print("Abriendo Archivo 1(Ford):")
                menudatos()
                output_data = raw_input("> ") #enviar datos aun no se usa
                s.send(bytes(output_data, "utf-8"))
                input_data = s.recv(1024)

                if input_data:
                # En Python 3 recv() retorna los datos leídos
                # como un vector de bytes. Convertir a una cadena
                # en caso de ser necesario.
                    print(input_data.decode("utf-8") if
                       isinstance(input_data, bytes) else input_data)
                    time.sleep(5)

            elif opcionMenu == "2":
                print("Abriendo archivo 2 (Nissan)")
                menudatos()
                output_data = raw_input("> ") #enviar datos aun no se usa
                s.send(bytes(output_data, "utf-8"))
                input_data = s.recv(1024)

                if input_data:
                # En Python 3 recv() retorna los datos leídos
                # como un vector de bytes. Convertir a una cadena
                # en caso de ser necesario.
                    print(input_data.decode("utf-8") if
                       isinstance(input_data, bytes) else input_data)
                    time.sleep(5)
            elif opcionMenu == "3":
                print("Abriendo archivo (Honda)")
                menudatos()
                output_data = raw_input("> ") #enviar datos aun no se usa
                s.send(bytes(output_data, "utf-8"))
                input_data = s.recv(1024)

                if input_data:
                # En Python 3 recv() retorna los datos leídos
                # como un vector de bytes. Convertir a una cadena
                # en caso de ser necesario.
                    print(input_data.decode("utf-8") if
                       isinstance(input_data, bytes) else input_data)
                    time.sleep(5)


            else:
                print("Opción Invalida... Saliendo.")
                os.system('clear')
                a = 3
                break

#        if output_data:
            # Enviar entrada. Comptabilidad con Python 3.
#            try:
 #               s.send(output_data)
  #          except TypeError:
   #             s.send(bytes(output_data, "utf-8"))
            
            # Recibir respuesta.
    #        input_data = s.recv(1024)
     #       if input_data:
                # En Python 3 recv() retorna los datos leídos
                # como un vector de bytes. Convertir a una cadena
                # en caso de ser necesario.
      #          print(input_data.decode("utf-8") if
       #               isinstance(input_data, bytes) else input_data)


if __name__ == "__main__":
    main()