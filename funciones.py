import os
def limpiar(sis):
	if sis == 0:
		os.system("cls")
	elif sis == 1:
		os.system("clear")
	else:
		errores.error(1)
