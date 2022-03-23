from environment import *
class Light:
    def __init__(self, env):
        self.deactivate()
        self.env=env
    
    def activate(self):
        self.activate=True
    
    def deactivate(self):
        self.activate=False

    def update(self):
        if self.env.get_lum()<40:
            self.activate()
        else:
            self.deactivate()
    
    def __str__(self):
        if self.activate:
            status = 'L'
        else: 
            status = 'R'
        return status