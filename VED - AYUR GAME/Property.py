import pygame,functions

pygame.init()

display_width = 1430
display_height = 800
card_length = 130
card_breadth = 60
boxl = 350
boxb = 215
gapv = (display_height - 2*boxl)/3
gaph = (display_width - display_height - 2*boxb)/3
cardl = 0.1*boxb
cardh = 0.1*boxl
cgaph = ((boxb/2)-(3*cardl))/4
cgapv = 0.03*boxl
c2gaph = ((boxb/2)-(2*cardl))/3
c3gaph = ((boxb/2)-(4*cardl))/5
tflag = 0
temo = None
timer = 8



white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
red = (255,0,0)
blue = (0,128,0) #lime green
#(0,0,255) #blue
green = (255,69,0) #orange
back = (100,10,100)
new = (10,100,100)
new1 = (200,150,50)
new2 = (67,234,169)
orange = (150,75,0) #brown
grey = (0,0,139) #dark blue
c1 = (69,43,122)
c2 = (255,102,255)
c3 = (102,0,0)
c4 = (102,255,255)
marine = (127,255,212)
pgreen = (152,251,152)
bgrey = (176,196,222)

fps = 100
clock = pygame.time.Clock()



class Property():                                                                   #creating a class property which will contain all data of properties and their respective functions

    def __init__(self,name,color,country,locx,locy,cost,benefit1,benefit2,benefit3,x1,y1,x2,y2):              #initialising every object(property) with its basic information
        self.name = name
        self.color = color
        self.country = country
        self.benefit1 = benefit1
        self.benefit2 = benefit2
        self.benefit3 = benefit3
        self.locx = locx
        self.locy = locy
        self.cost = cost
        self.houses = [0.1*self.cost,0.4*self.cost,0.5*self.cost,0.6*self.cost,self.cost]    #A list keeping track of rents to be paid v/s no. of houses
        self.mortgage = 0.4*self.cost
        self.mort = 0
        self.no_of_houses = 0
        self.owner = None
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def locmaker(self):                                         #it creates the respective property on the board 
        lfont = pygame.font.Font('freesansbold.ttf',10)
        if self.locx == card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[0,self.locy-card_breadth/2,card_length,card_breadth],1)
            #functions.gameDisplay.blit(lfont.render(self.name, True, (0,0,0)), (1*card_length,1*card_breadth))
            functions.gameDisplay.fill(self.color, rect = [0.7*card_length,self.locy-card_breadth/2,0.3*card_length,card_breadth])
            if  self.no_of_houses >= 1:
                functions.gameDisplay.fill(c1, rect = [0.7*card_length,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])
            if self.no_of_houses >= 2:
                functions.gameDisplay.fill(c2, rect = [0.7*card_length + 0.3*card_length/4,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])
            if self.no_of_houses >= 3:
                functions.gameDisplay.fill(c3, rect = [0.7*card_length + 0.6*card_length/4,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])
            if self.no_of_houses == 4:
                functions.gameDisplay.fill(c4, rect = [0.7*card_length + 0.9*card_length/4,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])    
        elif self.locx == display_height -  card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[display_height -  card_length,self.locy-card_breadth/2,card_length,card_breadth],1)
            functions.gameDisplay.fill(self.color, rect = [display_height -  card_length,self.locy-card_breadth/2,0.3*card_length,card_breadth])
            if self.no_of_houses >= 1:
                functions.gameDisplay.fill(c1, rect = [display_height -  card_length + 0.9*card_length/4 ,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])
            if self.no_of_houses >= 2:
                functions.gameDisplay.fill(c2, rect = [display_height -  card_length + 0.6*card_length/4 ,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])
            if self.no_of_houses >= 3:
                functions.gameDisplay.fill(c3, rect = [display_height -  card_length + 0.3*card_length/4 ,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])
            if self.no_of_houses == 4:
                functions.gameDisplay.fill(c4, rect = [display_height -  card_length  ,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])
        elif self.locy == card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[self.locx-card_breadth/2,0,card_breadth,card_length],1)
            a = self.name.split(' ')
            temp = 0
            for x in a:
                temp += 0.35*card_length
            functions.gameDisplay.fill(self.color, rect = [self.locx-card_breadth/2,0.7*card_length,card_breadth,0.3*card_length])
            if self.no_of_houses >= 1:
                functions.gameDisplay.fill(c1, rect = [self.locx-card_breadth/4,0.7*card_length,card_breadth/2,0.3*card_length/4])
            if self.no_of_houses >= 2:
                functions.gameDisplay.fill(c2, rect = [self.locx-card_breadth/4,0.7*card_length + 0.3*card_length/4,card_breadth/2,0.3*card_length/4])
            if self.no_of_houses >= 3:
                functions.gameDisplay.fill(c3, rect = [self.locx-card_breadth/4,0.7*card_length + 0.6*card_length/4,card_breadth/2,0.3*card_length/4])
            if self.no_of_houses == 4:
                functions.gameDisplay.fill(c4, rect = [self.locx-card_breadth/4,0.7*card_length + 0.9*card_length/4,card_breadth/2,0.3*card_length/4])
        elif self.locy ==  display_height -  card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[self.locx-card_breadth/2,display_height -  card_length,card_breadth,card_length],1)
            functions.gameDisplay.fill(self.color, rect = [self.locx-card_breadth/2,display_height -  card_length,card_breadth,0.3*card_length])
            if self.no_of_houses >= 1:
                functions.gameDisplay.fill(c1, rect = [self.locx-card_breadth/4,display_height -  card_length + 0.9*card_length/4,card_breadth/2,0.3*card_length/4])
            if self.no_of_houses >= 2:
                functions.gameDisplay.fill(c2, rect = [self.locx-card_breadth/4,display_height -  card_length + 0.6*card_length/4,card_breadth/2,0.3*card_length/4])
            if self.no_of_houses >= 3:
                functions.gameDisplay.fill(c3, rect = [self.locx-card_breadth/4,display_height -  card_length + 0.3*card_length/4,card_breadth/2,0.3*card_length/4])
            if self.no_of_houses == 4:
                functions.gameDisplay.fill(c4, rect = [self.locx-card_breadth/4,display_height -  card_length ,card_breadth/2,0.3*card_length/4])

    def card(self):                     #this draws the card of the property with the respective details on it
        functions.gameDisplay.fill(bgrey, rect = [1100,400,200,250])
        lfont = pygame.font.Font('freesansbold.ttf',25)
        sfont = pygame.font.Font('freesansbold.ttf',15)
        functions.text_in_box(self.name,lfont,self.color,1100,410,200,30)
        functions.text_in_box("BENEFITS ",lfont,black,1200,680,200,30)
        functions.text_in_box(self.benefit1,sfont,green,1200,720,200,30)
        functions.text_in_box(self.benefit2,sfont,green,1200,740,200,30)
        functions.text_in_box(self.benefit3,sfont,green,1200,760,200,30)

        functions.message_to_screen("Kanishk :  %d kanishk"%self.cost,black,1110,460,20)
        functions.message_to_screen("Darita :  %d kanishk"%self.houses[0],black,1110,480,20)
        functions.message_to_screen("1 krish: %d kanishk"%self.houses[1],black,1110,500,20)
        functions.message_to_screen("2 krish: %d kanishk"%self.houses[2],black,1110,520,20)
        functions.message_to_screen("3 krish: %d kanishk"%self.houses[3],black,1110,540,20)
        functions.message_to_screen("4 krish: %d kanishk"%self.houses[4],black,1110,560,20)
        functions.message_to_screen("Mortgage value: %d kanishk"%self.mortgage,black,1110,600,20)
        pygame.display.update()
        clock.tick(fps)

    def squares(self):                      #this draws the links of the property on the respective player boxes depending on the owner 
        global tflag ,timer,temo
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if self.owner == 0:
            pygame.draw.rect(functions.gameDisplay, self.color, [self.x1,self.y1,cardl,cardh])
            if self.x1 < mouse[0] < self.x1+cardl and self.y1 < mouse[1] < self.y1 + cardh:
                if click[0]==1:
                    tflag = 1
                    temo = self
            
        if self.owner == 1:
            pygame.draw.rect(functions.gameDisplay, self.color, [self.x1 + 215,self.y1,cardl,cardh])
            if self.x2 < mouse[0] < self.x2+cardl and self.y2 < mouse[1] < self.y2 + cardh:
                if click[0]==1:
                    tflag = 1
                    temo = self

