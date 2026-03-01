import os
import time
import json

from map import Map
from clouds import Clouds
from pynput import keyboard
from helicopter import Helicopter

TICK_RATE = 0.1
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
heli = Helicopter(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)

tick = 0
running = True

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def on_press(key):
    global running

    if hasattr(key, 'char') and key.char:
        c = key.char.lower()
        if c in ['w', 'ц']: heli.move(-1, 0, field)
        elif c in ['s', 'ы']: heli.move(1, 0, field)
        elif c in ['a', 'ф']: heli.move(0, -1, field)
        elif c in ['d', 'в']: heli.move(0, 1, field)
        elif c in ['e', 'у']: heli.process_action(field)
        elif c in ['f', 'а']: save_game() 
        elif c in ['g', 'п']: load_game() 
    elif key == keyboard.Key.esc:
        running = False

def save_game():
    data = {
        'heli': {
            'x': heli.x, 
            'y': heli.y, 
            'hp': heli.hp, 
            'w': heli.water, 
            'mw': heli.max_water, 
            's': heli.score
        }
    }
    
    with open('save.json', 'w') as f:
        json.dump(data, f)

def load_game():
    try:
        with open('save.json', 'r') as f:
            data = json.load(f)
            heli.x, heli.y = data['heli']['x'], data['heli']['y']
            heli.hp, heli.water = data['heli']['hp'], data['heli']['w']
            heli.max_water, heli.score = data['heli']['mw'], data['heli']['s']

    except FileNotFoundError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

while running:
    clear_screen()
    
    tick += 1
    if tick % 50 == 0:
        field.generate_forest(1, 1)

    if tick % 80 == 0:
        field.update_fires(heli)
        field.add_fire()

    if tick % 30 == 0:
        clouds.update()

        if clouds.cells[heli.x][heli.y] == 2:
            heli.hp -= 10

            if heli.hp <= 0:
                print('Вертолет разбился! Игра окончена.')
                break

    print(f'❤️ Здоровье: {heli.hp}/{heli.max_hp} | 💧 Вода: {heli.water}/{heli.max_water} | 💰 Очки: {heli.score}')
    print('Управление: W/A/S/D - полет | E - действие (вода/тушение/магазин) | F - сохр | G - загр | ESC - выход')
    field.print_map(heli, clouds)
    
    time.sleep(TICK_RATE)
