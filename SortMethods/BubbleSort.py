import pygame

from SortMethods.sort import Sort

GRAY = (192, 192, 192)
WHITE = (0, 0, 0)

pygame.font.init()

font = pygame.font.SysFont('arial', 30)


class BubbleSort(Sort):

    def __init__(self, x, y, width, height, win_width) -> None:
        super().__init__(x, y, width, height, win_width)
        self.text = "Bubble Sort"
        self.speed = 0.5

    def draw(self, win):
        super().draw(win, self.text)

    def sort(self):
        arr = self.array
        n = len(arr)
        for i in range(n):

            for j in range(0, n - i - 1):

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

                yield arr