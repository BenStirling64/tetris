import pygame

from board import Board
from tetronimo import Tetronimo
from text import Text

class App:
    def __init__(self):
        pygame.init()

        self.fps = 60

        self.screen = pygame.display.set_mode((640, 640))
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.frame_count = 0
        self.score = 0

        pygame.display.set_caption("Tetris")

        self.board = Board()
        self.falling_shape = Tetronimo()
        self.score_heading = Text("Score:", 480, 40)
        self.score_text = Text("0", 480, 80)
        self.game_over_text = Text("Game Over! :(", 480, 120)

        self.drawable_objects = [self.board, self.falling_shape, self.score_heading, self.score_text]

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and not self.game_over:
                if event.key == pygame.K_UP:
                    self.falling_shape.rotate(True)
                elif event.key == pygame.K_DOWN:
                    self.falling_shape.rotate(False)
                elif event.key == pygame.K_LEFT:
                    self.falling_shape.update_position((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.falling_shape.update_position((1, 0))

        # background
        self.screen.fill("black")

        # shape update
        if self.frame_count % 10 == 0 and not self.game_over:
            if self.falling_shape.update_position((0, 1)) or self.board.shape_collides(self.falling_shape):
                self.board.add(self.falling_shape)
                self.drawable_objects.remove(self.falling_shape)

                self.falling_shape = Tetronimo()
                self.drawable_objects.append(self.falling_shape)

            if self.board.is_full():
                self.game_over = True
                print("Game Over!")
            else:
                lines_cleared = self.board.check_for_full_line()

                if lines_cleared > 0:
                    if lines_cleared == 1:
                        self.score += 100
                    elif lines_cleared == 2:
                        self.score += 300
                    elif lines_cleared == 3:
                        self.score += 500
                    elif lines_cleared == 4:
                        self.score += 800

                    self.drawable_objects.remove(self.score_text)

                    self.score_text = Text(str(self.score), 480, 80)
                    self.drawable_objects.append(self.score_text)

        # ui
        pygame.draw.rect(self.screen, (0, 128, 128), pygame.Rect(320, 0, 320, 640))

        # object drawing
        for obj in self.drawable_objects:
            obj.display(self.screen)

        if not self.game_over:
            self.frame_count += 1
        else:
            self.game_over_text.display(self.screen)

        pygame.display.flip()
        self.clock.tick(self.fps)