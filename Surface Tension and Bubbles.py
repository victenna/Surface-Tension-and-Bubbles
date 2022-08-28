import pygame,random
pygame.init()
screen = pygame.display.set_mode((1600, 900))
timer = pygame.time.Clock()
class Pipe():
    def __init__(self,image,Xscale,Yscale):
        super().__init__()
        self.image=pygame.image.load(image)
        self.Xscale=Xscale
        self.Yscale=Yscale
        self.image=pygame.transform.scale(self.image,(self.Xscale,self.Yscale))
    def settings(self,x,y,angle):
        self.angle=angle
        self.image1=pygame.transform.rotate(self.image,angle)
        self.rect=self.image1.get_rect()
        self.x,self.y=x,y
        self.rect.center=(self.x,self.y)
    def draw(self):
        screen.blit(self.image1,self.rect)
        
class Face():
    def __init__(self,image,x,y):#,Xscale,Yscale):
        super().__init__()
        self.image=pygame.image.load(image)
        self.image=pygame.transform.scale(self.image,(300,260))
        
        self.x,self.y=x,y
        self.rect=self.image.get_rect()
        self.rect.center=(self.x,self.y)
        
        
    def update(self,Xscale,Yscale):
        self.Xscale=Xscale
        self.Yscale=Yscale
        self.image=pygame.transform.scale(self.image,(self.Xscale,self.Yscale))
        self.rect=self.image.get_rect(center=(self.x,self.y))
        #self.rect.center=(self.x,self.y)
        
    def draw(self):
        screen.blit(self.image,self.rect)
        
class Crash():
    def __init__(self,image,Xscale,Yscale):
        super().__init__()
        self.image=pygame.image.load(image)
        self.Xscale=Xscale
        self.Yscale=Yscale
        self.image=pygame.transform.scale(self.image,(self.Xscale,self.Yscale))
        self.rect=self.image.get_rect()
    def settings(self,x,y):
        self.x,self.y=x,y
        self.rect.center=(self.x,self.y)
    def draw(self):
        screen.blit(self.image,self.rect)


face1=Face('face5.png',658,236)
face2=Face('face6.png',665,236)
pipe1=Pipe('pipee.png',183,146)        
pipe2=Pipe('pipee2.png',183,146)
pipe3=Pipe('pipe3(2).png',30,145)
pipe4=Pipe('pipe4.png',140,140)
crash1=Crash('crash1.png',200,170)
crash1.settings(895,650)

crash2=Crash('crash2.png',200,170)
crash2.settings(895,650)
crash3=Crash('crash3.png',200,170)
crash3.settings(895,650)
timer=pygame.time.Clock()
X0,Y0=425,569
dy,dy1,dy2,dy3=0,0,0,0
T=0
angle=0
q1=0
q2=0
q3=0
face_X=230
face_Y=200
while True:
    T=T+1
    screen.fill('blue')
    pygame.draw.circle(screen,'light blue',(660,441),70,0)
    pipe1.settings(500,500,0)
    pipe1.draw()
    pipe2.settings(820,500,0)
    pipe2.draw()
    
    if T<=10:face1.draw()
        
    if T>10 and T<160:
        q3=q3+1
        q3=q3%20
        if q3<10:
            face1.draw()
        if q3>9:
            face2.draw()
    if T>159:
        face1.draw()

    pipe3.settings(660,300,0)
    pipe3.draw()
    pipe4.settings(660,441,angle)
    pipe4.draw()
    
    if T>20 and T<=180:
        if dy<=40:
            dy=dy+1
        pygame.draw.circle(screen,'red',(X0,Y0+dy),dy,0)
        
    if T>70 and T<=80:
        angle=angle-18

    if T>80 and T<210:
        if dy2<80:
            dy2=dy2+1
        pygame.draw.circle(screen,'gold',(895,Y0+dy2),dy2,0)
     
    if T>160 and T<=169:
        angle=angle+10
        
    if T>180 and T<220:
        dy1=dy1+1
        R1=40-dy1
        print('dy1=',dy1,'R1=',R1,'T=',T)
        pygame.draw.circle(screen,'red',(X0,Y0+R1),R1,0)
        dy3=dy3+1
        pygame.draw.circle(screen,'gold',(895,Y0+dy2+dy3),dy2+dy3,0)
 
    if T>219 and T<230:
        pygame.draw.circle(screen,'blue',(1895,Y0+dy2+dy3),dy2+dy3,0)
        crash1.draw()
        
    if T>=230 and T<240:
        crash2.draw()
        
    if T>=240 and T<250:
        crash3.draw()
        
    if T>=250:
        pygame.draw.circle(screen,'blue',(1895,Y0+dy2+dy3),dy2+dy3,0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
    timer.tick(20)