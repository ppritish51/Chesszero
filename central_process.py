import chess

class Conversion_of_postion_name(object):

	gap = 80
	def __init__(self, piece, i_pos = None, f_pos = None):
		
		self.i_pos = [i_pos[1]/Conversion_of_postion_name.gap, i_pos[0]/Conversion_of_postion_name.gap]
		self.f_pos = [f_pos[1]/Conversion_of_postion_name.gap, f_pos[0]/Conversion_of_postion_name.gap]
		self.dict_piece = {"WRook" : "R",
							"WKnight" : "N",
							"WBishop" : "B",
							"WKing" : "K",
							"WQueen" : "Q",
							"WPawn" : "P",
							"BRook" : "r",
							"BKnight" : "n",
							"BBishop" : "b",
							"BKing" : "k",
							"BQueen" : "q",
							"BPawn" : "p",
							None : 1
						}
		self.pseudo_dict_piece =   {"WRook" : "R",
								    "WKnight" : "N",
									"WBishop" : "B",
									"WKing" : "K",
									"WQueen" : "Q",
									"WPawn" : "P",
									"BRook" : "R",
									"BKnight" : "N",
									"BBishop" : "B",
									"BKing" : "K",
									"BQueen" : "Q",
									"BPawn" : "P",
									None : 1
								}
		
		self.piece = self.dict_piece[piece]
		self.pseudo_piece = self.pseudo_dict_piece[piece]
		if piece[0] == 'W':
			self.chance = 'W'
		elif piece[0] == 'B':
			self.chance = 'B'
		self.file = {
						0 : 'a',
						1 : 'b',
						2 : 'c',
						3 : 'd',
						4 : 'e',
						5 : 'f',
						6 : 'g',
						7 : 'h'
		}

		self.rank = {
						0 : '8',
						1 : '7',
						2 : '6',
						3 : '5',
						4 : '4',
						5 : '3',
						6 : '2',
						7 : '1'
		}

	def i_position(self):
		return self.file[self.i_pos[1]] + self.rank[self.i_pos[0]]

	def f_position(self):
		return self.file[self.f_pos[1]] + self.rank[self.f_pos[0]]

	def i_pos_ani(self):
		if self.i_pos[1] <= 7:
			return self.i_pos[0]*8 + self.i_pos[1]
		else:
			return 100

	def f_pos_ani(self):
		return self.f_pos[0]*8 + self.f_pos[1]	




def index_to_cell(index):
	rank = int ((63-index)/8 + 1)
	file = index%8
	file_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ]
	cell = file_list[file]+str(rank)
	return(cell)


class game_data():

	
	def __init__(self) :
		self.board = [None]*64
		self.board[4] = 'k'
		self.board[60] = 'K'
		# 0: white, 1: black
		self.active_color = 0
		self.K_c = 1
		self.Q_c = 1
		self.k_c = 1
		self.q_c = 1
		self.en_passant = 0
		self.half_moves = 0
		self.full_moves = 1
		self.fen = []


	def update(self, piece_type, i_pos, f_pos):
		# increase full moves by 1 if last move was by black
		if self.active_color == 1 :
			self.full_moves += 1
		# increase half moves by 1
		self.half_moves += 1
		# if pawn was moved, set half moves = 0
		# en passant capture
		if piece_type == 'p' or piece_type == 'P' :
			self.half_moves = 0
			if f_pos == self.en_passant :
				if self.active_color :
					remove_pawn_pos = f_pos-8
				else :
					remove_pawn_pos = f_pos+8
				self.board[remove_pawn_pos] = None
		# if capture occured, set half moves = 0
		if self.board[f_pos] != None :
			self.half_moves = 0
		# en passant
		if piece_type == 'p' or piece_type == 'P' :
			if f_pos-i_pos == 16 :
				self.en_passant = f_pos-8
			elif i_pos-f_pos == 16 :
				self.en_passant = f_pos+8
		else :
			self.en_passant = 0
		# update board
		if i_pos < 64 :
			self.board[i_pos] = None

		self.board[f_pos] = piece_type
		# update castling possibility
		if i_pos == 100 :
			if f_pos == 56 :
				self.Q_c = 1
			elif f_pos == 63 :
				self.K_c = 1
			elif f_pos == 0 :
				self.q_c = 1
			elif f_pos == 7 :
				self.k_c = 1
		if piece_type == 'K' and i_pos<64 :
			if f_pos-i_pos == 2 :
				if self.K_c :
					self.board[63] = None
					self.board[f_pos-1] = 'R'
			elif i_pos-f_pos == 2 :
				if self.Q_c :
					self.board[56] = None
					self.board[f_pos+1] = 'R'
			self.K_c = 0
			self.Q_c = 0
		elif piece_type == 'k' and i_pos<64 :
			if f_pos-i_pos == 2 :
				if self.k_c :
					self.board[7] = None
					self.board[f_pos-1] = 'r'
			elif i_pos-f_pos == 2 :
				if self.q_c :
					self.board[0] = None
					self.board[f_pos+1] = 'r'
			self.k_c = 0
			self.q_c = 0
		if piece_type == 'R' :
			if i_pos == 56 :
				self.Q_c = 0
			elif i_pos == 63 :
				self.K_c = 0
		elif piece_type == 'r' :
			if i_pos == 0 :
				self.q_c = 0
			elif i_pos == 7 :
				self.k_c = 0
		# toggle active color
		self.active_color = not self.active_color

	def generate_fen(self):
		self.fen = []
		count = 0
		for i in range(64):
			if self.board[i] == None :
				count += 1
			elif self.board[i] != None and count == 0 :
				self.fen.append(self.board[i])
			elif self.board[i] != None :
				self.fen.append(str(count))
				self.fen.append(self.board[i])
				count = 0
			if (i+1)%8 == 0 :
				if self.board[i] == None :
					self.fen.append(str(count))
				if i !=63 :
					self.fen.append('/')
				count = 0
		self.fen.append(' ')
		if self.active_color == 0 :
			self.fen.append('w')
		else :
			self.fen.append('b')
		self.fen.append(' ')
		if not (self.K_c or self.Q_c or self.k_c or self.q_c) :
			self.fen.append('-')
		else :
			if self.K_c :
				self.fen.append('K')
			else :
				#print('K castling disabled')
				pass
			if self.Q_c :
				self.fen.append('Q')
			if self.k_c :
				self.fen.append('k')
			if self.q_c :
				self.fen.append('q')
		self.fen.append(' ')
		if self.en_passant :
			self.fen.append(index_to_cell(self.en_passant))
		else :
			self.fen.append('-')
		self.fen.append(' ')
		self.fen.append(str(self.half_moves))
		self.fen.append(' ')
		self.fen.append(str(self.full_moves))

		return ''.join(self.fen)

