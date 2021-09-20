import pygame  # necessaire pour charger les images et les sons
import random
import math

class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.image = pygame.image.load("vaisseau1.png")
        self.sens = "O"
        self.vitesse = 2.75
        self.score=0
        self.health=100
        self.max_health=100
        self.rect=self.image.get_rect()
        self.rect.x=400
        self.rect.y=492
        self.font=font=pygame.font.Font("Oswald.ttf",25)
    def health_bar(self,surface):
        pygame.draw.rect(surface, (60,63,60), [self.rect.x-10,self.rect.y,self.max_health,5])
        pygame.draw.rect(surface, (111,210,46), [self.rect.x-10,self.rect.y,self.health,5])
    def deplacer(self) :
        if (self.sens == "droite") and (self.rect.x < 740):
            self.rect.x += self.vitesse
        elif (self.sens == "gauche") and (self.rect.x > 0):
           self.rect.x -= self.vitesse
    def tirer(self):
        self.sens = self.sens
    def marquer(self):
        self.score+= 1
    def update(self,screen):
        score_text=self.font.render(f"Score:{self.score}",1,(255,255,255))
        screen.blit(score_text,(20,20))
        
class Boss():
    def __init__(self):
        self.depart=300
        self.image=pygame.image.load("SiphaDrip.png")
        self.hauteur= 0
        self.health=500
        self.max_health=500
        self.rect=self.image.get_rect()
        self.rect.x=300
        self.rect.y=0
    def health_bar(self,surface):
        pygame.draw.rect(surface, (60,63,60), [self.rect.x-140,self.rect.y,self.max_health,5])
        pygame.draw.rect(surface, (111,210,46), [self.rect.x-140,self.rect.y,self.health,5])
        
class Comet():
    def __init__(self):
        self.depart= random.randint(0,740)
        self.image=pygame.image.load("papier.png")
        self.etat = "chargee"
        self.rect=self.image.get_rect()
        self.vitesse=random.randint(1,2)
    NbPapier=8
    def fall(self):
        self.rect.y+=self.vitesse
    def back(self):
        self.depart= random.randint(0,740)
        self.image=pygame.image.load("papier.png")
        self.rect=self.image.get_rect()
        self.vitesse=random.randint(1,2)
    def aie(self, moi):
        if (math.fabs(self.rect.y - moi.rect.y) < 40) and (math.fabs(self.depart - moi.rect.x) < 20):
            self.etat = "chargee"
            return True
class Ennemi():
    def __init__(self):
        self.depart= random.randint(0,740)
        self.hauteur= 0
        self.type= random.randint(1,2)
        if self.type==1:
                self.image=pygame.image.load("ufo.png")
                self.vitesse=0.1
        elif self.type==2:
                self.image=pygame.image.load("ufo1.png")
                self.vitesse=0.2 
    NbEnnemis=5
    def avancer(self):
        self.hauteur+=self.vitesse
    def disparaitre(self):
        self.depart= random.randint(0,740)
        self.hauteur= 0
        self.type= random.randint(1,2)
        if self.type==1:
                self.image=pygame.image.load("ufo1.png")
                self.vitesse=0.1
        elif self.type==2:
                self.image=pygame.image.load("ufo.png")
                self.vitesse=0.2

class Balle() :
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.rect.x + 16
        self.hauteur = 492
        self.image = pygame.image.load("Bullet.png")
        self.etat = "chargee"
    def bouger(self):
        if self.etat == "chargee":
            self.depart = self.tireur.rect.x + 16
            self.hauteur = 492
        elif self.etat == "tiree" :
            self.hauteur -= 5
        if self.hauteur < 0:
            self.etat = "chargee"
    def toucher(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40):
            self.etat = "chargee"
            return True
    def toucher2(self, siphano):
        if (math.fabs(self.hauteur - siphano.rect.y) < 300) and (math.fabs(self.depart - siphano.rect.x) < 110):
            self.etat = "chargee"
            return True
