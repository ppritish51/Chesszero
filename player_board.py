import pygame
from PIECES import *
import chess
import central_process as CP 
import copy


class DISPLAY(object):
	"""docstring for DISPLAY"""
	def __init__(self, screen):

		self._where ,self._to = None,None
		self.game_state = CP.game_data()
		

		self.screen = screen
		self.selection_bar_background = pygame.image.load('pieces/cover.png')
		self.selection_bar_effect = pygame.image.load('pieces/cover_effect.png')
		self.board_effect = pygame.image.load('pieces/cover_effect2.png')
		self.selection_bar_not_available = pygame.image.load('pieces/all_used.png')
		self.background = pygame.image.load('background.png')
		#variaables to update frequently
		self.whose_move = "white"
		self.selected_from_selection_bar = False
		self.selected_from_board = False
		self.selected_piece = None
		#current selected position
		self.selected_position = None #(0,560)

		#self.occupied_position_on_board = [(320,560),(320,0)]
		"""
		self.board_positions = []
		_temp__ = [None,None,None,None,None,None,None,None]
		for i in range(8):
			self.board_positions .append(list(_temp__))
		"""

		self.blit_piece = []#0: location 1: piece
		"""
		#just testing the program 
		self.board_positions[0][7] = 'BRook'
		self.board_positions[7][0] = 'WRook'
		print(self.board_positions)
		"""
			
		self.pieces = { 'WRook':WRook(),
						'WKnight':WKnight(),
						"WBishop":WBishop(),
						'WQueen':WQueen(),
						"WKing":WKing(),
						"WPawn":WPawn(),
						"BRook":BRook(),
						"BKnight":BKnight(),
						"BBishop":BBishop(),
						"BQueen":BQueen(),
						"BKing":BKing(),
						"BPawn":BPawn()}

		self.anirudh_2_pritish = {"R" :"WRook" ,
							"N" :"WKnight" ,
							"B" :"WBishop" ,
							"K" :"WKing" ,
							"Q" :"WQueen" ,
							"P" :"WPawn" ,
							"r" :"BRook" ,
							"n" :"BKnight" ,
							"b" :"BBishop" ,
							"k" :"BKing" ,
							"q" :"BQueen" ,
							"p" :"BPawn" ,
							None :None
						}
	def display_selection_bar(self):
		position_ = [(700,150),(800,150),(900,150),
					 (700,250),(800,250),(900,250),
					 (700,400),(800,400),(900,400),
					 (700,500),(800,500),(900,500)]

		for pos in position_:
			_pieces__ = Helping_Class.selection_bar_mapping[pos]
			#print(_pieces__)
			if self.pieces[_pieces__].availability:
				self.screen.blit(self.selection_bar_background,pos)
			else:
				self.screen.blit(self.selection_bar_not_available,pos)
			self.screen.blit(pygame.image.load('pieces/'+str(_pieces__)+'.png'),pos)

		if self.blit_piece :
			if self.pieces[self.blit_piece[1]].availability:
				self.screen.blit(self.selection_bar_effect,self.blit_piece[0])
				self.screen.blit(self.pieces[self.blit_piece[1]].image,self.blit_piece[0])

		if self.selected_from_selection_bar  :
			if self.pieces[self.selected_piece].availability:
				self.screen.blit(self.selection_bar_effect,Helping_Class.selection_bar_reverse_mapping[self.selected_piece])
				self.screen.blit(self.pieces[self.selected_piece].image,Helping_Class.selection_bar_reverse_mapping[self.selected_piece])



	
	def display_everything(self):
				

		self.screen.blit(self.background,(0,0))
		if self.selected_from_board:
			self.screen.blit(self.board_effect,self.selected_position)
		#if self._where:
		#	self.screen.blit(self.board_effect,self._where)
		#	self.screen.blit(self.board_effect,self._to)
		for i in range(64):
			x = i%8
			y = int(i/8)
			_temp__ = self.anirudh_2_pritish[self.game_state.board[i]]
				
			if _temp__:

				piece_image = self.pieces[_temp__].image 
				self.screen.blit(piece_image,(x*80+10,y*80+10))
			else:
				pass

		

	
	def main_board_maintenance(self,x_cor,y_cor,situation):

		"""
										`		clicked on board
											        |
									---------------------------------
									|								|
								   yes                              No
								    |                               |
						   selected from where                nothing to do
						            |
					    --------------------------------------------------------------------------------------
						|                                         |                                          |
			      selection_bar                                 Board                                  no selection 
				        |                                         |                                          |
			is clicked on valid position               is clicked on valid position(Rajan)           clicked on empty slot 
			   |                    |                   |     (it returns pgn)    |                           |
			   |                    |                   |                         |                           |
			  yes                  no                  yes                        no              -----------------------------
			   |                    |                   |                         |               |                           |
		  place it         (if his piece)    does move contain 'x' (capture)    select piece      no                         yes 
		(if not check)     change selection        |                      |    (Ask & Discuss)    |                           |                          
		                                          yes                     no                  is it his piece                 pass
		                                           |                      |                         |
		                     capture and update both pieces state    just place piece       -----------------------
		                                                                                    |                     |
		                                                                                    yes                  no
		                                                                                    |                     |
		                                                                            select the piece             pass
	"""

		for event in pygame.event.get():  
			if  event.type == pygame.QUIT:
				pygame.display.quit()
				pygame.quit()
				quit()  
			if event.type == pygame.MOUSEBUTTONDOWN:
				#'check','normal','checkmate'
				
				x_adjusted,y_adjusted = Helping_Class.convert_coordinate(x_cor,y_cor,from_where ='board')
				#print(x_adjusted/80,y_adjusted/80)
				print('situation',situation)
				if self.selected_from_selection_bar :
					
					x_adjusted,y_adjusted = Helping_Class.convert_coordinate(x_cor,y_cor,from_where ='board')

					temp_game_state = CP.game_data()
					temp_game_state = copy.deepcopy(self.game_state)
					data_convert = CP.Conversion_of_postion_name(self.selected_piece,Helping_Class.selection_bar_reverse_mapping[self.selected_piece] ,(x_adjusted,y_adjusted))
					temp_game_state.update(data_convert.piece, int(data_convert.i_pos_ani()), int(data_convert.f_pos_ani()))
					temp_game_state.active_color = not temp_game_state.active_color
					fen = temp_game_state.generate_fen()
					board2  = chess.Board(fen=fen)
					print(board2)
					print(fen)
					print('board2.is_check()',board2.is_check())
					#now we need to place the piece on board
					
					if self.game_state.board[Helping_Class.convert_my_coordinate_to_anirudh(x_adjusted,y_adjusted)] == None:
						#print(self.selected_position)
						if not board2.is_check():
							if self._check_valid_position_(x_adjusted,y_adjusted):
								self.place_piece_on_board_from_selection_bar(x_adjusted,y_adjusted)
								#rajan's
								#print(self.selected_piece)
								#print(self.selected_position)
								data_convert = CP.Conversion_of_postion_name(self.selected_piece,self.selected_position ,(x_adjusted,y_adjusted))
								self.game_state.update(data_convert.piece, int(data_convert.i_pos_ani()), int(data_convert.f_pos_ani()))
								#self._where,self._to = (x_adjusted,y_adjusted),self.selected_position
								self.selected_piece = None
								self.selected_position  = None
							else:
								pass
					#board position is filled then nothing to do
					else:
						#if his piece change selection
						self.selected_from_selection_bar =False
						self.selected_from_board  = True
						self.selected_piece = self.anirudh_2_pritish[self.game_state.board[Helping_Class.convert_my_coordinate_to_anirudh(x_adjusted,y_adjusted)]]
						self.selected_position = (x_adjusted,y_adjusted)
					

				elif self.selected_from_board:
					#print('inside selection bar board option')
					x_adjusted,y_adjusted = Helping_Class.convert_coordinate(x_cor,y_cor,from_where ='board')
					
					omega = True
					if self.selected_position:
						if self.selected_position == (x_adjusted,y_adjusted):
							omega = False
					#print(self.selected_position,(x_adjusted,y_adjusted))
					if omega:
						move = self._check_valid_move_(x_adjusted,y_adjusted)
						#print(move)
					if omega:
						if move:
							#if move contains x then we have update state of captured piece
							#else just update selected piece
							#print("correct move")
							self.capture_piece_update_board_or_place_piece(move,x_adjusted,y_adjusted)

						else:
							#select the piece
							if self.game_state.board[Helping_Class.convert_my_coordinate_to_anirudh(x_adjusted,y_adjusted)]:
								self.selected_piece = self.anirudh_2_pritish[self.game_state.board[Helping_Class.convert_my_coordinate_to_anirudh(x_adjusted,y_adjusted)]]
								self.selected_position = (x_adjusted,y_adjusted)
								self.selected_from_board = True
								
				else:
					
					x_adjusted,y_adjusted = Helping_Class.convert_coordinate(x_cor,y_cor,from_where ='board')
					if self.game_state.board[Helping_Class.convert_my_coordinate_to_anirudh(x_adjusted,y_adjusted)]:
						#select the piece
						if self.whose_move == 'white':
							if 'W' in self.anirudh_2_pritish[self.game_state.board[Helping_Class.convert_my_coordinate_to_anirudh(x_adjusted,y_adjusted)]]:
								self.selected_piece = self.anirudh_2_pritish[self.game_state.board[Helping_Class.convert_my_coordinate_to_anirudh(x_adjusted,y_adjusted)]]
								self.selected_from_board = True
								self.selected_position = (x_adjusted,y_adjusted)
							else:
								#nothing to do
								pass
						elif self.whose_move == 'black':
							if 'B' in self.anirudh_2_pritish[self.game_state.board[Helping_Class.convert_my_coordinate_to_anirudh(x_adjusted,y_adjusted)]]:
								self.selected_piece = self.anirudh_2_pritish[self.game_state.board[Helping_Class.convert_my_coordinate_to_anirudh(x_adjusted,y_adjusted)]]
								self.selected_from_board = True
								self.selected_position = (x_adjusted,y_adjusted)
							else:
								#nothing to do
								pass
					else:
						#it is none means nothing is their so nothing to do
						pass
					
			

			else:
				#print("not_pressed")
				pass

	def selection_board_maintenance(self,x_cor,y_cor,situation):
		"""
		                                      clicked on selection_bar
		                                               |
		                               --------------------------------------------------------------------------
		                               |                                                                        |
		                              Yes                                                                       No
		                               |                                                                         |
		            selected from where or not selected                                                   is it his piece 
		                              |                                                                           |
		        ---------------------------------------------                                      -----------------------------
		        |                  |                        |                                      |                           | 
		      selection_bar       board               nothing selected                            yes                          no                     
		          \                |                  /                                            |                           |
				   \               |                 /                                         blit cover                nothing to do
                    \              |                /
				 	  (if clicked piece is his piece == True) else nothing to do 
				 	      and if its availability is their            
                        \        /                |
                         \      /                 |
                          \    /                  |
                           \  /                   |
                            \/                    |
                     change selection     select selection
		"""		
		for event in pygame.event.get():    
			if  event.type == pygame.QUIT:
				pygame.display.quit()
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				#print("mouse is pressed")
				#everything begins here
				x_adjusted,y_adjusted,who_is_clicked,piece = Helping_Class.convert_coordinate(x_cor,
																				  y_cor,
																				  'selection_bar')
				#print(who_is_clicked)
				if (self.selected_from_selection_bar + self.selected_from_board):
					#print("inside selected item one")
					if Helping_Class._check_if_clicked_on_his_own_piece_(self.whose_move,who_is_clicked):
						
						if self.pieces[piece].availability:
							self.selected_from_board = False
							self.selected_from_selection_bar = True

							#update 
							self.selected_piece = piece
							self.selected_position =Helping_Class.selection_bar_reverse_mapping[piece]
					else:
						#nothing to do
						pass
				else:
					#print("nothing is selected")
					#check if clicked on his piece change then select it
					if Helping_Class._check_if_clicked_on_his_own_piece_(self.whose_move,who_is_clicked):

						if self.pieces[piece].availability:
							self.selected_from_selection_bar = True

							#update 
							self.selected_piece = piece
							self.selected_position =(x_adjusted,y_adjusted)
							#print(self.selected_piece,self.selected_position,self.selected_from_selection_bar)

						
					else:
						#nothing to do
						pass
						
				
			else:
				#color change
				#who_is_clicked is dummy variable as no click has occurred
				x_adjusted,y_adjusted,who_is_clicked,piece = Helping_Class.convert_coordinate(x_cor,
																				  y_cor,
																				  'selection_bar')

				self.blit_piece = [(x_adjusted,y_adjusted),piece] 


	def rest_part_maintenance(self,x_cor,y_cor,situation):
		for event in pygame.event.get():    
			if  event.type == pygame.QUIT:
				pygame.display.quit()
				pygame.quit()
				quit()


	def _check_valid_position_(self,x_adjusted,y_adjusted):
		initial_coordinates = self.pieces[self.selected_piece].inital_position
		if (x_adjusted,y_adjusted) in initial_coordinates:
			if not self.game_state.board[Helping_Class.convert_my_coordinate_to_anirudh(x_adjusted,y_adjusted)]:
				#print('working')
			#if (x_adjusted,y_adjusted) not in self.occupied_position_on_board:
				return 1
			else:
				#print("not working")
				return 0
		else:
			return 0
		

	def place_piece_on_board_from_selection_bar(self,x_adjusted,y_adjusted):
		#self.screen.blit(self.pieces[self.selected_piece].image,(x_adjusted,y_adjusted))
		
		#self.board_positions[int(y_adjusted/80)][int(x_adjusted/80)] = self.selected_piece
		#self.occupied_position_on_board.append((x_adjusted,y_adjusted))
		
		#updating variables
		self.pieces[self.selected_piece].availability -=1
		#self.pieces[self.selected_piece].placed = True
		######self.pieces[self.selected_piece].current_position.append((x_adjusted,y_adjusted))
		
		self.selected_from_selection_bar = False
		
		'''
		#self.selected_piece = None
		this is updated after updating rajan function
		'''
		##############################3
		#self.selected_position = None
		##############################3
		if self.whose_move == 'white':
			self.whose_move = 'black'
		else:
			self.whose_move = 'white'

	def _check_valid_move_(self,x_adjusted,y_adjusted):
		fen_prev = self.game_state.generate_fen()
		#print(fen_prev)
		data_convert = CP.Conversion_of_postion_name(self.selected_piece,self.selected_position ,(x_adjusted,y_adjusted))
		board = chess.Board(fen = fen_prev)
		
		legal_moves_ = str(board.legal_moves)

		move = legal_moves_.split('(')
		move = move[1].split(')')
		move = move[0]
		move = move.split(',')
		for i in range(len(move)):
			move[i] = move[i].strip()
		#print(move)
		_move_ = CP.pgn(move,data_convert)
		
		
		#CP.Conversion_of_postion_name(self.selected_piece, self.selected_position ,(x_adjusted,y_adjusted))
		
		if _move_:
			#place the piece
			self.game_state.update(data_convert.piece, int(data_convert.i_pos_ani()), int(data_convert.f_pos_ani()))
			return _move_
		else:

			#maa choudau -> do nothing
			return None

	def capture_piece_update_board_or_place_piece(self,move,x_adjusted,y_adjusted):
		#if 'x' in move:
			#print('a capture has been made')
		#	captured_piece = self.game_state.board[Helping_Class.convert_my_coordinate_to_anirudh(x_adjusted,y_adjusted)]
		#self.board_positions[int(y_adjusted/80)][int(x_adjusted/80)] = self.selected_piece
		#print(self.selected_position)
		#print(self.occupied_position_on_board)
		#####print(self.pieces[self.selected_piece].current_position)
		#self.occupied_position_on_board.remove(self.selected_position)

		#self.occupied_position_on_board.append((x_adjusted,y_adjusted))
		"""
		if "x" in move:
			#not en pasant
			if self.game_state.board[Helping_Class.convert_my_coordinate_to_anirudh(x_adjusted,y_adjusted)]:
				self.occupied_position_on_board.remove((x_adjusted,y_adjusted))
			else:
				#it is en pasant
				self.occupied_position_on_board.remove((x_adjusted,self.selected_position[1]))
		"""
		#updating board state
		#print(self.board_positions[int(self.selected_position[1]/80)][int(self.selected_position[0]/80)])
		#self.board_positions[int(self.selected_position[1]/80)][int(self.selected_position[0]/80)] = None
		#print(self.board_positions[int(self.selected_position[1]/80)][int(self.selected_position[0]/80)])		
		self.selected_from_board = False
		
		#in classes updating current position
		######self.pieces[self.selected_piece].current_position.remove(self.selected_position)
		
		#update 
		self.selected_piece = None
		#if 'x' in move:
			###self.pieces[captured_piece].current_position.remove((x_adjusted,y_adjusted))
			#self.occupied_position_on_board.append((x_adjusted,y_adjusted))
		#	pass
		#updating variables
		self.selected_position =None
		if self.whose_move == 'white':
			self.whose_move = 'black'
		elif self.whose_move == 'black':
			self.whose_move = 'white'


	def get_board_state(self):
		fen = self.game_state.generate_fen()

		board = chess.Board(fen = fen)
		#when check is their
		if board.is_check():
			#print('1')
			if board.is_checkmate():
				#print('2')
				checkmate = 'checkmate'
				if self.whose_move =='white':
					piece_list =['WRook','WQueen','WKnight','WBishop','WPawn']
				else:
					piece_list = ['BRook','BQueen','BKnight','BBishop','BPawn']
				for piece in piece_list:
					if self.pieces[piece].availability:
						for position in self.pieces[piece].inital_position:
							

							if not self.game_state.board[Helping_Class.convert_my_coordinate_to_anirudh(position[0],position[1])]:
								print('piece',piece,' at position :',position)
								temp_game_state = CP.game_data()
								temp_game_state = copy.deepcopy(self.game_state)
								data_convert = CP.Conversion_of_postion_name(piece,Helping_Class.selection_bar_reverse_mapping[piece] ,(position[0],position[1]))
								temp_game_state.update(data_convert.piece, int(data_convert.i_pos_ani()), int(data_convert.f_pos_ani()))
								temp_game_state.active_color = not temp_game_state.active_color
								fen = temp_game_state.generate_fen()
								board2  = chess.Board(fen=fen)
								#print(board2)
								#print(board2.is_check())
								if not board2.is_check():
									checkmate = 'pseudo_check'
									return checkmate
							
				return checkmate

			else:
				#normal check
				return 'check'
		else:
			#normal game
			return 'normal'
		

