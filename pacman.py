import pygame
import os,sys

width = 830
height = 700

background_color = pygame.Color(0,0,0)

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

boundaryImg = []
boundaryImg.append(pygame.image.load(os.path.join('images','boundary1.png')))
boundaryImg.append(pygame.image.load(os.path.join('images','boundary2.png')))
boundaryImg.append(pygame.image.load(os.path.join('images','boundary3.png')))
boundaryImg.append(pygame.image.load(os.path.join('images','boundary4.png')))
boundaryImg.append(pygame.image.load(os.path.join('images','boundary5.png')))

foodImg = pygame.image.load(os.path.join('images','food.png'))

boundaries = set([])
foods = set([])

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
def DrawElements(canvas):
	for bd in list(boundaries):
		bd.Draw(canvas)
	for fd in list(foods):
		fd.Draw(canvas)

def Play():
	AddElements()
	while True:
		display.fill(background_color)
		DrawElements(display)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				QuiteGame()
		pygame.display.update()
		clock.tick(30)

def QuiteGame():
	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	Play()