class special_cards():                          #for special cards that is utilities and railway

    def __init__(self,name,cost,locx,locy,x1,y1,x2,y2):
        self.name = name
        self.cost = cost
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.locx = locx
        self.locy = locy
        self.mortgage = 0.4*self.cost
        self.owner = None
    def card(self):                                     #this sketches the card of the utility when called upon
        functions.gameDisplay.fill(marine, rect = [1100,400,200,250])
        lfont = pygame.font.Font('freesansbold.ttf',25)
        functions.text_in_box(self.name,lfont,black,1100,410,200,30)
        functions.message_to_screen("Cost: %d kanishk"%self.cost,black,1110,460,20)
        functions.message_to_screen("If one utility is owned",black,1110,480,20)
        functions.message_to_screen("Rent = 100*(sum on Akshah)",black,1110,500,20)
        functions.message_to_screen("If both utilities are owned",black,1110,520,20)
        functions.message_to_screen("Rent = 300*(sum on Akshah)",black,1110,540,20)
        
        
        pygame.display.update()
        clock.tick(fps)
        
    def locmaker(self):                                             #this draws the railways at there respective positions on the board
        lfont = pygame.font.Font('freesansbold.ttf',10)
        if self.locx == card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[0,self.locy-card_breadth/2,card_length,card_breadth],1)
            #functions.text_in_box(self.name,lfont,black,0,self.locy-card_breadth/2,0.7*card_length,card_breadth)
            #functions.gameDisplay.fill(black, rect = [0.7*card_length,self.locy-card_breadth/2,0.3*card_length,card_breadth])
            
        elif self.locx == display_height -  card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[display_height -  card_length,self.locy-card_breadth/2,card_length,card_breadth],1)
            #functions.text_in_box(self.name,lfont,black,display_height -  0.7*card_length,self.locy-card_breadth/2,0.7*card_length,card_breadth)
            #functions.gameDisplay.fill(black, rect = [display_height -  card_length,self.locy-card_breadth/2,0.3*card_length,card_breadth])
            
        elif self.locy == card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[self.locx-card_breadth/2,0,card_breadth,card_length],1)
            a = self.name.split(' ')
            temp = 0
            for x in a:
                #functions.text_in_box(x,lfont,black,self.locx-card_breadth/2,temp,card_breadth,0.35*card_length)
                temp += 0.35*card_length
            #functions.gameDisplay.fill(black, rect = [self.locx-card_breadth/2,0.7*card_length,card_breadth,0.3*card_length])
            
        elif self.locy ==  display_height -  card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[self.locx-card_breadth/2,display_height -  card_length,card_breadth,card_length],1)
            #functions.text_in_box(self.name,lfont,black,self.locx-card_breadth/2,display_height -  0.7*card_length,card_breadth,0.7*card_length)
            #functions.gameDisplay.fill(black, rect = [self.locx-card_breadth/2,display_height -  card_length,card_breadth,0.3*card_length])
            
        
    def rcard(self):                            #this draws the card of the railway when called upon
        functions.gameDisplay.fill(white, rect = [1100,400,200,250])
        lfont = pygame.font.Font('freesansbold.ttf',25)
        functions.text_in_box(self.name,lfont,black,1100,410,200,30)
        functions.message_to_screen("Cost:  %d kanishk"%self.cost,black,1110,460,20)
        functions.message_to_screen("Owned          Darita",black,1110,480,20)
        functions.message_to_screen("1 Factory       250 kanishk",black,1110,500,20)
        functions.message_to_screen("2 Factory       500 kanishk",black,1110,520,20)
        functions.message_to_screen("3 Factory       1000 kanishk",black,1110,540,20)
        functions.message_to_screen("4 Factory       2000 kanishk",black,1110,560,20)
        
        pygame.display.update()
        clock.tick(fps)
    def squares(self):                      #this draws the links of the property on the respective owner boxes
        global tflag ,timer,temo
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if self.owner == 0:
            pygame.draw.rect(functions.gameDisplay, bgrey, [self.x1,self.y1,cardl,cardh])
            if self.x1 < mouse[0] < self.x1+cardl and self.y1 < mouse[1] < self.y1 + cardh:
                if click[0]==1:
                    tflag = 1
                    temo = self
        if self.owner == 1:
            pygame.draw.rect(functions.gameDisplay, bgrey, [self.x1 +  215,self.y1,cardl,cardh])
            if self.x2 < mouse[0] < self.x2+cardl and self.y2 < mouse[1] < self.y2 + cardh:
                if click[0]==1:
                    tflag = 1
                    temo = self
