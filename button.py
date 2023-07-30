import pygame 



#button class
class Button():
	def __init__(self, surface, x, y, image, size_x, size_y):
		self.image = pygame.transform.scale(image, (size_x, size_y))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.surface = surface

	def draw(self, settings):
		settings.action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == True and settings.clicked == False:
				settings.action = True
				settings.clicked = True

		if pygame.mouse.get_pressed()[0] == False:
			settings.clicked = False

		#draw button
		self.surface.blit(self.image, (self.rect.x, self.rect.y))

		return settings.action