##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################


class Helping_Class(object):
	"""docstring for Helping_Class"""

	
	selection_bar_mapping = {
					 (700,150):"BKing" ,(800,150):"BQueen" ,(900,150):"BRook" ,
					 (700,250):"BBishop" ,(800,250):"BKnight" ,(900,250):"BPawn" ,
					 (700,400):"WKing" ,(800,400):"WQueen" ,(900,400):"WRook" ,
					 (700,500):"WBishop" ,(800,500):"WKnight" ,(900,500):"WPawn" }

	selection_bar_reverse_mapping = {
					 "BKing":(700,150) ,"BQueen":(800,150) ,"BRook":(900,150) ,
					 "BBishop":(700,250) ,"BKnight":(800,250) ,"BPawn":(900,250) ,
					 "WKing":(700,400) ,"WQueen":(800,400) ,"WRook":(900,400) ,
					 "WBishop":(700,500) ,"WKnight":(800,500) ,"WPawn":(900,500) }
	
	def check_mouse_position():
		mouse = pygame.mouse.get_pos()
		_x_,_y_ = mouse[0],mouse[1]

		if _x_ <=640 and _y_ <=640:
			return _x_,_y_,'main_board' 

		elif  (    ((700<=_x_<=760)  & (150<=_y_<=210))
			    or ((800<=_x_<=860)  & (150<=_y_<=210))
			    or ((900<=_x_<=960)  & (150<=_y_<=210))
			    or ((700<=_x_<=760)  & (250<=_y_<=310))
			    or ((800<=_x_<=860)  & (250<=_y_<=310))
			    or ((900<=_x_<=960)  & (250<=_y_<=310))
			    or ((700<=_x_<=760)  & (400<=_y_<=460))
			    or ((800<=_x_<=860)  & (400<=_y_<=460))
			    or ((900<=_x_<=960)  & (400<=_y_<=460))
			    or ((700<=_x_<=760)  & (500<=_y_<=560))
			    or ((800<=_x_<=860)  & (500<=_y_<=560))
			    or ((900<=_x_<=960)  & (500<=_y_<=560))	):
			return _x_,_y_,'selection_board'

		else:
			return _x_,_y_,None

	"""		
	This fucntion return 2 values if its from board
	else:
		it returns 3 values (x_adjusted,y_adjusted,white or black)
	"""
	def convert_coordinate(x_cor,y_cor,from_where):
		#from_where is where click has been made
		if from_where == 'selection_bar':
			position_ = [(700,150),(800,150),(900,150),
				    	 (700,250),(800,250),(900,250),
				    	 (700,400),(800,400),(900,400),
				    	 (700,500),(800,500),(900,500)]
			_pieces__ = ['BKing','BQueen','BRook',
						 'BBishop','BKnight','BPawn',
						 'WKing','WQueen','WRook',
						 'WBishop','WKnight','WPawn',]
			x_adjusted,y_adjusted,where_clicked,piece = None,None,None,None
			
			if int(x_cor) in range(700,761):
				x_adjusted = 700
			elif int(x_cor) in range(800,861):
				x_adjusted = 800
			elif int(x_cor) in range(900,961):
				x_adjusted = 900

			if int(y_cor) in range(150,211):
				y_adjusted = 150
			elif int(y_cor) in range(250,311):
				y_adjusted = 250
			elif int(y_cor) in range(400,461):
				y_adjusted = 400
			elif int(y_cor) in range(500,561):
				y_adjusted = 500

			for index, item in enumerate(position_):
				if item == (x_adjusted,y_adjusted):
					piece = _pieces__[index]
					if index in range(0,6):
						where_clicked = 'black'
					elif index in range(6,12):
						where_clicked = 'white'

			return x_adjusted,y_adjusted,where_clicked,piece

		elif from_where == 'board':
			x = int(x_cor/80) * 80
			y = int(y_cor/80) * 80
			return x,y	

	def _check_if_clicked_on_his_own_piece_(whose_move,who_is_clicked):
		
		if whose_move == who_is_clicked:
			return True 
		else:
			return False

	def printing(board_positions):
		for i in range(8):
			line = []
			for j in range(8):
				if board_positions[i*8+j]:
					line.append(board_positions[i*8+j])
				else:
					line.append('*')
			print(line)

	def convert_my_coordinate_to_anirudh(x_adjusted,y_adjusted):
		x_adjusted = int(x_adjusted/80)
		y_adjusted = int(y_adjusted/80)
		return y_adjusted*8 + x_adjusted	