import pygame
import os,sys,math

width = 830
height = 700

pygame.init()

background_color = pygame.Color(0,0,0)
font_color = pygame.Color(35,40,125)

display = pygame.display.set_mode((width,height))
pygame.display.set_caption('Pacman')
clock = pygame.time.Clock()


class BoardElement:
	
	def __init__(self, pos, length, width, image):
		self.pos = pos
		self.length = length
		self.image = image
		self.width = width
	
	def Draw(self,canvas):
		canvas.blit(self.image, self.pos)

class Pacman(BoardElement):
	
	def __init__(self, pos, length, width, image, direction):
		super().__init__(pos, length, width, image)
		self.direction = direction
	
	def Move(self, step):
		flag_x = 1
		flag_y = 1
		for bd in list(boundaries):
			if (bd.pos[0]<self.pos[0]+step[0]<bd.pos[0]+bd.length or bd.pos[0]<self.pos[0]+step[0]+self.length<bd.pos[0]+bd.length) and (bd.pos[1]<self.pos[1]<bd.pos[1]+bd.width):
				flag_x = 0
			if (bd.pos[1]<self.pos[1]+step[1]<bd.pos[1]+bd.width or bd.pos[1]<self.pos[1]+step[1]+self.length<bd.pos[1]+bd.width) and (bd.pos[0]<self.pos[0]<bd.pos[0]+bd.length):
				flag_y = 0
			if (bd.pos[1]<self.pos[1]<bd.pos[1]+bd.width) or (bd.pos[1]<self.pos[1]+self.length<bd.pos[1]+bd.width) or (self.pos[1]<=bd.pos[1] and self.pos[1]+self.length>=bd.pos[1]+bd.width):
				if (bd.pos[0]<self.pos[0]+step[0]<bd.pos[0]+bd.length or bd.pos[0]<self.pos[0]+self.length+step[0]<bd.pos[0]+bd.length):
					flag_x =0
			if (bd.pos[0]<self.pos[0]<bd.pos[0]+bd.length) or (bd.pos[0]<self.pos[0]+self.length<bd.pos[0]+bd.length) or (self.pos[0]<=bd.pos[0] and self.pos[0]+self.length>=bd.pos[0]+bd.length):
				if (bd.pos[1]<self.pos[1]+step[1]<bd.pos[1]+bd.width or bd.pos[1]<self.pos[1]+self.length+step[1]<bd.pos[1]+bd.width):
					flag_y =0
		if (self.direction == 'right' or self.direction == 'left') and flag_x == 1:
			self.pos[0] += step[0]
		elif flag_y == 1:
			self.pos[1] += step[1]
		if self.pos[0] >= width:
			self.pos[0] = 0
		if self.pos[0] <=- self.width:
			self.pos[0] = width
		for fd in list(foods):
			if (self.pos[0]<fd.pos[0]<self.pos[0]+self.width) and (self.pos[1]<fd.pos[1]<self.pos[1]+self.width):
				foods.remove(fd)
		if(len(foods)) == 0:
			GameOver("You win")
		flag = False
		for gh in list(ghosts):
			dist = math.sqrt(((gh.pos[0]-self.pos[0])**2) + ((gh.pos[1]-self.pos[1])**2))
			if dist <= 40:
				flag = True
				break
		if flag:
			GameOver("You Loose")
	
	def ChangeDirection(self, direction):
		if self.direction == direction:
			return
		self.direction = direction
		if direction == 'right':
			self.image = PacImg[0]
		elif direction == 'left':
			self.image = PacImg[1]
		elif direction == 'up':
			self.image = PacImg[2]
		else:
			self.image = PacImg[3]

class Ghost(BoardElement):
	
	def __init__(self, pos, length, width, image, direction):
		super().__init__(pos, length, width, image)
		self.direction = direction
	
	def Move(self):
		if self.direction == 'right':
			self.pos[0] += 5
			if self.pos[0] >= width-self.length or self.pos[0] == 360:
				self.direction = 'left'
		elif self.direction == 'left':
			self.pos[0] -= 5
			if self.pos[0] <= 0 or self.pos[0] == 420:
				self.direction = 'right'
		elif self.direction == 'up':
			self.pos[1] -= 5
			if self.pos[1] <= 0:
				self.direction = 'down'
		elif self.direction == 'down':
			self.pos[1] += 5
			if self.pos[1] >= height-self.length:
				self.direction = 'up'


boundaryImg = []
boundaryImg.append(pygame.image.load(os.path.join('images','boundary1.png')))
boundaryImg.append(pygame.image.load(os.path.join('images','boundary2.png')))
boundaryImg.append(pygame.image.load(os.path.join('images','boundary3.png')))
boundaryImg.append(pygame.image.load(os.path.join('images','boundary4.png')))
boundaryImg.append(pygame.image.load(os.path.join('images','boundary5.png')))

foodImg = pygame.image.load(os.path.join('images','food.png'))

PacImg = []
PacImg.append(pygame.image.load(os.path.join('images','pac_right.png')))
PacImg.append(pygame.image.load(os.path.join('images','pac_left.png')))
PacImg.append(pygame.image.load(os.path.join('images','pac_up.png')))
PacImg.append(pygame.image.load(os.path.join('images','pac_down.png')))

ghostImg = pygame.image.load(os.path.join('images','ghost.png'))

boundaries = set([])
foods = set([])
ghosts = set([])

