import pygame
import random
pygame.init()
pygame.mixer.init()

screen_width = 320  
screen_height = 500

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("            FLAPPY BIRD")
pygame.display.update()

birdx = 50
birdy = 150
birdh = 30
birdw = 40
grdx = 0
grdy = 440
piph = 440
pipw = 37
up = 45
downspeed = 2
pipespeed = 1

bg = pygame.image.load("img/back.png")
bg = pygame.transform.scale(bg,(screen_width,screen_height)).convert_alpha()
start = pygame.image.load("img/start.jpg")
start = pygame.transform.scale(start,(screen_width,screen_height))
game = pygame.image.load("img/gameover.png")
game = pygame.transform.scale(game,(300,75))
night = pygame.image.load("img/night.png")
night = pygame.transform.scale(night,(screen_width,screen_height))
msg = pygame.image.load("img/msg.png")
msg = pygame.transform.scale(msg,(230,350))

birdu = pygame.image.load("img/birdu.png")
birdu = pygame.transform.scale(birdu,(birdw,birdh)).convert_alpha()
birdd = pygame.image.load("img/birdd.png")
birdd = pygame.transform.scale(birdd,(birdw,birdh)).convert_alpha()

bird2 = pygame.transform.scale(birdd,(50,35)).convert_alpha()

pipe = pygame.image.load("img/pipe.png")
pipe = pygame.transform.scale(pipe,(pipw,piph)).convert_alpha()
piper = pygame.image.load("img/piper.png")
piper = pygame.transform.scale(piper,(pipw,piph)).convert_alpha()
grd = pygame.image.load("img/ground.jpg")
grd = pygame.transform.scale(grd,(600,100 )).convert_alpha() 

