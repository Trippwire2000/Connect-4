def init_board():
	# Create list of lists, each list = 1 row,  0 at the top
	gb = []
	for i in range(6):
		gb.append([0,0,0,0,0,0,0])
	return gb

def printboard():
	for i in range(len(gb)):
		print(gb[i])

def column_ok(col):
	# Checks if the column is full ( top row should be 0)
	if gb[0][col] == 0:
		return True
	else:
		print('That column is full!')
		return False

def get_row(col):
	for i in reversed(range(0,6)):
		if gb[i][col] == 0:
			return i

def place_token(row, col, player):
	gb[row][col] = player

def check_win(gb):
	if p1 == True:
		t = 1
	else:
		t = 2

	for row in range(6):
		#check for horizontal win
		for col in range(4):
			if gb[row][col] == t and gb[row][col +1] == t and gb[row][col +2] ==t and gb[row][col +3] == t:
				print('Player {} wins!!'.format(t))

	for col in range(7):
		for row in range(3):
			if gb[row][col] == t and gb[row+1][col] == t and gb[row+2][col] == t and gb[row+3][col] == t:
				print('Player {} wins!!'.format(t))



def game():
	global p1

	if p1 == True:
		player = 1
	else:
		player = 2

	ok = False
	while ok == False:

		col = input('Player {}, choose your column (0-6) >> '.format(str(player)))

		if col in ['0','1','2','3','4','5','6']:
			col = int(col)
			ok = column_ok(col)

	row = get_row(col)
	place_token(row, col, player)
	check_win(gb)

	printboard()
	p1 = not p1
	game()

p1 = True
gb = init_board()
printboard()
game()










