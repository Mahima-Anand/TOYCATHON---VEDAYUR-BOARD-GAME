import pygame
global p
import functions

class leaderboard():
    winamount = 100000
    def __init__(self):
        
        self.name = "Mahaa"
        
fps = 100
clock = pygame.time.Clock()       
    
p = [leaderboard(),leaderboard()]

def screen1(a,b,c):    #for running screen 1
    
    leaderboard.winamount = (int)(c.get())
    p[1].name = b.get()
    p[0].name = a.get()

    pygame.init()

    display_width = 1430
    display_height = 800

    white = (255,255,255)
    black = (0,0,0)
    yellow = (255,255,0)
    red = (255,50,0)
    blue = (0,0,255)
    green = (0,255,0)
    back = (100,10,100)
    lblue = (228, 249, 245)



    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        x = 1050
        y1= 100
        y2= 200
    
        l=200
        h=50

        functions.gameDisplay.fill(back)
        img = pygame.image.load('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/startvedayur_.png')  #adding image
        functions.gameDisplay.blit(img, (0,0))
        #adding start button
        functions.button("START",x,y1,l,h,yellow,lblue,"next",black)   
        #adding quit button
        #functions.button("RULES",x,y2,l,h,yellow,white,"rules",black)     
        #adding quit button
        functions.button("QUIT",x,y2,l,h,yellow,lblue,"quit1",black)
        
       

        
        pygame.display.update()