def AddElements():
	global boundaries,foods,boundaryImg,foodImg
	boundaries.add(BoardElement([0,0],830,10,boundaryImg[0]))
	boundaries.add(BoardElement([0,690],830,10,boundaryImg[0]))
	boundaries.add(BoardElement([0,10],10,300,boundaryImg[1]))
	boundaries.add(BoardElement([0,390],10,300,boundaryImg[1]))
	boundaries.add(BoardElement([820,10],10,300,boundaryImg[1]))
	boundaries.add(BoardElement([820,390],10,300,boundaryImg[1]))
	boundaries.add(BoardElement([10,300],100,10,boundaryImg[4]))
	boundaries.add(BoardElement([10,390],100,10,boundaryImg[4]))
	boundaries.add(BoardElement([720,300],100,10,boundaryImg[4]))
	boundaries.add(BoardElement([720,390],100,10,boundaryImg[4]))
	boundaries.add(BoardElement([410,10],10,300,boundaryImg[1]))
	boundaries.add(BoardElement([410,390],10,300,boundaryImg[1]))
	boundaries.add(BoardElement([250,275],10,150,boundaryImg[3]))
	boundaries.add(BoardElement([575,275],10,150,boundaryImg[3]))
	boundaries.add(BoardElement([60,60],300,10,boundaryImg[2]))
	boundaries.add(BoardElement([470,60],300,10,boundaryImg[2]))
	boundaries.add(BoardElement([60,210],300,10,boundaryImg[2]))
	boundaries.add(BoardElement([470,210],300,10,boundaryImg[2]))
	boundaries.add(BoardElement([60,480],300,10,boundaryImg[2]))
	boundaries.add(BoardElement([470,480],300,10,boundaryImg[2]))
	boundaries.add(BoardElement([60,630],300,10,boundaryImg[2]))
	boundaries.add(BoardElement([470,630],300,10,boundaryImg[2]))
	boundaries.add(BoardElement([60,65],10,150,boundaryImg[3]))
	boundaries.add(BoardElement([350,65],10,150,boundaryImg[3]))
	boundaries.add(BoardElement([470,65],10,150,boundaryImg[3]))
	boundaries.add(BoardElement([760,65],10,150,boundaryImg[3]))
	boundaries.add(BoardElement([60,485],10,150,boundaryImg[3]))
	boundaries.add(BoardElement([350,485],10,150,boundaryImg[3]))
	boundaries.add(BoardElement([470,485],10,150,boundaryImg[3]))
	boundaries.add(BoardElement([760,485],10,150,boundaryImg[3]))
	x1,x2,y1,y2 = 30,440,30,450
	for i in range(1,55):
		foods.add(BoardElement([x1,y1],10,10,foodImg))
		foods.add(BoardElement([x1,y2],10,10,foodImg))
		foods.add(BoardElement([x2,y1],10,10,foodImg))
		foods.add(BoardElement([x2,y2],10,10,foodImg))
		if y1 == 30:
			x1 += 20
			x2 += 20
		if x1 == 390 or x1 == 380:
			x1 = 380
			x2 = 790
			y1 += 20
			y2 += 20
		if y1 == 250 or y1 == 240:
			y1 = 240
			y2 = 660
			x1 -= 20
			x2 -= 20
		if x1 == 20 or x1==30 and 30<y1<=240:
			x1 =30
			x2 = 440
			y1 -= 20
			y2 -= 20
	x,y = 10,350
	for i in range(1,40):
		foods.add(BoardElement([x,y],10,10,foodImg))
		if x==230:
			x += 40
		elif x==550:
			x += 50
		else:
			x += 20
	ghosts.add(Ghost([420,20],50,50,ghostImg,'down'))
	ghosts.add(Ghost([360,640],50,50,ghostImg,'up'))
	ghosts.add(Ghost([360,220],50,50,ghostImg,'left'))
	ghosts.add(Ghost([420,430],50,50,ghostImg,'right'))
	ghosts.add(Ghost([420,220],50,50,ghostImg,'right'))
	ghosts.add(Ghost([360,430],50,50,ghostImg,'left'))

def DrawElements(canvas):
	for bd in list(boundaries):
		bd.Draw(canvas)
	for fd in list(foods):
		fd.Draw(canvas)
	for gh in list(ghosts):
		gh.Draw(canvas)
		gh.Move()

def Play():
	AddElements()
	GameObject = Pacman([200,10], 50, 50, PacImg[0], 'right')
	x_change = 5
	y_change = 0
	direction = None
	while True:
		display.fill(background_color)
		DrawElements(display)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				QuiteGame()
			if event.type == pygame.QUIT:
				QuiteGame()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					x_change = 5
					y_change = 0
					direction = 'right'
				if event.key == pygame.K_LEFT:
					x_change = -5
					y_change = 0
					direction = 'left'
				if event.key == pygame.K_UP:
					y_change = -5
					x_change = 0
					direction = 'up'
				if event.key == pygame.K_DOWN:
					y_change = 5
					x_change = 0
					direction = 'down'
			if event.type == pygame.KEYUP:
				direction = None
		GameObject.Draw(display)
		GameObject.Move([x_change, y_change])
		if direction:
			GameObject.ChangeDirection(direction)
		pygame.display.update()
		clock.tick(30)
def GameOver(message):
	font = pygame.font.SysFont("comicsansms",60)
	text = font.render(message, True, font_color)
	while True:
		display.fill(background_color)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				QuiteGame()
		display.blit(text,(250,300))
		pygame.display.update()
		clock.tick(15)

def QuiteGame():
	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	Play()