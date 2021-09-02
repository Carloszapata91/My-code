import os 
from os import system
import sys
import time 

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

#! Reto 1

print(
"""
+===============================================================+
| Bienvenido al sistema de ubicación para zonas públicas WIFI   |
+===============================================================+
""")  #Mensaje de bienvenida
nombre_usuario=51607  #Nombre de usuario predeterminado
contrasena=70615       #Contrasena predeterminada

while True:
    try:
        nombre_usuario_ingresado = int(input("Ingresa el nombre de usuario: "))  #El usuario ingresa el nombre de usuario y lo convierto a entero
        break  # Si no da error, corto el while con break
    except ValueError:
        print("Error"), sys.exit()


if  nombre_usuario_ingresado==nombre_usuario:    #Verificacion de nombre de usuario
    contrasena_ingresada= input("Ingresa tu contraseña: ")  #El usuario ingresa su contraseña

    while True:
        try:
            contrasena_ingresada1 = int(contrasena_ingresada)  #Convierto a entero a la contrasena
            break  # Si no da error, corto el while con break
        except ValueError:
            print("Error"), sys.exit()

    if contrasena_ingresada1== contrasena:       #Verificacion de contraseña
      print("Usuario y contraseña correctos")   #Mensaje de usuario y contraseña correctos

    else: print('Error'), sys.exit()     #Mensaje de error si  la contraseña es incorrecta

else: print('Error'), sys.exit() #exit()    #Mensaje de error si el nombre de usuario es incorrecto


#Captcha
variable=((5*1)+(1+1))-7-6+6  #Calculo del segundo termino de la suma del captcha
ultimos_cod_grupo=607
resultado_captcha=ultimos_cod_grupo+variable    #Resultado de la suma del captcha
print("Ingresa el resultado de la suma que aparece a continuacion:")  #El usuario ingresa la suma del captcha
print(ultimos_cod_grupo," + ", variable, "=" , end=" ")
variable2=input( )


while True:
    try:
        variable3 = int(variable2)  #Convierto a entero el valor introducido
        break  # Si no da error, corto el while con break
    except ValueError:
        print("Error"), sys.exit()

import time

if variable3==resultado_captcha:   #Verificacion de que el resultado ingresado es el correcto
   print('Sesión iniciada'), time.sleep(3), os.system('cls')

else: print('Error'), sys.exit()

