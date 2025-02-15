import pygame

from app import App

if __name__ == "__main__":
    instance = App()

    while instance.running:
        instance.update()

    pygame.quit()