import random
PlayerCard = []
ComputerCard=[]
bidamt = 0
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five','Six','Seven', 'Eight', 'Nine', 'Jack', 'Queen', 'King','Ace')
value = {'Two':2, 'Three':3, 'Four':4, 'Five':5,'Six':6,'Seven':7, 'Eight':8, 'Nine':9, 'Jack':10, 'Queen':11, 'King':12,'Ace':13}
playersum=0
computersum=0
class StartGame:
	def Shuffle():
		def calc():
			suitschoice = random.sample(suits,1)
			rankschoice = random.sample(ranks,1)
			return [suitschoice,rankschoice]
		if calc() in PlayerCard or calc() in ComputerCard:
			calc()
		return calc()
	def bid():
		global bidamt
		bidamt = int(input('Welcome Please place a bid!:'))
		StartGame.play(suits,ranks)

	def play(suits,ranks):
		FlagSwitch=True
		for i in range(1,5):
			if FlagSwitch==True:
				PlayerCard.append(StartGame.Shuffle())
				FlagSwitch=False
			elif FlagSwitch==False:
				ComputerCard.append(StartGame.Shuffle())
				FlagSwitch=True
			else:
				pass
		StartGame.printout()
		StartGame.playing()
	def printout():
		print('____________________________________________________')

		print('Your Cards are:')
		for i in range(0,len(PlayerCard)):
			print("{} of {}".format(PlayerCard[i][0],PlayerCard[i][1]))
		print("Computers Card are:")
		print("First Card unknown")
		for i in range(1,len(ComputerCard)):
			print("{} of {}".format(ComputerCard[i][0],ComputerCard[i][1]))

		print('____________________________________________________')
	def printoutfinal():
		print('Your Cards are:')
		for i in range(0,len(PlayerCard)):
			print("{} of {}".format(PlayerCard[i][0],PlayerCard[i][1]))
		print("Computers Card are:")
		for i in range(0,len(ComputerCard)):
			print("{} of {}".format(ComputerCard[i][0],ComputerCard[i][1]))

	def playing():
		Turn = True
		Valid = True
		while Valid == True:
			print("Player's Turn")
			ans = input('Enter H to HIT or S to Stay')
			if ans == "H":
				PlayerCard.append(StartGame.Shuffle())
				#check statement here
				ComputerCard.append(StartGame.Shuffle())
				StartGame.printout()
				Valid = StartGame.total()
			elif ans == "S":
				ComputerCard.append(StartGame.Shuffle())
				StartGame.printout()
				Valid = StartGame.total()
			else:
				print('Invalid input! Try again!')
				Valid = True
	def total():
		global bidamt
		print(bidamt)
		playersum=0
		computersum=0
		for i in range(0,len(PlayerCard)):
			playersum = playersum + value["".join(PlayerCard[i][1])]
		for i in range(0,len(ComputerCard)):
			computersum = computersum + value["".join(ComputerCard[i][1])]

		#calculation of whether conditions!
		if playersum < computersum and computersum <= 21:
			print('Game OVER! Computer Wins! Total more than playersum less than 21')
			print('Lost your Money!')
			bidamt=0
			StartGame.printoutfinal()
			return False
		elif playersum > computersum and playersum == 21:
			print('Congratulations! Perfect 21!')
			print('Your have now totalled up to: {}'.format(bidamt*2))
			StartGame.printoutfinal()
			return False
		elif playersum>21:
			print('Ooops! Over 21. Lost!')
			print('Lost your Money!')
			bidamt=0
			StartGame.printoutfinal()
			return False
		elif computersum>21:
			print('Computersum over 21. Congratulations!')
			print('Your have now totalled up to: {}'.format(bidamt*2))
			StartGame.printoutfinal()
			return False
		else:
			return True


P1=StartGame
P1.bid()
