import random
import os
import time

game_over	=	False
ready_players	=	False
ready_dimension	=	False
create_board	=	True
player_tags	=	[" X ", " O ", " V ", " H ", " M "]
tie_count = 0


# CHECKS FOR VALID DIMENSIONS
while not ready_dimension:
	NUMS_ROWS	=	input("\nPlease choose the number of rows of your board (must be an integer between 4 and 26): ")
	NUMS_COLS	=	input("\nPlease choose the number of columns of your board (must be and integer between 4 and 26): ")


	if NUMS_ROWS.isdigit()	==	False	or	NUMS_COLS.isdigit()	==	False: # CHECKS IF THE USER INPUT IS NOT A NUMBER
		print("\nYour dimensions should only consist of integers. Restart.\n")
		ready_dimension	=	False
	else:
		NUMS_ROWS	=	int(NUMS_ROWS)
		NUMS_COLS	=	int(NUMS_COLS)
		if 26<NUMS_ROWS or NUMS_ROWS<4: # CHECKS IF THE USER INPUT IS NOT WITHIN RANGE
			print("\nThe number of rows should be an integer between 4 and 26. Restart\n") 
			ready_dimension	=	False
		elif 26<NUMS_COLS or NUMS_COLS<4: # CHECKS IF THE USER INPUT IS NOT WITHIN RANGE
			print("\nThe number of columns should be an integer between 4 and 26. Restart\n")
			ready_dimension	=	False
		else:
			ready_dimension	=	True # STOPS ASKING FOR ROW AND COLOUMN INPUTS WHEN THEY ARE CORRECT

			# CHECKS FOR VALID NUMBER OF PLAYERS
			while not ready_players:
				players	=	input("\nPlease enter the number of players playing (must be an integer between 2 and 5): ")

				if not players.isdigit(): # CHECKS IF THE USER INPUT IS NOT AN INTEGER
					print("\nPlease enter the number of players in an integer form. Restart")
					ready_players = False
				elif players.isdigit():
					players = int(players)
					if players<2 or players>5: # CHECKS IF THE USER INPUT IS NOT WITHIN RANGE
						print("\nThe number of players must be an integer between 2 and 5. Restart")
						ready_players = False

					else:
						ready_players	=	True # STOPS ASKING FOR NUMBER OF PLAYERS AFTER EACH TURN
						player_tags	=	player_tags[:players] #OVERWRITES THE ORIGINAL LIST OF PLAYERS ACCORDING TO THE NUMBER PLAYERS CHOSEN
						print("\nThe players are"+",".join(player_tags)+"--respectively.\n\nYou will play in that order, after the first player is chosen at random.\n\nA sample baord will be shown to you first.\n\nSTART CONNECTING!")
						first_turn	=	random.randint(0,	players	-	1) #ASSIGNS A RANDOM PLAYER FROM THE OVERWRITTEN LIST OF PLAYERS
					


# CREATES THE BOARD
board = []
for i in range(NUMS_ROWS):
	row = []
	for j in range(NUMS_COLS):
		row.append("   ")
	board.append(row)

row=[]                  # ROW COORDINATES
column=[]               # COLUMN COORDINATES

for i in range(NUMS_COLS):
	row.append(chr(65	+	i))   # ASCII CODE FOR LETTER A IS 65

for i in range(NUMS_ROWS):
	column.append(" ")                   

def new_board():
	print('')
	for cols in range(NUMS_COLS):
		print("   "+str(row[cols]), end="")
	for i in range(NUMS_ROWS):
		print("\n +"+"---+"*NUMS_COLS)
		print(column[i]+'|', end="")
		for j in range(NUMS_COLS):
			print(board[i][j]+'|', end="")
	print("\n +"+"---+"*NUMS_COLS)
new_board()
		

