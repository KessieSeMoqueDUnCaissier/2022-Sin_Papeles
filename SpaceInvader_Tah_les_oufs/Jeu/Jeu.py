import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'application

# lancement des modules inclus dans pygame
pygame.init() 
# définir ue clock
clock=pygame.time.Clock()
FPS=400
# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders") 
# chargement de l'image de fond
fond = pygame.image.load('background.jpg')
# creation du joueur
player = space.Joueur()
siphan0 = space.Boss()
# creation de la balle
tir = space.Balle(player)
tir.etat = "chargee"
# creation des ennemis
listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)
# projectiles
listePapiers=[]
for papier in range(space.Comet.NbPapier):
    projectile=space.Comet()
    listePapiers.append(projectile)
### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))
    # joueur en action
    player.health_bar(screen)
    player.update(screen)
    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
       
       # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_SPACE : # espace pour tirer
                player.tirer()
                tir.etat = "tiree"
            if event.key== pygame.K_a:
                pygame.mixer.music.load("bmw.mp3")
                pygame.mixer.music.play()
            if event.key==pygame.K_e:
                pygame.mixer.music.load("paris.mp3")
                pygame.mixer.music.play()  
            if event.key==pygame.K_z:
                pygame.mixer.music.load("illuminati.mp3")
                pygame.mixer.music.play()
            if event.key==pygame.K_r:
                pygame.mixer.music.load("dj-alex.mp3")
                pygame.mixer.music.play()
            if event.key==pygame.K_t:
                pygame.mixer.music.load("dollars.mp3")
                pygame.mixer.music.play()  
    ### Actualisation de la scene ###
    # Gestions des collisions
    oof=pygame.mixer.Sound("oof.mp3")
    for ennemi in listeEnnemis:
        if tir.toucher(ennemi):
            ennemi.disparaitre()
            oof.play()
            player.marquer()
    # placement des objets
    if player.score==68:
        listeEnnemis=[]
        listeEnnemis.append(vaisseau)
        pygame.mixer.music.load("doigbyUI.mp3")
        pygame.mixer.music.play()
    # le joueur
    player.deplacer()
    screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur        
    # la balle
    tir.bouger()
    screen.blit(player.image,[player.rect.x,500]) # appel de la fonction qui dessine le vaisseau du joueur
    # les ennemis
    for ennemi in listeEnnemis:
        ennemi.avancer()
        screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
    # invocation du boss
    if player.score==69:
        screen.blit(siphan0.image,[siphan0.rect.x,15])
        siphan0.health_bar(screen)
        listeEnnemis=[]
        if tir.toucher2(siphan0):
            oof.play()
            siphan0.health-=5
        for shot in listePapiers:
            screen.blit(shot.image,[shot.depart, shot.rect.y])
            if siphan0.health<=500:
                shot.fall()
                if shot.rect.y>=570:
                    shot.back()
            if shot.aie(player):
                player.health-=0.90
        if player.health<=0:
            running = False # running est sur False
            sys.exit() 
        if siphan0.health<=0:
            running = False # running est sur False
            sys.exit() 
    pygame.display.update() # pour ajouter tout changement à l'écran
    clock.tick(FPS)