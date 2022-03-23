# Blinker position (pos attribute)
BLINKER_FRONT = 1
BLINKER_REAR = 2

class engine:
    """clase del motor"""

    def __init__(self):
        self.rpm = 0
        self.gear = 0
    def modify_rpm(self, value):
        self.rpm += value
    def modify_gear(self, value):
        self.gear += value
    def get_speed(self):
        if self.gear >=0:
            speed = (self.rpm*self.gear/5)/10
        elif self.rpm>0:
            speed = -10
        else:
            speed = 0
        return speed
    def __str__(self):
            #print(self.rpm, ' ','rpm',' ',self.gear,' ',self.get_speed())
            status = str(self.rpm) + str('rpm')+ str(' ') + str(self.gear)+ str(' ') +str(self.get_speed()) + str('Km/h')
            return status