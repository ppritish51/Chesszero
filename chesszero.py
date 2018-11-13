import pygame
import computer_board 
import player_board
import intro
import time
import win32gui, win32con

pygame.init()

infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w,infoObject.current_h), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

pygame.display.set_caption('ChessZero')




#            R   G    B
WHITE    = (255, 255, 255)
black    = (0,    0,   0)
green    = (0,180,0)
red     = (180,0,0)
bright_green =(0,255,0)
bright_red = (255,0,0)

clock = pygame.time.Clock()

#tuple ()

def play_against_computer(screen):
	screen.fill(WHITE)
	background = pygame.image.load('background.png')
	screen.blit(background,(0,0))
	
	BOARD = computer_board.DISPLAY(screen)

	while True:

		
		BOARD.display_everything()
		board_state = BOARD.get_board_state()
		print('board_state : ',board_state)
		
		x,y,board_part = computer_board.Helping_Class.check_mouse_position()
		#blit cover process
		if BOARD.blit_piece :
			if (not x in range(int(BOARD.blit_piece[0][0]),int(BOARD.blit_piece[0][0])+61)) : 
				BOARD.blit_piece = []
			elif (not y in range(int(BOARD.blit_piece[0][1]),int(BOARD.blit_piece[0][1])+61)):
				BOARD.blit_piece = []
			if BOARD.blit_piece:
				if BOARD.whose_move == 'black':
					if (BOARD.blit_piece[0][0],BOARD.blit_piece[0][1]) in [(700,400),(800,400),(900,400),(700,500),(800,500),(900,500)]:
						BOARD.blit_piece = []
				else:
					if (BOARD.blit_piece[0][0],BOARD.blit_piece[0][1]) in [(700,150),(800,150),(900,150),(700,250),(800,250),(900,250)]:
						BOARD.blit_piece = []
		#print(board_part)
		BOARD.display_selection_bar()
		#Board display pieces on board at places
		################### to make ################
		#Board.display_pieces()
		

		if not BOARD.computer_turn:

			if board_part == 'main_board':
				BOARD.main_board_maintenance(x,y)
			elif board_part == 'selection_board':
				BOARD.selection_board_maintenance(x,y)
			else:
				_temp_ = BOARD.rest_part_maintenance(x,y)
				if _temp_ =='exit':
					return
		else:
			_temp_ = BOARD.rest_part_maintenance(x,y)
			if _temp_ =='exit':
				return
			BOARD.computer_move()

		if board_state=='checkmate':
			time.sleep(3)
			return BOARD.whose_move

			#print(event)

		pygame.display.update() #or use pygame.display.flip()
		clock.tick(60)

def player_versus_player(screen):
	screen.fill(WHITE)
	background = pygame.image.load('background.png')
	screen.blit(background,(0,0))
	
	BOARD = player_board.DISPLAY(screen)

	while True:

			

		BOARD.display_everything()
		
		board_state = BOARD.get_board_state()
		print('board_state : ',board_state)

		x,y,board_part = player_board.Helping_Class.check_mouse_position()
		#blit cover process
		if BOARD.blit_piece :
			if (not x in range(int(BOARD.blit_piece[0][0]),int(BOARD.blit_piece[0][0])+61)) : 
				BOARD.blit_piece = []
			elif (not y in range(int(BOARD.blit_piece[0][1]),int(BOARD.blit_piece[0][1])+61)):
				BOARD.blit_piece = []
			if BOARD.blit_piece:
				if BOARD.whose_move == 'black':
					if (BOARD.blit_piece[0][0],BOARD.blit_piece[0][1]) in [(700,400),(800,400),(900,400),(700,500),(800,500),(900,500)]:
						BOARD.blit_piece = []
				else:
					if (BOARD.blit_piece[0][0],BOARD.blit_piece[0][1]) in [(700,150),(800,150),(900,150),(700,250),(800,250),(900,250)]:
						BOARD.blit_piece = []
		#print(board_part)
		BOARD.display_selection_bar()
		#Board display pieces on board at places
		################### to make ################
		#Board.display_pieces()
		
		if board_part == 'main_board':
			BOARD.main_board_maintenance(x,y,situation = board_state)
		elif board_part == 'selection_board':
			BOARD.selection_board_maintenance(x,y,situation = board_state)
		else:
			_temp_ = BOARD.rest_part_maintenance(x,y,situation = board_state)
			if _temp_ =='exit':
				return
	
		if board_state=='checkmate':
			time.sleep(3)
			return BOARD.whose_move
			#print(event)

		pygame.display.update() #or use pygame.display.flip()
		clock.tick(60)


def introduction(screen):

	while True:
		
		with_whom = intro.Home(screen)
		if with_whom=='computer':
			who_lost = play_against_computer(screen)	
		elif with_whom=='player':
			who_lost =player_versus_player(screen)
		
		intro.who_won(screen,who_lost)

		
introduction(screen)
   