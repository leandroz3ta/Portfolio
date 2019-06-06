from random import randint
from time import sleep

escolhas = ("Pedra", "Papel", "Tesoura")

robo = randint(0,2)

ganhos = 0
perdas = 0
empates = 0

print (30 * '-')
print ("   J O K E N - P O")
print (30 * '-')
 
loop=True 
 
while loop: 
		## Get input ###
		escolha = input('Faça sua escolha [ Pedra[0] Papel[1] Tesoura[2] ] : ')
		 
		### Convert string to int type ##
		escolha = int(escolha)
		 
		print("-="*20)
		print("O computador escolheu: {}".format(escolhas[robo]))
		print("Voce escolheu: {}".format(escolhas[escolha]))
		print("-="*20) 
		 
		### Take action as per selected menu-option ###
		if escolha == 0:
				if robo == 0:
					print ("Empate")
					empates = empates+1
				elif robo == 1:
					print ("Voce perdeu!")
					perdas = perdas+1
				elif robo == 2:
					print ("Voce ganhou!")
					ganhos = ganhos+1
		elif escolha == 1:
				if robo == 0:
					print ("Voce ganhou!")
					ganhos = ganhos+1
				elif robo == 1:
					print ("Empate")
					empates = empates+1
				elif robo == 2:
					print ("Voce Perdeu")
					perdas = perdas+1
		elif escolha == 2:
				if robo == 0:
					print ("Voce ganhou!")
					ganhos = ganhos+1
				elif robo == 1:
					print ("Voce ganhou!")
					perdas = perdas+1
				elif robo == 2:
					print ("Empate.")
					empates = empates+1
		elif escolha == 5:
					loop=False
					print("fim.")
					print("Voce ganhou "+ganhos+", perdeu "+perdas+" e empatou "+empates)
		else:    ## default ##
				raw_input ("Para de zuera e escolha o numero certo!")
