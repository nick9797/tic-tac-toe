#This program is a game of tic tac toe.

import random
from random import randint

board=[" "," "," ",
       " "," "," ",
       " "," "," "]

wins=['0','0']

def initgame():
	print("Welcome to tictactoe!")
	print("This is a game where you must be the first person to get a row of three x's or o's. Whoever gets their row done first wins!")
	print("You will make your move first, followed by the computer.")
	print("This is what the board looks like. To place an x or o, input the any number on the board. The number will be replaced by your x or o.")
	print(" 0 | 1 | 2 ")
	print("-----------")
	print(" 3 | 4 | 5 ")
	print("-----------")
	print(" 6 | 7 | 8 ")

initgame()

def printboard():
	print(board[0],' | ',board[1],' | ',board[2])
	print("--------------")
	print(board[3],' | ',board[4],' | ',board[5])
	print("--------------")
	print(board[6],' | ',board[7],' | ',board[8])

def check_win():
	if board[0]==board[1] and board[2]==board[1]:
		if board[0] == " ":
			return
		elif board[0] == "X":
			print("You win!")
			i = 21
			wins[0]=1
		elif board[0] == "O":
			print("The computer wins! You lose!")
			i = 11
			wins[1]=1
	elif board[3]==board[4] and board[5]==board[4]:
		if board[3]== " ":
			return
		elif board[3] == "X":
			print("You win!")
			i = 21
			wins[0]=1
		elif board[3] == "O":
			print("The computer wins! You lose!")
			i = 11
			wins[1]=1
	elif board[6]==board[7] and board[8]==board[7]:
		if board[6]== " ":
			return
		elif board[6] == "X":
			print("You win!")
			i = 21
			wins[0]=1
		elif board[6] == "O":
			print("The computer wins! You lose!")
			i = 11
			wins[1]=1
	elif board[0]==board[3] and board[6]==board[3]:
		if board[0]== " ":
			return
		elif board[0] == "X":
			print("You win!")
			i = 21
			wins[0]=1
		elif board[0] == "O":
			print("The computer wins! You lose!")
			i = 11
			wins[1]=1
	elif board[1]==board[4] and board[7]==board[4]:
		if board[1]== " ":
			return
		elif board[1] == "X":
			print("You win!")
			i = 21
			wins[0]=1
		elif board[1] == "O":
			print("The computer wins! You lose!")
			i = 11
			wins[1]=1
	elif board[2]==board[5] and board[8]==board[5]:
		if board[2]== " ":
			return
		elif board[2] == "X":
			print("You win!")
			i = 21
			wins[0]=1
		elif board[2] == "O":
			print("The computer wins! You lose!")
			i = 11
			wins[1]=1
	elif board[0]==board[4] and board[8]==board[4]:
		if board[0]== " ":
			return
		elif board[0] == "X":
			print("You win!")
			i = 21
			wins[0]=1
		elif board[0] == "O":
			print("The computer wins! You lose!")
			i = 11
			wins[1]=1
	elif board[2]==board[4] and board[6]==board[4]:
		if board[2]== " ":
			return
		elif board[2] == "X":
			print("You win!")
			i = 21
			wins[0]=1
		elif board[2] == "O":
			print("The computer wins! You lose!")
			i = 11
			wins[1]=1
check_win()

printboard()

def getPlayerMove():
		move=int(input("Enter the spot you want...: "))
		if move < 9 and move > -1:
			if board[move] == " ":
				board[move] = "X"
				printboard()
				return	
			else:
				print("Sorry! That spot has already been taken.")
		else: 
			print("You picked a number that is not on the board.")
		getPlayerMove()

def getComputerMove():
	print("The computer makes a move!")
	move=random.randrange(0,9)
	if move < 9 and move > -1:
		if board[move] == " ":
			board[move] = "O"
			printboard()
			return
	getComputerMove()

def playGame():
	i=0
	k=0
	while i <9:
		if k==0:
			getPlayerMove()
			check_win()
			if wins[0]==1:
				break
			k=1
			i=i+1
		elif k==1:
			getComputerMove()
			check_win()
			if wins[1]==1:
				break
			k=0
			i=i+1
	if i==9:
		print("The game is a tie...")
playGame()

print("End of game! Thanks for playing!")