def coordenadas():
    
    Matriz2=[]
                #Menu ingreso de coordenadas
    if Matriz2==[]:
        print('***Ingresa las coordenadas de tus 3 lugares favoritos***')
        Matriz1 = []
        filas = int (3)
        columnas = int (2)
        print('Ingresa primero la LATITUD y luego la LONGITUD de cada coordenada')
        for j in range (filas):
            Matriz1.append([])
            for i in range(columnas):
                valor0=(input('Coordenada {}: '.format(j+1, i+1)))      
                if valor0=='':
                    print('Error'), sys.exit()
                else: valor=float(valor0)
                if i==0 and valor>=-4.227 and valor<=-3.002:
                    Matriz1[j].append(valor)
                elif i==1 and valor>=-70.365 and valor<=-69.714:
                    Matriz1[j].append(valor)
                else: print('Error coordenada'), sys.exit()    
            Matriz2=Matriz1[:]
        os.system('cls')
        #print(Matriz1)
        #break
    else: os.system('cls'), print('Estas son sus coordenadas actuales:')
    #print(Matriz2)
    if Matriz2!=[]:
        for i in range(0,len(Matriz2)):
            fila=Matriz2[i]
            print('coordenada [Latitud,longitud]', i+1, ': ', end=' ')
            print('[', end="'")
            for j in range(0,len(fila)):
                if j==0:
                    print(end="")
                    print(fila[j],end="")
                    print("'",end="")
                    print(",",end=" ")
                else:
                    print("'",end="")
                    print(fila[j], end="'")
            print(']')
        Matrizcomparacion=[]
            
        #Determinacion de las coordenadas mas cercanas al oriente y al occidente
        Matrizcomparacion.append(Matriz2[0][1]) 
        Matrizcomparacion.append(Matriz2[1][1])
        Matrizcomparacion.append(Matriz2[2][1])
        mayor=Matrizcomparacion[0]
        menor=Matrizcomparacion[0]
        for i in Matrizcomparacion:
            if i>mayor:
                mayor=i
            if i<menor:
                menor=i
        EncontrarMayor=mayor
        EncontradoM=False
        for i in range(0,len(Matriz2)):
            EncontradoM = Matrizcomparacion[i] == EncontrarMayor
            if EncontradoM:
                break          
        posicionMayor=i+1
        EncontrarMenor=menor
        Encontradom=False
        for i in range(0,len(Matriz2)):
            Encontradom= Matrizcomparacion[i] == EncontrarMenor
            if  Encontradom:
                break
        posicionMenor=i+1
        print('La coordenada ', posicionMayor, 'es la que está más al oriente')
        print('La coordenada ', posicionMenor, 'es la que está más al occidente')  
        print('Presione 1,2 o 3 para actualizar la respectiva coordenada')
        print('Presione 0 para regresar al menu')
        
        nuevoingreso=input()  #Seleccion para actualizar una de las tres coordenadas
        if nuevoingreso=='0':
            time.sleep(3), os.system('cls')
            #continue
        elif nuevoingreso=='1': #Actualiza coordenada 1
            print('Ingrese la nueva coordenada:')
            nuevaLat=input('Latitud: ')
            if nuevaLat=='':
                print('Error'), sys.exit()
            else: valorNLat=float(nuevaLat)
            if valorNLat>=-4.227 and valorNLat<=-3.002:
                Matriz2[0][0]=valorNLat
                Matriz2=Matriz2[:]
            else: print('Error coordenada'), sys.exit()
            nuevaLon=input('Longitud: ')
            if nuevaLon==' ':
                print('Error'), sys.exit() 
            else: valorNLon=float(nuevaLon)   
            if valorNLon>=-70.365 and valorNLon<=-69.714:
                Matriz2[0][1]=valorNLon
                Matriz2=Matriz2[:]
                os.system('cls')
            else: print('Error coordenada'), sys.exit()    
        elif nuevoingreso=='2': #Actualiza coordenada 2
            print('Ingrese la nueva coordenada:')
            nuevaLat=input('Latitud: ')
            if nuevaLat=='':
                print('Error'), sys.exit()
            else: valorNLat=float(nuevaLat)
            if valorNLat>=-4.227 and valorNLat<=-3.002:
                Matriz2[1][0]=valorNLat
                Matriz2=Matriz2[:]
            else: print('Error coordenada'), sys.exit()
            nuevaLon=input('Longitud: ')
            if nuevaLon==' ':
                print('Error'), sys.exit() 
            else: valorNLon=float(nuevaLon)   
            if valorNLon>=-70.365 and valorNLon<=-69.714:
                Matriz2[1][1]=valorNLon
                Matriz2=Matriz2[:]
                os.system('cls')
            else: print('Error coordenada'), sys.exit() 
        elif nuevoingreso=='3': #Actualiza coordenada 3
            print('Ingrese la nueva coordenada:')
            nuevaLat=input('Latitud: ')
            if nuevaLat=='':
                print('Error'), sys.exit()
            else: valorNLat=float(nuevaLat)
            if valorNLat>=-4.227 and valorNLat<=-3.002:
                Matriz2[2][0]=valorNLat
                Matriz2=Matriz2[:]
            else: print('Error coordenada'), sys.exit()
            nuevaLon=input('Longitud: ')
            if nuevaLon==' ':
                print('Error'), sys.exit() 
            else: valorNLon=float(nuevaLon)   
            if valorNLon>=-70.365 and valorNLon<=-69.714:
                Matriz2[2][1]=valorNLon
                Matriz2=Matriz2[:]
                os.system('cls')
            else: print('Error coordenada'), sys.exit()
        else: print('Error actualización'), sys.exit() 
    return Matriz2
