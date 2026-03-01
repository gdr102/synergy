import random

class Clouds:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for _ in range(w)] for _ in range(h)]

    def update(self):
        self.cells = [[0 for _ in range(self.w)] for _ in range(self.h)]
        
        for _ in range(5):
            r, c = random.randint(0, self.h - 1), random.randint(0, self.w - 1)
            self.cells[r][c] = random.choices([1, 2], weights=[0.8, 0.2])[0]
