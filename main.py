import pygame
import time
import random
import math

pygame.init()

pygame.mixer.music.load("beat1814.wav")

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
bluespace = (14, 31, 191)
red = (200, 0, 0)
bright_red = (255, 0, 0)
redtext = (181, 16, 11)
redtextbutton = (161, 16, 11)
limegreen = (38, 224, 38)
bright_limegreen = (38, 255, 38)
greentext = (16, 161, 11)
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Yeger's asteroid")

clock = pygame.time.Clock()

ufoimg = pygame.image.load("ufo80pixel.png")
ufo_width = 79
ufo_height = 45

pygame.display.set_icon(ufoimg)

asteroidimg = pygame.image.load("asteroidsquared62px.png")
asteroid_width = 62
asteroid_height = 51

def asteroidposition(asteroid_startx, asteroid_starty, asteroid_speedx, asteroid_speedy, difficolta):

    asteroid_startx = random.randrange(-100, display_width+100)
    asteroid_starty = random.randrange(-100, display_height+100)

    asteroid_sector = 0

    if asteroid_startx > 0 and asteroid_startx < display_width and asteroid_starty > 0 and asteroid_starty < display_height:
        random_number = random.randrange(1,3)
        if random_number == 1:
            asteroid_startx = random.randrange(-100, 0)
            asteroid_starty = random.randrange(-100, display_height+100)
        if random_number == 2:
            asteroid_startx = random.randrange(display_width, display_width+100)
            asteroid_starty = random.randrange(-100, display_height+100)



    if asteroid_startx < 0 and asteroid_starty < 0:
        asteroid_sector = 1
    if asteroid_startx > 0 and asteroid_startx < display_width and asteroid_starty < 0:
        asteroid_sector = 2
    if asteroid_startx > display_width and asteroid_starty < 0:
        asteroid_sector = 3
    if asteroid_startx > display_width and asteroid_starty > 0 and asteroid_starty < display_height:
        asteroid_sector = 4
    if asteroid_startx > display_width and asteroid_starty > display_height:
        asteroid_sector = 5
    if asteroid_startx > 0 and asteroid_startx < display_width and asteroid_starty > display_height:
        asteroid_sector = 6
    if asteroid_startx < 0 and asteroid_starty > display_height:
        asteroid_sector = 7
    if asteroid_startx < 0 and asteroid_starty > 0 and asteroid_starty < display_height:
        asteroid_sector = 8


    if asteroid_sector == 1:
        asteroid_speedx = random.randrange(1, difficolta)
        asteroid_speedy = random.randrange(1, difficolta)
    if asteroid_sector == 2:
        asteroid_speedx = random.randrange(-difficolta, difficolta)
        asteroid_speedy = random.randrange(1, difficolta)
    if asteroid_sector == 3:
        asteroid_speedx = random.randrange(-difficolta, 0)
        asteroid_speedy = random.randrange(1, difficolta)
    if asteroid_sector == 4:
        asteroid_speedx = random.randrange(-difficolta, 0)
        asteroid_speedy = random.randrange(-difficolta, difficolta)
    if asteroid_sector == 5:
        asteroid_speedx = random.randrange(-difficolta, 0)
        asteroid_speedy = random.randrange(-difficolta, 0)
    if asteroid_sector == 6:
        asteroid_speedx = random.randrange(-difficolta, difficolta)
        asteroid_speedy = random.randrange(-difficolta, 0)
    if asteroid_sector == 7:
        asteroid_speedx = random.randrange(1, difficolta)
        asteroid_speedy = random.randrange(-difficolta, 0)
    if asteroid_sector == 8:
        asteroid_speedx = random.randrange(1, difficolta)
        asteroid_speedy = random.randrange(-difficolta, difficolta)

    #print(difficolta)
    return asteroid_startx, asteroid_starty, asteroid_speedx, asteroid_speedy


