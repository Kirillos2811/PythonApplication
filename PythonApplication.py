from time import sleep
from random import randint as rnd
from pynput import keyboard
import json
from world import World
from objects import Shop, Hospital
from utils import gameOver


TICK_SLEEP = 0.05
ADD_TREE = 75
FIRE_UPDATE = 200
CLOUDS_UPDATE = 350
FIRES_RANGE_AT_ONCE = (1, 4)
HELICOPTER_CONTROL_BUTTONS = "wasd"
SAVE_GAME_BUTTON = "k"
RECOVER_GAME_BUTTON = "r"


if __name__ == "__main__":
    width = int(input("Enter game world width: "))
    height = int(input("Enter game world height: "))

    world = World(width, height)
    world.put_on_field(Shop)
    world.put_on_field(Hospital)
    world.generate_rivers(2, 4)
    world.generate_forests()
    world.display()


    def onRelease(key):
        global tick
        try:
            button = key.char.lower()
        except AttributeError:
            pass
        else:
            if button in HELICOPTER_CONTROL_BUTTONS:
                if button == "d":
                    world.helicopter.right()
                elif button == "a":
                    world.helicopter.left()
                elif button == "w":
                    world.helicopter.up()
                elif button == "s":
                    world.helicopter.down()

                world.helicopter.process_events(world)
                world.display()
            elif button == SAVE_GAME_BUTTON:
                with open("game.json", "w") as file:
                    json.dump({"tick": tick, "world": world.toJson()}, file)
            elif button == RECOVER_GAME_BUTTON:
                with open("game.json", "r") as file:
                    data = json.load(file)
                    tick = int(data["tick"])
                    world.loadFromJson(data["world"])
                world.display()
        
        
    listener = keyboard.Listener(
        on_release=onRelease
    )
    listener.start()


    tick = 1
    while True:
        if world.helicopter.lives == 0:
            gameOver(world.helicopter.get_score())
            break

        if tick % ADD_TREE == 0:
            world.generate_tree()
            world.display()

        if tick % FIRE_UPDATE == 0:
            world.process_not_extinguished_fires()
            for i in range(rnd(FIRES_RANGE_AT_ONCE[0], FIRES_RANGE_AT_ONCE[1])):
                world.add_fire()
            world.display()

        if tick % CLOUDS_UPDATE == 0:
            world.update_clouds()
            world.display()

        sleep(TICK_SLEEP)
        tick += 1