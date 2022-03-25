class Environment:
    def __init__(self):
        self.lum = 50
    def modify_lum(self,variacion):
        self.lum += variacion   # la luminosidad tiene un valor y varía según indique el usuario
        if self.lum < 0:
            self.lum = 0
        elif self.lum >= 99:
            self.lum = 99
    def set_lum(self,value):
        self.lum = value    # el usuario indica el valor de luminosidad del ambiente
    def get_lum(self):
        return self.lum
    def __str__(self):
        status = str(self.lum) +' '+ str('(luminosidad en %)')
        return status