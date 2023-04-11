import pygame
#Classe du vaiseau du joueur
class Spaceship:

    
    def __init__(self,pv_max,speed):
        self.pv = pv_max
        self.max_pv = pv_max
        self.speed = speed

    def deplacement():
        for event in pygame.event.get():
            try:
                # détecte si une touche est enfoncée
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("La touche espace est enfoncée")
                    elif event.key == pygame.K_z or event.key == pygame.K_UP:
                        print("La touche z ou flèche du haut est enfoncée")
                    elif event.key == pygame.K_q or event.key == pygame.K_LEFT:
                        print("La touche z ou flèche du haut est enfoncée")
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        print("La touche z ou flèche du haut est enfoncée")
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        print("La touche z ou flèche du haut est enfoncée")

                # détecte si une touche est relâchée
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        print("La touche espace est relâchée")
                    elif event.key == pygame.K_z or event.key == pygame.K_UP:
                        print("La touche z ou flèche du haut est relâchée")
                    elif event.key == pygame.K_q or event.key == pygame.K_LEFT:
                        print("La touche z ou flèche du haut est relâchée")
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        print("La touche z ou flèche du haut est relâchée")
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        print("La touche z ou flèche du haut est relâchée")
            except AttributeError:
                # ignore tous les événements qui ne sont pas liés aux touches
                pass
                    
    def get_health(pv, damage):
        if pv-damage >0:
            pv = pv - damage
        else:
            pv = 0
            print("Game Over")
    