import pygame,time
import functions,Property,player,firstpage
from tkinter import *

pygame.init()
#initialising all the hard coding values
display_width = 1430
display_height = 800
card_length = 130
card_breadth = 60
blockl = 120
blockh = 50
boxl = 350
boxb = 215
gapv = (display_height - 2*boxl)/3
gaph = (display_width - display_height - 2*boxb)/3
#initialising all the colour with the respective RGB values
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
red = (200,0,0)
blue = (0,0,255)
green = (0,150,0)
lblue = (0,0,100)

maroon = (100,10,100)
grey = (160,160,160)
orange = (228,142,88)
mauve = (188,143,143)
lgreen = (144,238,144)
llblue = (255,192,203) #pink
plum = (221,160,221)
#initialising all the checkpoints used throughout the program
player_index = 0
rollonce = 0
card_display = 0
endturn = 0
key = 0
place = " "
timer = 8
n=0
incometax = 0
gotojail = 0
cround = [0,0]
round_complete = 0
spcard_display = 0
railway = 0
rent = 0
rolloncejail = 0
temporary = 0
chance = 0
comm = 0
gameover = 0
timerr = 8
risk = 0

__font = pygame.font.Font('freesansbold.ttf',15)

fps = 1000
clock = pygame.time.Clock()

#the main funtion
def mainscreen():
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                gameExit = True
        
        #updating the screen again and again 
        drawing()
        clock.tick(fps)
                
