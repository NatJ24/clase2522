class Environment:
    def __init__(self,lum):
        self.lum = lum
    def modify_lum(self,variacion):
        self.lum += variacion   # la luminosidad tiene un valor y varía según indique el usuario
    def set_lum(self,value):
        self.lum = value    # el usuario indica el valor de luminosidad del ambiente
    def get_lum(self):
        