#initialising special card's objects
sproperty = {  "pharmacy":special_cards("Pharmacy",250,card_length/2,7*card_breadth+card_breadth/2+card_length,display_height + gaph + c2gaph,gapv + 0.2*boxl + 5*cgapv + 4*cardh,display_height + gaph + c2gaph,2*gapv + boxl + 0.2*boxl + 5*cgapv + 4*cardh)
             , "clinic":special_cards("Clinic",700,7*card_breadth+card_breadth/2+card_length,card_length/2,display_height + gaph + 2*c2gaph + cardl,gapv + 0.2*boxl + 5*cgapv + 4*cardh,display_height + gaph + 2*c2gaph + cardl,2*gapv + boxl + 0.2*boxl + 5*cgapv + 4*cardh)
             , "factory1":special_cards("FACTORY",400,card_length + 9*card_breadth/2,display_height - card_length/2,display_height + gaph + boxb/2+  c3gaph,gapv + 0.2*boxl + 5*cgapv + 4*cardh,display_height + gaph + boxb/2+ c3gaph,2*gapv + boxl + 0.2*boxl + 5*cgapv + 4*cardh)
             , "factory2":special_cards("FACTORY",400,card_length/2,card_length + 9*card_breadth/2,display_height + gaph + boxb/2+  2*c3gaph + cardl,gapv + 0.2*boxl + 5*cgapv + 4*cardh,display_height + gaph + boxb/2+ 2*c3gaph + cardl,2*gapv + boxl + 0.2*boxl + 5*cgapv + 4*cardh)  
             , "factory3":special_cards("FACTORY",400,card_length + 9*card_breadth/2,card_length/2,display_height + gaph + boxb/2+  3*c3gaph + 2*cardl,gapv + 0.2*boxl + 5*cgapv + 4*cardh,display_height + gaph + boxb/2+ 3*c3gaph + 2*cardl,2*gapv + boxl + 0.2*boxl + 5*cgapv + 4*cardh)
             , "factory4":special_cards("FACTORY",400,display_height - card_length/2,card_length + 9*card_breadth/2,display_height + gaph + boxb/2+  4*c3gaph + 3*cardl,gapv + 0.2*boxl + 5*cgapv + 4*cardh,display_height + gaph + boxb/2+ 4*c3gaph + 3*cardl,2*gapv + boxl + 0.2*boxl + 5*cgapv + 4*cardh)
            }