#Funcion para ingreso de coordenadas  (Reto 3)

Matriz2=[]

#! Reto2 y Reto3
contrasena='70615'
#--> Menu de opciones <--
while True:  #While para mostrar el menu original
    print('1. Cambiar contraseña','2. Ingresar coordenadas actuales','3. Ubicar zona wifi más cercana','4. Guardar archivo con ubicación cercana','5. Actualizar registros de zonas wifi desde archivo','6. Elegir opción de menú favorita','7. Cerrar sesión',sep="\n")
    
    variable0=(input('Elija una opción '))  #pido al usuario que elija una opcion de 1 a 7
    #borrarPantalla() #os.system('cls')
    contadorError=0
    if variable0=='7':  #si elige 7, entonces sale del programa
        print('Hasta pronto'), sys.exit() 
    elif variable0=='1':  #?Cambio de contrasena
        print('Usted ha elegido la opción 1. Cambiar contraseña')
        ingreso=input("Ingrese su contrasena actual: ")   
        if ingreso==contrasena:
            nuevacontrasena=input("Ingrese su nueva contrasena: ")
            if nuevacontrasena!=contrasena:
                contrasena=nuevacontrasena
            else: print('Error:La nueva contraseña no puede ser igual a la contraseña actual.'), sys.exit()
            os.system('cls')
        else: print('Error'), sys.exit()
        
    elif variable0=='2':  #Menu ingreso de coordenadas
        if Matriz2==[]:
            print('***Ingresa las coordenadas de tus 3 lugares favoritos***')
            Matriz1 = []
            filas = int (3)
            columnas = int (2)
            print('Ingresa primero la LATITUD y luego la LONGITUD de cada coordenada')
            for j in range (filas):
                Matriz1.append([])
                for i in range(columnas):
                    valor0=(input('Coordenada {}: '.format(j+1, i+1)))      
                    if valor0=='':
                        print('Error'), sys.exit()
                    else: valor=float(valor0)
                    if i==0 and valor>=-4.227 and valor<=-3.002:
                        Matriz1[j].append(valor)
                    elif i==1 and valor>=-70.365 and valor<=-69.714:
                        Matriz1[j].append(valor)
                    else: print('Error coordenada'), sys.exit()    
                Matriz2=Matriz1[:]
            os.system('cls')
            #print(Matriz1)
            continue
        else: os.system('cls'), print('Estas son sus coordenadas actuales:')
        #print(Matriz2)
        for i in range(0,len(Matriz2)):
            fila=Matriz2[i]
            print('coordenada [Latitud,longitud]', i+1, ': ', end=' ')
            print('[', end="'")
            for j in range(0,len(fila)):
                if j==0:
                    print(end='')
                    print(fila[j],end='')
                    print("'",end="")
                    print(',', end=" ")
                else:
                    print("'",end="")
                    print(fila[j], end="'")
            print(']')
        Matrizcomparacion=[]
            
        #Determinacion de las coordenadas mas cercanas al oriente y al occidente
        Matrizcomparacion.append(Matriz2[0][1]) 
        Matrizcomparacion.append(Matriz2[1][1])
        Matrizcomparacion.append(Matriz2[2][1])
        mayor=Matrizcomparacion[0]
        menor=Matrizcomparacion[0]
        for i in Matrizcomparacion:
            if i>mayor:
                mayor=i
            if i<menor:
                menor=i
        EncontrarMayor=mayor
        EncontradoM=False
        for i in range(0,len(Matriz2)):
            EncontradoM = Matrizcomparacion[i] == EncontrarMayor
            if EncontradoM:
                break          
        posicionMayor=i+1
        EncontrarMenor=menor
        Encontradom=False
        for i in range(0,len(Matriz2)):
            Encontradom= Matrizcomparacion[i] == EncontrarMenor
            if  Encontradom:
                break
        posicionMenor=i+1
        print('La coordenada ', posicionMayor, 'es la que está más al oriente')
        print('La coordenada ', posicionMenor, 'es la que está más al occidente')  
        print('Presione 1,2 o 3 para actualizar la respectiva coordenada')
        print('Presione 0 para regresar al menu')
        
        nuevoingreso=input()  #Seleccion para actualizar una de las tres coordenadas
        if nuevoingreso=='0': #Regresa al menu
            time.sleep(3), os.system('cls')
            continue
        elif nuevoingreso=='1': #Actualiza coordenada 1
            print('Ingrese la nueva coordenada:')
            nuevaLat=input('Latitud: ')
            if nuevaLat=='':
                print('Error'), sys.exit()
            else: valorNLat=float(nuevaLat)
            if valorNLat>=-4.227 and valorNLat<=-3.002:
                Matriz2[0][0]=valorNLat
                Matriz2=Matriz2[:]
            else: print('Error coordenada'), sys.exit()
            nuevaLon=input('Longitud: ')
            if nuevaLon==' ':
                print('Error'), sys.exit() 
            else: valorNLon=float(nuevaLon)   
            if valorNLon>=-70.365 and valorNLon<=-69.714:
                Matriz2[0][1]=valorNLon
                Matriz2=Matriz2[:]
                os.system('cls')
            else: print('Error coordenada'), sys.exit()    
        elif nuevoingreso=='2': #Actualiza coordenada 2
            print('Ingrese la nueva coordenada:')
            nuevaLat=input('Latitud: ')
            if nuevaLat=='':
                print('Error'), sys.exit()
            else: valorNLat=float(nuevaLat)
            if valorNLat>=-4.227 and valorNLat<=-3.002:
                Matriz2[1][0]=valorNLat
                Matriz2=Matriz2[:]
            else: print('Error coordenada'), sys.exit()
            nuevaLon=input('Longitud: ')
            if nuevaLon==' ':
                print('Error'), sys.exit() 
            else: valorNLon=float(nuevaLon)   
            if valorNLon>=-70.365 and valorNLon<=-69.714:
                Matriz2[1][1]=valorNLon
                Matriz2=Matriz2[:]
                os.system('cls')
            else: print('Error coordenada'), sys.exit() 
        elif nuevoingreso=='3': #Actualiza coordenada 3
            print('Ingrese la nueva coordenada:')
            nuevaLat=input('Latitud: ')
            if nuevaLat=='':
                print('Error'), sys.exit()
            else: valorNLat=float(nuevaLat)
            if valorNLat>=-4.227 and valorNLat<=-3.002:
                Matriz2[2][0]=valorNLat
                Matriz2=Matriz2[:]
            else: print('Error coordenada'), sys.exit()
            nuevaLon=input('Longitud: ')
            if nuevaLon==' ':
                print('Error'), sys.exit() 
            else: valorNLon=float(nuevaLon)   
            if valorNLon>=-70.365 and valorNLon<=-69.714:
                Matriz2[2][1]=valorNLon
                Matriz2=Matriz2[:]
                os.system('cls')
            else: print('Error coordenada'), sys.exit()
        else: print('Error actualización'), sys.exit() 

        
    elif variable0=='3'  or variable0=='4' or variable0=='5':
        sys.exit()    #Si elige 1, 2, 3, 4 o 5 sale porque no hay mas instrucciones
    elif variable0=='6':
        break
    elif variable0!='6':  #Si el usuario ingresa un valor inesperado, Error y sale del sistema
        while contadorError!=4:   #Si el usuario mete 3 valores incorrectos luego del menu principal, sale error
            contadorError=contadorError+1
            variable1=input()
            if variable1=="6":
                break
            elif variable1=='1' or variable1=='2' or variable1=='3'  or variable1=='4' or variable1=='5':
                quit, sys.exit(), quit     #Si elige 1, 2, 3, 4 o 5 sale porque no hay mas instrucciones
            elif variable1=='7':  #si elige 7, entonces sale del programa
                print('Hasta pronto'), sys.exit(), quit 
            elif contadorError>=3:
                print('Error'), sys.exit()
            else:    
                continue


