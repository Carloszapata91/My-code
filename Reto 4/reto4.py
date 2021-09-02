import os 
from os import system
import sys
import time 
import math

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

Matriz2=[]

def coordenadas():

    global Matriz2
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

#Funcion para calcular la distancia entre coordenada habitual y las zonas wifi #! Reto 4
def distancia(Lat1,Lon1): 
    global salidaF
    Matrizdist=[]
    #Zonas Wifi predeterminadas a la zona 0 (Leticia, Amazonas)
    MatrizZWifi=[[-3.777,-70.302,91],[-4.134,-69.983,233],[-4.006,-70.132,149],[-3.846,-70.222,211]]
    #Lat2=MatrizZWifi[0][0]
    #Lon2=MatrizZWifi[0][1]
    #difLat=Lat2-Lat1
    #difLon=Lon2-Lon1
    #raiz=((math.sin(difLat/2))**2)+(math.cos(Lat1))*(math.cos(Lat2))*((math.sin(difLon/2))**2)
    #distancia=2*6372.795477598*math.asin(math.sqrt(raiz)) 

    for i in range(4):
        Matrizdist.append([])
        for j in range(1):
            Lat2=MatrizZWifi[i][j]
            Lon2=MatrizZWifi[i][j+1]
            difLat=Lat2-Lat1
            difLon=Lon2-Lon1
            raiz=((math.sin(difLat/2))**2)+(math.cos(Lat1))*(math.cos(Lat2))*((math.sin(difLon/2))**2)
            distancia=2*6372.795477598*math.asin(math.sqrt(raiz))
            Matrizdist[i].append(round(distancia))
    salidaF=Matrizdist[:]
 
    return salidaF   #Devuelve una lista con las distancias de un punto a las 4 zonas Wifi

#Funcion para indicar el recorrido desde lugar fav. a la zona wifi elegida  #! Reto 4
def instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav):
    if float(lon_pos_fav)<float(lon_pos_wifi):
        a='Para llegar a la zona wifi dirigirse primero al oriente'
        print(a,end="")
    else: 
        b='Para llegar a la zona wifi dirigirse primero al occidente'
        print(b, end="")
    if float(lat_pos_fav)>float(lat_pos_wifi):
        c=' y luego hacia el sur'
        print(c)
    else: 
        d=' y luego hacia el norte'
        print(d)
    return