enter = pygame.image.load("img/enter.jpg")
enter = pygame.transform.scale(enter,(170,30)).convert_alpha()
def middleloop():
    down = 1
    grdx = 0
    groundspeed = 3
    birdy = 150
    while True:
        screen.blit(night,(0,0))
        screen.blit(grd,(grdx,grdy))
        screen.blit(birdu,(birdx,birdy+90))
        screen.blit(msg,(45,20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type== pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameloop()
        birdy += down
        if grdx==-45:
            grdx = 0
        if birdy == 180:
            birdy = 150
            pygame.mixer.music.load("sounds/swoosh.mp3")
            pygame.mixer.music.play()
        pygame.display.update()
        grdx += -groundspeed
        pygame.display.update()
        pygame.time.Clock().tick(80)


def gameloop():
    birdh = 30
    birdw = 40
    birdu = pygame.image.load("img/birdu.png")
    birdu = pygame.transform.scale(birdu,(birdw,birdh)).convert_alpha()
    birdx = 50
    birdy = 150
    birdh = 30
    birdw = 40
    grdx = 0
    grdy = 440
    piph = 440
    pipw = 37
    up = 60
    downspeed = 2
    pipespeed = 1
    groundspeed = 3


    pipx1 = 400
    pipx2 = 570
    pipx3 = 740
    pipx4 = 910
    pipx5 = 1080
    pipx6 = 1250

    pipry1 = -295
    pipry2 = -190
    pipry3 = -340
    pipry5 = -180
    pipry6 = -100

    pipy1 = 265
    pipy2 = 360
    pipy3 = 200
    pipy4 = 120
    pipy5 = 360
       
    gameover = False
    while not gameover:
        screen.blit(bg,(0,0))

        screen.blit(pipe,(pipx1,pipy1))           
        screen.blit(piper,(pipx1,pipry1))         
        screen.blit(piper,(pipx2,pipry2))          
        screen.blit(pipe,(pipx2,pipy2))            
        screen.blit(piper,(pipx3,pipry3))           
        screen.blit(pipe,(pipx3,pipy3))             
        screen.blit(pipe,(pipx4,pipy4))
        screen.blit(piper,(pipx5,pipry5))
        screen.blit(pipe,(pipx5,pipy5))
        screen.blit(piper,(pipx6,pipry6))

        screen.blit(birdu,(birdx,birdy))
        screen.blit(grd,(grdx,grdy))


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    birdy += -up
                    pygame.mixer.music.load("sounds/wing.mp3")
                    pygame.mixer.music.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                birdy += -up
                pygame.mixer.music.load("sounds/wing.mp3")
                pygame.mixer.music.play()
                            
        if birdx in range(pipx1-birdh,(pipx1-birdh)+pipw) and birdy in range (pipry1,pipry1+440):
            up = 0
            pipespeed = 0
            downspeed += 2
            pygame.mixer.music.load("sounds/hit.mp3")
            pygame.mixer.music.play()
        if birdx in range(pipx2-birdh,(pipx2-birdh)+pipw) and birdy in range (pipry2,pipry2+440):
            up = 0
            pipespeed = 0      
            downspeed += 2
            pygame.mixer.music.load("sounds/hit.mp3")
            pygame.mixer.music.play()
        if birdx in range(pipx3-birdh,(pipx3-birdh)+pipw) and birdy in range (pipry3,pipry3+440):
            downspeed += 2
            up = 0
            pipespeed = 0
            pygame.mixer.music.load("sounds/hit.mp3")
            pygame.mixer.music.play()
        if birdx in range(pipx5-birdh,(pipx5-birdh)+pipw) and birdy in range (pipry5,pipry5+440):
            downspeed += 2
            up = 0
            pipespeed = 0
            pygame.mixer.music.load("sounds/hit.mp3")
            pygame.mixer.music.play()
        if birdx in range(pipx6-birdh,(pipx6-birdh)+pipw) and birdy in range (pipry6,pipry6+440):
            downspeed += 2
            up = 0
            pipespeed = 0
            pygame.mixer.music.load("sounds/hit.mp3")
            pygame.mixer.music.play()

        if birdx in range(pipx1-birdw,(pipx1-birdw)+pipw) and (birdy+birdh) in range (pipy1,(pipy1+440)):
            downspeed += 2
            up =  0
            pipespeed = 0
            pygame.mixer.music.load("sounds/hit.mp3")
            pygame.mixer.music.play()

        if birdx in range(pipx2-birdw,(pipx2-birdw)+pipw) and (birdy+birdh) in range (pipy2,(pipy2+440)):
            downspeed += 2
            up =  0
            pipespeed = 0
            pygame.mixer.music.load("sounds/hit.mp3")
            pygame.mixer.music.play()
        if birdx in range(pipx3-birdw,(pipx3-birdw)+pipw) and (birdy+birdh) in range (pipy3,(pipy3+440)):
            downspeed += 2
            up =  0
            pipespeed = 0
            pygame.mixer.music.load("sounds/hit.mp3")
            pygame.mixer.music.play()
        if birdx in range(pipx4-birdw,(pipx4-birdw)+pipw) and (birdy+birdh) in range (pipy4,(pipy4+440)):
            downspeed += 2
            up =  0
            pipespeed = 0
            pygame.mixer.music.load("sounds/hit.mp3")
            pygame.mixer.music.play()
        if birdx in range(pipx5-birdw,(pipx5-birdw)+pipw) and (birdy+birdh) in range (pipy5,(pipy5+440)):
            downspeed += 2
            up =  0  
            pipespeed = 0    
            pygame.mixer.music.load("sounds/hit.mp3")
            pygame.mixer.music.play()

        if birdx == pipx1 or birdx == pipx2 or birdx == pipx3 or birdx == pipx4 or birdx == pipx5 or birdx == pipx6:
            pygame.mixer.music.load("sounds/point.mp3")
            pygame.mixer.music.play()

        if pipx1 < -pipw:
            pipx1 += 1020
        if pipx2 < -pipw:
            pipx2 += 1020
        if pipx3 < -pipw:
            pipx3 += 1020
        if pipx4 < -pipw:
            pipx4 += 1020
        if pipx5 < -pipw:
            pipx5 += 1020
        if pipx6 < -pipw:
            pipx6 += 1020  

        if (birdy+30) > grdy:
            groundspeed = 0
            downspeed = 0
            birdx = 1800
            birdy = 200
            pygame.mixer.music.load("sounds/die.mp3")
            pygame.mixer.music.play()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        middleloop()
          
        if birdy<0:
            groundspeed = 0
            downspeed = 0
            birdx = 1800
            birdy = 200
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        middleloop()
        if birdx > 700:
            screen.blit(game,(10,100))
            screen.blit(enter,(-20,475))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        middleloop()
                if event.type== pygame.MOUSEBUTTONDOWN:
                    middleloop()

            
        if grdx == -45:
            grdx = 0
     
        birdy += downspeed
        grdx += -groundspeed
        pipx1 += -pipespeed
        pipx2 += -pipespeed
        pipx3 += -pipespeed
        pipx4 += -pipespeed
        pipx5 += -pipespeed
        pipx6 += -pipespeed

        pygame.display.update()
        pygame.time.Clock().tick(80)

def startloopp():
    birdx2 = 130
    birdy2 = 166
    grdx = 0
    while True:
        screen.blit(start,(0,0))
        screen.blit(bird2,(birdx2,birdy2))
        screen.blit(grd,(grdx,grdy))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    middleloop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                middleloop()
        grdx+= -3
        birdy2 += 1
        if grdx == -30:
            grdx = 0
        if birdy2 == 188:
            birdy2 = 160
            pygame.mixer.music.load("sounds/swoosh.mp3")
            pygame.mixer.music.play()

        pygame.time.Clock().tick(70)
        pygame.display.update()
middleloop()
pygame.QUIT
quit()



