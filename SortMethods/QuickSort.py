from ast import Yield
from tkinter import Y
import pygame
from SortMethods.sort import Sort

GRAY = (192, 192, 192)
WHITE = (0, 0, 0)

pygame.font.init()

font = pygame.font.SysFont('arial', 30)


class QuickSort(Sort):

    def __init__(self, x, y, width, height, win_width) -> None:
        super().__init__(x, y, width, height, win_width)
        self.text = "Quick Sort"

        self.speed = 20

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

    def partition(self, arr, low, high):
        i = (low - 1)
        pivot = arr[high]

        for j in range(low, high):

            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    def sort(self, arr=None, low=0, high=-1):

        if high == -1:
            high = len(self.array) - 1
        if arr == None:
            arr = self.array

        if len(arr) == 1:
            yield arr
        if low < high:
            pi = self.partition(arr, low, high)
            yield arr

            yield from self.sort(arr, low, pi - 1)
            yield from self.sort(arr, pi + 1, high)