#! Reto 2  y  Reto 3
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
                    if i==0 and valor>=-4.227 and valor<=-3.002: #Rango Latitud
                        Matriz1[j].append(valor)
                    elif i==1 and valor>=-70.365 and valor<=-69.714: #Rango Longitud
                        Matriz1[j].append(valor)
                    else: print('Error coordenada'), sys.exit()    
                Matriz2=Matriz1[:]
            os.system('cls')
            #print(Matriz2), time.sleep(5)
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

    #! Reto 4 --- La opcion 3 del menu principal
    elif variable0=='3':
        os.system('cls')
        #print('Usted ha elegido la opción 3. Ubicar zona wifi más cercana')
        if Matriz2==[]:
            print('Error sin registro de coordenadas'), sys.exit()
        else:
            print('Estas son sus ubicaciones favoritas: Trabajo, Casa y Parque') 
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
            op_coord=input('Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: ')
            if op_coord!='1' and op_coord!='2' and op_coord!='3':
                print('Error ubicación'), sys.exit()
            elif op_coord=='1': 
                #os.system('cls')
                print('Elegiste la ubicación 1') 
                Lat1=Matriz2[0][0] 
                Lon1=Matriz2[0][1] 
                #print(distancia(Lat1,Lon1))
                #time.sleep(5)
                listadesor=distancia(Lat1,Lon1)
                #listadesor=listadesor[:]
                listaok=salidaF.sort()  #Lista con las distancias ordenadas de min a mayor
                #print(salidaF, 'coco')
                #listaok=listaok[:]
                MatrizZWifi=[[-3.777,-70.302,91],[-4.134,-69.983,233],[-4.006,-70.132,149],[-3.846,-70.222,211]]
                Hallar1=salidaF[0][0]
                Hallado1=False
                for i in range(3):  #Busco la posicion de las 2 primeras zonas wifi en la lista de las distancias
                    Hallado1=listadesor[i][0]==Hallar1
                    if Hallado1:
                        break
                if Hallado1: 
                    Posmascerca1=i
                    #print("Elemento encontrado en el índice", i)                 
                    #print('Zonas wifi cercanas con menos usuarios: prueba')
                    #print('La zona wifi 1: ubicada en', '[',MatrizZWifi[i][0],',',MatrizZWifi[i][1],'] a', listadesor[i] ,'metros , tiene en promedio', MatrizZWifi[i][2] ,'usuarios')  
                    N_usuar1=listadesor[i]        
                Hallar2=salidaF[1][0]
                Hallado2=False
                for i in range(3):  #Busco la posicion de las 2 primeras zonas wifi en la lista de las distancias
                    Hallado2=listadesor[i][0]==Hallar2
                    if Hallado2:
                        break
                if Hallado2: 
                    Posmascerca2=i
                    #print("Elemento encontrado en el índice", i)                 
                    #print('La zona wifi 2: ubicada en','[', MatrizZWifi[i][0],',',MatrizZWifi[i][1],'] a', listadesor[i] ,'metros , tiene en promedio', MatrizZWifi[i][2] ,'usuarios')  
                    #print('Fin prueba')
                    N_usuar2=listadesor[i]
                    #time.sleep(5)
                if N_usuar1>N_usuar2:
                    Dist_x=listadesor[Posmascerca2]
                    Dist_xx=listadesor[Posmascerca1]
                    Dist_x1=Dist_x[:]
                    Dist_xx1=Dist_xx[:]
                    print('La zona wifi 1: ubicada en','[', MatrizZWifi[Posmascerca2][0],',',MatrizZWifi[Posmascerca2][1],'] a', Dist_x1[0] ,'metros , tiene en promedio', MatrizZWifi[Posmascerca2][2] ,'usuarios')
                    print('La zona wifi 2: ubicada en', '[',MatrizZWifi[Posmascerca1][0],',',MatrizZWifi[Posmascerca1][1],'] a', Dist_xx1[0] ,'metros , tiene en promedio', MatrizZWifi[Posmascerca1][2] ,'usuarios')
                    ent_lleg=input('Elija 1 o 2 para recibir indicaciones de llegada ')
                    
                    if ent_lleg=='1':  
                        print('Elegiste la zona wifi 1')
                        time.sleep(2)
                        lat_pos_wifi=MatrizZWifi[Posmascerca2][0]
                        lon_pos_wifi=MatrizZWifi[Posmascerca2][1]
                        lat_pos_fav=Matriz2[0][0]
                        lon_pos_fav=Matriz2[0][1]
                        #instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)  #Invocacion funcion
                        print('Estas son las instrucciones de llegada: ',end="")
                        instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)
                        cosa=listadesor[Posmascerca2]
                        cosa1=cosa[:]
                        print('Llegar a pie toma: ', round(cosa1[0]/28.98,2), 'minutos')
                        print('Lllegar en auto toma: ',round(cosa1[0]/1249.8,2), 'minutos')
                        opc_salir=input('Presione 0 para salir')
                        if opc_salir=='0':
                            os.system('cls')
                            continue
                        else: sys.exit()
                    elif ent_lleg=='2':
                        print('Elegiste la zona wifi 2')
                        time.sleep(2)
                        lat_pos_wifi=MatrizZWifi[Posmascerca1][0]
                        lon_pos_wifi=MatrizZWifi[Posmascerca1][1]
                        lat_pos_fav=Matriz2[0][0]
                        lon_pos_fav=Matriz2[0][1]
                        #instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)  #Invocacion funcion
                        print('Estas son las instrucciones de llegada: ',end="") 
                        instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)
                        cosa=listadesor[Posmascerca1]
                        cosa1=cosa[:]
                        print('Llegar a pie toma: ', round(cosa1[0]/28.98,2), 'minutos')
                        print('Lllegar en auto toma: ',round(cosa1[0]/1249.8,2), 'minutos')
                        opc_salir=input('Presione 0 para salir')
                        if opc_salir=='0':
                            os.system('cls')
                            continue
                        else: sys.exit()
                else:
                    Dist_x=listadesor[Posmascerca2]
                    Dist_xx=listadesor[Posmascerca1]
                    Dist_x1=Dist_x[:]
                    Dist_xx1=Dist_xx[:]
                    print('La zona wifi 1: ubicada en', '[',MatrizZWifi[Posmascerca1][0],',',MatrizZWifi[Posmascerca1][1],'] a', Dist_xx1[0] ,'metros , tiene en promedio', MatrizZWifi[Posmascerca1][2] ,'usuarios')
                    print('La zona wifi 2: ubicada en','[', MatrizZWifi[Posmascerca2][0],',',MatrizZWifi[Posmascerca2][1],'] a', Dist_x1[0] ,'metros , tiene en promedio', MatrizZWifi[Posmascerca2][2] ,'usuarios')
                    ent_lleg=input('Elija 1 o 2 para recibir indicaciones de llegada ') 
                
                    if ent_lleg=='1':  
                        print('Elegiste la zona wifi 1')
                        time.sleep(2)
                        lat_pos_wifi=MatrizZWifi[Posmascerca1][0]
                        lon_pos_wifi=MatrizZWifi[Posmascerca1][1]
                        lat_pos_fav=Matriz2[0][0]
                        lon_pos_fav=Matriz2[0][1]
                        #instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)  #Invocacion funcion
                        print('Estas son las instrucciones de llegada: ',end="") 
                        instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)
                        cosa=listadesor[Posmascerca1]
                        cosa1=cosa[:]
                        #print(cosa1)
                        #print(cosa1[0])
                        print('Llegar a pie toma: ', round(cosa1[0]/28.98,2), 'minutos')
                        print('Llegar en auto toma: ',round(cosa1[0]/1249.8,2), 'minutos')
                        opc_salir=input('Presione 0 para salir')
                        if opc_salir=='0':
                            os.system('cls')
                            continue
                        else: sys.exit()
                    elif ent_lleg=='2':
                        print('Elegiste la zona wifi 2')
                        time.sleep(2)
                        lat_pos_wifi=MatrizZWifi[Posmascerca2][0]
                        lon_pos_wifi=MatrizZWifi[Posmascerca2][1]
                        lat_pos_fav=Matriz2[0][0]
                        lon_pos_fav=Matriz2[0][1]
                        #instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)  #Invocacion funcion
                        print('Estas son las instrucciones de llegada: ',end="") 
                        instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)
                        cosa=listadesor[Posmascerca2]
                        cosa1=cosa[:]
                        print('Llegar a pie toma: ', round(cosa1[0]/28.98,2), 'minutos')
                        print('Llegar en auto toma: ',round(cosa1[0]/1249.8,2), 'minutos' )
                        opc_salir=input('Presione 0 para salir')
                        if opc_salir=='0':
                            os.system('cls')
                            continue
                        else: sys.exit()
                    else: 
                        print('Error zona wifi')
                        sys.exit()

            elif op_coord=='2': 
                print('Elegiste la ubicación 2')
                Lat1=Matriz2[1][0]
                Lon1=Matriz2[1][1]
                #print(distancia(Lat1,Lon1))
                #time.sleep(5)
                listadesor=distancia(Lat1,Lon1)
                #listadesor=listadesor[:]
                listaok=salidaF.sort()  #Lista con las distancias ordenadas de min a mayor
                #print(salidaF, 'coco')
                #listaok=listaok[:]
                MatrizZWifi=[[-3.777,-70.302,91],[-4.134,-69.983,233],[-4.006,-70.132,149],[-3.846,-70.222,211]]
                Hallar1=salidaF[0][0]
                Hallado1=False
                for i in range(3):  #Busco la posicion de las 2 primeras zonas wifi en la lista de las distancias
                    Hallado1=listadesor[i][0]==Hallar1
                    if Hallado1:
                        break
                if Hallado1: 
                    Posmascerca1=i
                    #print("Elemento encontrado en el índice", i)                 
                    #print('Zonas wifi cercanas con menos usuarios: prueba')
                    #print('La zona wifi 1: ubicada en', '[',MatrizZWifi[i][0],',',MatrizZWifi[i][1],'] a', listadesor[i] ,'metros , tiene en promedio', MatrizZWifi[i][2] ,'usuarios')  
                    N_usuar1=listadesor[i]        
                Hallar2=salidaF[1][0]
                Hallado2=False
                for i in range(3):  #Busco la posicion de las 2 primeras zonas wifi en la lista de las distancias
                    Hallado2=listadesor[i][0]==Hallar2
                    if Hallado2:
                        break
                if Hallado2: 
                    Posmascerca2=i
                    #print("Elemento encontrado en el índice", i)                 
                    #print('La zona wifi 2: ubicada en','[', MatrizZWifi[i][0],',',MatrizZWifi[i][1],'] a', listadesor[i] ,'metros , tiene en promedio', MatrizZWifi[i][2] ,'usuarios')  
                    #print('Fin prueba')
                    N_usuar2=listadesor[i]
                    time.sleep(1)
                if N_usuar1>N_usuar2:
                    Dist_x=listadesor[Posmascerca2]
                    Dist_xx=listadesor[Posmascerca1]
                    Dist_x1=Dist_x[:]
                    Dist_xx1=Dist_xx[:]
                    print('La zona wifi 1: ubicada en','[', MatrizZWifi[Posmascerca2][0],',',MatrizZWifi[Posmascerca2][1],'] a', Dist_x1[0] ,'metros , tiene en promedio', MatrizZWifi[Posmascerca2][2] ,'usuarios')
                    print('La zona wifi 2: ubicada en', '[',MatrizZWifi[Posmascerca1][0],',',MatrizZWifi[Posmascerca1][1],'] a', Dist_xx1[0] ,'metros , tiene en promedio', MatrizZWifi[Posmascerca1][2] ,'usuarios')
                    ent_lleg=input('Elija 1 o 2 para recibir indicaciones de llegada ')
                    
                    if ent_lleg=='1':  
                        print('Elegiste la zona wifi 1')
                        time.sleep(2)
                        lat_pos_wifi=MatrizZWifi[Posmascerca2][0]
                        lon_pos_wifi=MatrizZWifi[Posmascerca2][1]
                        lat_pos_fav=Matriz2[1][0]
                        lon_pos_fav=Matriz2[1][1]
                        #instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)  #Invocacion funcion
                        print('Estas son las instrucciones de llegada: ',end="")
                        instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)
                        cosa=listadesor[Posmascerca2]
                        cosa1=cosa[:]
                        print('Llegar a pie toma: ', round(cosa1[0]/28.98,2), 'minutos')
                        print('Lllegar en auto toma: ',round(cosa1[0]/1249.8,2), 'minutos')
                        opc_salir=input('Presione 0 para salir')
                        if opc_salir=='0':
                            os.system('cls')
                            continue
                        else: sys.exit()
                    elif ent_lleg=='2':
                        print('Elegiste la zona wifi 2')
                        time.sleep(2)
                        lat_pos_wifi=MatrizZWifi[Posmascerca1][0]
                        lon_pos_wifi=MatrizZWifi[Posmascerca1][1]
                        lat_pos_fav=Matriz2[1][0]
                        lon_pos_fav=Matriz2[1][1]
                        #instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)  #Invocacion funcion
                        print('Estas son las instrucciones de llegada: ',end="")
                        instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)
                        cosa=listadesor[Posmascerca1]
                        cosa1=cosa[:]
                        print('Llegar a pie toma: ', round(cosa1[0]/28.98,2), 'minutos')
                        print('Lllegar en auto toma: ',round(cosa1[0]/1249.8,2), 'minutos')
                        opc_salir=input('Presione 0 para salir')
                        if opc_salir=='0':
                            os.system('cls')
                            continue
                        else: sys.exit()
                else:
                    Dist_x=listadesor[Posmascerca2]
                    Dist_xx=listadesor[Posmascerca1]
                    Dist_x1=Dist_x[:]
                    Dist_xx1=Dist_xx[:]
                    print('La zona wifi 1: ubicada en', '[',MatrizZWifi[Posmascerca1][0],',',MatrizZWifi[Posmascerca1][1],'] a', Dist_xx1[0] ,'metros , tiene en promedio', MatrizZWifi[Posmascerca1][2] ,'usuarios')
                    print('La zona wifi 2: ubicada en','[', MatrizZWifi[Posmascerca2][0],',',MatrizZWifi[Posmascerca2][1],'] a', Dist_x1[0] ,'metros , tiene en promedio', MatrizZWifi[Posmascerca2][2] ,'usuarios')
                    ent_lleg=input('Elija 1 o 2 para recibir indicaciones de llegada ') 
                
                    if ent_lleg=='1':  
                        print('Elegiste la zona wifi 1')
                        time.sleep(2)
                        lat_pos_wifi=MatrizZWifi[Posmascerca1][0]
                        lon_pos_wifi=MatrizZWifi[Posmascerca1][1]
                        lat_pos_fav=Matriz2[1][0]
                        lon_pos_fav=Matriz2[1][1]
                        #instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)  #Invocacion funcion
                        print('Estas son las instrucciones de llegada: ',end="")
                        instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)
                        cosa=listadesor[Posmascerca1]
                        cosa1=cosa[:]
                        print('Llegar a pie toma: ', round(cosa1[0]/28.98,2), 'minutos')
                        print('Llegar en auto toma: ',round(cosa1[0]/1249.8,2), 'minutos')
                        opc_salir=input('Presione 0 para salir')
                        if opc_salir=='0':
                            os.system('cls')
                            continue
                        else: sys.exit()
                    elif ent_lleg=='2':
                        print('Elegiste la zona wifi 2')
                        time.sleep(2)
                        lat_pos_wifi=MatrizZWifi[Posmascerca2][0]
                        lon_pos_wifi=MatrizZWifi[Posmascerca2][1]
                        lat_pos_fav=Matriz2[1][0]
                        lon_pos_fav=Matriz2[1][1]
                        #instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)  #Invocacion funcion
                        print('Estas son las instrucciones de llegada: ',end="")
                        instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)
                        cosa=listadesor[Posmascerca2]
                        cosa1=cosa[:]
                        print('Llegar a pie toma: ', round(cosa1[0]/28.98,2), 'minutos')
                        print('Llegar en auto toma: ',round(cosa1[0]/1249.8,2), 'minutos' )
                        opc_salir=input('Presione 0 para salir')
                        if opc_salir=='0':
                            os.system('cls')
                            continue
                        else: sys.exit()
                    else: 
                        print('Error zona wifi')
                        sys.exit()

            elif op_coord=='3': 
                print('Elegiste la ubicación 3')
                Lat1=Matriz2[2][0]
                Lon1=Matriz2[2][1]
                #print(distancia(Lat1,Lon1))
                #time.sleep(5)
                listadesor=distancia(Lat1,Lon1)
                #listadesor=listadesor[:]
                listaok=salidaF.sort()  #Lista con las distancias ordenadas de min a mayor
                #print(salidaF, 'coco')
                #listaok=listaok[:]
                MatrizZWifi=[[-3.777,-70.302,91],[-4.134,-69.983,233],[-4.006,-70.132,149],[-3.846,-70.222,211]]
                Hallar1=salidaF[0][0]
                Hallado1=False
                for i in range(3):  #Busco la posicion de las 2 primeras zonas wifi en la lista de las distancias
                    Hallado1=listadesor[i][0]==Hallar1
                    if Hallado1:
                        break
                if Hallado1: 
                    Posmascerca1=i
                    #print("Elemento encontrado en el índice", i)                 
                    #print('Zonas wifi cercanas con menos usuarios: prueba')
                    #print('La zona wifi 1: ubicada en', '[',MatrizZWifi[i][0],',',MatrizZWifi[i][1],'] a', listadesor[i] ,'metros , tiene en promedio', MatrizZWifi[i][2] ,'usuarios')  
                    N_usuar1=listadesor[i]        
                Hallar2=salidaF[1][0]
                Hallado2=False
                for i in range(3):  #Busco la posicion de las 2 primeras zonas wifi en la lista de las distancias
                    Hallado2=listadesor[i][0]==Hallar2
                    if Hallado2:
                        break
                if Hallado2: 
                    Posmascerca2=i
                    #print("Elemento encontrado en el índice", i)                 
                    #print('La zona wifi 2: ubicada en','[', MatrizZWifi[i][0],',',MatrizZWifi[i][1],'] a', listadesor[i] ,'metros , tiene en promedio', MatrizZWifi[i][2] ,'usuarios')  
                    #print('Fin prueba')
                    N_usuar2=listadesor[i]
                    time.sleep(3)
                if N_usuar1>N_usuar2:  #Muestro en pantalla las zonas wifi, su distancia a la ubicacion del usuario y el numero de usuarios conectados
                    Dist_x=listadesor[Posmascerca2]
                    Dist_xx=listadesor[Posmascerca1]
                    Dist_x1=Dist_x[:]
                    Dist_xx1=Dist_xx[:]
                    print('La zona wifi 1: ubicada en','[', MatrizZWifi[Posmascerca2][0],',',MatrizZWifi[Posmascerca2][1],'] a', Dist_x1[0] ,'metros , tiene en promedio', MatrizZWifi[Posmascerca2][2] ,'usuarios')
                    print('La zona wifi 2: ubicada en', '[',MatrizZWifi[Posmascerca1][0],',',MatrizZWifi[Posmascerca1][1],'] a', Dist_xx1[0] ,'metros , tiene en promedio', MatrizZWifi[Posmascerca1][2] ,'usuarios')
                    ent_lleg=input('Elija 1 o 2 para recibir indicaciones de llegada ')
                    
                    if ent_lleg=='1':  
                        print('Elegiste la zona wifi 1')
                        time.sleep(2)
                        lat_pos_wifi=MatrizZWifi[Posmascerca2][0]
                        lon_pos_wifi=MatrizZWifi[Posmascerca2][1]
                        lat_pos_fav=Matriz2[2][0]
                        lon_pos_fav=Matriz2[2][1]
                        #instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)  #Invocacion funcion
                        print('Estas son las instrucciones de llegada: ',end="")
                        instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)
                        cosa=listadesor[Posmascerca2]
                        cosa1=cosa[:]
                        print('Llegar a pie toma: ', round(cosa1[0]/28.98,2), 'minutos')
                        print('Lllegar en auto toma: ',round(cosa1[0]/1249.8,2), 'minutos')
                        opc_salir=input('Presione 0 para salir')
                        if opc_salir=='0':
                            os.system('cls')
                            continue
                        else: sys.exit()
                    elif ent_lleg=='2':
                        print('Elegiste la zona wifi 2')
                        time.sleep(2)
                        lat_pos_wifi=MatrizZWifi[Posmascerca1][0]
                        lon_pos_wifi=MatrizZWifi[Posmascerca1][1]
                        lat_pos_fav=Matriz2[2][0]
                        lon_pos_fav=Matriz2[2][1]
                        #instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)  #Invocacion funcion
                        print('Estas son las instrucciones de llegada: ',end="")
                        instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)
                        cosa=listadesor[Posmascerca1]
                        cosa1=cosa[:]
                        print('Llegar a pie toma: ', round(cosa1[0]/28.98,2), 'minutos')
                        print('Lllegar en auto toma: ',round(cosa1[0]/1249.8,2), 'minutos')
                        opc_salir=input('Presione 0 para salir')
                        if opc_salir=='0':
                            os.system('cls')
                            continue
                        else: sys.exit()
                else: #Muestro en pantalla las zonas wifi, su distancia a la ubicacion del usuario y el numero de usuarios conectados
                    Dist_x=listadesor[Posmascerca2]
                    Dist_xx=listadesor[Posmascerca1]
                    Dist_x1=Dist_x[:]
                    Dist_xx1=Dist_xx[:]
                    print('La zona wifi 1: ubicada en', '[',MatrizZWifi[Posmascerca1][0],',',MatrizZWifi[Posmascerca1][1],'] a', Dist_xx1[0] ,'metros , tiene en promedio', MatrizZWifi[Posmascerca1][2] ,'usuarios')
                    print('La zona wifi 2: ubicada en','[', MatrizZWifi[Posmascerca2][0],',',MatrizZWifi[Posmascerca2][1],'] a', Dist_x1[0] ,'metros , tiene en promedio', MatrizZWifi[Posmascerca2][2] ,'usuarios')
                    ent_lleg=input('Elija 1 o 2 para recibir indicaciones de llegada ') 
                #Indico la forma de llegar a la zona wifi elegida:
                    if ent_lleg=='1':  
                        print('Elegiste la zona wifi 1')
                        time.sleep(2)
                        lat_pos_wifi=MatrizZWifi[Posmascerca1][0]
                        lon_pos_wifi=MatrizZWifi[Posmascerca1][1]
                        lat_pos_fav=Matriz2[2][0]
                        lon_pos_fav=Matriz2[2][1]
                        #instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)  #Invocacion funcion
                        print('Estas son las instrucciones de llegada: ',end="")
                        instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)
                        cosa=listadesor[Posmascerca1]
                        cosa1=cosa[:]
                        print('Llegar a pie toma: ', round(cosa1[0]/28.98,2), 'minutos')
                        print('Llegar en auto toma: ',round(cosa1[0]/1249.8,2), 'minutos')
                        opc_salir=input('Presione 0 para salir')
                        if opc_salir=='0':
                            os.system('cls')
                            continue
                        else: sys.exit()
                    elif ent_lleg=='2':
                        print('Elegiste la zona wifi 2')
                        time.sleep(2)
                        lat_pos_wifi=MatrizZWifi[Posmascerca2][0]
                        lon_pos_wifi=MatrizZWifi[Posmascerca2][1]
                        lat_pos_fav=Matriz2[2][0]
                        lon_pos_fav=Matriz2[2][1]
                        #instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)  #Invocacion funcion
                        print('Estas son las instrucciones de llegada: ',end="")
                        instrucciones_llegada(lat_pos_wifi,lon_pos_wifi,lat_pos_fav,lon_pos_fav)
                        cosa=listadesor[Posmascerca2]
                        cosa1=cosa[:]
                        print('Llegar a pie toma: ', round(cosa1[0]/28.98,2), 'minutos')
                        print('Llegar en auto toma: ',round(cosa1[0]/1249.8,2), 'minutos' )
                        opc_salir=input('Presione 0 para salir')
                        if opc_salir=='0':
                            os.system('cls')
                            continue
                        else: sys.exit()
                    else: 
                        print('Error zona wifi')
                        sys.exit()

    elif variable0=='4' or variable0=='5':
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
#borrarPantalla() #os.system('cls')  #? Cosas Reto 2
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
