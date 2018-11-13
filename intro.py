import pygame



#            R   G    B
WHITE    = (255, 255, 255)
black    = (0,    0,   0)
green    = (0,180,0)
red     = (180,0,0)
bright_green =(0,255,0)
bright_red = (255,0,0)
grey = (100,100,100)
dark_grey = (200,200,200)
blue = (0,0,255)

clock = pygame.time.Clock()


def text_objects(screen,text,font,color=black):
	#true is for anti-aliasling
	textsurface = font.render(text,True,color)
	return textsurface,textsurface.get_rect()

def display_text(screen,text,x,y,font_size = 25,color=black, align_left=False):
	
	largeText = pygame.font.SysFont("comicsansms",font_size)
	TextSurf, TextRect = text_objects(screen,text, largeText,color)
	if align_left:
		TextRect[0] = x
		TextRect[1] = y
	else:
		TextRect.center = (x,y)
	screen.blit(TextSurf, TextRect)

def button(screen,msg,x,y,w,h,ic,ac,action = None):
	mouse = pygame.mouse.get_pos()
	#print(mouse)
	click = pygame.mouse.get_pressed()
	#print(click)
	if x+w > mouse[0] > x and y+h>mouse[1]>y:
		pygame.draw.rect(screen,ac,(x,y,w,h))
		if click[0]==1 and action != None:
			#this works as will documented part
			
			if action == "computer_play":
				return 'computer'
			elif action == "2player":
				return 'player'
			elif action == 'Ordinary':
				Rules_for_ordinary_chess(screen)
			elif action == 'ChessZero':
				ChessZero_rules(screen)	
			elif action == 'Home':
				return 'home'
				#Home(screen)
			elif action == 'Basic_moves':
				Basic_moves(screen)
			elif action == 'Castling':
				Castling(screen)
			elif action == 'En passant':
				En_passant(screen)
			
			elif action =='Pawn_Promotion':
				Pawn_Promotion(screen)
			elif action =='Check':
				Check(screen) 
			elif action == 'Checkmate':
				Checkmate(screen)
			elif action == "quitgame":
				pygame.quit()
				quit()
			

	else:
		pygame.draw.rect(screen,ic,(x,y,w,h))

	smalltext = pygame.font.SysFont("comicsansms",20)
	TextSurf,TextRect = text_objects(screen,msg,smalltext)
	TextRect.center = ( (x+(w/2)),(y+(h/2)) )
	screen.blit(TextSurf,TextRect)


