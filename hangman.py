# Hangman Game: HACK
# By: Andrew Whitehurst
# Created 24Aug2017

import time
import os
import sys
import random
import threading
from random import randint

#determine enviornment for "clear" variable
def os_check():
	if sys.platform.startswith('win'):
		clr = 'CLS'
	elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
		clr = 'clear'
	elif sys.platform.startswith('cygwin'):
		clr = "alias clear='printf \"\\033c\"'"
	else:
		raise EnvironmentError('Unsupported platform')
	return clr

#for UNIX systems -> hides the cursor
def hide_cursor():
	if os.name == 'posix':
		sys.stdout.write("\033[?25l")
		sys.stdout.flush()

#ascii functions******************************
#opening screen
def line(ch):
	for i in range(0,80):
		print(ch, end='')
	print('')
		
def boarder(ch):
	for i in range(0,3):
		print(ch, end='')
	for i in range(0,74):
		print(' ', end='')
	for i in range(0,3):
		print(ch, end='')
	print('')
		
def open_image(art):
	cut_art = art.splitlines() #turn into list of str lines
	height_art = len(cut_art) #find height of art
	width_art = len(cut_art[0]) #find width of art
	excess_vert = height_art % 2 #becomes 1 if number of lines is odd
	excess_horz = width_art % 2
	bulk_vert = int((20 - height_art) / 2) #find number of lines without art
	bulk_horz = int((80 - width_art - 6)/2)
	
	#begins printing art
	for i in range(0,bulk_vert):
		boarder('*')
	#PRINT ART... DO IT!!!
	for i in range(0,height_art):
		print('***', end='')
		for f in range(0,bulk_horz):
			print(' ', end='')
		print(cut_art[i], end='')
		for e in range(0,bulk_horz+excess_horz):
			print(' ', end='')
		print('***')
	#end of art bulk area
	for i in range(0,bulk_vert+excess_vert):
		boarder('*')
	
def open_screen(art_str):	
	for i in range(0,2):
		line('*')
	
	open_image(art_str)
		
	for i in range(0,1):
		line('*')

#function to flicker open screen away
def flicker(screen, img, clr):
	screen(img)
	time.sleep(3)
	os.system(clr)
	time.sleep(.3)
	screen(img)
	time.sleep(2)
	os.system(clr)
	time.sleep(.2)
	for i in range (0,3):
		screen(img)
		time.sleep(.3)
		os.system(clr)
		time.sleep(.1)
	time.sleep(.5)
		
#text screen function
def hello_print(line):
	for i in range(0,len(line)):
		x = random.uniform(.1,.4)
		print(line[i],end='',flush=True) #flush is used here for buffering issue
		time.sleep(x)
		i = i + 1
	time.sleep(2)
	os.system(clr)

#'typed' text intro		
def hello_screen():
	line1 = "Wake up..."
	line2 = "The Matrix has you."
	line3 = "Follow the white rabbit."
	line4 = "Knock, knock."
	lines = [line1, line2, line3, line4]
	for i in range(0, 4):
		hello_print(lines[i])
	time.sleep(1)

#white rabbit animation
def print_rabbit(img_list, pos):
	for x in range(0,11):
		for i in range(0,pos):
			print(" ", end ='')
		print(img_list[x])

def white_rabbit(sit,hop):
	cut_sit = sit.splitlines()
	cut_hop = hop.splitlines()
	i = 0
	while(i < 60): #16 is longest line length
		print_rabbit(cut_sit, i)
		time.sleep(1)
		os.system(clr)
		print_rabbit(cut_hop, i + 6)
		time.sleep(.2)
		os.system(clr)
		i = i + 10


#Directions screen****************************
def directions():
	print("Hangman type game. No numbers, or spaces.")
	print("For every guessed letter, it will show in the code.")
	print("Guessing the same letter is a penalty.")
	print("You may guess the whole word, but it count double against you.")
	print("Once the code has siezed, you have lost.")
	print("Good luck.")
	
	input("[Press Enter to begin]")

#gameside functions*******************
#8 guess game
numOfGuess = 8

