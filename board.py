import pygame

from tetronimo import default_colours

class Board:
    def __init__(self):
        self.tiles = [["." for _ in range(10)] for _ in range(20)]
    
    def add(self, shape):
        for i in range(16):
            if shape.layout[i] == "X":
                self.tiles[i // 4 + shape.coords[1] - 2][i % 4 + shape.coords[0] - 2] = shape.shape_char

    # returns the number of lines cleared
    def check_for_full_line(self):
        lines_cleared = 0

        for r in range(3, 20):
            if "." in self.tiles[r]:
                continue

            lines_cleared += 1

            for i in range(r, 2, -1):
                self.tiles[i] = self.tiles[i - 1]
            
            self.tiles[3] = ["." for _ in range(10)]

        return lines_cleared

    def display(self, screen):
        for i in range(20):
            for j in range(10):
                if self.tiles[i][j] != ".":
                    pygame.draw.rect(screen, default_colours[self.tiles[i][j]], pygame.Rect(j * 32, i * 32, 32, 32))

    def is_full(self):
        return self.tiles[2] != ["."] * 10

    def shape_collides(self, shape):
        for i in range(16):
            if shape.layout[i] == "X":
                try:
                    if self.tiles[i // 4 + shape.coords[1] - 1][i % 4 + shape.coords[0] - 2] != ".":
                        return True
                except IndexError:
                    return False
                
        return False