#this sketches the screen  
def drawing():
    #global variables called
            global key,timer,incometax,gotojail,round_complete,cround,rent,railway,temporary,chance,rollonce,endturn,timerr,risk
            #side bg
            functions.gameDisplay.fill(black)
            
            pygame.draw.rect(functions.gameDisplay, white, [0,0,display_height,display_height])
            #main board bg
            pygame.draw.rect(functions.gameDisplay, white, [card_length,card_length,display_height-2*card_length,display_height - 2*card_length])
            _font = pygame.font.Font('freesansbold.ttf',20)

            pygame.draw.rect(functions.gameDisplay,plum, [display_height + gaph,gapv,boxb,boxl])
            #pygame.draw.rect(functions.gameDisplay,mauve, [display_height + gaph,boxl + 2*gapv,boxb,boxl])
            pygame.draw.rect(functions.gameDisplay,llblue, [1100,30,boxb,boxl])
            
            #board sketched
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/groww.png',display_height-card_length,display_height-card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/just.png',display_height-card_length,0)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/v.png',0,0)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/univrsity.png',0,display_height-card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/luck.png',card_length+2*card_breadth,display_height-card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/luck2.png',display_height-card_length,card_length+5*card_breadth)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/luck.png',card_breadth+card_length,0)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/comm.png',7*card_breadth+card_length,display_height-card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/comm1.png',0,2*card_breadth+card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/comm2.png',display_height-card_length,2*card_breadth+card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/clinic_copy.png',7*card_breadth+card_length,0)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/pharmacy.png',0,7*card_breadth+card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/yogalaya.png',display_height-card_length,7*card_breadth+card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/clinic.png',card_length+5*card_breadth,display_height-card_length)
            
            #Krish names
            #cinamonfunctions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/Aparajita.png',1*card_breadth+card_length,0)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/Aparajita.png',0*card_breadth+card_length,display_height-card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/Hibiscus.png',1*card_breadth+card_length,display_height-card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/Bringaraj.png',3*card_breadth+card_length,display_height-card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/Fenugreek.png',6*card_breadth+card_length,display_height-card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/Ajwain.png',8*card_breadth+card_length,display_height-card_length)

            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/tumeric.png',0,0*card_breadth+card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/ginger.png',0,1*card_breadth+card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/shatavari.png',0,3*card_breadth+card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/cardamom.png',0,5*card_breadth+card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/cumin.png',0,6*card_breadth+card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/lotus.png',0,8*card_breadth+card_length)

            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/manjistha.png',0*card_breadth+card_length,0)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/cinamon.png',2*card_breadth+card_length,0)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/guggul.png',3*card_breadth+card_length,0)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/ashwagandha.png',5*card_breadth+card_length,0)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/pepper.png',6*card_breadth+card_length,0)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/amla.png',8*card_breadth+card_length,0)

            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/bhibitaki.png',display_height-card_length,0*card_breadth+card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/moringa.png',display_height-card_length,1*card_breadth+card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/kalmegh.png',display_height-card_length,3*card_breadth+card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/Tulsi.png',display_height-card_length,6*card_breadth+card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/Neem.png',display_height-card_length,8*card_breadth+card_length)

            #Factory 
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/factory1.png',4*card_breadth+card_length,display_height-card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/factory2.png',0,4*card_breadth+card_length)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/factory3.png',4*card_breadth+card_length,0)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/factory4.png',display_height-card_length,4*card_breadth+card_length)
           
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/image_.png',130,130)
            functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/benifits.png',1100,670)
         
            
            #sketching dice
            functions.text_in_box("Abhineta %r's turn "%(player_index+1),_font,black,card_length,card_length,(display_height-2*card_length)/2,blockh)
            if functions.a == 1:
                functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/dice1_.png',display_height/2 - 30 ,card_length + 10)
            if functions.a == 2:
                functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/dice2_.png',display_height/2 - 30,card_length + 10)
            if functions.a == 3:
                functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/dice3_.png',display_height/2 - 30,card_length + 10)
            if functions.a == 4:
                functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/dice4_.png',display_height/2 - 30,card_length + 10)
            if functions.a == 5:
                functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/dice5_.png',display_height/2 - 30,card_length + 10)
            if functions.a == 6:
                functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/dice6_.png',display_height/2 - 30,card_length + 10)
            if functions.b== 1:
                functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/dice1_.png',display_height/2 + 50,card_length + 10)
            if functions.b == 2:
                functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/dice2_.png',display_height/2 + 50,card_length + 10)
            if functions.b == 3:
                functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/dice3_.png',display_height/2 + 50,card_length + 10)
            if functions.b == 4:
                functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/dice4_.png',display_height/2 + 50,card_length + 10)
            if functions.b == 5:
                functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/dice5_.png',display_height/2 + 50,card_length + 10)
            if functions.b == 6:
                functions.addimage('C:/Users/HP/Documents/DS/Toycathon/Monopoly-game-master/images/dice6_.png',display_height/2 + 50,card_length + 10)
        
        
            

            #sketching buttons
            Button("ROLL DICE",display_height + gaph,2*gapv+boxl + 0.1*boxl ,boxb,0.1*boxl,yellow,white,"roll",red)
            Button("MORTGAGE",display_height + gaph,2*gapv+boxl+0.7*boxl,boxb,0.1*boxl,red,white,"mort",red)
            Button("END TURN",display_height + gaph,2*gapv+boxl+0.9*boxl,boxb,0.1*boxl,yellow,white,"endturn",red)
            Button("BUILD",display_height + gaph,2*gapv+boxl+0.5*boxl,boxb,0.1*boxl,yellow,white,"build",red)
            Button("SELL",display_height + gaph,2*gapv+boxl+0.3*boxl,boxb,0.1*boxl,yellow,white,"sell",red)
            #sketching properties on board
            Property._property["manjistha"].locmaker()
            Property._property["cinnamon"].locmaker()
            Property._property["guggul"].locmaker()
            Property._property["ashwagandha"].locmaker()
            Property._property["pepper"].locmaker()
            Property._property["amla"].locmaker()
            Property._property["bhibitaki"].locmaker()
            Property._property["moringa"].locmaker()
            Property._property["kalmegh"].locmaker()
            Property._property["tumeric"].locmaker()
            Property._property["ginger"].locmaker()
            Property._property["shatavari"].locmaker()
            Property._property["cardamom"].locmaker()
            Property._property["cumin"].locmaker()
            Property._property["lotus"].locmaker()
            Property._property["aparjita"].locmaker()
            Property._property["hibiscus"].locmaker()
            Property._property["bringaraj"].locmaker()
            Property._property["tulsi"].locmaker()
            Property._property["neem"].locmaker()
            Property._property["fenugreek"].locmaker()
            Property._property["ajwain"].locmaker()
            Property.sproperty["factory1"].locmaker()
            Property.sproperty["factory2"].locmaker()
            Property.sproperty["factory3"].locmaker()
            Property.sproperty["factory4"].locmaker()
            _font_ = pygame.font.Font('freesansbold.ttf',50)
            lack_font = pygame.font.Font('freesansbold.ttf',40)
            #checking if someone reached winning amount 
            if player.player[0].total_wealth >= firstpage.p[0].winamount or player.player[1].total_wealth >= firstpage.p[0].winamount:
                rollonce = 1
                endturn = 1
                
                if player.player[0].total_wealth >= firstpage.p[0].winamount:
                    functions.gameDisplay.fill(black)
                    functions.text_in_box("%r Won...Congratulations!!!"%firstpage.p[0].name,_font_,orange,card_length,(display_height/2+card_length)/2 + 1.25*blockh,display_height- 2*card_length,display_height/2 - ((display_height/2+card_length)/2 + 1.25*blockh))

                if player.player[1].total_wealth >= firstpage.p[0].winamount:
                    functions.gameDisplay.fill(black)
                    functions.text_in_box("%r Won...Congratulations!!!"%firstpage.p[1].name,_font_,orange,card_length,(display_height/2+card_length)/2 + 1.25*blockh,display_height- 2*card_length,display_height/2 - ((display_height/2+card_length)/2 + 1.25*blockh))
            
            if player.player[0].total_wealth <=0:
                functions.gameDisplay.fill(black)
                functions.text_in_box("%r Won...Congratulations!!!"%firstpage.p[1].name,_font_,orange,card_length,(display_height/2+card_length)/2 + 1.25*blockh,display_height- 2*card_length,display_height/2 - ((display_height/2+card_length)/2 + 1.25*blockh))
            
            if player.player[1].total_wealth <=0:
                functions.gameDisplay.fill(black)
                functions.text_in_box("%r Won...Congratulations!!!"%firstpage.p[0].name,_font_,orange,card_length,(display_height/2+card_length)/2 + 1.25*blockh,display_height- 2*card_length,display_height/2 - ((display_height/2+card_length)/2 + 1.25*blockh))
            #checking if someone cash <=0
            if player.player[player_index].cash < 0:
                functions.text_in_box("Oops ! %r ,You are lack of kanishk, sell your krish to play more !"%firstpage.p[player_index].name,__font,red,card_length,130,510,1000)
                risk = 1
                endturn = 1
            if risk == 1 and player.player[player_index].cash > 0:
                endturn = 0
                
            if round_complete == 1:
                functions.text_in_box("You Crossed Grow , You gained 400 kanishk",__font,orange,card_length,130,510,1000)
                if timerr == 8:
                    player.player[player_index].cash += 400
                    player.player[player_index].total_wealth += 400
                    cround[player_index]-=40
                timerr-=3
                if timerr == 0:
                        
                        round_complete = 0
                        timerr = 8
