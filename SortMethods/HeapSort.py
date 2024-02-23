import pygame

from SortMethods.sort import Sort

GRAY = (192, 192, 192)
WHITE = (0, 0, 0)

pygame.font.init()

font = pygame.font.SysFont('arial', 30)


class HeapSort(Sort):

    def __init__(self, x, y, width, height, win_width) -> None:
        super().__init__(x, y, width, height, win_width)
        self.text = "Heap Sort"
        self.speed = 3

    def draw(self, win):
        super().draw(win, self.text)

    def sort(self):
        arr = self.array
        n = len(arr)

        for i in range(n // 2, -1, -1):
            self.heapify(arr, n, i)
            yield arr

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]

            self.heapify(arr, i, 0)

            yield arr

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