def Basic_moves(screen):
	y = 0 
	y_change = 0
	while True:
		screen.fill(WHITE)
		#intro.Home(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					y_change = +20
				if event.key == pygame.K_DOWN:
					y_change = -20

			if event.type == pygame.KEYUP:
				if (event.key  == pygame.K_UP or 
					event.key == pygame.K_DOWN):
					y_change = 0		
	
		y += y_change
		if y>0:
			y =0
		elif y<1450:
			y = max(y,-1200)
		
		display_text(screen,'ChessZero',500,50+y,50,red)

		#king
		msg = 'King'
		display_text(screen,msg,75,100+y,20,bright_red)
		msg = '-> The king moves exactly one square horizontally, vertically, or diagonally.'
		display_text(screen,msg,350,125+y,15,black)
		msg = 'A special move with the king known as castling is allowed only once per player, per game'
		display_text(screen,msg,400,150+y,15,black)

		image_ = pygame.image.load('instructions image/king_move.png')
		screen.blit(image_,(750,100+y))

		#Queen
		msg = 'Queen'
		display_text(screen,msg,75,350+y,20,bright_red)
		msg = '-> The queen moves any number of vacant squares in a horizontal, vertical, or diagonal direction.'
		display_text(screen,msg,400,375+y,15,black)
		
		image_ = pygame.image.load('instructions image/queen_move.png')
		screen.blit(image_,(750,350+y))

		#Rook(gap of 250 in y)
		msg = 'Rook'
		display_text(screen,msg,75,600+y,20,bright_red)
		msg = '-> A rook moves any number of vacant squares in a horizontal or vertical direction.'
		display_text(screen,msg,350,625+y,15,black)
		msg = ' It also is moved when castling.'
		display_text(screen,msg,200,650+y,15,black)
		image_ = pygame.image.load('instructions image/rook_move.png')
		screen.blit(image_,(750,600+y))

		#Bishop(gap of 250 in y)
		msg = 'Bishop'
		display_text(screen,msg,75,850+y,20,bright_red)
		msg = '->A bishop moves any number of vacant squares in any diagonal direction.'
		display_text(screen,msg,320,875+y,15,black)
		image_ = pygame.image.load('instructions image/bishop_move.png')
		screen.blit(image_,(750,850+y))

		#Knight(gap of 250 in y)
		msg = 'Knight'
		display_text(screen,msg,75,1100+y,20,bright_red)
		msg = '->A knight moves to the nearest square not on the same rank, file, or diagonal.'
		display_text(screen,msg,320,1125+y,15,black)
		msg = 'This can be thought of as moving two squares horizontally then one square '
		display_text(screen,msg,320,1150+y,15,black)
		msg = 'vertically, or moving one square horizontally then two squares vertically—i.e. in an "L" pattern.'
		display_text(screen,msg,390,1175+y,15,black)
		msg = 'The knight is not blocked by other pieces: it jumps to the new location.'
		display_text(screen,msg,320,1200+y,15,black)
		image_ = pygame.image.load('instructions image/knight_move.png')
		screen.blit(image_,(750,1100+y))

		#Pawn(gap of 250 in y)
		msg = 'Pawn'
		display_text(screen,msg,75,1450+y,20,bright_red)
		msg = '->Pawns have the most complex rules of movement:'
		display_text(screen,msg,300,1475+y,15,black)
		msg = '1. A pawn moves straight forward one square, if that square is vacant.'
		display_text(screen,msg,300,1500+y,15,black)
		msg = 'If it has not yet moved, a pawn also has the option of moving two '
		display_text(screen,msg,300,1525+y,15,black)
		msg = 'squares straight forward, provided both squares are vacant. Pawns cannot move backwards.'
		display_text(screen,msg,375,1550+y,15,black)
		msg = '2. Pawns are the only pieces that capture differently from how they move.'
		display_text(screen,msg,300,1575+y,15,black)
		msg = 'A pawn can capture an enemy piece on either of the two squares '
		display_text(screen,msg,300,1600+y,15,black)
		msg = 'diagonally in front of the pawn (but cannot move to those squares if they are vacant).'
		display_text(screen,msg,375,1625+y,15,black)
		msg = 'The pawn is also involved in the two special moves en passant and promotion'
		display_text(screen,msg,350,1650+y,15,red)
		image_ = pygame.image.load('instructions image/pawn_move.png')
		screen.blit(image_,(750,1450+y))



		display_text(screen,'Use arrow keys to navigate',500,650,20,red)
		
		msg = 'Home'
		message = button(screen,msg,150,600,100,50,grey,dark_grey,action = "Home")
		if message =='home':
			return
		msg = 'QUIT'
		button(screen,msg,800,600,75,50,red,bright_red,"quitgame")

		pygame.display.update() #or use pygame.display.flip()
		clock.tick(120)

def Castling(screen):
	y = 0 
	y_change = 0
	while True:
		screen.fill(WHITE)
		#intro.Home(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		display_text(screen,'ChessZero',500,50+y,50,red)

		#Pawn(gap of 250 in y)
		msg = 'Castling'
		display_text(screen,msg,75,100+y,20,bright_red)
		msg = '->Castling consists of moving the king two squares towards a rook,'
		display_text(screen,msg,300,125+y,15,black)
		msg = 'then placing the rook on the other side of the king, adjacent to it.'
		display_text(screen,msg,300,150+y,15,black)
		msg = 'Castling is only permissible if all of the following conditions hold:'
		display_text(screen,msg,310,175+y,20,red)
		msg = '1. The king and rook involved in castling must not have previously moved.'
		display_text(screen,msg,375,200+y,15,black)
		msg = '2. There must be no pieces between the king and the rook.'
		display_text(screen,msg,300,225+y,15,black)
		msg = '3. The king may not currently be in check, nor may the king '
		display_text(screen,msg,300,250+y,15,black)
		msg = 'pass through or end up in a square that is under attack by '
		display_text(screen,msg,300,275+y,15,black)
		msg = 'an enemy piece (though the rook is permitted to be under attack and to pass over an attacked square)'
		display_text(screen,msg,375,300+y,15,black)
		msg = '4. The king and the rook must be on the same rank (Schiller 2003:19)'
		display_text(screen,msg,375,325+y,15,black)
		image_ = pygame.image.load('instructions image/before_castling.png')
		screen.blit(image_,(50,350+y))
		image_ = pygame.image.load('instructions image/after_castling.png')
		screen.blit(image_,(400,350+y))



		
		msg = 'Home'
		message  =button(screen,msg,150,600,100,50,grey,dark_grey,action = "Home")
		if message =='home':
			return
		msg = 'QUIT'
		button(screen,msg,800,600,75,50,red,bright_red,"quitgame")

		pygame.display.update() #or use pygame.display.flip()
		clock.tick(60)

