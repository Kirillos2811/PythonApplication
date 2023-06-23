from utils import checkBounds

class Field:
    def __init__(self):
        pass

    def __str__(self):
        return "🟩"
    
    def serialize(self):
        return "Field()"
    
class Tree:
    def __init__(self):
        pass

    def __str__(self):
        return "🌲"
    
    def serialize(self):
        return "Tree()"
    
class River:
    def __init__(self):
        pass

    def __str__(self):
        return "🌊"
    
    def serialize(self):
        return "River()"
    

class Fire:
    def __init__(self):
        pass

    def __str__(self):
        return "🔥"
    
    def serialize(self):
        return "Fire()"
    
class Cloud:
    def __init__(self):
        pass

    def __str__(self):
        return "🌨️󠀠󠀠󠀠󠀠󠀠󠁪🌨️󠀠󠀠󠀠󠀠󠀠"
    
    def serialize(self):
        return "Cloud()"
    
class ThunderCloud:
    def __init__(self):
        pass

    def __str__(self):
        return "⛈️⛈️"
    
    def serialize(self):
        return "ThunderCloud()"
    
class Shop:
    TANK_UPGRADE_COST = 500
    def __init__(self):
        pass

    def __str__(self):
        return "🏢"
    
    def serialize(self):
        return "Shop()"
    
class Hospital:
    LIFE_COST = 1000
    def __init__(self):
        pass

    def __str__(self):
        return "🏥"
    
    def serialize(self):
        return "Hospital()"
    
class Helicopter:
    def __init__(self, x, y, map_width, map_height, score = 0, lives = 3, tank = 0, max_tank = 1):
        self.x = x
        self.y = y
        self.w = map_width
        self.h = map_height
        self.__score = score
        self.lives = lives
        self.tank = tank
        self.max_tank = max_tank

    def __str__(self):
        return "🚁"
    
    def change_score(self, x):
        if self.__score + x >= 0:
            self.__score += x
        else:
            self.__score = 0
    
    def get_score(self):
        return self.__score

    def left(self):
        if checkBounds(self.x, self.y - 1, self.w, self.h):
            self.y -= 1

    def right(self):
        if checkBounds(self.x, self.y + 1, self.w, self.h):
            self.y += 1

    def up(self):
        if checkBounds(self.x - 1, self.y, self.w, self.h):
            self.x -= 1

    def down(self):
        if checkBounds(self.x + 1, self.y, self.w, self.h):
            self.x += 1

    def process_events(self, world):
        x = self.x
        y = self.y
        if isinstance(world.ground_objects[x][y], River):
            self.tank = self.max_tank
        if isinstance(world.ground_objects[x][y], Fire) and self.tank > 0:
            world.ground_objects[x][y] = Tree()
            self.change_score(100)
            self.tank -= 1
        if isinstance(world.aboveground_objects[x][y], ThunderCloud):
            self.lives -= 1
        if isinstance(world.ground_objects[x][y], Hospital):
            if self.__score >= Hospital.LIFE_COST:
                self.__score -= Hospital.LIFE_COST
                self.lives += 1
        if isinstance(world.ground_objects[x][y], Shop):
            if self.__score >= Shop.TANK_UPGRADE_COST:
                self.__score -= Shop.TANK_UPGRADE_COST
                self.max_tank += 1

    def toJson(self):
        return {"x": self.x,
                "y": self.y,
                "w": self.w,
                "h": self.h,
                "score": self.__score,
                "lives": self.lives,
                "tank": self.tank,
                "max_tank": self.max_tank
                }
    
    def loadFromJson(self, data):
        self.x = int(data["x"])
        self.y = int(data["y"])
        self.w = int(data["w"])
        self.h = int(data["h"])
        self.__score = int(data["score"])
        self.lives = int(data["lives"])
        self.tank = int(data["tank"])
        self.max_tank = int(data["max_tank"])