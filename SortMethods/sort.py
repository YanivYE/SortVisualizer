import pygame
import random

GRAY = (192, 192, 192)
WHITE = (0, 0, 0)

pygame.font.init()

font = pygame.font.SysFont('arial', 30)


class Sort:

    def __init__(self, x, y, width, height, win_width) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.win_width = win_width
        self.array = []

    def draw(self, win, text):
        pygame.draw.rect(win, GRAY, [self.x, self.y, self.width, self.height], 4, 3)

        button_text = font.render(text, False, (0, 0, 0))

        win.blit(button_text, (self.x + 16, self.y + 20))

    # this function will create an array, which each element in it has a random number, and a random color
    def generateArray(self, size):
        created_array = []

        for i in range(size):
            created_array.append(
                (random.randint(30, 400), (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))))

        self.array = created_array

    def draw_array(self, win, arr):
        for i in range(0, len(arr)):
            element_width = (self.win_width / len(arr))
            x = i * element_width
            color = arr[i][1]

            pygame.draw.rect(win, color, [x, 400 - arr[i][0], element_width, arr[i][0]])