def En_passant(screen):
	y = 0 
	y_change = 0
	while True:
		screen.fill(WHITE)
		#intro.Home(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		display_text(screen,'ChessZero',500,50+y,50,red)

		#Pawn(gap of 250 in y)
		msg = 'En passant'
		display_text(screen,msg,75,100+y,20,bright_red)
		msg = '->When a pawn advances two squares from its original square and ends the turn adjacent'
		display_text(screen,msg,320,125+y,15,black)
		msg = "to a pawn of the opponent's on the same rank, it may be captured by that pawn of the"
		display_text(screen,msg,320,150+y,15,black)
		msg = "opponent's, as if it had moved only one square forward. This capture is only legal on the opponent's"
		display_text(screen,msg,360,175+y,15,black)
		msg = "next move immediately following the first pawn's advance. The diagrams on the right"
		display_text(screen,msg,320,200+y,15,black)
		msg = 'demonstrate an instance of this: if the white pawn moves from a2 to a4, the'
		display_text(screen,msg,320,225+y,15,black)
		msg = 'black pawn on b4 can capture it en passant, moving from b4 to a3 while the white'
		display_text(screen,msg,320,250+y,15,black)
		msg = 'pawn on a4 is removed from the board.'
		display_text(screen,msg,320,275+y,15,black)
		image_ = pygame.image.load('instructions image/en_passant.png')
		screen.blit(image_,(400,325+y))
		


		
		msg = 'Home'
		message =button(screen,msg,150,600,100,50,grey,dark_grey,action = "Home")
		if message =='home':
			return
		msg = 'QUIT'
		button(screen,msg,800,600,75,50,red,bright_red,"quitgame")

		pygame.display.update() #or use pygame.display.flip()
		clock.tick(60)

def Pawn_Promotion(screen):
	y = 0 
	y_change = 0
	while True:
		screen.fill(WHITE)
		#intro.Home(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		display_text(screen,'ChessZero',500,50+y,50,red)

		#Pawn(gap of 250 in y)
		msg = 'Pawn Promotion'
		display_text(screen,msg,75,100+y,20,bright_red)
		msg = '->If a player advances a pawn to its eighth rank, the pawn is then promoted (converted)'
		display_text(screen,msg,320,125+y,15,black)
		msg = "to a queen, rook, bishop, or knight of the same color at the choice of the player (a queen is usually chosen)."
		display_text(screen,msg,380,150+y,15,black)
		msg = "The choice is not limited to previously captured pieces. Hence it is theoretically possible for a player to"
		display_text(screen,msg,380,175+y,15,black)
		msg = "have up to nine queens or up to ten rooks, bishops, or knights if all of their"
		display_text(screen,msg,320,200+y,15,black)
		msg = 'pawns are promoted. If the desired piece is not available, the player '
		display_text(screen,msg,320,225+y,15,black)
		msg = 'should call the arbiter to provide the piece (Schiller 2003:17–19).'
		display_text(screen,msg,320,250+y,15,black)
		


		
		msg = 'Home'
		message = button(screen,msg,150,600,100,50,grey,dark_grey,action = "Home")
		if message =='home':
			return
		msg = 'QUIT'
		button(screen,msg,800,600,75,50,red,bright_red,"quitgame")

		pygame.display.update() #or use pygame.display.flip()
		clock.tick(60)