def asteroidblit(asteroidx, asteroidy):
    gameDisplay.blit(asteroidimg, (asteroidx, asteroidy))

def ufo(x, y):
    gameDisplay.blit(ufoimg, (x, y))

def textObjects(text, font):
    if text == "Play":
        textSurface = font.render(text, True, greentext)
        return textSurface, textSurface.get_rect()
    if text == "Quit":
        textSurface = font.render(text, True, redtextbutton)
        return textSurface, textSurface.get_rect()

    textSurface = font.render(text, True, redtext)
    return textSurface, textSurface.get_rect()

def message_display(text):
    fonttext = pygame.font.Font("freesansbold.ttf", 120)

    textSurface, textRectangle = textObjects(text, fonttext)
    textRectangle.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textSurface, textRectangle)

    pygame.display.update()

    time.sleep(2)

    #gameloop(asteroid_startx, asteroid_starty, asteroid_speedx, asteroid_speedy, asteroid_startx1, asteroid_starty1, asteroid_speedx1, asteroid_speedy1, asteroid_startx2, asteroid_starty2, asteroid_speedx2, asteroid_speedy2, asteroid_startx3, asteroid_starty3, asteroid_speedx3, asteroid_speedy3, asteroid_startx4, asteroid_starty4, asteroid_speedx4, asteroid_speedy4, asteroid_startx5, asteroid_starty5, asteroid_speedx5, asteroid_speedy5, asteroid_startx6, asteroid_starty6, asteroid_speedx6, asteroid_speedy6, asteroid_startx7, asteroid_starty7, asteroid_speedx7, asteroid_speedy7, record)
    game_intro()

def crash():
    message_display("You Crashed")


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(bluespace)
        fonttext = pygame.font.Font("freesansbold.ttf", 90)
        textSurface, textRectangle = textObjects("Yeger's asteroid", fonttext)
        textRectangle.center = ((display_width/2), (display_height*0.25))
        gameDisplay.blit(textSurface, textRectangle)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(mouse)

        if 350 > mouse[0] > 100 and 450 > mouse[1] > 350:
            pygame.draw.rect(gameDisplay, bright_limegreen, (100, 350, 250, 100))
            if click[0] == 1:
                gameloop(asteroid_startx, asteroid_starty, asteroid_speedx, asteroid_speedy, asteroid_startx1, asteroid_starty1, asteroid_speedx1, asteroid_speedy1, asteroid_startx2, asteroid_starty2, asteroid_speedx2, asteroid_speedy2, asteroid_startx3, asteroid_starty3, asteroid_speedx3, asteroid_speedy3, asteroid_startx4, asteroid_starty4, asteroid_speedx4, asteroid_speedy4, asteroid_startx5, asteroid_starty5, asteroid_speedx5, asteroid_speedy5, asteroid_startx6, asteroid_starty6, asteroid_speedx6, asteroid_speedy6, asteroid_startx7, asteroid_starty7, asteroid_speedx7, asteroid_speedy7, record)
        else:
            pygame.draw.rect(gameDisplay, limegreen, (100, 350, 250, 100))

        smallText = pygame.font.Font("freesansbold.ttf", 50)
        textSurface, textRectangle = textObjects("Play", smallText)
        textRectangle.center = ((220), (400))
        gameDisplay.blit(textSurface, textRectangle)


        if 700 > mouse[0] > 450 and 450 > mouse[1] > 350:
            pygame.draw.rect(gameDisplay, bright_red, (450, 350, 250, 100))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay, red, (450, 350, 250, 100))

        smallText = pygame.font.Font("freesansbold.ttf", 50)
        textSurface, textRectangle = textObjects("Quit", smallText)
        textRectangle.center = ((580), (400))
        gameDisplay.blit(textSurface, textRectangle)

        pygame.display.update()
        clock.tick(15)


