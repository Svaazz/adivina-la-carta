#Made by Svaazz

import random
import auto
import errores
import os
import check
import funciones
rounds = 1
won = 0
lost = 0


def rps():
	global won
	global lost
	global rounds

	Cards = ["As","2","3","4","5","6","7","8","9","10","Jota","Reina","Rey"]
	Suits = ["Espadas","Corazones","Picas","Diamantes"]
	print("")
	print("")
	print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	print(" Ronda: ", rounds)
	print("=================================================")
	print(" Tu carta es el/la ", Cards[Card_number]," de ",Suits[Suits_choice])
	print("=================================================")

	print(" Crees que la siguiente carta sera mayor o menor?")
	print(" + para MAYOR o - para MENOR")
	Question1Answer = str(input(">> "))

	if Question1Answer == "+":
		newCard_Value = random.randint(1,13)
		#Evitar que la carta sea igual
		while newCard_Value == Card_number:
			newCard_Value = random.randint(1,13)
		
		if newCard_Value < Card_number + 1:
			print(" Lo siento, has fallado!. La carta es el/la ", Cards[newCard_Value], " de ", Suits[Suits_choice])
			lost += 1
		elif newCard_Value > Card_number:
			print(" Felicidades! Has acertado. La carta es el/la ", Cards[newCard_Value], " de ", Suits[Suits_choice])
			won += 1
	if Question1Answer == "-":
		newCard_Value = random.randint(1,13)
		#newCard_number= Cards.index(newCard_Value)
		if newCard_Value > Card_number - 1:
			print(" Lo siento, has fallado!. La carta es el/la ", Cards[newCard_Value], " de ",Suits[Suits_choice])
			lost += 1
		elif newCard_Value < Card_number:
			print(" Felicidades! Has acertado. La carta es el/la ", Cards[newCard_Value], " de ", Suits[Suits_choice])
			won += 1 
	if Question1Answer == "a":
		auto.automa(Card_number)
		rps()
	print("=================================================")
	print(" Rondas Ganadas ", won)
	print(" Rondas Perdidas ", lost)
	print("=================================================")
	
	repeat = str(input(" Escribe 's' para volver a jugar >> "))
	if repeat == "s":
		
		rounds += 1
		start()
	else:
		exit()

def start():
	global Card_number
	global Suits_choice
	Card_number = random.randint(1,13)
	Suits_choice = random.randint(1,4)
	rps()
	
for i in range(4):
	print("")
print(" ¡Bienvenido a ADIVINA LA CARTA!")
print("")
print("=================================================")
check.sistemac()
start()




