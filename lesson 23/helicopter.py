class Helicopter:
    def __init__(self, w, h):
        self.x = h // 2
        self.y = w // 2
        self.water = 0
        self.max_water = 1 
        self.hp = 100      
        self.max_hp = 100
        self.score = 0     

    def move(self, dx, dy, map_obj):
        nx, ny = self.x + dx, self.y + dy

        if map_obj.check_bounds(nx, ny):
            self.x, self.y = nx, ny

    def process_action(self, map_obj):
        cell = map_obj.cells[self.x][self.y]
        
        if cell == 1 and self.water < self.max_water:
            self.water = self.max_water
            
        elif cell == 5 and self.water > 0:
            map_obj.cells[self.x][self.y] = 2 
            self.water -= 1
            self.score += 100
            
        elif cell == 3 and self.score >= 50 and self.hp < self.max_hp:
            self.hp = min(self.max_hp, self.hp + 20)
            self.score -= 50
            
        elif cell == 4 and self.score >= 200:
            self.max_water += 1
            self.score -= 200