#running different functions based on the call
            if spcard_display == 1:
                spcard_displayy()

            if railway == 1:
                railways()

            if card_display == 1:
                Prop()

            if chance == 1:
                Chance()
            if comm == 1:
                CommChest()
          

            if incometax == 1:
                if key == 0:
                    player.player[player_index].total_wealth = 0.9*player.player[player_index].total_wealth
                    player.player[player_index].cash = 0.9*(player.player[player_index].total_wealth*10/9)
                    key = 2
                if key == 2:
                    timer-=3
                    functions.text_in_box("You have reached Yogalaya ! Pay fee of kanishk %r"%(0.1*(player.player[player_index].total_wealth*10/9)),__font,orange,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
                    if timer == 0:
                        incometax = 0
                        timer = 8
                        key = 1
            elif incometax == 2:
                if key == 0:
                    player.player[player_index].total_wealth -= 500 
                    player.player[player_index].cash -= 500
                    key = 2
                if key == 2:
                    timer-=3
                    functions.text_in_box("Enjoy your peaceful time !",__font,orange,display_height/2,display_height/2 +20 ,display_height/2-card_length,display_height/2-card_length)
                    if timer == 0:
                        incometax = 0
                        timer = 8
                        key = 1                               
            player.player[1].draw()
            player.player[0].draw()
#sketching the players boxes
            for item,tempo in Property._property.items():
                Property._property[item].squares()
            Property.sproperty["pharmacy"].squares()
            Property.sproperty["clinic"].squares()
            Property.sproperty["factory1"].squares()
            Property.sproperty["factory2"].squares()
            Property.sproperty["factory3"].squares()
            Property.sproperty["factory4"].squares()
            
            if Property.tflag == 1:
                if Property.temo == Property.sproperty["factory1"] or Property.temo == Property.sproperty["factory2"] or Property.temo == Property.sproperty["factory3"] or Property.temo == Property.sproperty["factory4"]:
                    Property.temo.rcard()
                    
                else :
                    Property.temo.card()
                
            if gotojail == 1:
                GoToJail()
                

            functions.text_in_box(firstpage.p[0].name,_font,black,display_height + gaph,gapv,boxb,0.1*boxl)
            functions.text_in_box("Kanishk %r"%player.player[0].cash,_font,black,display_height + gaph,gapv + 0.1*boxl ,boxb,0.1*boxl)
            functions.text_in_box("Net Worth %r"%player.player[0].total_wealth,_font,black,display_height + gaph,gapv+0.9*boxl,boxb,0.1*boxl)
            #functions.text_in_box(firstpage.p[1].name,_font,white,display_height + gaph,2*gapv + boxl,boxb,0.1*boxl)
            functions.text_in_box(firstpage.p[1].name,_font,black,display_height + gaph + 20,gapv,boxb + 6*gaph,0.1*boxl)
            #functions.text_in_box("Kanishk %r"%player.player[1].cash,_font,black,display_height + gaph,2*gapv+boxl + 0.1*boxl ,boxb,0.1*boxl)
            #functions.text_in_box("Net Worth %r"%player.player[1].total_wealth,_font,black,display_height + gaph,2*gapv+boxl+0.9*boxl,boxb,0.1*boxl)

            functions.text_in_box("Kanishk %r"%player.player[1].cash,_font,black,display_height + gaph + 20,gapv+0.1*boxl,boxb + 6*gaph,0.1*boxl)
            functions.text_in_box("Net Worth %r"%player.player[1].total_wealth,_font,black,display_height + gaph + 20,gapv + 0.9*boxl,boxb + 6*gaph,0.1*boxl)
            pygame.display.update()
            clock.tick(10000)

def Button(msg,x,y,l,h,ac,ic,function,tc):                  #for drawing buttons 
            global player_index,place,card_display,spcard_display,railway,rolloncejail,temporary,timer,timerr
            global rollonce,endturn,key,n,incometax,gotojail,cround,round_complete 
            pygame.draw.rect(functions.gameDisplay, ic, [x,y,l,h])
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x < mouse[0] < x+l and y < mouse[1] < y+h:           
                pygame.draw.rect(functions.gameDisplay, ac, [x,y,l,h])
                if click[0]==1:                     #checking if pressed
                    if function == "roll":
                        if gotojail == 0 and player.player[player_index].released == 1 and rollonce == 0:           #diff working done based on the button pressed
                            n = functions.rolldice()
                            
                            cround[player_index] += n
                            player.player[player_index].movement(n)
                            rollonce = 1

                            working()
                            
                        if gotojail == 1 and player.player[player_index].released == 0 and key == 3 and rolloncejail == 0:
                            n = functions.rolldice()
                            if functions.a == functions.b:
                                player.player[player_index].released = 1
                            rolloncejail = 1
                            key = 4
                            endturn = 0
                            
                    if function == "endturn" and endturn == 0:              #if endturn pressed
                        if player_index == 0:
                            player_index+=1
                        elif player_index == 1:
                            player_index-=1
                        if player.player[player_index].released == 0:
                            gotojail = 1
                        rollonce = 0
                        card_display = 0
                        endturn = 1
                        Property.tflag = 0
                        spcard_display = 0
                        railway = 0
                        timer = 8
                        timerr = 8
                        
                    if function == "yes":
                        player.player[player_index].cash -= Property._property[place].cost
                        Property._property[place].owner = player_index
                        player.player[player_index].properties.append(place)
                        
                        key = 2

                    if function == "Yes":
                        player.player[player_index].cash -= Property.sproperty[place].cost
                        Property.sproperty[place].owner = player_index
                        
                        key = 2

                    if function == "YeS":
                        player.player[player_index].cash -= Property.sproperty[place].cost
                        Property.sproperty[place].owner = player_index
                        
                        player.player[player_index].no_of_railways += 1
                        key = 2   
                        
                    if function == "no":
                        card_display = 0
                        spcard_display = 0
                        railway = 0
                    if function == "mort":
                        vvalid = 1
                        if Property.temo.owner != player_index or Property.temo.no_of_houses > 0:
                            vvalid =0
                        for xplace,tempo in Property._property.items():
                            if Property._property[xplace].country == Property.temo.country:
                                if Property._property[xplace].no_of_houses > 0 :
                                    vvalid = 0
                                    break
                        if vvalid ==1:
                            Property.temo.owner = None
                            player.player[player_index].cash +=  Property.temo.mortgage
                            player.player[player_index].total_wealth +=  Property.temo.mortgage
                            player.player[player_index].total_wealth -=  Property.temo.cost
                                
                    if function == "build":
                        valid = 1
                        if Property.temo.owner != player_index or Property.temo.no_of_houses == 4:
                            valid = 0
                        for xplace,tempo in Property._property.items():
                            if Property._property[xplace].country == Property.temo.country:
                                if (Property._property[xplace].no_of_houses < Property.temo.no_of_houses) or Property._property[xplace].owner != player_index:
                                    valid = 0
                                    break
                        if valid == 1:
                            Property.temo.no_of_houses += 1
                            player.player[player_index].cash -= Property.temo.cost 
                    if function == "sell":
                        valid = 1
                        if Property.temo.owner != player_index or Property.temo.no_of_houses == 0:
                            valida = 0
                        for xplace,tempo in Property._property.items():
                            if Property._property[xplace].country == Property.temo.country:
                                if (Property._property[xplace].no_of_houses > Property.temo.no_of_houses) or Property._property[xplace].owner != player_index:
                                    valida = 0
                                    break
                        if valida == 1:
                            Property.temo.no_of_houses -= 1
                            player.player[player_index].cash += 0.5*Property.temo.cost 
                    if function == "roll_for_double":
                        key = 3
                        rolloncejail = 0
                    if function == "pay":
                        key = 5
                        player.player[player_index].cash -= 500
                        player.player[player_index].total_wealth -= 500
                        player.player[player_index].released = 1
                        endturn = 0
                            
            _font = pygame.font.Font('freesansbold.ttf',20)
            functions.text_in_box(msg, _font,tc,x,y,l,h)

def working():              #decides which checkpoints to on based on the players current position 
                global player_index,place,card_display,spcard_display,railway,rolloncejail,temporary
                global rollonce,endturn,key,n,incometax,gotojail,cround,round_complete,comm,chance
                if cround[player_index] >= 40:
                    round_complete = 1
                            
                for tplace,tempo in Property._property.items():
                    if Property._property[tplace].locx == player.player[player_index].posx and Property._property[tplace].locy == player.player[player_index].posy:
                        card_display = 1
                        key = 0
                        place = tplace
                if (player.player[player_index].posx == card_length+2.5*card_breadth and display_height-card_length/2 == player.player[player_index].posy) or (player.player[player_index].posx == card_length+1.5*card_breadth and card_length/2 == player.player[player_index].posy) or (player.player[player_index].posx == display_height - card_length/2 and card_length + 5.5*card_breadth == player.player[player_index].posy):
                    chance = 1
                if (player.player[player_index].posx == card_length+7.5*card_breadth and display_height-card_length/2 == player.player[player_index].posy) or (player.player[player_index].posx == card_length/2 and card_length + 2.5*card_breadth  == player.player[player_index].posy) or (player.player[player_index].posx == display_height - card_length/2 and card_length + 2.5*card_breadth == player.player[player_index].posy):
                    comm = 1    

                if (player.player[player_index].posx == Property.sproperty["pharmacy"].locx and Property.sproperty["pharmacy"].locy == player.player[player_index].posy) or (player.player[player_index].posx == Property.sproperty["clinic"].locx and Property.sproperty["clinic"].locy == player.player[player_index].posy):
                    if player.player[player_index].posx == Property.sproperty["pharmacy"].locx:
                        place = "pharmacy"
                    elif player.player[player_index].posx == Property.sproperty["clinic"].locy:
                        place = "clinic"
                    spcard_display = 1
                    key = 0

                if (player.player[player_index].posx == Property.sproperty["factory1"].locx  and Property.sproperty["factory1"].locy == player.player[player_index].posy) or (player.player[player_index].posx == Property.sproperty["factory2"].locx  and Property.sproperty["factory2"].locy == player.player[player_index].posy) or (player.player[player_index].posx == Property.sproperty["factory3"].locx  and Property.sproperty["factory3"].locy == player.player[player_index].posy) or (player.player[player_index].posx == Property.sproperty["factory4"].locx  and Property.sproperty["factory4"].locy == player.player[player_index].posy):
                    if (player.player[player_index].posx == Property.sproperty["factory1"].locx  and Property.sproperty["factory1"].locy == player.player[player_index].posy):
                        place = "factory1"
                    elif (player.player[player_index].posx == Property.sproperty["factory2"].locx  and Property.sproperty["factory2"].locy == player.player[player_index].posy):
                        place = "factory2"
                    elif (player.player[player_index].posx == Property.sproperty["factory3"].locx  and Property.sproperty["factory3"].locy == player.player[player_index].posy):
                        place = "factory3"
                    elif (player.player[player_index].posx == Property.sproperty["factory4"].locx  and Property.sproperty["factory4"].locy == player.player[player_index].posy):
                        place = "factory4"
                    railway = 1
                    key = 0
                                
                if player.player[player_index].posx == (card_length+5*card_breadth + 0.5*card_breadth) and player.player[player_index].posy == (display_height-card_length/2):
                    incometax = 1
                    key = 0
                if player.player[player_index].posx == display_height-card_length/2 and player.player[player_index].posy == 7*card_breadth+card_length+0.5*card_breadth :
                    incometax = 2
                    key = 0
                if player.player[player_index].posx == display_height-card_length/2 and player.player[player_index].posy == card_length/2:
                                
                    player.player[player_index].posx = card_length/2
                    player.player[player_index].posy = display_height-card_length/2
                    cround[player_index] -= 20
                    gotojail = 1
                    key = 0
                    temporary = 1
                endturn = 0      
def railways():         #respectve changes on screen if railways if concersnesd
                global key,timer,incometax,gotojail,round_complete,cround,rent,railway,temporary
                if Property.sproperty[place].owner != None and key == 0 and player_index != Property.sproperty[place].owner:
                    Property.sproperty[place].rcard()
                    
                    if timer == 8:
                        if player.player[Property.sproperty[place].owner].no_of_railways == 1:
                            rent = 250
                        if player.player[Property.sproperty[place].owner].no_of_railways == 2:
                            rent = 500
                        if player.player[Property.sproperty[place].owner].no_of_railways == 3:
                            rent = 1000
                        if player.player[Property.sproperty[place].owner].no_of_railways == 4:
                            rent = 2000
                        player.player[player_index].cash -= rent
                        player.player[player_index].total_wealth -= rent
                        player.player[Property.sproperty[place].owner].cash += rent
                        player.player[Property.sproperty[place].owner].total_wealth += rent
                    functions.text_in_box("You paid Darita of %r to Abhineta %r?"%(rent,Property.sproperty[place].owner+1),__font,orange,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
                    timer -= 3
                    if timer == 0:
                        key = 1
                        timer = 8
                if Property.sproperty[place].owner == None and key == 0:
                    Property.sproperty[place].rcard()
                    functions.text_in_box("Do you want to purchase %r ?"%Property.sproperty[place].name,__font,orange,display_height/2,display_height/2 - blockh,display_height/2-card_length,display_height/2-card_length)
                    Button("YES",display_height*3/4 - card_length/2-blockl,display_height*3/4 - card_length/2 + blockh/2,blockl/2,blockh,yellow,llblue,"YeS",red)
                    Button("NO",display_height*3/4 - card_length/2 + blockl/2,display_height*3/4 - card_length/2 + blockh/2,blockl/2,blockh,yellow,llblue,"no",red)
                if key == 2:
                    Property.sproperty[place].rcard()
                    functions.text_in_box("Successfully purchased %r !!"%(Property.sproperty[place].name),__font,orange,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
                    timer -= 3
                    if timer == 0:
                        key = 1
                        timer = 8
def spcard_displayy():      #if playaer lands on utillies then the work happening on screeen 
                global key,timer,incometax,gotojail,round_complete,cround,rent,railway,temporary
                if Property.sproperty[place].owner != None and key == 0 and player_index != Property.sproperty[place].owner:
                    Property.sproperty[place].card()
                    
                    if timer == 8:

                        dice_sum = functions.a + functions.b
                        if Property.sproperty["pharmacy"].owner == Property.sproperty["clinic"].owner:
                            rent = 300*dice_sum
                        else:
                            rent = 100*dice_sum
                        player.player[player_index].cash -= rent
                        player.player[player_index].total_wealth -= rent
                        player.player[Property.sproperty[place].owner].cash += rent
                        player.player[Property.sproperty[place].owner].total_wealth += rent
                    functions.text_in_box("You paid Darita of %r to Abhineta %r"%(rent,Property.sproperty[place].owner+1),__font,orange,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
                    timer -= 3
                    if timer == 0:
                        key = 1
                        timer = 8
                if Property.sproperty[place].owner == None and key == 0:
                    Property.sproperty[place].card()
                    functions.text_in_box("Do you want to purchase %r ?"%Property.sproperty[place].name,__font,orange,display_height/2,display_height/2 - blockh,display_height/2-card_length,display_height/2-card_length)
                    Button("YES",display_height*3/4 - card_length/2-blockl,display_height*3/4 - card_length/2 + blockh/2,blockl/2,blockh,yellow,llblue,"Yes",red)
                    Button("NO",display_height*3/4 - card_length/2 + blockl/2,display_height*3/4 - card_length/2 + blockh/2,blockl/2,blockh,yellow,llblue,"no",red)
                if key == 2:
                    Property.sproperty[place].card()
                    functions.text_in_box("Successfully purchased %r !!"%(Property.sproperty[place].name),__font,orange,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
                    timer -= 3
                    if timer == 0:
                        key = 1
                        timer = 8

def GoToJail():  #if the player lands on gotojail
                global key,timer,incometax,gotojail,round_complete,cround,rent,railway,temporary    
                if temporary == 1:
                    player.player[player_index].released = 0
                    temporary = 0 
                if key == 0:
                    timer -= 8
                    functions.text_in_box("Alert! You have arrived just visit.. Miss a turn",__font,orange,card_length,(display_height/2+card_length)/2 + 1.25*blockh,display_height- 2*card_length,display_height/2 - ((display_height/2+card_length)/2 + 1.25*blockh))
                    if timer == 0:
                        key = 1
                        timer = 8
                if key == 1 or key == 0:
                    Button("Pay 700 kanishk for tuition fee",card_length + 0.1*(display_height - 2*card_length),display_height/2,0.8*(display_height - 2*card_length),blockh,yellow,llblue,"pay",red)
                    Button("Roll Akshah for a scholarship !",card_length + 0.1*(display_height - 2*card_length),display_height/2 + 2*blockh,0.8*(display_height - 2*card_length),blockh,yellow,llblue,"roll_for_double",red)
                
                if key == 3:
                    functions.text_in_box("Roll your Akshah once",__font,orange,card_length,(display_height/2+card_length)/2 + 1.25*blockh,display_height- 2*card_length,display_height/2 - ((display_height/2+card_length)/2 + 1.25*blockh))
                if key == 4 and player.player[player_index].released == 1:
                    timer -= 8
                    functions.text_in_box("Lucky Guy! You are free!",__font,orange,card_length,(display_height/2+card_length)/2 + 1.25*blockh,display_height- 2*card_length,display_height/2 - ((display_height/2+card_length)/2 + 1.25*blockh))
                    if timer == 0:
                        key = 1
                        gotojail = 0
                        timer = 8
                if key == 4 and player.player[player_index].released == 0:
                    timer -= 8
                    functions.text_in_box("Better Luck next time!",__font,orange,card_length,(display_height/2+card_length)/2 + 1.25*blockh,display_height- 2*card_length,display_height/2 - ((display_height/2+card_length)/2 + 1.25*blockh))
                    if timer == 0:
                        key = 1
                        gotojail = 0
                        timer = 8
                if key == 5:
                    timer -= 8
                    functions.text_in_box("You have paid the fees !",__font,orange,card_length,(display_height/2+card_length)/2 + 1.25*blockh,display_height- 2*card_length,display_height/2 - ((display_height/2+card_length)/2 + 1.25*blockh))
                    if timer == 0:
                        key = 1
                        gotojail = 0
                        timer = 8

def Prop():         #if player lands on a property
                global key,timer,incometax,gotojail,round_complete,cround,rent,railway,temporary 
                if Property._property[place].owner != None and key == 0 and player_index != Property._property[place].owner:
                    Property._property[place].card()
                    if timer == 8:
                        player.player[player_index].cash -= Property._property[place].houses[Property._property[place].no_of_houses]
                        player.player[player_index].total_wealth -= Property._property[place].houses[Property._property[place].no_of_houses]
                        player.player[Property._property[place].owner].cash += Property._property[place].houses[Property._property[place].no_of_houses]
                        player.player[Property._property[place].owner].total_wealth += Property._property[place].houses[Property._property[place].no_of_houses]
                    functions.text_in_box("You paid Darita of %r to Abhineta %r?"%(Property._property[place].houses[Property._property[place].no_of_houses],Property._property[place].owner+1),__font,orange,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
                    timer -= 3
                    if timer == 0:
                        key = 1
                        timer = 8
                if Property._property[place].owner == None and key == 0:
                    Property._property[place].card()
                    functions.text_in_box("Do you want to purchase %r ?"%Property._property[place].name,__font,orange,display_height/2,display_height/2 - blockh,display_height/2-card_length,display_height/2-card_length)
                    Button("YES",display_height*3/4 - card_length/2-blockl,display_height*3/4 - card_length/2 + blockh/2,blockl/2,blockh,yellow,llblue,"yes",red)
                    Button("NO",display_height*3/4 - card_length/2 + blockl/2,display_height*3/4 - card_length/2 + blockh/2,blockl/2,blockh,yellow,llblue,"no",red)
                if key == 2:
                    Property._property[place].card()
                    functions.text_in_box("Successfully purchased %r !!"%(Property._property[place].name),__font,orange,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
                    timer -= 3
                    if timer == 0:
                        key = 1
                        timer = 8
      
def Chance(): #if player lands on chance
    global key,timer,incometax,gotojail,round_complete,cround,rent,railway,temporary,chance,timerr 
    n = functions.a + functions.b
    if n == 2:
        if timer == 8:
            player.player[player_index].posx = display_height - card_length/2
            player.player[player_index].posy = display_height - card_length/2
            cround[player_index] = 40
            round_complete = 1
        functions.text_in_box("Advance to Grow !",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        timer -= 3
        if timer == 0:
            timer = 8
            chance = 0

    if n == 3:
        timer -= 2
        if timer == 0:
            player.player[player_index].posx = card_length + card_breadth/2
            player.player[player_index].posy = display_height - card_length/2
            if cround[player_index]>9:
                cround[player_index] = 49
                round_complete = 1
            else:
                cround[player_index] = 9
        functions.text_in_box("You are given a free visit to Aparajitha ,Enjoy the delight of it!",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        
        if timer == 0:
            timer = 8
            chance = 0
            working()    
    if n == 4:
        if timer == 8:
            player.player[player_index].cash -= 500
            player.player[player_index].total_wealth -= 500
        functions.text_in_box("Pay land tax",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        timer -= 2
        if timer == 0:
            timer = 8
            chance = 0
        
    if n == 5:
        if timer == 8:
            player.player[player_index].posx = display_height - card_length/2
            player.player[player_index].posy = card_length/2
            
            cround[player_index] = 30
            
        functions.text_in_box("Go to Chakra University",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        timer -= 2
        if timer == 0:
            timer = 8
            chance = 0
            working()    
    if n == 6:
        timer -= 2
        if timer == 0:
            player.player[player_index].movement(37)
            cround[player_index] = cround[player_index]%40
            
        functions.text_in_box("Earthquake expected! Go back three spaces",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        
        if timer == 0:
            timer = 8
            chance = 0
            working()
    if n == 7:
        if timer == 8:
            player.player[player_index].cash -= 300
            player.player[player_index].total_wealth -= 300
        functions.text_in_box("You have joined “Indian Ayurveda Medical Association”. Pay 300 kanishk",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        timer -= 2
        if timer == 0:
            timer = 8
            chance = 0
    if n == 8:
        if timer == 8:
            player.player[player_index].cash += 400
            player.player[player_index].total_wealth += 400
        functions.text_in_box("Water saved due to heavy rain. Collect 400 kanishk as Water tax rebate",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        timer -= 2
        if timer == 0:
            timer = 8
            chance = 0
    if n == 9:
        timer -= 3
        if timer == 0:
            player.player[player_index].posx = card_length + card_breadth/2
            player.player[player_index].posy = card_length/2
            if cround[player_index]>21:
                cround[player_index] = 61
                round_complete = 1
            else :
                cround[player_index] = 21
                            
        functions.text_in_box("Go for a field trip to Manjistha ,Enjoy the delight of it!",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        if timer == 0:
            timer = 8
            chance = 0
            working()    
    if n == 10:
        timer -= 3
        if timer == 0:
            player.player[player_index].posx = card_length/2 
            player.player[player_index].posy = display_height - card_length - 1.5*card_breadth
            

        functions.text_in_box("Go to Pharmacy and buy basic medicines !",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        if timer == 0:
            timer = 8
            chance = 0
            working()    
    if n == 11:
        if timer == 8:
            player.player[player_index].cash += 300
            player.player[player_index].total_wealth += 300
        functions.text_in_box("It’s Dhanvantari Jayanti ! Collect 300 kanishk",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        timer -= 2
        if timer == 0:
            timer = 8
            chance = 0
    if n == 12:
        if timer == 8:
            player.player[player_index].cash -= 300
            player.player[player_index].total_wealth -= 300
        functions.text_in_box("You have joined “Indian Ayurveda Medical Association”. Pay 300 kanishk",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        timer -= 2
        if timer == 0:
            timer = 8
            chance = 0            
def CommChest():   #if player lands on community chest
    global key,timer,incometax,gotojail,round_complete,cround,rent,railway,temporary,chance,comm,timerr  
    n = functions.a + functions.b
    if n == 2:
        timer -= 3
        if timer == 8:
            player.player[player_index].posx = display_height - card_length/2
            player.player[player_index].posy = display_height - card_length/2
            cround[player_index] = 40
            round_complete = 1
        functions.text_in_box("Go to our prime location GROW ",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        timer -= 3
        if timer == 0:
            timer = 8
            comm = 0

    if n == 3:
        timer -= 3
        if timer == 0:
            player.player[player_index].posx = card_length + card_breadth/2
            player.player[player_index].posy = display_height - card_length/2
            if cround[player_index]>9:
                cround[player_index] = 49
                round_complete = 1
            else:
                cround[player_index] = 9
        functions.text_in_box("Go on a field trip to Aparajita ,Enjoy the delight of it!",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        timer -=2
        
        if timer == 0:
            timer = 8
            comm = 0
            working()    
    if n == 4:
        timer -= 3
        if timer == 8:
            player.player[player_index].cash -= 500
            player.player[player_index].total_wealth -= 500
        functions.text_in_box("Pay land tax",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        timer -= 8

        if timer == 0:
            timer = 8
            comm = 0
    if n == 5:
        timer -= 3
        if timer == 0:
            player.player[player_index].posx = display_height - card_length/2
            player.player[player_index].posy = card_length/2
            
            cround[player_index] = 30
            
        functions.text_in_box("Go to Chakra University",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        if timer == 0:
            timer = 8
            comm = 0
            working()    
    if n == 6:
        timer -= 3
        if timer == 0:
            player.player[player_index].movement(37)
            cround[player_index] = cround[player_index]%40
            
        functions.text_in_box("Earthquake expected! Go back three spaces",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        if timer == 0:
            timer = 8
            comm = 0
            working()    
    if n == 7:
        if timer == 8:
            player.player[player_index].cash -= 300
            player.player[player_index].total_wealth -= 300
        functions.text_in_box("You have joined 'Indian Ayurvedic Medical Association' pay 300 kanishk",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        timer -= 2
        if timer == 0:
            timer = 8
            comm = 0
    if n == 8:
        if timer == 8:
            player.player[player_index].cash += 400
            player.player[player_index].total_wealth += 400
        functions.text_in_box("Water saved due to heavy rain. Collect 400 kanishk as Water tax rebate",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        timer -= 2

        if timer == 0:
            timer = 8
            comm = 0
    if n == 9:
        timer -= 3
        if timer == 0:
            player.player[player_index].posx = card_length + card_breadth/2
            player.player[player_index].posy = card_length/2
            if cround[player_index]>21:
                cround[player_index] = 61
                round_complete = 1
            else :
                cround[player_index] = 21
               
        functions.text_in_box("Go on a field trip to Manjistha ,Enjoy the delight of it!",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        if timer == 0:
            timer = 8
            comm = 0
            working()     
    if n == 10:
        timer -= 3
        if timer == 0:
            player.player[player_index].posx = card_length/2 
            player.player[player_index].posy = display_height - card_length - 1.5*card_breadth
            

        functions.text_in_box("Go to pharmacy and buy basic medicines ",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        if timer == 0:
            timer = 8
            comm = 0
            working()    
    if n == 11:
        timer -= 3
        if timer == 8:
            player.player[player_index].cash += 300
            player.player[player_index].total_wealth += 300
        functions.text_in_box("It's Dhanvantri Jayanti. Collect 300 kanishk",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        timer -= 2
        if timer == 0:
            timer = 8
            comm = 0
    if n == 12:
        timer -= 3
        if timer == 8:
            player.player[player_index].cash -= 500
            player.player[player_index].total_wealth -= 500
        functions.text_in_box("Crops destroyed due to pest attack. Pay 500 kanishk for repair",__font,red,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
        pygame.display.update()
        timer -= 2
        if timer == 0:
            timer = 8
            comm = 0            
