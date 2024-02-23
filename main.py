from re import T
from tkinter import N
import pygame
from slider import Slider
from SortMethods.insertionSort import InsertionSort
from SortMethods.bubbleSort import BubbleSort
from SortMethods.quickSort import QuickSort

# initialises and global variables

pygame.font.init()
font = pygame.font.SysFont('arial', 28)
FPS = 60
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)

WIDTH = 1000
HEIGHT = 600


def drawWin(win, slider, sort_buttons):
    win.fill(WHITE)

    draw_sort_buttons(win, sort_buttons)

    slider.draw(win)

    pygame.display.update()


def draw_sort_buttons(win, sort_buttons):
    for btn in sort_buttons:
        btn.draw(win)


def buttons_clicked(buttons, mouse):
    for button in buttons:
        if button.x <= mouse[0] <= button.x + button.width and button.y <= mouse[1] <= button.y + button.height:
            return button

    return None


def drawSorting(win, sort_btn, state):
    win.fill(WHITE)
    sort_btn.draw_array(win, state)
    pygame.display.update()


def main():
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sort algorithm")

    pygame.font.init()
    clock = pygame.time.Clock()

    slider = Slider(200, 500, 600, 50)

    insertion = InsertionSort(200, 120, 200, 80, WIDTH)

    bubble = BubbleSort(200, 220, 200, 80, WIDTH)

    quick = QuickSort(600, 120, 200, 80, WIDTH)

    sort_btns = [insertion, bubble, quick]

    clicked_button = None
    running = True
    while clicked_button == None and running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if slider.x < mouse[0] <= slider.x + slider.width and slider.y <= mouse[
                    1] <= slider.y + slider.height:  # pressed on the slider
                    slider.value = (mouse[0] - slider.x) / 2
                clicked_button = buttons_clicked(sort_btns, mouse)
        drawWin(win, slider, sort_btns)

    clicked_button.generateArray(int(slider.value))

    sorting_states = clicked_button.sort()
    curr_state = 0

    calculated_fps = len(clicked_button.array) / clicked_button.speed
    while running:

        clock.tick(calculated_fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        try:
            drawSorting(win, clicked_button, next(sorting_states))
        except StopIteration:
            print(curr_state)
            running = False

        curr_state += 1


main()