#initialising the property objects
_property = { "manjistha":Property("Manjistha",red,"Bark",card_length + card_breadth/2,card_length/2,800,"Promotes healthy liver function","Skin whitening","Removes stagnant blood",display_height + gaph + cgaph,gapv + 0.2*boxl + cgapv,display_height + gaph + cgaph,2*gapv + boxl + 0.2*boxl + cgapv )
            , "cinnamon":Property("Cinnamon",red,"Bark",card_length + 5*(card_breadth/2),card_length/2,2000,"Heals wounds,sores and boils","Strengthens digestion","Has warming properties",display_height + gaph + 2*cgaph + cardl,gapv + 0.2*boxl + cgapv,display_height + gaph + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + cgapv )
            , "guggul":Property("Guggul",red,"Bark",card_length + 7*(card_breadth/2),card_length/2,3000,"Treats hardening of arteries","Treats acne","Helps in weight loss",display_height + gaph + 3*cgaph + 2*cardl,gapv + 0.2*boxl + cgapv,display_height + gaph + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + cgapv )  
            , "ashwagandha":Property("Ashwagandha",yellow,"Fruit",card_length + 11*(card_breadth/2),card_length/2,100,"Reduces blood sugar level","Helps stress tolerance & immunity","Treats joint pains,skin sores",display_height + gaph + boxb/2 + cgaph,gapv + 0.2*boxl + cgapv,display_height + gaph + boxb/2 + cgaph,2*gapv + boxl + 0.2*boxl + cgapv)
            , "pepper":Property("Pepper",yellow,"Fruit",card_length + 13*(card_breadth/2),card_length/2,200,"Heals wounds","Heals sores and boils","Improves blood sugar control",display_height + gaph + boxb/2 + 2*cgaph + cardl,gapv + 0.2*boxl + cgapv,display_height + gaph + boxb/2 + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + cgapv)
            , "amla":Property("Amla",yellow,"Fruit",card_length + 17*(card_breadth/2),card_length/2,250,"Antioxidant, antistress","Treats constipation","Treats fever",display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,gapv + 0.2*boxl + cgapv,display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + cgapv)
            , "bhibitaki":Property("Bhibitaki",blue,"Fruit",display_height -  card_length/2,card_length + 1*(card_breadth/2),950 ,"Good for diabetes","Blood sugar dysregulation","Promotes stamina & strength",display_height + gaph + cgaph,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph +2*cgapv + cardh,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh )
            , "moringa":Property("Moringa",blue,"Leaf",display_height -  card_length/2,card_length + 3*(card_breadth/2),50,"Treats stomach pain"," Treats ulcers,poor vision","Treats joint pain",display_height + gaph + 2*cgaph + cardl,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh )
            , "kalmegh":Property("Kalmegh",blue,"Leaf",display_height -  card_length/2,card_length + 7*(card_breadth/2),200,"Treats indigestion","Treats acne","Treats diarrhea",display_height + gaph + 3*cgaph + 2*cardl,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh)
            , "tumeric":Property("Tumeric",green,"Root",card_length/2,card_length + 1*(card_breadth/2),500,"Treat rheumatoid arthritis","Treats small pox,chicken pox","Treats urinary tract infections",display_height + gaph + boxb/2 + cgaph,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph + boxb/2 + cgaph,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh)
            , "ginger":Property("Ginger",green,"Root",card_length/2,card_length + 3*(card_breadth/2),350,"Good for digestion","Reduces nausea","Help fight the flu",display_height + gaph + boxb/2 + 2*cgaph + cardl,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph + boxb/2 + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh)           
            , "shatavari":Property("Shatavari",green,"Root",card_length/2,card_length + 7*(card_breadth/2),50,"Treats infertility","Treats loss of libido","Treats kidney stones",display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh)
            , "cardamom":Property("Cardamom",back,"Spices",card_length/2,card_length + 11*(card_breadth/2),3500,"Treats nausea","Treats vomiting", "Treats dry cough",display_height + gaph + cgaph,gapv + 0.2*boxl + 3*cgapv + 2*cardh,display_height + gaph +2*cgapv + cardh,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh )
            , "cumin":Property("Cumin",back,"Spices",card_length/2,card_length + 13*(card_breadth/2),500,"Improves vision","Cleanses and detoxifies uterus","Treats scorpion stings",display_height + gaph + 2*cgaph + cardl,gapv + 0.2*boxl +3*cgapv + 2*cardh,display_height + gaph + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh )
            , "lotus":Property("Lotus",back,"Flowers",card_length/2,card_length + 17*(card_breadth/2),150,"Treatment of diarrhea","Tissue inflammation","Treats homeostasis",display_height + gaph + 3*cgaph + 2*cardl,gapv + 0.2*boxl + 3*cgapv + 2*cardh,display_height + gaph + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh)
            , "aparjita":Property("Aparajita",new,"Flowers",card_length + 1*(card_breadth/2),display_height - card_length/2,1050,"Diabetes","Reduces fever [Blue tea]","Helps in weight loss " ,display_height + gaph + boxb/2 + cgaph,gapv + 0.2*boxl + 3*cgapv + 2*cardh,display_height + gaph + boxb/2 + cgaph,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh)
            , "hibiscus":Property("Hibiscus",new,"Flowers",card_length + 3*(card_breadth/2),display_height - card_length/2,575,"Helps lower body temperature", "Treat heart diseases" ,"Treats nerve diseases",display_height + gaph + boxb/2 + 2*cgaph + cardl,gapv + 0.2*boxl + 3*cgapv + 2*cardh,display_height + gaph + boxb/2 + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh)
            , "bringaraj":Property("Bhringaraj",new,"Flowers",card_length + 7*(card_breadth/2),display_height - card_length/2,325,"Treats hair problems","Cures skin and tooth infections","Treats asthma",display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,gapv + 0.2*boxl + 3*cgapv + 2*cardh,display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh)
            , "tulsi":Property("Tulsi",grey,"Whole plant",display_height - card_length/2,card_length + 13*(card_breadth/2),200,"Helps cure indigestion","Cures heart diseases","Treats respiratory diseases",display_height + gaph + c2gaph,gapv + 0.2*boxl + 4*cgapv + 3*cardh,display_height + gaph + c2gaph,2*gapv + boxl + 0.2*boxl + 4*cgapv + 3*cardh)
            , "neem":Property("Neem",grey,"Whole plant",display_height - card_length/2,card_length + 17*(card_breadth/2),100,"Treats leprosy","Cures eye disorders","Treats intestinal worms",display_height + gaph + 2*c2gaph + cardl,gapv + 0.2*boxl + 4*cgapv + 3*cardh,display_height + gaph + 2*c2gaph + cardl,2*gapv + boxl + 0.2*boxl + 4*cgapv + 3*cardh)
            , "fenugreek":Property("Fenugreek",orange,"Seeds",card_length + 13*(card_breadth/2),display_height - card_length/2,300,"Helps treat loss of appetite", "Cures stomach upset, constipation","Cures inflammation of the stomach",display_height + gaph + boxb/2+  c2gaph,gapv + 0.2*boxl + 4*cgapv + 3*cardh,display_height + gaph + boxb/2+ c2gaph,2*gapv + boxl + 0.2*boxl + 4*cgapv + 3*cardh)
            , "ajwain":Property("Ajwain",orange,"Seeds",card_length + 17*(card_breadth/2),display_height - card_length/2,415,"Regulates antacids for healthy gastric acid flow", "Helps in digestion","Relieves arthritis",display_height + gaph + boxb/2+ 2*c2gaph + cardl,gapv + 0.2*boxl + 4*cgapv + 3*cardh,display_height + gaph + boxb/2+ 2*c2gaph + cardl,2*gapv + boxl + 0.2*boxl + 4*cgapv + 3*cardh)              
            }


        