def check(x, puzzle_word):
	found = False
	for i in range(0,len(puzzle_word)):
		if (x == puzzle_word[i]):
			found = True
	return found

	
#win screen
def solved():
	os.system(clr)
	print("you win")
	time.sleep(2)
	
#lost screen
def lost():
	os.system(clr)
	print("you lose")
	time.sleep(2)

#word guessing game portion
def guessing(trysLeft, puzzleword):
	loop = True
	filledBox = False
	guessedLetters = list()
	x = ''
	while(loop == True):
		filledBox = animation(guessedLetters, puzzleword)
		if (filledBox == True): #win if all puzzle letters guessed
			solved()
			loop = False
			return
		x = input('') #get guess from usr
		x = x.upper()
		if(len(x)<=1): #anylize if only single letter input
			guessedLetters += x
			isIn = True
			isIn = check(x, puzzleword)
			if (isIn == False):
				trysLeft = trysLeft-1
		elif (puzzleword.strip() == x.strip()): #win if usr guesses puzzle right
			loop = False
			time.sleep(1.5)
			solved()
		else: #2 point penalty for improper word guess or character
			trysLeft = trysLeft-2
		if(trysLeft <= 0): #lose from too many tries
			loop = False
			print(puzzleword)
			time.sleep(1.5)
			lost()
			
#game screen
def animation(usedCharList, puzzleword):
	os.system(clr)
	graphicsBox = list() #box of misc characters
	for i in range(0,80*11): #x * y #create box
		randchar = chr(randint(33,47))
		graphicsBox += randchar
	for c in range(0,len(usedCharList)): #places used letters in misc char graphic
		haltLetter = str(usedCharList[c])
		for i in range(0, 75):
			randPos = randint(0,80*11 - 1)
			graphicsBox[randPos] = haltLetter
	puzzleBox = puzzleword #create puzzle char underscores or correct guessed letters
	for i in range(0,len(puzzleword)-1): 
		if puzzleword[i] not in usedCharList:
			puzzleBox = puzzleBox.replace(puzzleword[i], '_')
	if '_' not in puzzleBox:
		return True #if no '_' , the player has won
	for i in range(0,len(graphicsBox)): #prints graphics
		print(graphicsBox[i], end='')
	print()
	print()
	puzzleBox = puzzleBox.split()
	for i in range(0,len(puzzleBox)): #prints puzzle situation
		print(puzzleBox[i], end ='')
		print(' ', end='')
	return False #if player hasnt won yet
	
		
#picks a random word from list
def puzzlewords(word_list):
	x = randint(0,len(word_list)-1)
	return word_list[x]

#resource files*******************************
#list of words -> word_list
text_file = open("WordList.txt")
word_list = text_file.readlines()

#list of 'opening' ascii art ->opening
text_file = open("opening.txt")
opening = text_file.read()

#list of 'rabbit' 1 & 2 ascii art -> rab_sit, rab_hop
#art by Joan Stark
text_file = open("rabbitSit.txt")
rab_sit = text_file.read()

text_file = open("rabbitHop.txt")
rab_hop = text_file.read()

def playMore(): #function to keep playing or not
	os.system(clr)
	print("Care to see how deep the rabbit hole goes?")
	print("[Take the Red pill, or the Blue pill]")
	ans = input("(Hint:Red, play again. Blue, quit)")
	ans = ans.upper()
	if ans in ['R', 'RED']:
		return True
	elif ans in ['B', 'BLUE']:
		return False
	else:
		print('There is no ' + ans)
		time.sleep(1.5)
		return playMore()
		

#Running operations***************************

hide_cursor()
clr = os_check()
os.system(clr)
flicker(open_screen, opening, clr)
hello_screen()
white_rabbit(rab_sit,rab_hop)
directions()

playAgain = True

while (playAgain == True):
	puzzleword = puzzlewords(word_list)
	guessing(numOfGuess, puzzleword.upper())
	playAgain = playMore()
	
#playing quiting game
os.system(clr)
print("Thanks for playing")
time.sleep(1.5)