def Check(screen):
	y = 0 
	y_change = 0
	while True:
		screen.fill(WHITE)
		#intro.Home(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		display_text(screen,'ChessZero',500,50+y,50,red)

		#Pawn(gap of 250 in y)
		msg = 'Check'
		display_text(screen,msg,75,100+y,20,bright_red)
		msg = '->A king is in check when it is under attack by at least one enemy piece. A piece unable to '
		display_text(screen,msg,360,125+y,15,black)
		msg = "move because it would place its own king in check (it is pinned against its own king) may still deliver check to the opposing player."
		display_text(screen,msg,480,150+y,15,black)
		msg = "It is illegal to make a move that places or leaves one's king in check. The possible ways to get out of check are:"
		display_text(screen,msg,400,175+y,15,red)
		msg = "1. Move the king to a square where it is not in check."
		display_text(screen,msg,220,200+y,15,black)
		msg = '2. Capture the checking piece (possibly with the king).'
		display_text(screen,msg,220,225+y,15,black)
		msg = "3. Block the check by placing a piece between the king and the opponent's threatening piece"
		display_text(screen,msg,350,250+y,15,black)
		image_ = pygame.image.load('instructions image/check.png')
		screen.blit(image_,(400,325+y))
		


		
		msg = 'Home'
		message =button(screen,msg,150,600,100,50,grey,dark_grey,action = "Home")
		if message =='home':
			return
		msg = 'QUIT'
		button(screen,msg,800,600,75,50,red,bright_red,"quitgame")

		pygame.display.update() #or use pygame.display.flip()
		clock.tick(60)

def Checkmate(screen):
	y = 0 
	y_change = 0
	while True:
		screen.fill(WHITE)
		#intro.Home(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		display_text(screen,'ChessZero',500,50+y,50,red)

		#Pawn(gap of 250 in y)
		msg = 'Checkmate'
		display_text(screen,msg,75,100+y,20,bright_red)
		msg = "->If a player's king is placed in check and there is no legal move that player can make to "
		display_text(screen,msg,360,125+y,15,black)
		msg = "escape check, then the king is said to be checkmated, the game ends, and that player loses."
		display_text(screen,msg,360,150+y,15,black)
		msg = "Unlike other pieces, the king is never actually captured or removed from the board because  "
		display_text(screen,msg,400,175+y,15,black)
		msg = "checkmate ends the game."
		display_text(screen,msg,150,200+y,15,black)
		image_ = pygame.image.load('instructions image/checkmate.png')
		screen.blit(image_,(400,325+y))
		


		
		msg = 'Home'
		message =button(screen,msg,150,600,100,50,grey,dark_grey,action = "Home")
		if message =='home':
			return
		msg = 'QUIT'
		button(screen,msg,800,600,75,50,red,bright_red,"quitgame")

		pygame.display.update() #or use pygame.display.flip()
		clock.tick(60)



def Rules_for_ordinary_chess(screen):
	

	while True:
		screen.fill(WHITE)
		#intro.Home(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
	
		
		display_text(screen,'ChessZero',500,50,50,red)
		msg = 'Basic moves'
		button(screen,msg,200,250,150,50,green,bright_green,action = "Basic_moves")

		msg = 'Castling'
		button(screen,msg,200,325,150,50,green,bright_green,action = "Castling")
				
		msg = 'En passant'
		button(screen,msg,200,400,150,50,green,bright_green,action = "En passant")
		
		msg = 'Pawn Promotion'
		button(screen,msg,700,250,150,50,green,bright_green,action = "Pawn_Promotion")
	
		msg = 'Check'
		button(screen,msg,700,325,150,50,green,bright_green,action = "Check")

		msg = 'Checkmate'
		button(screen,msg,700,400,150,50,green,bright_green,action = "Checkmate")

		msg = 'Home'
		message =button(screen,msg,150,600,100,50,grey,dark_grey,action = "Home")
		if message =='home':
			return
		msg = 'QUIT'
		button(screen,msg,850,600,75,50,red,bright_red,"quitgame")

		pygame.display.update() #or use pygame.display.flip()
		clock.tick(60)