variable1=6 
#borrarPantalla() #os.system('cls')
while variable1==6:  #El usuario ingresa a la opcion 6 para elegir opcion favorita y tener menu nuevo
    Eleccion=input('Seleccione opción favorita ')
    #borrarPantalla() #os.system('cls')
    if Eleccion=='1' or Eleccion=='2' or Eleccion=='3' or Eleccion=='4' or Eleccion=='5':
        print('Antes de cambiar el menu, es necesario hacer dos comprobaciones de seguridad:')
        adivinanza1='0'
        adivinanza2='7'
        respuesta1=input('Soy el numero que no vale nada:')
        respuesta2=input('Numero de dias que tiene la semana:')
        borrarPantalla() #os.system('cls')
        if respuesta1=='0' and respuesta2=='7':  #Nuevo menu con opcion favorita en posicion 1
            #print('Guay')
            borrarPantalla() #os.system('cls')
            if Eleccion=='1':
                borrarPantalla() #os.system('cls'),
                print('1. Cambiar contraseña','2. Ingresar coordenadas actuales','3. Ubicar zona wifi más cercana','4. Guardar archivo con ubicación cercana','5. Actualizar registros de zonas wifi desde archivo','6. Elegir opción de menú favorita','7. Cerrar sesión',sep="\n")
                nuevaentrada=input('Elija una opción ')
                if nuevaentrada=='1':
                    print('Usted ha elegido la opción 1. Cambiar contraseña')
                    ingreso=input("Ingrese su contrasena actual: ")
                    if ingreso==contrasena:
                        nuevacontrasena=input("Ingrese su nueva contrasena: ")
                        if nuevacontrasena!=contrasena:
                            contrasena=nuevacontrasena
                        else: print('Error:La nueva contraseña no puede ser igual a la contraseña actual.'), sys.exit()
                        os.system('cls')
                        print('1. Cambiar contraseña','2. Ingresar coordenadas actuales','3. Ubicar zona wifi más cercana','4. Guardar archivo con ubicación cercana','5. Actualizar registros de zonas wifi desde archivo','6. Elegir opción de menú favorita','7. Cerrar sesión',sep="\n")
                    else: print('Error'), sys.exit()
                elif nuevaentrada=='2':
                    coordenadas()
                else: continue  
            elif Eleccion=='2':
                 borrarPantalla() #os.system('cls')
                 print('1. Ingresar coordenadas actuales','2. Cambiar contraseña','3. Ubicar zona wifi más cercana','4. Guardar archivo con ubicación cercana','5. Actualizar registros de zonas wifi desde archivo','6. Elegir opción de menú favorita','7. Cerrar sesión',sep="\n")
                 nuevaentrada=input('Elija una opción ')
                 if nuevaentrada=='2':
                    print('Usted ha elegido la opción 2. Cambiar contraseña')
                    ingreso=input("Ingrese su contrasena actual: ")
                    if ingreso==contrasena:
                        nuevacontrasena=input("Ingrese su nueva contrasena: ")
                        if nuevacontrasena!=contrasena:
                            contrasena=nuevacontrasena
                        else: print('Error:La nueva contraseña no puede ser igual a la contraseña actual.'), sys.exit()
                        os.system('cls')
                        print('1. Ingresar coordenadas actuales','2. Cambiar contraseña','3. Ubicar zona wifi más cercana','4. Guardar archivo con ubicación cercana','5. Actualizar registros de zonas wifi desde archivo','6. Elegir opción de menú favorita','7. Cerrar sesión',sep="\n")
                    else: print('Error'), sys.exit()
                 elif nuevaentrada=='1':
                     coordenadas()
                 else: continue
            elif Eleccion=='3':
                 borrarPantalla() #os.system('cls')
                 print('1. Ubicar zona wifi más cercana','2. Cambiar contraseña','3. Ingresar coordenadas actuales','4. Guardar archivo con ubicación cercana','5. Actualizar registros de zonas wifi desde archivo','6. Elegir opción de menú favorita','7. Cerrar sesión', sep="\n")
                 nuevaentrada=input('Elija una opción ')
                 if nuevaentrada=='2':
                    print('Usted ha elegido la opción 2. Cambiar contraseña')
                    ingreso=input("Ingrese su contrasena actual: ")
                    if ingreso==contrasena:
                        nuevacontrasena=input("Ingrese su nueva contrasena: ")
                        if nuevacontrasena!=contrasena:
                            contrasena=nuevacontrasena
                        else: print('Error:La nueva contraseña no puede ser igual a la contraseña actual.'), sys.exit()
                        os.system('cls')
                        print('1. Ubicar zona wifi más cercana','2. Cambiar contraseña','3. Ingresar coordenadas actuales','4. Guardar archivo con ubicación cercana','5. Actualizar registros de zonas wifi desde archivo','6. Elegir opción de menú favorita','7. Cerrar sesión', sep="\n")
                    else: print('Error'), sys.exit()
                 elif nuevaentrada=='3':
                     coordenadas()
                 else: continue
            elif Eleccion=='4':
                 borrarPantalla() #os.system('cls')
                 print('1. Guardar archivo con ubicación cercana','2. Cambiar contraseña','3. Ingresar coordenadas actuales','4. Ubicar zona wifi más cercana','5. Actualizar registros de zonas wifi desde archivo','6. Elegir opción de menú favorita','7. Cerrar sesión',sep="\n")
                 nuevaentrada=input('Elija una opción ')
                 if nuevaentrada=='2':
                    print('Usted ha elegido la opción 2. Cambiar contraseña')
                    ingreso=input("Ingrese su contrasena actual: ")
                    if ingreso==contrasena:
                        nuevacontrasena=input("Ingrese su nueva contrasena: ")
                        if nuevacontrasena!=contrasena:
                            contrasena=nuevacontrasena
                        else: print('Error:La nueva contraseña no puede ser igual a la contraseña actual.'), sys.exit()
                        os.system('cls')
                        print('1. Guardar archivo con ubicación cercana','2. Cambiar contraseña','3. Ingresar coordenadas actuales','4. Ubicar zona wifi más cercana','5. Actualizar registros de zonas wifi desde archivo','6. Elegir opción de menú favorita','7. Cerrar sesión',sep="\n")
                    else: print('Error'), sys.exit()
                 elif nuevaentrada=='3':
                     coordenadas()
                 else: continue
            elif Eleccion=='5':
                 borrarPantalla() #os.system('cls'),
                 print('1. Actualizar registros de zonas wifi desde archivo','2. Cambiar contraseña','3. Ingresar coordenadas actuales','4. Ubicar zona wifi más cercana','5. Guardar archivo con ubicación cercana','6. Elegir opción de menú favorita','7. Cerrar sesión',sep="\n")   
                 nuevaentrada=input('Elija una opción ')
                 if nuevaentrada=='2':
                    print('Usted ha elegido la opción 2. Cambiar contraseña')
                    ingreso=input("Ingrese su contrasena actual: ")
                    if ingreso==contrasena:
                        nuevacontrasena=input("Ingrese su nueva contrasena: ")
                        if nuevacontrasena!=contrasena:
                            contrasena=nuevacontrasena
                        else: print('Error:La nueva contraseña no puede ser igual a la contraseña actual.'), sys.exit()
                        os.system('cls')
                        print('1. Actualizar registros de zonas wifi desde archivo','2. Cambiar contraseña','3. Ingresar coordenadas actuales','4. Ubicar zona wifi más cercana','5. Guardar archivo con ubicación cercana','6. Elegir opción de menú favorita','7. Cerrar sesión',sep="\n")   
                    else: print('Error'), sys.exit()
                 elif nuevaentrada=='3':
                     coordenadas()
                 else: continue
            nuevaentrada=input('Elija una opción ')  #!Poner 'Elija una opción '?
            #print('Usted ha elegido la opción', nuevaentrada)
            if nuevaentrada=='7':
                print('Usted ha elegido la opción ', nuevaentrada)
                print('Hasta pronto'), sys.exit()
            elif nuevaentrada=='3'  or nuevaentrada=='4' or nuevaentrada=='5':
                print('Usted ha elegido la opción', nuevaentrada), sys.exit() 
            elif nuevaentrada!='6':
                print('Error'), time.sleep(1)
                while True:
                    os.system('cls')
                    if Eleccion=='1': print('1. Cambiar contraseña','2. Ingresar coordenadas actuales','3. Ubicar zona wifi más cercana','4. Guardar archivo con ubicación cercana','5. Actualizar registros de zonas wifi desde archivo','6. Elegir opción de menú favorita','7. Cerrar sesión',sep="\n") 
                    if Eleccion=='2': print('1. Ingresar coordenadas actuales','2. Cambiar contraseña','3. Ubicar zona wifi más cercana','4. Guardar archivo con ubicación cercana','5. Actualizar registros de zonas wifi desde archivo','6. Elegir opción de menú favorita','7. Cerrar sesión',sep="\n")
                    if Eleccion=='3': print('1. Ubicar zona wifi más cercana','2. Cambiar contraseña','3. Ingresar coordenadas actuales','4. Guardar archivo con ubicación cercana','5. Actualizar registros de zonas wifi desde archivo','6. Elegir opción de menú favorita','7. Cerrar sesión', sep="\n")
                    if Eleccion=='4': print('1. Guardar archivo con ubicación cercana','2. Cambiar contraseña','3. Ingresar coordenadas actuales','4. Ubicar zona wifi más cercana','5. Actualizar registros de zonas wifi desde archivo','6. Elegir opción de menú favorita','7. Cerrar sesión',sep="\n")
                    if Eleccion=='5': print('1. Actualizar registros de zonas wifi desde archivo','2. Cambiar contraseña','3. Ingresar coordenadas actuales','4. Ubicar zona wifi más cercana','5. Guardar archivo con ubicación cercana','6. Elegir opción de menú favorita','7. Cerrar sesión',sep="\n")
                    otra=input('Elija una opción ') #os.system('cls')
                    if Eleccion=='1' and otra=='1' or Eleccion=='2' and otra=='2' or Eleccion=='3' and otra=='2' or Eleccion=='4' and otra=='2'or Eleccion=='5' and otra=='2':
                        print('Usted ha elegido la opción - Cambiar contraseña')
                        ingreso=input("Ingrese su contrasena actual: ")
                        if ingreso==contrasena:
                            nuevacontrasena=input("Ingrese su nueva contrasena: ")
                            if nuevacontrasena!=contrasena:
                                contrasena=nuevacontrasena
                            else: print('Error:La nueva contraseña no puede ser igual a la contraseña actual.'), sys.exit()
                            os.system('cls')
                        else: print('Error'), sys.exit()
                    if Eleccion=='1' and otra=='2' or Eleccion=='2' and otra=='1' or Eleccion=='3' and otra=='3' or Eleccion=='4' and otra=='3'or Eleccion=='5' and otra=='3' :
                        print('Usted ha elegido la opción - Ingresar coordenadas actuales')
                        coordenadas()
                    if otra=='3' or otra=='4' or otra=='5':
                       print('Usted ha elegido la opción', otra), sys.exit()
                    elif otra=='7':
                        print('Hasta pronto'), sys.exit() #! print('Sesión cerrada')?
                    elif otra=='6': 
                        borrarPantalla(), os.system('cls')
                        break      
                    else: print('Error'), time.sleep(1), borrarPantalla() 
                    continue    
        else: print('Respuesta equivocada'), time.sleep(2)
        borrarPantalla()
        print('1. Cambiar contraseña','2. Ingresar coordenadas actuales','3. Ubicar zona wifi más cercana','4. Guardar archivo con ubicación cercana','5. Actualizar registros de zonas wifi desde archivo','6. Elegir opción de menú favorita','7. Cerrar sesión',sep="\n")
        continue       
    else: print('Error'), sys.exit()
