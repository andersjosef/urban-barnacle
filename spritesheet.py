import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frames , width_start, height_start, width, height, scale_x, scale_y):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), (width_start , height_start, width, height))
        image = pygame.transform.scale(image, (scale_x, scale_y))

        return image