# THE GAME OFFICIALLY STARTS (AS LONG AS THERE IS NO WIN OR TIE)
while not game_over and tie_count !=	NUMS_COLS:

	if first_turn	== players	-	1: #ALTERNATES PLAYER WHEN THE PLAYER IS THE LAST PERSON ON THE LIST
		first_turn	=	(first_turn)%(players-1)
	else: #ALTERNATES PLAYER WHEN THE PLAYER IS NOT THE LAST PERSON ON THE LIST
		first_turn	=	((first_turn)%(players-	1))	+	1 

	
	new_board()
	user_input = input("Player"+player_tags[first_turn]+", please enter the letter of the column you want to drop your checker in: ").upper() # MAKES SURE THE USER INPUT IS CAPITALIZED TO MAKE PUTTING THE CHECKER EASIER
	
	# CHECKS FOR INVALID COORDINATES
	if len(user_input)	!=	1 or user_input[0].isdigit() or (ord(user_input[0]) not in range(65,	NUMS_COLS	+	65)): # CHECKS IF THE USER INPUT IS NOT 1 CHARACTER LONG OR IS A NUMBER OR IS NOT IN THE RANGE
		print("\nYour input must be 1 letter that is included in board's labels. Try again.\n\nPLEASE WAIT")
		time.sleep(3) # GIVES TIME FOR THE USER TO READ THE ERROR BEFORE PRINTING A NEW BOARD
		
		# MAKES SURE THE PLAYER'S TURN IS NOT SKIPPED
		if first_turn	==	0:
			(first_turn)	=	(first_turn)	+	(players	-	1)
		else:
			first_turn	=	first_turn	-	1 
		start_play	=	True
		

	elif board[0][ord(user_input[0])	-	65]	!=	"   ": # MAKES SURE THE PLAYER'S TURN IS SKIPPED
		print("\nThe column is full. Your turn will be skipped. Be careful next time.\n\nPLEASE WAIT")
		time.sleep(3)
		start_play	=	True



	else:
		win_turn	=	player_tags[first_turn] # SAVES THE PLAYER WHO LAST PLAYED IN CASE THEY WIN IN ORDER TO DISPLAY THEIR NAME
		board[0][ord(user_input[0])	-	65]	=	player_tags[first_turn] # INPUTS THE CHECKER COORESPONDING TO THE PLAYER'S NAME

		#INSERTS THE CHECKER IN THE CORRECT POSITION
		for i in range(NUMS_ROWS-1):
			for rows in range(NUMS_ROWS-2,	-1,	-1):
				for cols in range(NUMS_COLS):
					if (board[rows][cols]	==	" X " or board[rows][cols]	== " O " or board[rows][cols]	==	" V " or board[rows][cols]	==	" H " or board[rows][cols]	==	" M ") and (board[rows	+	1][cols]	!=	" X " and board[rows	+	1][cols]	!=	" O " and board[rows	+	1][cols]	!=	" V " and board[rows	 +	1][cols]	!=	" H " and board[rows	+	1][cols]	!=	" M "):
						board[rows][cols] = "   "
						board[rows	+	1][cols] = player_tags[first_turn]
			os.system("clear")
		

		#CHECKS FOR A WIN
		for i in range(NUMS_ROWS):
			for j in range(NUMS_COLS):
				if board[i][j]	==	"   ":
					continue
				if (board[i][j]	== " X " or board[i][j]	== " O " or board[i][j]	==	" V " or board[i][j]	==	" H " or board[i][j]	==	" M "):
					checker	=	board[i][j] # STORES THE CHECKER VARIABLE 
					
					# CHECKS FOR A HORISZONTAL WIN
					try:
						counter	=	0 # COUNTS THE NEEDED CHECKER TO WIN, AND ENDS WHEN IT IS TRUE	
						for k in range(1,4):
							if board[i][j	+	k]	==	checker: 
								counter	=	counter	+	1
								if counter	==	3:
									game_over	=	True 
									
							else:
								break # BREAKS WHEN THERE IS NO HORISZONTAL WIN

					except IndexError: # TRY-EXCEPT TO IGNORE INDEX ERRORS WHEN CHECKING FOR WINS
						pass
					
					# CHECKS FOR A VERTICAL WIN
					try:
						counter	=	0 # COUNTS THE NEEDED CHECKER TO WIN, AND ENDS WHEN IT IS TRUE	
						for k in range(1,4):
							if board[i	+	k][j]==checker: 
								counter	=	counter	+	1
								if counter	==	3:
									game_over	=	True
									
							else:
								break # BREAKS WHEN THERE IS NO VERTICAL WIN

					except IndexError: # TRY-EXCEPT TO IGNORE INDEX ERRORS WHEN CHECKING FOR WINS
						pass

					# CHECKS FOR A NEGATIVELY SLOPED DIAGONAL WIN	
					try:
						counter	=	0 # COUNTS THE NEEDED CHECKER TO WIN, AND ENDS WHEN IT IS TRUE	
						for k in range(1,4):
							if board[i	+	k][j	+	k]	==	checker: 
								counter	=	counter	+	1
								if counter	==	3:
									game_over	=	True
									
							else:
								break # BREAKS WHEN THERE IS NO NEGATIVELY SLOPED DIAGONAL WIN

					except IndexError: # TRY-EXCEPT TO IGNORE INDEX ERRORS WHEN CHECKING FOR WINS
						pass

					# CHECKS FOR A POSITIVELY SLOPED DIAGONAL WIN
					try:
						counter=0 # COUNTS THE NEEDED CHECKER TO WIN, AND ENDS WHEN IT IS TRUE	
						for k in range(1,4):
							if board[i	+	k][j	-	k]	==	checker: 
								counter	=	counter	+	1
								if counter	==	3:
									game_over	=	True
									
							else:
								break # BREAKS WHEN THERE IS NO POSITIVELY SLOPED DIAGONAL WIN

					except IndexError: # TRY-EXCEPT TO IGNORE INDEX ERRORS WHEN CHECKING FOR WINS
						pass

		tie_count	=	0 # COUNTER FOR EMPTY CELLS
		for j in range(NUMS_COLS): # CHECKS FOR EMPTY CELLS IN EACH COLUMN FOR A TIE
			if board[0][j]	!=	"   ":
				tie_count	=	tie_count	+	1
	os.system("clear") 	

if tie_count	==	NUMS_COLS:
	new_board()
	print("\nYou have tied!\n\nBetter luck next time!")
else:
	new_board()
	print()
	print (f"Player {win_turn} Won!")
				
					









	










