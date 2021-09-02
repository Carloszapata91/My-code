import sys 
print('Bienvenido al sistema de ubicación para zonas públicas WIFI')  #Mensaje de bienvenida
nombre_usuario=51607  #Nombre de usuario predeterminado
contrasena=70615       #Contrasena predeterminada

while True:
    try:
        nombre_usuario_ingresado = int(input("Ingresa el nombre de usuario: "))  #El usuario ingresa el nombre de usuario y lo convierto a entero
        break  # Si no da error, corto el while con break
    except ValueError:
        print("Error"), sys.exit()


if  nombre_usuario_ingresado==nombre_usuario:    #Verificacion de nombre de usuario
    contrasena_ingresada= input("Ingresa su contraseña: ")  #El usuario ingresa su contraseña

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


if variable3==resultado_captcha:   #Verificacion de que el resultado ingresado es el correcto
   print('Sesión iniciada')

else: print('Error'), sys.exit()
