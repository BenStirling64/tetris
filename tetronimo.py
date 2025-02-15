from random import randint
import pygame

possible_shapes = ["T", "I", "O", "S", "J", "L", "Z"]

starting_layouts = {
    "T": "......X..XXX....",
    "I": "....XXXX........",
    "O": ".....XX..XX.....",
    "S": "......XX.XX.....",
    "J": ".....X...XXX....",
    "L": "......X.XXX.....",
    "Z": "....XX...XX....."
}

default_colours = {
    "T": (128, 0, 128),
    "I": (0, 255, 255),
    "O": (255, 255, 0),
    "S": (0, 255, 0),
    "J": (0, 0, 255),
    "L": (255, 165, 0),
    "Z": (255, 0, 0)
}

class Tetronimo:
    def __init__(self):
        self.shape_char = possible_shapes[randint(0, 6)]
        self.layout = starting_layouts[self.shape_char]
        self.colour = default_colours[self.shape_char]
        self.coords = [5, 1]

    def display(self, screen):
        for i in range(16):
            if self.layout[i] == "X":
                x = 32 * (i % 4 - 2 + self.coords[0])
                y = 32 * (i // 4 - 2 + self.coords[1])

                pygame.draw.rect(screen, self.colour, pygame.Rect(x, y, 32, 32))

    def rotate(self, clockwise):
        new_layout_list = ["."] * 16

        for i in range(4):
            for j in range(4):
                if self.layout[i * 4 + j] == "X":
                    if clockwise:
                        new_layout_list[j * 4 + 3 - i] = "X"
                    else:
                        new_layout_list[(3 - j) * 4 + i] = "X"

        self.layout = "".join(new_layout_list)

    # returns true if the tetronimo reaches the bottom of the board, otherwise returns false
    def update_position(self, new_coords):
        if new_coords[0] > 0:
            for c in range(3, 0, -1):
                if self.layout[c::4] != "....":
                    if self.coords[0] + c - 1 < 10:
                        self.coords[0] += new_coords[0]
                    
                    break
        elif new_coords[0] < 0:
            for c in range(3):
                if self.layout[c::4] != "....":
                    if self.coords[0] + c - 2 > 0:
                        self.coords[0] += new_coords[0]
                    
                    break

        if new_coords[1] > 0:
            for i in range(12, 0, -4):
                if self.layout[i:i+4] != "....":
                    if self.coords[1] + i // 4 <= 20:
                        self.coords[1] += new_coords[1]
                    else:
                        return True

                    break

        return False