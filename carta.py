#Made by Svaazz

import random
rounds = 1
Cards = ["As","2","3","4","5","6","7","8","9","10","Jota","Reina","Rey"]
Suits = ["Espadas","Corazones","Picas","Diamantes"]
won = 0
lost = 0

def rps():

	Card_number = random.randint(1,13)
	Suits_choice = random.randint(1,4)
	global won
	global lost
	print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	print(" Ronda: ", rounds)
	print("=================================================")
	print(" Tu primera carta es el/la ", Cards[Card_number]," de ",Suits[Suits_choice])
	print("=================================================")


	for i in range(1,rounds+1):
		print(" Crees que la siguiente carta sera mayor o menor?")
		print(" + para MAYOR o - para MENOR")
		Question1Answer = str(input(">> "))
		print(" Ronda", i)
			
	if Question1Answer == "+":
		newCard_Value= random.randint(1,13)
		#newCard_number= Cards.index(newCard_Value)
		if newCard_Value < Card_number + 1:
			print(" Lo siento, has fallado!. La carta es el/la ", Cards[newCard_Value], " de ", Suits[Suits_choice])
			lost += 1
		elif newCard_Value > Card_number:
			print(" Felicidades! Has acertado. La carta es el/la ", Cards[newCard_Value], " de ", Suits[Suits_choice])
			won += 1
	if Question1Answer== "-":
		newCard_Value= random.randint(1,13)
		#newCard_number= Cards.index(newCard_Value)
		if newCard_Value > Card_number - 1:
			print(" Lo siento, has fallado!. La carta es el/la ", Cards[newCard_Value], " de ",Suits[Suits_choice])
			lost += 1
		elif newCard_Value < Card_number:
			print(" Felicidades! Has acertado. La carta es el/la ", Cards[newCard_Value], " de ", Suits[Suits_choice])
			won += 1 
	print("=================================================")
	print(" Rondas Ganadas ", won)
	print(" Rondas Perdidas ", lost)
	print("=================================================")

	repeat = str(input(" Escribe 's' para volver a jugar >> "))
	if repeat == "s":
		global rounds
		rounds += 1
		rps()
def start():		
	print(" ¡Bienvenido a ADIVINA LA CARTA!")
	print("Hecho por Svaazz")
	print("=================================================")
	rps()
	

start()