def ChessZero_rules(screen):
	y = 0 
	y_change = 0
	while True:
		screen.fill(WHITE)
		#intro.Home(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					y_change = +20
				if event.key == pygame.K_DOWN:
					y_change = -20

			if event.type == pygame.KEYUP:
				if (event.key  == pygame.K_UP or 
					event.key == pygame.K_DOWN):
					y_change = 0	

			#if event.type == pygame.MOUSEBUTTONDOWN:
			#	if event.button == 4:
			#		y_change = +20
			#	if event.button == 5:
			#		y_change = -20	
	
		y += y_change
		if y>0:
			y =0
		elif y<1450:
			y = max(y,-950)
		
		h0 = 100
		display_text(screen,'About ChessZero',500,50+y,50,red)
		msg = 'Rules'
		display_text(screen,msg,60,h0+y,20,bright_red, True)
		msg = 'This is the most realistic and ultimate version of chess which you can think of!!!. Initially there are'
		display_text(screen,msg,60,h0+40+y,15,black, True)
		msg = 'only kings on the board to protect their kingdom. But now with the commencement of war, both'
		display_text(screen,msg,60,h0+65+y,15,black, True)
		msg = 'king will exercise their powers in the boundation of some rules. '
		display_text(screen,msg,60,h0+90+y,15,black, True)
		msg = '•••  The King can either command the pieces on board to move or he/she can bring new soldiers'
		display_text(screen,msg,60,h0+130+y,15,black, True)
		msg = '       from the'
		display_text(screen,msg,60,h0+155+y,15,black, True)
		msg = 'barrack'
		display_text(screen,msg,155,h0+155+y,15,green, True)
		msg = 'and the last resort for him is to move himself.'
		display_text(screen,msg,215,h0+155+y,15,black, True)
		msg = '•••  In this game, you can block check/checkmate by blocking the attacker with your piece from'
		display_text(screen,msg,60,h0+180+y,15,black, True)
		msg = '       barrack'
		display_text(screen,msg,60,h0+205+y,15,green, True)
		msg = '•••  Other rules are same as of Standard Chess'
		display_text(screen,msg,60,h0+230+y,15,black, True)


		h1 = 400
		display_text(screen, 'Barrack', 60, h1+y, 20, bright_red,True)
		msg = 'Barrack is a place which provides accomodation for soldiers (pieces in our game). They can be'
		display_text(screen, msg, 60, h1+40+y, 15, black, True)
		msg = 'activated by their king to some specific'
		display_text(screen,msg,60,h1+65+y, 15, black, True)
		msg = 'birth points'
		display_text(screen, msg, 340, h1+65+y,15, green, True)

		h2 = 535
		display_text(screen, 'Birth Squares', 60, h2+y, 20, bright_red, True)
		msg = 'These are specific squares for a particular piece being called from barrack to be placed on.'
		display_text(screen,msg,60,h2+40+y, 15, black,True)
		msg = '•••  Rook : a/h file    White : 1 rank    Black : 8 rank'
		display_text(screen,msg,60,h2+65+y, 15, black,True)
		msg = '•••  Knight : b/g file    White : 1 rank    Black : 8 rank'
		display_text(screen,msg,60,h2+90+y, 15, black,True)
		msg = '•••  Bishop : c/f file    White : 1 rank    Black : 8 rank'
		display_text(screen,msg,60,h2+115+y, 15, black,True)
		msg = '•••  Queen : d file    White : 1 rank    Black : 8 rank'
		display_text(screen,msg,60,h2+140+y, 15, black,True)
		msg = '•••  Pawn : any file    White : 2 rank    Black : 7 rank'
		display_text(screen,msg,60,h2+165+y, 15, black,True)
		msg = 'A piece can born on a single square of possible birth squares multiple times as long as it is vacant.'
		display_text(screen,msg,60,h2+190+y, 15, black,True)

		h3 = 795
		msg = 'Life'
		display_text(screen, msg, 60, h3+y, 20, bright_red, True)
		msg = 'It denotes the number of times a particular piece can be born on board'
		display_text(screen, msg, 60, h3+40+y, 15, black, True)
		msg = '•••  Rook : 2'
		display_text(screen, msg, 60, h3+65+y, 15, black, True)
		msg = '•••  Knight : 2'
		display_text(screen, msg, 60, h3+90+y, 15, black, True)
		msg = '•••  Bishop : 2'
		display_text(screen, msg, 60, h3+115+y, 15, black, True)
		msg = '•••  Queen : 1'
		display_text(screen, msg, 60, h3+140+y, 15, black,True)
		msg = '•••  Pawn : 8'
		display_text(screen, msg, 60, h3+165+y, 15, black, True)

		h4 = 1060
		msg = 'About ChessZero'
		display_text(screen, msg, 60, h4+y, 25, blue, True)
		msg = 'ChessZero is an amazing variant of chess developed by Team ARP. Standard Chess features two main strategy of chess namely'
		display_text(screen, msg, 60, h4+50+y, 15, black, True)
		msg = 'Attack'
		display_text(screen,msg,60,h4+75+y,15, green, True)
		msg = 'and'
		display_text(screen,msg,115,h4+75+y,15, black, True)
		msg = 'Development'
		display_text(screen,msg,145,h4+75+y,15, green, True)
		msg = "•••  Attack : When a king aggresively orders a piece to move in a way to attack the enemy's army straightaway"
		display_text(screen, msg, 60, h4+100+y, 15, black, True)
		msg = '•••  Development : When a king improves the position of a piece on board such that it will attack enemy afterwards'
		display_text(screen,msg,60,h4+125+y,15, black, True)
		msg = 'Usually in Standard Chess, Attack & Development are inter-related. You don\'t have to think much of what type of move you should play.'
		display_text(screen,msg,60,h4+150+y,15, black, True)
		msg = 'But in'
		display_text(screen,msg,60,h4+175+y,15, black, True)
		msg = 'ChessZero'
		display_text(screen,msg,107,h4+175+y,15, red, True)
		msg = ', Development is entirely different from Attack. The Birth of pieces from barrack to the board gives the additional'
		display_text(screen,msg,180,h4+175+y,15, black, True)
		msg = 'development chances. This makes it very difficult for player to think which type of move he/she should play.'
		display_text(screen, msg, 60, h4+200+y,15, black, True)
		msg = 'We hope you will enjoy playing this innovative variant of chess :)'
		display_text(screen, msg, 60, h4+260+y, 20, black, True)




		display_text(screen,'Use arrow keys to navigate',500,650,20,red)
		
		msg = 'Home'
		message = button(screen,msg,150,600,100,50,grey,dark_grey,action = "Home")
		if message =='home':
			return
		msg = 'QUIT'
		button(screen,msg,800,600,75,50,red,bright_red,"quitgame")

		pygame.display.update() #or use pygame.display.flip()
		clock.tick(120)

