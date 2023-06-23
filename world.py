from random import randint as rnd, choice
from os import system
from objects import Field, Tree, River, Fire, \
                    Helicopter, Cloud, ThunderCloud
from utils import randBool, randCell, checkBounds, \
                    two_dim_obj_list_to_json, two_dim_obj_list_from_json


class World:
    __GENERATE_CLOUD_CHANCE = 10
    __GENERATE_THUNDERCLOUD_CHANCE = 20
    __GENERATE_FORESTS_CHANCE = 20
    __RIVERS_NUMBER = rnd(2, 5)
    __MOVES = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ground_objects = [[Field() for i in range(width)] for i in range(height)]
        self.aboveground_objects = [[None for i in range(width)] for i in range(height)]
        self.helicopter = Helicopter(*randCell(width, height), width, height)

    def generate_rivers(self, min_len, max_len):
        for i in range(self.__RIVERS_NUMBER):
            try:
                x, y = self.get_coords_of_rand_cell_of_class(Field, self.ground_objects)
            except ValueError:
                pass
            else:
                self.generate_river(x, y, rnd(min_len, max_len))

    def generate_forests(self):
        for x in range(self.height):
            for y in range(self.width):
                cell = self.ground_objects[x][y]
                if isinstance(cell, Field) and randBool(self.__GENERATE_FORESTS_CHANCE):
                    self.ground_objects[x][y] = Tree()

    def update_clouds(self):
        self.aboveground_objects = [[None for i in range(self.width)] for i in range(self.height)]
        for ri in range(self.height):
            for ci in range(self.width):
                if randBool(self.__GENERATE_CLOUD_CHANCE):
                    self.aboveground_objects[ri][ci] = Cloud()
                    if randBool(self.__GENERATE_THUNDERCLOUD_CHANCE):
                        self.aboveground_objects[ri][ci] = ThunderCloud()

    def process_not_extinguished_fires(self):
        fires_coords = self.get_coords_of_all_cells_of_class(Fire, self.ground_objects)
        self.helicopter.change_score(-100 * len(fires_coords))
        for fire_coords in fires_coords:
            fire_x = fire_coords[0]
            fire_y = fire_coords[1]
            self.ground_objects[fire_x][fire_y] = Field()

    def display(self):
        from PythonApplication import SAVE_GAME_BUTTON, RECOVER_GAME_BUTTON
        system("clear")
        print("🏆", self.helicopter.get_score(), end=" ")
        print("💓", self.helicopter.lives, end=" ")
        print("💦", self.helicopter.tank, "/", self.helicopter.max_tank)
        print("⬛" * (self.width + 2))
        for x in range(self.height):
            print("⬛", end="")
            for y in range(self.width):
                if self.aboveground_objects[x][y] is not None:
                    print(self.aboveground_objects[x][y], end="")
                elif self.helicopter.x == x and self.helicopter.y == y:
                    print(self.helicopter, end="")
                else:
                    print(self.ground_objects[x][y], end="")
            print("⬛")
        print("⬛" * (self.width + 2))
        print(f"SAVE PROGRESS: '{SAVE_GAME_BUTTON}'")
        print(f"RECOVER PROGRESS: '{RECOVER_GAME_BUTTON}'")
        

    def put_on_field(self, obj_class):
        x, y = self.get_coords_of_rand_cell_of_class(Field, self.ground_objects)
        self.ground_objects[x][y] = obj_class()

    def add_fire(self):
        try:
            x, y = self.get_coords_of_rand_cell_of_class(Tree, self.ground_objects)
        except ValueError:
            pass
        else:
            self.ground_objects[x][y] = Fire()

    def generate_river(self, x, y, l):
        self.ground_objects[x][y] = River()
        l -= 1
        if l == 0:
            return
        try:
            new_x, new_y = self.get_rand_neighbour_cell_coords_of_class(x, y, 
                                                                    self.ground_objects, Field)
        except ValueError:
            pass
        else:
            self.generate_river(new_x, new_y, l)

    def generate_tree(self):
        try:
            x, y = self.get_coords_of_rand_cell_of_class(Field, self.ground_objects)
        except ValueError:
            pass
        else:
            self.ground_objects[x][y] = Tree()


    def get_rand_neighbour_cell_coords_of_class(self, x, y, obj_arr, _class):
        variants = []
        for item in self.__MOVES:
            new_x = x + item[0]
            new_y = y + item[1]
            if checkBounds(new_x, new_y, self.width, self.height) and \
                isinstance(obj_arr[new_x][new_y], _class):
                variants.append((new_x, new_y))
        
        if len(variants) == 0:
            raise ValueError
        return choice(variants)
    
    def get_coords_of_all_cells_of_class(self, cell_class, cell_arr):
        coords = []
        for x in range(self.height):
            for y in range(self.width):
                if isinstance(cell_arr[x][y], cell_class):
                    coords.append((x, y))
        return coords

    def get_coords_of_rand_cell_of_class(self, cell_class, cell_arr):
        variants = self.get_coords_of_all_cells_of_class(cell_class, cell_arr)
        
        if len(variants) == 0:
            raise ValueError
        return choice(variants)
    
    def toJson(self):
        return {"width": self.width,
                "height": self.height,
                "ground_objects": two_dim_obj_list_to_json(self.ground_objects,
                                                            self.width, self.height),
                "aboveground_objects": two_dim_obj_list_to_json(self.aboveground_objects,
                                                                    self.width, self.height),
                "helicopter": self.helicopter.toJson()
                }
    
    def loadFromJson(self, data):
        self.width = int(data["width"])
        self.height = int(data["height"])
        self.ground_objects = two_dim_obj_list_from_json(data["ground_objects"],
                                                          self.width, self.height)
        self.aboveground_objects = two_dim_obj_list_from_json(data["aboveground_objects"],
                                                               self.width, self.height)
        self.helicopter.loadFromJson(data["helicopter"])