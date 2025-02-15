import pygame

class Text:
    def __init__(self, message, x=320, y=320):
        self.message = message
        self.font = pygame.font.Font(None, 36)

        self.text_obj = self.font.render(self.message, True, (255, 255, 255))
        self.text_rect = self.text_obj.get_rect()

        self.text_rect.center = (x, y)

    def display(self, screen):
        screen.blit(self.text_obj, self.text_rect)