def Home(screen):
	

	while True:
		screen.fill(WHITE)
		#intro.Home(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
	
		
		display_text(screen,'ChessZero',500,50,50,red)
		
		msg = 'TWO PLAYER!!!'
		temp1 = button(screen,msg,350,200,300,50,green,bright_green,action = "2player")
		
		msg = 'PLAY AGAINST COMPUTER'
		temp2 = button(screen,msg,350,300,300,50,green,bright_green,action = "computer_play")

		#temp1 = player temp2 = computer
		if temp1:
			return temp1
		elif temp2:
			return temp2

		msg = 'Rules specific to ChessZero'
		button(screen,msg,350,400,300,50,green,bright_green,action = "ChessZero")
		msg = 'Rules of Ordinary Chess'
		button(screen,msg,350,500,300,50,green,bright_green,action = "Ordinary")
		
		msg = 'QUIT'
		button(screen,msg,460,600,75,50,red,bright_red,"quitgame")

		pygame.display.update() #or use pygame.display.flip()
		clock.tick(60)

def who_won(screen,who_lost):
	

	if who_lost =='white':
		text_  = 'BLACK WINS'
	else:
		text_  = 'WHITE WINS'

	while True:
		screen.fill(WHITE)
		#intro.Home(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
	
		
		display_text(screen,'ChessZero',500,50,50,red)
		
		display_text(screen,text_ ,500,250,100,bright_red)
		
		
		
		msg = 'Home'
		
		message = button(screen,msg,150,600,100,50,grey,dark_grey,action = "Home")
		if message =='home':
			return

		msg = 'QUIT'
		button(screen,msg,800,600,75,50,red,bright_red,"quitgame")

		pygame.display.update() #or use pygame.display.flip()
		clock.tick(60)
