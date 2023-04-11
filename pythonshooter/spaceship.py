#Classe du vaiseau du joueur
class Spaceship:

    def __init__(self,pv_max,speed):
        self.pv = pv_max
        self.max_pv = pv_max
        self.speed = speed

    def get_health(pv, damage):
        if pv-damage >0:
            pv = pv - damage
        else:
            pv = 0
    