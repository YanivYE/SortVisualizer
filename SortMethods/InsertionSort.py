from array import array
import pygame

from SortMethods.sort import Sort

GRAY = (192, 192, 192)
WHITE = (0, 0, 0)

pygame.font.init()

font = pygame.font.SysFont('arial', 30)


class InsertionSort(Sort):

    def __init__(self, x, y, width, height, win_width) -> None:
        super().__init__(x, y, width, height, win_width)
        self.text = "Insertion Sort"
        self.speed = 1

    def draw(self, win):
        super().draw(win, self.text)

    def sort(self):
        arr = self.array
        for i in range(1, len(arr)):
            j = i
            while j >= 0 and arr[j - 1] > arr[j]:
                temp = arr[j - 1]  # swapping all the smaller numbers
                arr[j - 1] = arr[j]
                arr[j] = temp
                j -= 1
                yield arr

