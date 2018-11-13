import pygame


class BaseClass(pygame.sprite.Sprite):
	"""docstring for BaseClass"""
	def __init__(self):
		
		pygame.sprite.Sprite.__init__(self)
		self.moved = False
		self.placed = False		
		self.current_position = []




class WRook(BaseClass):
	"""docstring for WRook"""
	def __init__(self):	
		BaseClass.__init__(self)
		self.image = pygame.image.load('pieces/WRook.png')
		self.inital_position = [(0,560),(560,560)]
		self.availability = 2



	# def move(self):
	# 	pass


class WKnight(BaseClass):
	"""docstring for WKnight"""
	def __init__(self):	
		BaseClass.__init__(self)
		self.image = pygame.image.load('pieces/WKnight.png')
		self.inital_position = [(80,560),(480,560)]
		self.availability = 2
	# def move(self):
	# 	pass

class WBishop(BaseClass):
	"""docstring for WBishop"""
	def __init__(self):	
		BaseClass.__init__(self)
		self.image = pygame.image.load('pieces/WBishop.png')
		self.inital_position = [(160,560),(400,560)]
		self.availability = 2
	# def move(self):
	# 	pass


class WQueen(BaseClass):
	"""docstring for WQueen"""
	def __init__(self):	
		BaseClass.__init__(self)
		self.image = pygame.image.load('pieces/WQueen.png')
		self.inital_position = [(240,560)]
		self.availability = 1
	# def move(self):
	# 	pass

class WKing(BaseClass):
	"""docstring for WKing"""
	def __init__(self):	
		BaseClass.__init__(self)
		self.image = pygame.image.load('pieces/WKing.png')
		self.inital_position = [(320,560)]
		self.availability = 0

	# def move(self):
	# 	pass

class WPawn(BaseClass):
	"""docstring for WPawn"""
	def __init__(self):	
		BaseClass.__init__(self)
		self.image = pygame.image.load('pieces/WPawn.png')
		self.inital_position = [(0,480),(80,480),(160,480),(240,480),(320,480),(400,480),(480,480),(560,480)]
		self.availability = 8
	# def move(self):
	# 	pass




class BRook(BaseClass):
	"""docstring for BRook"""
	def __init__(self):	
		BaseClass.__init__(self)
		self.image = pygame.image.load('pieces/BRook.png')
		self.inital_position = [(0,0),(560,0)]
		self.availability = 2

	# def move(self):
	# 	pass

class BKnight(BaseClass):
	"""docstring for BKnight"""
	def __init__(self):	
		BaseClass.__init__(self)
		self.image = pygame.image.load('pieces/BKnight.png')
		self.inital_position = [(80,0),(480,0)]
		self.availability = 2

	# def move(self):
	# 	pass

class BBishop(BaseClass):
	"""docstring for WBishop"""
	def __init__(self):	
		BaseClass.__init__(self)
		self.image = pygame.image.load('pieces/BBishop.png')
		self.inital_position = [(160,0),(400,0)]
		self.availability = 2

	# def move(self):
	# 	pass


class BQueen(BaseClass):
	"""docstring for WQueen"""
	def __init__(self):	
		BaseClass.__init__(self)
		self.image = pygame.image.load('pieces/BQueen.png')
		self.inital_position = [(240,0)]
		self.availability = 1

	# def move(self):
	# 	pass

class BKing(BaseClass):
	"""docstring for WKing"""
	def __init__(self):	
		BaseClass.__init__(self)
		self.image = pygame.image.load('pieces/BKing.png')
		self.inital_position = [(320,0)]
		self.availability = 0

	# def move(self):
	# 	pass

class BPawn(BaseClass):
	"""docstring for WPawn"""
	def __init__(self):	
		BaseClass.__init__(self)
		self.image = pygame.image.load('pieces/BPawn.png')
		self.inital_position = [(0,80),(80,80),(160,80),(240,80),(320,80),(400,80),(480,80),(560,80)]
		self.availability = 8

	# def move(self):
	# 	pass

