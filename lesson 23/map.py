import random

CELL_EMPTY = '⬛'
CELL_RIVER = '🌊'
CELL_TREE = '🌲'
CELL_FIRE = '🔥'
CELL_BURNED = '🟫'
CELL_HOSPITAL = '🏥'
CELL_SHOP = '🏪'

class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for _ in range(w)] for _ in range(h)]

        self.generate_forest(3, 10)
        self.generate_river(10)
        self.generate_building(3)
        self.generate_building(4)

    def check_bounds(self, x, y):
        return 0 <= x < self.h and 0 <= y < self.w

    def generate_river(self, length):
        rc = random.randint(0, self.w - 1)
        rr = random.randint(0, self.h - 1)

        for _ in range(length):
            self.cells[rr][rc] = 1 

            if random.randint(0, 1):
                rc = min(self.w - 1, max(0, rc + random.choice([-1, 1])))

            else:
                rr = min(self.h - 1, max(0, rr + random.choice([-1, 1])))

    def generate_forest(self, r, max_trees):
        for _ in range(max_trees):
            rc, rr = random.randint(0, self.w - 1), random.randint(0, self.h - 1)
            
            if self.cells[rr][rc] == 0:
                self.cells[rr][rc] = 2

    def generate_building(self, building_type):
        while True:
            rc, rr = random.randint(0, self.w - 1), random.randint(0, self.h - 1)
            
            if self.cells[rr][rc] == 0:
                self.cells[rr][rc] = building_type
                break

    def add_fire(self):
        trees = []
        
        for r in range(self.h):
            for c in range(self.w):
                if self.cells[r][c] == 2: 
                    trees.append((r, c))
        
        if trees:
            r, c = random.choice(trees)
            self.cells[r][c] = 5

    def update_fires(self, helicopter):
        for r in range(self.h):
            for c in range(self.w):
                if self.cells[r][c] == 5:
                    self.cells[r][c] = 6
                    helicopter.score -= 50
                    
    def print_map(self, heli, clouds):
        for r in range(self.h):
            row = ''

            for c in range(self.w):
                if heli.x == r and heli.y == c:
                    row += '🚁'

                elif clouds.cells[r][c] == 1:
                    row += '☁️'

                elif clouds.cells[r][c] == 2:
                    row += '⚡'

                elif self.cells[r][c] == 0: row += CELL_EMPTY
                elif self.cells[r][c] == 1: row += CELL_RIVER
                elif self.cells[r][c] == 2: row += CELL_TREE
                elif self.cells[r][c] == 3: row += CELL_HOSPITAL
                elif self.cells[r][c] == 4: row += CELL_SHOP
                elif self.cells[r][c] == 5: row += CELL_FIRE
                elif self.cells[r][c] == 6: row += CELL_BURNED

            print(row)
            