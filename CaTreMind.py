#VERSION MAS DIFICIL DE MASTERMIND BY CATRE
import random
import time
import datetime

print("""
BIENVENIDO A....
 _____       _____          ___  ___ _             _ 
/  __ \     |_   _|         |  \/  |(_)           | |
| /  \/  __ _ | | _ __  ___ | .  . | _  _ __    __| |
| |     / _` || || '__|/ _ \| |\/| || || '_ \  / _` |
| \__/\| (_| || || |  |  __/| |  | || || | | || (_| |
 \____/ \__,_|\_/|_|   \___|\_|  |_/|_||_| |_| \__,_|
---------------------*by CaTre*----------------------          
                                                   

""")

tiempo_actual = time.strftime("%H:%M:%S",time.localtime())

print("Son a las", tiempo_actual)


tiempo_raro = time.strftime("%H",time.localtime())

if tiempo_raro < "12":
	nombre = input("Buenos dias, ¿como te llamas? ")
	print("Gusto en conocerte ",nombre,"!!!")

if "12" <= tiempo_raro < "20":
	nombre = input("Buenas tardes, ¿como te llamas? ")
	print("Gusto en conocerte ",nombre,"!!!")

if tiempo_raro >= "20":
	nombre = input("Buenas noches, ¿como te llamas? ")
	print("Gusto en conocerte ",nombre,"!!!")

print(""" """)

seguir = int(input("""Escoje la modalidad de juego o ve a los creditos:: 
	1 = SOLO NUMEROS, )
	2 = LETRAS Y NUMEROS
	3 = CREDITOS(SALIR)"""))
if seguir == 3:
	print("""Creditos....
					Version basada en MasterMind de..
					https://www.youtube.com/channel/UC8mLKwIn-2Yb7nssjgEHWrw
					y mejorada por LuisCaTre
	         """)

while seguir == 1:
	print("Tendras que adivinar un codigo")
	print("""Estas son las dificultades: 
		1 = Facil
		2 = Medio 
		3 = Dificil  
		4 = Pesadilla""")
	dificultad = int(input("¿Que dificultad quieres?(Elije con cuidado) "))

	if dificultad == 1:
		cant_digitos = 4
	elif dificultad == 2:
		cant_digitos = 6
	elif dificultad == 3:
		cant_digitos = 8
	elif dificultad == 4:
		cant_digitos = 10
	digitos = ('0','1','2','3','4','5','6','7','8','9')
	codigo = ""

	for i in range(cant_digitos):
		elegido = random.choice(digitos)
		while elegido in codigo:
			elegido = random.choice(digitos)
		codigo = codigo + elegido

	print("Tienes que adivinar un codigo de ",cant_digitos , " numeros distintos")
	print("              Buena suerte!!!")
	propuesta = input("¿Que codigo propones? ")
	inicio = time.time()
	intentos = 1

	while propuesta != codigo:
		intentos = intentos + 1
		aciertos = 0
		coincidencias = 0
		for i in range(cant_digitos):
			if propuesta[i] == codigo[i]:
				aciertos = aciertos + 1
			elif propuesta[i] in codigo:
				coincidencias = coincidencias + 1
		print("Tu propuesta(",propuesta,") tiene ", aciertos,
			"aciertos y ",coincidencias," coincidencias")
		propuesta = input("Propon otro codigo: ")
	final = time.time()
	tiempo = round(final - inicio,0)
	print("ALV!!!, adivinaste el codigo en", intentos," intentos y en ",tiempo," segundos")
	seguir = int(input("¿Quieres seguir jugando?, puedes cambiar de modalidad, o salir(00)"))
	if seguir == 00:
		break



while seguir == 2:
	print("Tendras que adivinar un codigo con numeros y letras")
	print("""Estas son las dificultades:
		1 = Medio
		2 = Dificil
		3 = Pesadilla 
		4 = IMPOSIBLE!!!""")
	dificultad = int(input("¿Que dificultad quieres?(Elije con cuidado) "))

	if dificultad == 1:
		cant_digitos = 4
	elif dificultad == 2:
		cant_digitos = 6
	elif dificultad == 3:
		cant_digitos = 8
	elif dificultad == 4:
		cant_digitos = 10
	digitos =('0','1','2','3','4','5','6','7','8','9',"A","B",
	"C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")
	codigo = ""

	for i in range(cant_digitos):
		elegido = random.choice(digitos)
		while elegido in codigo:
			elegido = random.choice(digitos)
		codigo = codigo + elegido

	print("Tienes que adivinar un codigo de ",cant_digitos , " numeros y letras distintas")
	print("              Buena suerte!!!")
	propuesta = input("¿Que codigo propones? ")
	inicio = time.time()
	intentos = 1

	while propuesta != codigo:
		intentos = intentos + 1
		aciertos = 0
		coincidencias = 0
		for i in range(cant_digitos):
			if propuesta[i] == codigo[i]:
				aciertos = aciertos + 1
			elif propuesta[i] in codigo:
				coincidencias = coincidencias + 1
		print("Tu propuesta(",propuesta,") tiene ", aciertos,
			"aciertos y ",coincidencias," coincidencias")
		propuesta = input("Propon otro codigo: ")
	final = time.time()
	tiempo = round(final - inicio,0)
	print("""

		______   _ _      _     _           _          
		|  ___| | (_)    (_)   | |         | |         
		| |_ ___| |_  ___ _  __| | __ _  __| | ___ ___ 
		|  _/ _ | | |/ __| |/ _` |/ _` |/ _` |/ _ / __|
		| ||  __| | | (__| | (_| | (_| | (_| |  __\__ \
		\_| \___|_|_|\___|_|\__,_|\__,_|\__,_|\___|___/
                                               
        ALV!!!, adivinaste el codigo en""", intentos,""" intentos y""", tiempo,""" segundos
         """)

	seguir = int(input("¿Quieres seguir jugando?, puedes cambiar de modalidad, o salir(00)"))
	if seguir == 00:
		break
print("")
if seguir == 3:
	print("""Creditos....
					Version basada en MasterMind de devidcoptero..
					https://www.youtube.com/channel/UC8mLKwIn-2Yb7nssjgEHWrw
					y mejorada por LuisCaTre
	         """)

print("""Hasta luego...

______               ______                  
| ___ \              | ___ \                 
| |_/ /_   _  ___    | |_/ /_   _  ___       
| ___ | | | |/ _ \   | ___ | | | |/ _ \      
| |_/ | |_| |  __/_ _| |_/ | |_| |  __/_ _ _ 
\____/ \__, |\___(_(_\____/ \__, |\___(_(_(_)
        __/ |                __/ |           
       |___/                |___/            
      							  by CaTre...
      """)

