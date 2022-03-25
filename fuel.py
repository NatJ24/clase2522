from engine import *
class Fuel:
    def __init__(self, engine):
        self.level = 1000
        self.engine = engine

    def update(self):
        self.level = self.level - abs(self.engine.get_speed())*0.01
        if self.level < 0:
            self.level = 0
    
    def __str__(self):
        status = str(self.level) + str('L')
        return status