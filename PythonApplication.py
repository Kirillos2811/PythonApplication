class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

AutoBus = Transport("Renaul Logan", 180, 12)
print(f"Название автомобиля: {AutoBus.name} Скорость: {AutoBus.max_speed} Пробег: {AutoBus.mileage}")