def gameloop(asteroid_startx, asteroid_starty, asteroid_speedx, asteroid_speedy, asteroid_startx1, asteroid_starty1, asteroid_speedx1, asteroid_speedy1, asteroid_startx2, asteroid_starty2, asteroid_speedx2, asteroid_speedy2, asteroid_startx3, asteroid_starty3, asteroid_speedx3, asteroid_speedy3, asteroid_startx4, asteroid_starty4, asteroid_speedx4, asteroid_speedy4, asteroid_startx5, asteroid_starty5, asteroid_speedx5, asteroid_speedy5, asteroid_startx6, asteroid_starty6, asteroid_speedx6, asteroid_speedy6, asteroid_startx7, asteroid_starty7, asteroid_speedx7, asteroid_speedy7,record):

    x = (display_width * 0.45)
    y = (display_height * 0.45)

    xchange = 0
    ychange = 0

    global meteoriti_schivati
    meteoriti_schivati = 0

    gameExit = False

    while gameExit == False:

        for event in pygame.event.get():

            keyStates = pygame.key.get_pressed()

            if keyStates[pygame.K_LEFT]:
                xchange = -8
                ychange = 0
            elif keyStates[pygame.K_RIGHT]:
                xchange = 8
                ychange = 0
            elif keyStates[pygame.K_UP]:
                ychange = -8
                xchange = 0
            elif keyStates[pygame.K_DOWN]:
                ychange = 8
                xchange = 0
            else:
                xchange = 0
                ychange = 0

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        x += xchange
        y += ychange

        gameDisplay.fill(bluespace)

        if asteroid_startx > display_width+200 or asteroid_startx < -200 or asteroid_starty > display_height+200 or asteroid_starty < -200:
            asteroid_startx, asteroid_starty, asteroid_speedx, asteroid_speedy = asteroidposition(asteroid_startx, asteroid_starty, asteroid_speedx, asteroid_speedy, int(-0.85+(3.5*math.log(meteoriti_schivati+3))))
            meteoriti_schivati += 1

        if asteroid_startx1 > display_width+200 or asteroid_startx1 < -200 or asteroid_starty1 > display_height+200 or asteroid_starty1 < -200:
            asteroid_startx1, asteroid_starty1, asteroid_speedx1, asteroid_speedy1 = asteroidposition(asteroid_startx1, asteroid_starty1, asteroid_speedx1, asteroid_speedy1, int(-0.85+(3.5*math.log(meteoriti_schivati+3))))

        if asteroid_startx2 > display_width+200 or asteroid_startx2 < -200 or asteroid_starty2 > display_height+200 or asteroid_starty2 < -200:
            asteroid_startx2, asteroid_starty2, asteroid_speedx2, asteroid_speedy2 = asteroidposition(asteroid_startx2, asteroid_starty2, asteroid_speedx2, asteroid_speedy2, int(-0.85+(3.5*math.log(meteoriti_schivati+3))))

        if asteroid_startx3 > display_width+200 or asteroid_startx3 < -200 or asteroid_starty3 > display_height+200 or asteroid_starty3 < -200:
            asteroid_startx3, asteroid_starty3, asteroid_speedx3, asteroid_speedy3 = asteroidposition(asteroid_startx3, asteroid_starty3, asteroid_speedx3, asteroid_speedy3, int(-0.85+(3.5*math.log(meteoriti_schivati+3))))

        if asteroid_startx4 > display_width+200 or asteroid_startx4 < -200 or asteroid_starty4 > display_height+200 or asteroid_starty4 < -200:
            asteroid_startx4, asteroid_starty4, asteroid_speedx4, asteroid_speedy4 = asteroidposition(asteroid_startx4, asteroid_starty4, asteroid_speedx4, asteroid_speedy4, int(-0.85+(3.5*math.log(meteoriti_schivati+3))))

        if asteroid_startx5 > display_width+200 or asteroid_startx5 < -200 or asteroid_starty5 > display_height+200 or asteroid_starty5 < -200:
            asteroid_startx5, asteroid_starty5, asteroid_speedx5, asteroid_speedy5 = asteroidposition(asteroid_startx5, asteroid_starty5, asteroid_speedx5, asteroid_speedy5, int(-0.85+(3.5*math.log(meteoriti_schivati+3))))

        if asteroid_startx6 > display_width+200 or asteroid_startx6 < -200 or asteroid_starty6 > display_height+200 or asteroid_starty6 < -200:
            asteroid_startx6, asteroid_starty6, asteroid_speedx6, asteroid_speedy6 = asteroidposition(asteroid_startx6, asteroid_starty6, asteroid_speedx6, asteroid_speedy6, int(-0.85+(3.5*math.log(meteoriti_schivati+3))))

        if asteroid_startx7 > display_width+200 or asteroid_startx7 < -200 or asteroid_starty7 > display_height+200 or asteroid_starty7 < -200:
            asteroid_startx7, asteroid_starty7, asteroid_speedx7, asteroid_speedy7 = asteroidposition(asteroid_startx7, asteroid_starty7, asteroid_speedx7, asteroid_speedy7, int(-0.85+(3.5*math.log(meteoriti_schivati+3))))

        asteroidblit(asteroid_startx, asteroid_starty)
        asteroidblit(asteroid_startx1, asteroid_starty1)
        asteroidblit(asteroid_startx2, asteroid_starty2)
        asteroidblit(asteroid_startx3, asteroid_starty3)
        asteroidblit(asteroid_startx4, asteroid_starty4)
        asteroidblit(asteroid_startx5, asteroid_starty5)
        asteroidblit(asteroid_startx6, asteroid_starty6)
        asteroidblit(asteroid_startx7, asteroid_starty7)

        asteroid_startx += asteroid_speedx
        asteroid_starty += asteroid_speedy

        asteroid_startx1 += asteroid_speedx1
        asteroid_starty1 += asteroid_speedy1

        asteroid_startx2 += asteroid_speedx2
        asteroid_starty2 += asteroid_speedy2

        asteroid_startx3 += asteroid_speedx3
        asteroid_starty3 += asteroid_speedy3

        asteroid_startx4 += asteroid_speedx4
        asteroid_starty4 += asteroid_speedy4

        asteroid_startx5 += asteroid_speedx5
        asteroid_starty5 += asteroid_speedy5

        asteroid_startx6 += asteroid_speedx6
        asteroid_starty6 += asteroid_speedy6

        asteroid_startx7 += asteroid_speedx7
        asteroid_starty7 += asteroid_speedy7

        #print(asteroid_startx, asteroid_starty)

        ufo(x, y)


        font = pygame.font.SysFont(None, 25)
        textscore = font.render("Score: "+str(meteoriti_schivati), True, white)
        gameDisplay.blit(textscore, (0, 0))


        pygame.display.update() #senza parametri aggiorna tutto il display
        clock.tick(60)

        if x < 0 or y < 0 or x > display_width-ufo_width or y > display_height-ufo_height:
            crash()

        if (asteroid_startx > x+5) and (asteroid_startx < x+ufo_width-5) and (asteroid_starty > y+5) and (asteroid_starty < y+ufo_height) :
            crash()
        if (asteroid_startx+asteroid_width > x+5) and (asteroid_startx+asteroid_width < x+ufo_width-5) and (asteroid_starty > y+5) and (asteroid_starty < y+ufo_height) :
            crash()
        if (asteroid_startx+asteroid_width > x+5) and (asteroid_startx+asteroid_width < x+ufo_width-5) and (asteroid_starty+asteroid_height > y+5) and (asteroid_starty+asteroid_height < y+ufo_height) :
            crash()
        if (asteroid_startx > x+5) and (asteroid_startx < x+ufo_width-5) and (asteroid_starty+asteroid_height > y+5) and (asteroid_starty+asteroid_height < y+ufo_height) :
            crash()


        if (asteroid_startx1 > x+5) and (asteroid_startx1 < x+ufo_width-5) and (asteroid_starty1 > y+5) and (asteroid_starty1 < y+ufo_height) :
            crash()
        if (asteroid_startx1+asteroid_width > x+5) and (asteroid_startx1+asteroid_width < x+ufo_width-5) and (asteroid_starty1 > y+5) and (asteroid_starty1 < y+ufo_height) :
            crash()
        if (asteroid_startx1+asteroid_width > x+5) and (asteroid_startx1+asteroid_width < x+ufo_width-5) and (asteroid_starty1+asteroid_height > y+5) and (asteroid_starty1+asteroid_height < y+ufo_height) :
            crash()
        if (asteroid_startx1 > x+5) and (asteroid_startx1 < x+ufo_width-5) and (asteroid_starty1+asteroid_height > y+5) and (asteroid_starty1+asteroid_height < y+ufo_height) :
            crash()

        if (asteroid_startx2 > x+5) and (asteroid_startx2 < x+ufo_width-5) and (asteroid_starty2 > y+5) and (asteroid_starty2 < y+ufo_height) :
            crash()
        if (asteroid_startx2+asteroid_width > x+5) and (asteroid_startx2+asteroid_width < x+ufo_width-5) and (asteroid_starty2 > y+5) and (asteroid_starty2 < y+ufo_height) :
            crash()
        if (asteroid_startx2+asteroid_width > x+5) and (asteroid_startx2+asteroid_width < x+ufo_width-5) and (asteroid_starty2+asteroid_height > y+5) and (asteroid_starty2+asteroid_height < y+ufo_height) :
            crash()
        if (asteroid_startx2 > x+5) and (asteroid_startx2 < x+ufo_width-5) and (asteroid_starty2+asteroid_height > y+5) and (asteroid_starty2+asteroid_height < y+ufo_height) :
            crash()

        if (asteroid_startx3 > x+5) and (asteroid_startx3 < x+ufo_width-5) and (asteroid_starty3 > y+5) and (asteroid_starty3 < y+ufo_height) :
            crash()
        if (asteroid_startx3+asteroid_width > x+5) and (asteroid_startx3+asteroid_width < x+ufo_width-5) and (asteroid_starty3 > y+5) and (asteroid_starty3 < y+ufo_height) :
            crash()
        if (asteroid_startx3+asteroid_width > x+5) and (asteroid_startx3+asteroid_width < x+ufo_width-5) and (asteroid_starty3+asteroid_height > y+5) and (asteroid_starty3+asteroid_height < y+ufo_height) :
            crash()
        if (asteroid_startx3 > x+5) and (asteroid_startx3 < x+ufo_width-5) and (asteroid_starty3+asteroid_height > y+5) and (asteroid_starty3+asteroid_height < y+ufo_height) :
            crash()

        if (asteroid_startx4 > x+5) and (asteroid_startx4 < x+ufo_width-5) and (asteroid_starty4 > y+5) and (asteroid_starty4 < y+ufo_height) :
            crash()
        if (asteroid_startx4+asteroid_width > x+5) and (asteroid_startx4+asteroid_width < x+ufo_width-5) and (asteroid_starty4 > y+5) and (asteroid_starty4 < y+ufo_height) :
            crash()
        if (asteroid_startx4+asteroid_width > x+5) and (asteroid_startx4+asteroid_width < x+ufo_width-5) and (asteroid_starty4+asteroid_height > y+5) and (asteroid_starty4+asteroid_height < y+ufo_height) :
            crash()
        if (asteroid_startx4 > x+5) and (asteroid_startx4 < x+ufo_width-5) and (asteroid_starty4+asteroid_height > y+5) and (asteroid_starty4+asteroid_height < y+ufo_height) :
            crash()

        if (asteroid_startx5 > x+5) and (asteroid_startx5 < x+ufo_width-5) and (asteroid_starty5 > y+5) and (asteroid_starty5 < y+ufo_height) :
            crash()
        if (asteroid_startx5+asteroid_width > x+5) and (asteroid_startx5+asteroid_width < x+ufo_width-5) and (asteroid_starty5 > y+5) and (asteroid_starty5 < y+ufo_height) :
            crash()
        if (asteroid_startx5+asteroid_width > x+5) and (asteroid_startx5+asteroid_width < x+ufo_width-5) and (asteroid_starty5+asteroid_height > y+5) and (asteroid_starty5+asteroid_height < y+ufo_height) :
            crash()
        if (asteroid_startx5 > x+5) and (asteroid_startx5 < x+ufo_width-5) and (asteroid_starty5+asteroid_height > y+5) and (asteroid_starty5+asteroid_height < y+ufo_height) :
            crash()

        if (asteroid_startx6 > x+5) and (asteroid_startx6 < x+ufo_width-5) and (asteroid_starty6 > y+5) and (asteroid_starty6 < y+ufo_height) :
            crash()
        if (asteroid_startx6+asteroid_width > x+5) and (asteroid_startx6+asteroid_width < x+ufo_width-5) and (asteroid_starty6 > y+5) and (asteroid_starty6 < y+ufo_height) :
            crash()
        if (asteroid_startx6+asteroid_width > x+5) and (asteroid_startx6+asteroid_width < x+ufo_width-5) and (asteroid_starty6+asteroid_height > y+5) and (asteroid_starty6+asteroid_height < y+ufo_height) :
            crash()
        if (asteroid_startx6 > x+5) and (asteroid_startx6 < x+ufo_width-5) and (asteroid_starty6+asteroid_height > y+5) and (asteroid_starty6+asteroid_height < y+ufo_height) :
            crash()

        if (asteroid_startx7 > x+5) and (asteroid_startx7 < x+ufo_width-5) and (asteroid_starty7 > y+5) and (asteroid_starty7 < y+ufo_height) :
            crash()
        if (asteroid_startx7+asteroid_width > x+5) and (asteroid_startx7+asteroid_width < x+ufo_width-5) and (asteroid_starty7 > y+5) and (asteroid_starty7 < y+ufo_height) :
            crash()
        if (asteroid_startx7+asteroid_width > x+5) and (asteroid_startx7+asteroid_width < x+ufo_width-5) and (asteroid_starty7+asteroid_height > y+5) and (asteroid_starty7+asteroid_height < y+ufo_height) :
            crash()
        if (asteroid_startx7 > x+5) and (asteroid_startx7 < x+ufo_width-5) and (asteroid_starty7+asteroid_height > y+5) and (asteroid_starty7+asteroid_height < y+ufo_height) :
            crash()


#main:
asteroid_startx = 9999999
asteroid_starty = 9999999
asteroid_speedx = 0
asteroid_speedy = 0

asteroid_startx1 = 9999999
asteroid_starty1 = 9999999
asteroid_speedx1 = 0
asteroid_speedy1 = 0

asteroid_startx2 = 9999999
asteroid_starty2 = 9999999
asteroid_speedx2 = 0
asteroid_speedy2 = 0

asteroid_startx3 = 9999999
asteroid_starty3 = 9999999
asteroid_speedx3 = 0
asteroid_speedy3 = 0


asteroid_startx4 = 9999999
asteroid_starty4 = 9999999
asteroid_speedx4 = 0
asteroid_speedy4 = 0

asteroid_startx5 = 9999999
asteroid_starty5 = 9999999
asteroid_speedx5 = 0
asteroid_speedy5 = 0

asteroid_startx6 = 9999999
asteroid_starty6 = 9999999
asteroid_speedx6 = 0
asteroid_speedy6 = 0

asteroid_startx7 = 9999999
asteroid_starty7 = 9999999
asteroid_speedx7 = 0
asteroid_speedy7 = 0

record = 0

pygame.mixer.music.play(-1)
game_intro()

pygame.quit()
quit()