def pgn(move,data_convert):
	for i in range(len(move)):
		if move[i][0] == data_convert.pseudo_piece:
			if move[i][-1] != '+' and move[i][-1] != '#':
				if move[i][-1] == str(data_convert.f_position())[1] and move[i][-2] == str(data_convert.f_position())[0]:
					if len(move[i]) == 3:
						return move[i]
					elif len(move[i]) == 4:
						if move[i][1] == 'x':
							return move[i]
						else:
							if move[i][1] == str(data_convert.i_position())[0] or move[i][1] == str(data_convert.i_position())[1]:
								return move[i]
					elif len(move[i]) == 5:
						if move[i][1] == str(data_convert.i_position())[0] or move[i][1] == str(data_convert.i_position())[1]:
							return move[i]

				

			elif move[i][-1] == '+' or move[i][-1] == '#':
				if move[i][-2] == str(data_convert.f_position())[1] and move[i][-3] == str(data_convert.f_position())[0]:
					if len(move[i]) == 4:
						return move[i]
					elif len(move[i]) == 5:
						if move[i][1] == 'x':
							return move[i]
						else:
							if move[i][1] == str(data_convert.i_position())[0] or move[i][1] == str(data_convert.i_position())[1]:
								return move[i]
					elif len(move[i]) == 6:
						if move[i][1] == str(data_convert.i_position())[0] or move[i][1] == str(data_convert.i_position())[1]:
							return move[i]



		elif data_convert.pseudo_piece == 'P':
			if move[i][0] == str(data_convert.f_position())[0]:
				if move[i][-1] != '+' or move[i][-1] != '#':
					if len(move[i]) == 2:
						if move[i][1] == str(data_convert.f_position())[1]:
							return move[i]
				elif move[i][-1] == '+' or move[i][-1] == '#':
					if len(move[i]) == 3:
						return move[i]

			elif move[i][0] == str(data_convert.i_position())[0]:
				if move[i][-1] != '+' or move[i][-1] != '#':
					if move[i][-1] == str(data_convert.f_position())[1] and move[i][-2] == str(data_convert.f_position())[0]:
						if len(move[i]) == 4:
							return move[i]
				elif move[i][-1] == '+' or move[i][-1] == '#':
					if len(move[i]) == 5:
						return move[i]

		elif data_convert.pseudo_piece == 'K':
			if move[i][-1] != '+' and move[i][-1] != '#':
				if str(data_convert.i_position())[0] == 'e':
					if str(data_convert.f_position())[0] == 'g' and move[i] == 'O-O':
						return 'O-O'
					elif str(data_convert.f_position())[0] == 'c' and move[i] == 'O-O-O':
						return 'O-O-O'

			elif move[i][-1] == '+' or move[i][-1] == '#':
				if str(data_convert.i_position())[0] == 'e':
					if str(data_convert.f_position())[0] == 'g':
						if move[i] == 'O-O+':
							return move[i]
						elif move[i] == 'O-O#':
							return move[i]
					elif str(data_convert.f_position())[0] == 'c':
						if move[i] == 'O-O-O+':
							return move[i]
						elif move[i] == 'O-O-O#':
							return move[i]

#game_state = game_data()
#temp_game_state = game_data()





"""
fen_prev = game_state.generate_fen()
#Conversion_of_postion_name("Wking", (900, 560), (320, 560))
data_convert = Conversion_of_postion_name("WKing", (900, 560), (320, 560))
game_state.update(data_convert.piece, int(data_convert.i_pos_ani()), int(data_convert.f_pos_ani()))

#print(data_convert)



########################## CONVERSION TO PGN ######################################
board = chess.Board(fen = fen_prev)





legal = str(board.legal_moves)

move = legal.split('(')
move = move[1].split(')')
move = move[0]
move = move.split(',')
for i in range(len(move)):
	move[i] = move[i].strip()
if move == ['']:
	print(pgn(move,data_convert))



"""