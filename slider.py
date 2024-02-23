import pygame

GRAY = (192, 192, 192)
WHITE = (0, 0, 0)

pygame.font.init()

font = pygame.font.SysFont('arial', 30)


class Slider:

    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max = 330
        self.min = 30
        self.one_percent = (330 - 30) // 100  # this will be the represntation of one perecnt of the slider value
        self.value = self.one_percent * 50  # at the start the value will be exactly in the half

    def draw(self, win):
        pygame.draw.rect(win, GRAY, [self.x, self.y, self.width, self.height], 4, 3)
        pygame.draw.rect(win, GRAY, [self.x, self.y, self.value * (self.width / (self.max - self.min)), self.height])

        slider_min = font.render("0", False, (0, 0, 0))
        slider_max = font.render("300", False, (0, 0, 0))
        slider_info = font.render("Array size ", False, (0, 0, 0))

        slider_value = font.render(str(int(self.value)), False, (0, 0, 0))

        win.blit(slider_min, (160, 505))
        win.blit(slider_max, (800, 505))
        win.blit(slider_value, (self.value * (self.width / (self.max - self.min)) + self.x, 455))
        win.blit(slider_info, (230, 555))
