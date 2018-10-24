#Picking numbers for the lottery

import random

#fucntion to choose numbers for Lotto
def lotto(y):
	while y>0:
		randList=[]
		for num in range(6):
			randList.append(random.randrange(0, 48, 1))
		print(str(randList))
		y=y-1
	
#function to choose numbers for EuroMillions
def euroM(x):
	while x>0:
		randList=[]
		luckyStars=[]
		for num in range(5):
			randList.append(random.randrange(0, 51, 1))
		for luckyNums in range(2):
			luckyStars.append(random.randrange(0,13,1))
		print(str(randList) + str(luckyStars))
		x=x-1



#First choose the game you wish to play
game = input('Do you wish to play Irish Lotto (L) or EuroMillions (E): ')
numLines = input('How many lines do you wish to play: ')

if game == 'L' or game == 'l':
	lotto(int(numLines))
else:
	euroM(int(numLines))
