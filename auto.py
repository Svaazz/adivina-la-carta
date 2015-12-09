import random

def automa(card):
	if card < 6:
		opinion("mayor")
	elif card > 6:
		opinion("menor")
	if card == 6:
		x = random.randint(1, 2)
		if x == 1:
			opinion("mayor")
		else:
			opinion("menor")

			
	
def opinion(opi):
		print("####### LA MAQUINA CREE QUE ########")
		print("##      La carta sera ", opi, "     ##")
		print("####################################")
