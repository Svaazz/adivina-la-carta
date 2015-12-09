import funciones
import random
	
def sistemac():
	global sistema
	print("QUE SISTEMA OPERATIVO ESTAS UTILIZANDO?")
	sistema = int(input("0 para WINDOWS y 1 para LINUX "))
	funciones.limpiar(sistema)	

	
