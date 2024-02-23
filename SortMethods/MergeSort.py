import pygame

from SortMethods.sort import Sort

GRAY = (192, 192, 192)
WHITE = (0, 0, 0)

pygame.font.init()

font = pygame.font.SysFont('arial', 30)


class MergeSort(Sort):

    def __init__(self, x, y, width, height, win_width) -> None:
        super().__init__(x, y, width, height, win_width)
        self.text = "Merge Sort"
        self.speed = 3

    def draw(self, win):
        super().draw(win, self.text)

    def sort(self):
        arr = self.array
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            L.sort()
            R.sort()

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
                yield arr

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
                yield arr

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
                yield arr
