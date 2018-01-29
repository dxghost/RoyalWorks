'''
consider appending all troop animations in Units_list and when they are killed remove them
'''
import os
import pygame
import sys, random, math
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import time
import math
import cannon

pygame.init()
SIZE = WIDTH, HEIGHT = 500, 750
FPS = 60

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('RoyalWorks')
'''
pri_ui = pygame.image.load("Assets\\EXir\\prince.png")
pri_ui = pygame.transform.scale(pri_ui, (73, 93))
giant_ui = pygame.image.load("Assets\\EXir\\giant.png")
giant_ui = pygame.transform.scale(giant_ui, (73, 93))
goblins_ui = pygame.image.load("Assets\\EXir\\goblins.png")
goblins_ui = pygame.transform.scale(goblins_ui, (73, 93))
skeletons_ui = pygame.image.load("Assets\\EXir\\skeletons.png")
skeletons_ui = pygame.transform.scale(skeletons_ui, (73, 93))
knight_ui = pygame.image.load("Assets\\EXir\\knight.png")
knight_ui =pygame.transform.scale(knight_ui, (73, 93))
mini_PEKKA = pygame.image.load("Assets\\EXir\\mini_PEKKA.png")
mini_PEKKA = pygame.transform.scale(mini_PEKKA, (73, 93))
hog_rider = pygame.image.load("Assets\\EXir\\hog_rider.png")
hog_rider = pygame.transform.scale(hog_rider, (73, 93))
'''
def drawUI():
    global pri_ui
    UITab = pygame.image.load("Assets\\EXir\\UITab.png")
    pri_ui = pygame.image.load("Assets\\EXir\\prince.png")
    pri_ui = pygame.transform.scale(pri_ui, (73, 93))
    giant_ui = pygame.image.load("Assets\\EXir\\giant.png")
    giant_ui = pygame.transform.scale(giant_ui, (73, 93))
    goblins_ui = pygame.image.load("Assets\\EXir\\goblins.png")
    goblins_ui = pygame.transform.scale(goblins_ui, (73, 93))
    skeletons_ui = pygame.image.load("Assets\\EXir\\skeletons.png")
    skeletons_ui = pygame.transform.scale(skeletons_ui, (73, 93))
    knight_ui = pygame.image.load("Assets\\EXir\\knight.png")
    knight_ui =pygame.transform.scale(knight_ui, (73, 93))
    mini_PEKKA = pygame.image.load("Assets\\EXir\\mini_PEKKA.png")
    mini_PEKKA = pygame.transform.scale(mini_PEKKA, (73, 93))
    hog_rider = pygame.image.load("Assets\\EXir\\hog_rider.png")
    hog_rider = pygame.transform.scale(hog_rider, (73, 93))
    screen.blit(UITab, (155, 600 ))
    screen.blit(pri_ui, (182,610))
    screen.blit(giant_ui, (257, 610))
    screen.blit(mini_PEKKA, (332, 610))
    screen.blit(hog_rider , (406, 610))
Units_Animations_list=[[], []]
class Units(pygame.sprite.Sprite):
    '''
    def __init__(self):
        self.movement_types=['Fly','Walk']
        self.shoot_types=['Air','Ground','Both']
        self.target_types=['Building','Any']
        self.rarity_types = ['Common','Rare','Epic','Legendary']
        self.movement_speeds = ['Slow','Normal','Fast']
        self.elixir_costs = [1,2,3,4,5,6,7,8,9,10]
        self.counts = [i for i in range(1,15)]
        self.hitpoints = [i for i in range(10,3000)]
        self.damages=[i for i in range(10,1000)]
        self.life_states=['Dead','Alive']
        self.deploy_states=['Deployed','inDeck','notinDeck']
        self.deploy_state = ['notinDeck','inDeck']
        self.attack_types = ['Melee','Ranged']
    '''

    def wethertomove(self):
        global Units_Animations_list
        self.wethertomove_counter=True
        if self.target_type == 'Any':
            if self.side=='Down':
                for i in Units_Animations_list[0]:
                    if (abs(self.Animation.rect.center[0]-i.rect.center[0])**2+abs(self.Animation.rect.center[1]-i.rect.center[1])**2)**0.5 <=self.Animation.range:
                        self.wethertomove_counter=False
                        i.hp -= self.Animation.damage
                        if i.hp <1:
                            i.stat='Dead'
                            Units_Animations_list[0].remove(i)
                            i.hp=i.hitpoint
            if self.side=='Up':
                for i in Units_Animations_list[1]:
                    if (abs(self.Animation.rect.center[0]-i.rect.center[0])**2 + abs(self.Animation.rect.center[1]-i.rect.center[1])**2)**0.5 <=self.Animation.range:
                        self.wethertomove_counter=False
                        self.enemy_Animation = i
                        i.hp -= self.Animation.damage
                        if i.hp <1:
                            i.stat='Dead'
                            Units_Animations_list[1].remove(i)
                            i.hp=i.hitpoint
        return self.wethertomove_counter

    def move(self):
        #Hit
        dt=0.03
        self.HitGroup.update(dt)
        #waghti ke rah miran
        if self.Animation.stat=='Alive':
            if self.wethertomove() == True:
                dt=0.03
                self.Group.update(dt)
                if self.wetheranimate_counter==True:
                    self.Group.draw(screen)
                if self.side == 'Down':
                    if 0<=self.x <= 225 :
                        if self.Animation.rect.center!= (130,282) and self.leftmovecounter!=1:
                            self.xmovefactor = 130 - self.Animation.rect.center[0]
                            self.ymovefactor = 282 - self.Animation.rect.center[1]
                            if self.ymovefactor!=0:
                                self.Angle=math.atan2(self.ymovefactor,self.xmovefactor)
                                self.dx=math.cos(self.Angle)*2
                                self.dy=math.sin(self.Angle)*2
                                #should consider wether princess tower is destroyed or not
                                self.Animation.rect.move_ip(self.dx,self.dy)
                                self.HitAnimation.rect.move_ip(self.dx,self.dy)
                        else:
                            if self.Animation.rect.center != (130, 402) :
                                self.xmovefactor = 130 - self.Animation.rect.center[0]
                                self.ymovefactor = 402 - self.Animation.rect.center[1]
                                if self.ymovefactor != 0:
                                    self.Angle = math.atan2(self.ymovefactor, self.xmovefactor)
                                    self.dx = math.cos(self.Angle) * 1.5
                                    self.dy = math.sin(self.Angle) * 1.5
                                    # should consider wether princess tower is destroyed or not
                                    self.Animation.rect.move_ip(self.dx, self.dy)
                                    self.HitAnimation.rect.move_ip(self.dx, self.dy)
                                    self.leftmovecounter=1
                                #self.Group.
                    elif 225<self.x<=500:
                        if self.Animation.rect.center!= (408,282) and self.rightmovecounter!=1:
                            self.xmovefactor =abs( 408 - self.Animation.rect.center[0])
                            self.ymovefactor =abs( 282 - self.Animation.rect.center[1])
                            if self.ymovefactor!=0:
                                self.Angle=math.atan2(self.ymovefactor,self.xmovefactor)
                                self.dx=math.cos(self.Angle)*2
                                self.dy=math.sin(self.Angle)*2
                                #should consider wether princess tower is destroyed or not
                                self.Animation.rect.move_ip(self.dx,self.dy)
                                self.HitAnimation.rect.move_ip(self.dx,self.dy)
                        else:
                            if self.Animation.rect.center != (408, 402) :
                                self.xmovefactor = 408 - self.Animation.rect.center[0]
                                self.ymovefactor = 402 - self.Animation.rect.center[1]
                                if self.ymovefactor != 0:
                                    self.Angle = math.atan2(self.ymovefactor, self.xmovefactor)
                                    self.dx = math.cos(self.Angle) * 1.5
                                    self.dy = math.sin(self.Angle) * 1.5
                                    # should consider wether princess tower is destroyed or not
                                    self.Animation.rect.move_ip(self.dx, self.dy)
                                    self.HitAnimation.rect.move_ip(self.dx, self.dy)
                                    self.rightmovecounter=1
                elif self.side =='Up':
                    if 0<=self.x <= 225 :
                        if self.Animation.rect.center!= (130,340) and self.leftmovecounter!=1:
                            self.xmovefactor = 130 - self.Animation.rect.center[0]
                            self.ymovefactor = 340 - self.Animation.rect.center[1]
                            if self.ymovefactor!=0:
                                self.Angle=math.atan2(self.ymovefactor,self.xmovefactor)
                                self.dx=math.cos(self.Angle)*2
                                self.dy=math.sin(self.Angle)*2
                                #should consider wether princess tower is destroyed or not
                                self.Animation.rect.move_ip(self.dx,self.dy)
                                self.HitAnimation.rect.move_ip(self.dx,self.dy)
                        else:
                            if self.Animation.rect.center != (130, 210) :
                                self.xmovefactor = 130 - self.Animation.rect.center[0]
                                self.ymovefactor = 210 - self.Animation.rect.center[1]
                                if self.ymovefactor != 0:
                                    self.Angle = math.atan2(self.ymovefactor, self.xmovefactor)
                                    self.dx = math.cos(self.Angle) * 1.5
                                    self.dy = math.sin(self.Angle) * 1.5
                                    # should consider wether princess tower is destroyed or not
                                    self.Animation.rect.move_ip(self.dx, self.dy)
                                    self.HitAnimation.rect.move_ip(self.dx, self.dy)
                                    self.leftmovecounter=1
                    elif 225<self.x<=500:
                        if self.Animation.rect.center!= (408,340) and self.rightmovecounter!=1:
                            self.xmovefactor =abs( 408 - self.Animation.rect.center[0])
                            self.ymovefactor =-abs( 340 - self.Animation.rect.center[1])
                            if self.ymovefactor!=0:
                                self.Angle=math.atan2(self.ymovefactor,self.xmovefactor)
                                self.dx=math.cos(self.Angle)*2
                                self.dy=math.sin(self.Angle)*2
                                #should consider wether princess tower is destroyed or not
                                self.Animation.rect.move_ip(self.dx,self.dy)
                                self.HitAnimation.rect.move_ip(self.dx,self.dy)
                        else:
                            if self.Animation.rect.center != (408, 210) :
                                self.xmovefactor = 408 - self.Animation.rect.center[0]
                                self.ymovefactor = 210 - self.Animation.rect.center[1]
                                if self.ymovefactor != 0:
                                    self.Angle = math.atan2(self.ymovefactor, self.xmovefactor)
                                    self.dx = math.cos(self.Angle) * 1.5
                                    self.dy = math.sin(self.Angle) * 1.5
                                    # should consider wether princess tower is destroyed or not
                                    self.Animation.rect.move_ip(self.dx, self.dy)
                                    self.HitAnimation.rect.move_ip(self.dx, self.dy)
                                    self.rightmovecounter=1
        #consider splash elixir effect when they are destroyed

            #hit
            #waghti ba ye sarbaze dige dargir mishan
            else:
                self.HitGroup.draw(screen)

            #waghti be tower miresan
            if self.side=='Down':
                #towere payin chap
                if 0<=self.x<=225:
                    if self.Animation.rect.center == (130,402):
                        self.wetheranimate_counter=False
                        self.HitGroup.draw(screen)
                #towere payin rast
                else:
                    if self.Animation.rect.center ==(408,402):
                        self.wetheranimate_counter=False
                        self.HitGroup.draw(screen)
            else:
                #towere bala chap
                if 0<=self.x<=225:
                    if self.Animation.rect.center == (130,210):
                        self.wetheranimate_counter=False
                        self.HitGroup.draw(screen)
                #towere bala rast
                else:
                    if self.Animation.rect.center ==(408,210):
                        self.wetheranimate_counter=False
                        self.HitGroup.draw(screen)
class Giant(Units):
    def __init__(self, x, y, side):
        global Units_Animations_list
        # needed for all troops classes
        # attributes
        self.side = side
        # for movement
        self.leftmovecounter = 0
        self.rightmovecounter = 0
        #
        self.elixir_cost = 4
        self.target_type = 'Building'


        # load image
        self.x = x
        self.y = y
        self.Goimages = []
        self.Hitimages = []
        self.wetheranimate_counter = True
        if self.side =='Down':
            for i in range(1,17):
                self.img= pygame.image.load("Assets\\chr_giant_out\\%s_%s.png"%(i,self.side))
                self.img=pygame.transform.scale(self.img,(90,90))
                self.Goimages.append(self.img)
            for i in range(1,11):
                self.img2= pygame.image.load("Assets\\chr_giant_out\\%s_Hit_%s.png"%(i,self.side))
                self.img2 = pygame.transform.scale(self.img2, (90, 90))
                self.Hitimages.append(self.img2)
        if self.side =='Up':
            for i in range(1,17):
                self.img= pygame.image.load("Assets\\chr_giant_out\\%s_%s.png"%(i,self.side))
                self.img=pygame.transform.scale(self.img,(90,90))
                self.Goimages.append(self.img)
            for i in range(1,11):
                self.img2 = pygame.image.load("Assets\\chr_giant_out\\%s_Hit_%s.png"%(i,self.side))
                self.img2 = pygame.transform.scale(self.img2, (90, 90))
                self.Hitimages.append(self.img2)
        self.Animation = AnimatedSprite((self.x, self.y), self.Goimages)
        self.HitAnimation = AnimatedSprite((self.Animation.rect.center[0] - 50, self.Animation.rect.center[1] - 80),
                                           self.Hitimages)
        self.HitGroup = pygame.sprite.Group(self.HitAnimation)

        self.Group = pygame.sprite.Group(self.Animation)
        if self.side =='Down':
            Units_Animations_list[1].append(self.Animation)
        if self.side =='Up' :
            Units_Animations_list[0].append(self.Animation)
        #____________________DMG_________________#
        self.Animation.range=30
        self.Animation.stat = 'Alive'
        self.Animation.hitpoint = 300
        self.Animation.hp = self.Animation.hitpoint
        self.Animation.damage = 2
class Hogrider(Units):
    def __init__(self, x, y, side):
        global Units_Animations_list
        # needed for all troops classes
        # attributes
        self.side = side
        # for movement
        self.leftmovecounter = 0
        self.rightmovecounter = 0
        #
        self.elixir_cost = 4
        self.target_type = 'Building'


        # load image
        self.x = x
        self.y = y
        self.Goimages = []
        self.Hitimages = []
        self.wetheranimate_counter = True
        if self.side =='Down':
            for i in range(1,9):
                self.img= pygame.image.load("Assets\\chr_hogrider_out\\%s_%s.png"%(i,self.side))
                self.img=pygame.transform.scale(self.img,(90,90))
                self.Goimages.append(self.img)
            for i in range(1,11):
                self.img2= pygame.image.load("Assets\\chr_hogrider_out\\%s_Hit_%s.png"%(i,self.side))
                self.img2 = pygame.transform.scale(self.img2, (90, 90))
                self.Hitimages.append(self.img2)
        if self.side =='Up':
            for i in range(1,9):
                self.img= pygame.image.load("Assets\\chr_hogrider_out\\%s_%s.png"%(i,self.side))
                self.img=pygame.transform.scale(self.img,(90,90))
                self.Goimages.append(self.img)
            for i in range(1,11):
                self.img2 = pygame.image.load("Assets\\chr_hogrider_out\\%s_Hit_%s.png"%(i,self.side))
                self.img2 = pygame.transform.scale(self.img2, (90, 90))
                self.Hitimages.append(self.img2)
        self.Animation = AnimatedSprite((self.x, self.y), self.Goimages)
        self.HitAnimation = AnimatedSprite((self.Animation.rect.center[0] - 50, self.Animation.rect.center[1] - 80),
                                           self.Hitimages)
        self.HitGroup = pygame.sprite.Group(self.HitAnimation)

        self.Group = pygame.sprite.Group(self.Animation)
        if self.side =='Down':
            Units_Animations_list[1].append(self.Animation)
        if self.side =='Up' :
            Units_Animations_list[0].append(self.Animation)
        #____________________DMG_________________#
        self.Animation.range=30
        self.Animation.stat = 'Alive'
        self.Animation.hitpoint = 400
        self.Animation.hp = self.Animation.hitpoint
        self.Animation.damage = 3
class Prince(Units):
    def __init__(self,x,y,side):
        global Units_Animations_list
        #needed for all troops classes
        #attributes
        self.side = side
        # for movement
        self.leftmovecounter = 0
        self.rightmovecounter = 0
        self.target_type = 'Any'
        self.elixir_cost = 3
        # load image
        self.x = x
        self.y = y
        self.Goimages = []
        self.Hitimages = []

        self.wetheranimate_counter = True
        if self.side =='Down':
            for i in range(1,11):
                self.img= pygame.image.load("Assets\\chr_prince_out\\%s_%s.png"%(i,self.side))
                self.img=pygame.transform.scale(self.img,(90,90))
                self.Goimages.append(self.img)
                self.img2= pygame.image.load("Assets\\chr_prince_out\\%s_Hit.png"%(i))
                self.img2 = pygame.transform.scale(self.img2, (90, 90))
                self.Hitimages.append(self.img2)
        if self.side =='Up':
            for i in range(1,11):
                self.img= pygame.image.load("Assets\\chr_prince_out\\%s_%s.png"%(i,self.side))
                self.img=pygame.transform.scale(self.img,(90,90))
                self.Goimages.append(self.img)
                self.img2 = pygame.image.load("Assets\\chr_prince_out\\%s_Hit_%s.png"%(i,self.side))
                self.img2 = pygame.transform.scale(self.img2, (90, 90))
                self.Hitimages.append(self.img2)
        self.Animation = AnimatedSprite((self.x, self.y), self.Goimages)
        self.HitAnimation = AnimatedSprite((self.Animation.rect.center[0] - 40, self.Animation.rect.center[1] - 80),
                                           self.Hitimages)
        self.HitGroup = pygame.sprite.Group(self.HitAnimation)

        self.Group = pygame.sprite.Group(self.Animation)

        if self.side =='Down':
            Units_Animations_list[1].append(self.Animation)
        if self.side =='Up' :
            Units_Animations_list[0].append(self.Animation)
        #--------------------------DAMAGE------------------------------#
        self.Animation.range=30
        self.Animation.stat='Alive'
        self.Animation.hitpoint = 400
        self.Animation.hp=self.Animation.hitpoint
        self.Animation.damage = 3
class Knight(Units):
    def __init__(self,x,y,side):
        global Units_Animations_list
        #needed for all troops classes
        #attributes
        self.side = side
        # for movement
        self.leftmovecounter = 0
        self.rightmovecounter = 0
        self.target_type = 'Any'
        self.elixir_cost = 2
        # load image
        self.x = x
        self.y = y
        self.Goimages = []
        self.Hitimages = []

        self.wetheranimate_counter = True
        if self.side =='Down':
            for i in range(1,15):
                self.img= pygame.image.load("Assets\\chr_knight_out\\%s_%s.png"%(i,self.side))
                self.img=pygame.transform.scale(self.img,(90,90))
                self.Goimages.append(self.img)
                self.img2= pygame.image.load("Assets\\chr_knight_out\\%s_Hit.png"%(i))
                self.img2 = pygame.transform.scale(self.img2, (90, 90))
                self.Hitimages.append(self.img2)
        if self.side =='Up':
            for i in range(1,13):
                self.img= pygame.image.load("Assets\\chr_knight_out\\%s_%s.png"%(i,self.side))
                self.img=pygame.transform.scale(self.img,(90,90))
                self.Goimages.append(self.img)
            for i in range(1,12):
                self.img2 = pygame.image.load("Assets\\chr_knight_out\\%s_Hit_%s.png"%(i,self.side))
                self.img2 = pygame.transform.scale(self.img2, (90, 90))
                self.Hitimages.append(self.img2)
        self.Animation = AnimatedSprite((self.x, self.y), self.Goimages)
        self.HitAnimation = AnimatedSprite((self.Animation.rect.center[0] - 50, self.Animation.rect.center[1] - 70),
                                           self.Hitimages)
        self.HitGroup = pygame.sprite.Group(self.HitAnimation)

        self.Group = pygame.sprite.Group(self.Animation)

        if self.side =='Down':
            Units_Animations_list[1].append(self.Animation)
        if self.side =='Up' :
            Units_Animations_list[0].append(self.Animation)
        #--------------------------DAMAGE------------------------------#
        self.Animation.range=30
        self.Animation.stat='Alive'
        self.Animation.hitpoint = 300
        self.Animation.hp=self.Animation.hitpoint
        self.Animation.damage = 2
class Minipekka(Units):
    def __init__(self,x,y,side):
        global Units_Animations_list
        #needed for all troops classes
        #attributes
        self.side = side
        # for movement
        self.leftmovecounter = 0
        self.rightmovecounter = 0
        self.target_type = 'Any'
        self.elixir_cost = 2
        # load image
        self.x = x
        self.y = y
        self.Goimages = []
        self.Hitimages = []

        self.wetheranimate_counter = True
        if self.side =='Down':
            for i in range(1,13):
                self.img= pygame.image.load("Assets\\chr_mini_PEKKA_out\\%s_%s.png"%(i,'Dwon'))
                self.img=pygame.transform.scale(self.img,(75,75))
                self.Goimages.append(self.img)
            for i in range(1,11):
                self.img2= pygame.image.load("Assets\\chr_mini_PEKKA_out\\%s_Hit_%s.png"%(i,'Down'))
                self.img2 = pygame.transform.scale(self.img2, (75, 75))
                self.Hitimages.append(self.img2)
        if self.side =='Up':
            for i in range(1,13):
                self.img= pygame.image.load("Assets\\chr_mini_PEKKA_out\\%s_%s.png"%(i,self.side))
                self.img=pygame.transform.scale(self.img,(75,75))
                self.Goimages.append(self.img)
            for i in range(1,12):
                self.img2 = pygame.image.load("Assets\\chr_mini_PEKKA_out\\%s_Hit_%s.png"%(i,self.side))
                self.img2 = pygame.transform.scale(self.img2, (75, 75))
                self.Hitimages.append(self.img2)
        self.Animation = AnimatedSprite((self.x, self.y), self.Goimages)
        self.HitAnimation = AnimatedSprite((self.Animation.rect.center[0] - 50, self.Animation.rect.center[1] - 70),
                                           self.Hitimages)
        self.HitGroup = pygame.sprite.Group(self.HitAnimation)

        self.Group = pygame.sprite.Group(self.Animation)

        if self.side =='Down':
            Units_Animations_list[1].append(self.Animation)
        if self.side =='Up' :
            Units_Animations_list[0].append(self.Animation)
        #--------------------------DAMAGE------------------------------#
        self.Animation.range=30
        self.Animation.stat='Alive'
        self.Animation.hitpoint = 250
        self.Animation.hp=self.Animation.hitpoint
        self.Animation.damage = 3
#consider deploying three goblins at the same time
class Goblin(Units):
    def __init__(self,x,y,side):
        global Units_Animations_list
        #needed for all troops classes
        #attributes
        self.side = side
        # for movement
        self.leftmovecounter = 0
        self.rightmovecounter = 0
        self.target_type = 'Any'
        self.elixir_cost = 1
        # load image
        self.x = x
        self.y = y
        self.Goimages = []
        self.Hitimages = []

        self.wetheranimate_counter = True
        if self.side =='Down':
            for i in range(1,9):
                self.img= pygame.image.load("Assets\\chr_goblins_out\\%s_%s.png"%(i,'Down'))
                self.img=pygame.transform.scale(self.img,(60,60))
                self.Goimages.append(self.img)
            for i in range(1,10):
                self.img2= pygame.image.load("Assets\\chr_goblins_out\\%s_Hit_%s.png"%(i,'Down'))
                self.img2 = pygame.transform.scale(self.img2, (60, 60))
                self.Hitimages.append(self.img2)
        if self.side =='Up':
            for i in range(1,9):
                self.img= pygame.image.load("Assets\\chr_goblins_out\\%s_%s.png"%(i,self.side))
                self.img=pygame.transform.scale(self.img,(60,60))
                self.Goimages.append(self.img)
            for i in range(1,9):
                self.img2 = pygame.image.load("Assets\\chr_goblins_out\\%s_Hit_%s.png"%(i,self.side))
                self.img2 = pygame.transform.scale(self.img2, (60, 60))
                self.Hitimages.append(self.img2)
        self.Animation = AnimatedSprite((self.x, self.y), self.Goimages)
        self.HitAnimation = AnimatedSprite((self.Animation.rect.center[0] - 50, self.Animation.rect.center[1] - 70),
                                           self.Hitimages)
        self.HitGroup = pygame.sprite.Group(self.HitAnimation)

        self.Group = pygame.sprite.Group(self.Animation)

        if self.side =='Down':
            Units_Animations_list[1].append(self.Animation)
        if self.side =='Up' :
            Units_Animations_list[0].append(self.Animation)
        #--------------------------DAMAGE------------------------------#
        self.Animation.range=30
        self.Animation.stat='Alive'
        self.Animation.hitpoint = 100
        self.Animation.hp=self.Animation.hitpoint
        self.Animation.damage = 1
def drawTowerUp():
    Enm_tower = pygame.image.load("Assets\\Towers\\Enm_town_main.png")
    Enm_tower = pygame.transform.scale(Enm_tower, (100, 115))
    Enm_small_tower = pygame.image.load("Assets\\Towers\\Enm_town - Copy.png")
    Enm_small_tower = pygame.transform.scale(Enm_small_tower, (70, 90))
    Enm_small_tower_2 = pygame.image.load("Assets\\Towers\\Enm_town.png")
    Enm_small_tower_2 = pygame.transform.scale(Enm_small_tower_2, (70, 90))
    screen.blit(Enm_tower, (200, 1))
    screen.blit(Enm_small_tower, (78, 80))
    screen.blit(Enm_small_tower_2, (347, 80))
def drawTowerDown():
    self_tower = pygame.image.load("Assets\\Towers\\Self_town_main.png")
    self_tower = pygame.transform.scale(self_tower, (100,118))
    self_small_tower = pygame.image.load("Assets\\Towers\\Self_town - Copy.png")
    self_small_tower = pygame.transform.scale(self_small_tower, (70, 90))
    self_small_tower_2 = pygame.image.load("Assets\\Towers\\Self_town.png")
    self_small_tower_2 = pygame.transform.scale(self_small_tower_2, (70, 90))
    screen.blit(self_tower, (200, 445))
    screen.blit(self_small_tower, (78, 395))
    screen.blit(self_small_tower_2, (347, 395))
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, position, images):
        """
        Animated sprite object.

        Args:
            position: x, y coordinate on the screen to place the AnimatedSprite.
            images: Images to use in the animation.
        """
        super(AnimatedSprite, self).__init__()

        size = (96, 144)  # This should match the size of the images.

        self.rect = pygame.Rect(position, size)
        self.images = images
        self.images_right = images
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the animation.


        self.animation_time = 0.07
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0

    def getindex(self):
        return self.index
    def update_time_dependent(self, dt):
        """
        Updates the image of Sprite approximately every 0.1 second.

        Args:
            dt: Time elapsed between each frame.
        """

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]


    def update_frame_dependent(self):
        """
        Updates the image of Sprite every 6 frame (approximately every 0.1 second if frame rate is 60).
        """

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
class Exirbar(pygame.sprite.Sprite):

    def __init__(self, position):
        """
        Animated sprite object.

        Args:
            position: x, y coordinate on the screen to place the AnimatedSprite.
            images: Images to use in the animation.
        """
        super(Exirbar, self).__init__()
        images = []
        images.append(pygame.image.load("Assets\\EXir\\exribar\\1.png"))
        images.append(pygame.image.load("Assets\\EXir\\exribar\\2.png"))
        images.append(pygame.image.load("Assets\\EXir\\exribar\\3.png"))
        images.append(pygame.image.load("Assets\\EXir\\exribar\\4.png"))
        images.append(pygame.image.load("Assets\\EXir\\exribar\\5.png"))
        images.append(pygame.image.load("Assets\\EXir\\exribar\\6.png"))
        images.append(pygame.image.load("Assets\\EXir\\exribar\\7.png"))
        images.append(pygame.image.load("Assets\\EXir\\exribar\\8.png"))


        size = (307, 56)  # This should match the size of the images.

        self.rect = pygame.Rect(position, size)
        self.images = images
        self.images_right = images
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the animation.

        self.animation_time = 2
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0

    def getindex(self):
        return self.index

    def update_time_dependent(self, dt):
        """
        Updates the image of Sprite approximately every 0.1 second.

        Args:
            dt: Time elapsed between each frame.
        """
        if self.index == 7:
            return None
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]


    def update_frame_dependent(self):
        """
        Updates the image of Sprite every 6 frame (approximately every 0.1 second if frame rate is 60).
        """

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)

    def setindex(self, indexs):
        self.index = indexs
class Checkwin(pygame.sprite.Sprite):
    def __init__(self, position, images):

        super(Checkwin, self).__init__()


        size = (120, 180)  # This should match the size of the images.

        self.rect = pygame.Rect(position, size)
        self.images = images
        self.images_right = images
         # 'image' is the current image of the animation.
        self.image = self.images[0]
        self.position = position


    def getindex(self, x):
        self.index = x
        self.image = self.images[self.index]
class Healthbar:
    def __init__(self, ELH , Sc, x, y):
        self.x = x
        self.y = y
        self.x_var = Sc
        self.ELH = ELH

    def setHB(self, n):
        self.n = n
        self.Scale = self.n // self.x_var
        self.ElpsHealth = self.ELH - self.n

        self.text = str(self.ElpsHealth).rjust(3)
        self.font = pygame.font.SysFont('Consolas', 10)
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 60, 8))
        pygame.draw.rect(screen, (255, 255, 255), (self.x + 1, self.y + 1, 58 - self.Scale, 6))
        screen.blit(self.font.render(self.text, True, (100, 100, 100)), (self.x + 15, self.y - 1))
def DrawBg():
    # background of the troops table
    ttabe = pygame.image.load('Assets\\EXir\\ui_sprite_264.png')
    ttabe = pygame.transform.scale(ttabe, (250, 500))
    ttabe = pygame.transform.rotate(ttabe, 90)
    screen.blit(ttabe, (0, 600))
def loadimageself():
    images = []
    a = pygame.image.load("Assets\\EXir\\Checkwin\\1.png")
    a = pygame.transform.scale(a, (60, 80))
    images.append(a)
    a = pygame.image.load("Assets\\EXir\\Checkwin\\2.png")
    a = pygame.transform.scale(a, (60, 80))
    images.append(a)
    a = pygame.image.load("Assets\\EXir\\Checkwin\\3.png")
    a = pygame.transform.scale(a, (60, 80))
    images.append(a)
    a = pygame.image.load("Assets\\EXir\\Checkwin\\4.png")
    a = pygame.transform.scale(a, (60, 80))
    images.append(a)
    return images
def loadimageEn():
    images = []
    a = pygame.image.load("Assets\\EXir\\Checkwin\\0_0.png")
    a = pygame.transform.scale(a, (60, 80))
    images.append(a)
    a = pygame.image.load("Assets\\EXir\\Checkwin\\1_1.png")
    a = pygame.transform.scale(a, (60, 80))
    images.append(a)
    a = pygame.image.load("Assets\\EXir\\Checkwin\\2_2.png")
    a = pygame.transform.scale(a, (60, 80))
    images.append(a)
    a = pygame.image.load("Assets\\EXir\\Checkwin\\3_3.png")
    a = pygame.transform.scale(a, (60, 80))
    images.append(a)

    return images
def main():
    # create counter for end the game :)
    counter = 120
    text = '120'.rjust(2)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consloas', 30)
    DrawBg()
    drawTowerUp()
    drawTowerDown()
    '''
    Troops'''
    P=Minipekka(210,100,'Down')
    G=Goblin(235,120,'Down')
    S=Goblin(215,320,'Up')
    F=Minipekka(230,350,'Up')
    #Draw Health Bar
    DHB_left = Healthbar(ELH= 1000, Sc= 17.5, x= 87, y= 440)
    DHB_Right = Healthbar(ELH= 1000, Sc= 17.5, x= 355, y= 441)
    DHB_Main = Healthbar(ELH= 2000, Sc= 35, x= 223, y= 501)
    DHB_left_En = Healthbar(ELH= 1000, Sc= 17.5, x= 87, y= 70)
    DHB_Right_En = Healthbar(ELH= 1000, Sc= 17.5, x= 356, y= 70)
    DHB_Main_En = Healthbar(ELH= 1000, Sc= 17.5, x= 223, y= 0)
    running = True
    drawUI()
    temper = pygame.image.load("Assets\\Map\\map.png")
    temper = pygame.transform.scale(temper, (500, 600))
    #draw result of game in instant
    load_image_self = loadimageself()
    load_image_En   = loadimageEn()
    Chkresself = Checkwin((430, 320), load_image_self)
    Chkresself_sprite = pygame.sprite.Group(Chkresself)
    ChkresEn = Checkwin((430, 220), load_image_En)
    ChkresEn_sprite = pygame.sprite.Group(ChkresEn)
    #create a glow gif when a exir bar is complete

    #draw exir bar
    exirbar = Exirbar(position=(170, 690))
    exirbar_sprite = pygame.sprite.Group(exirbar)
    C_pr = True

    timeSC = pygame.image.load('Assets\\EXir\\ui_sprite_476.png')
    timeSC = pygame.transform.scale(timeSC, (55, 25))

    while running:
        dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop.
        #pygame.draw.rect(screen, (255, 255, 255), (0, 0, 480, 480))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.USEREVENT and counter != 0 :
                counter -= 1
                text = str(counter).rjust(3)

        if C_pr == True:
            if exirbar.getindex() >= 5:
                exirbar.setindex(exirbar.getindex()-4)
                C_pr = False

        screen.blit(temper, (0, 0))

        exirbar_sprite.update(dt)
        exirbar_sprite.draw(screen)

        #get the favorite index
        Chkresself.getindex(2)
        ChkresEn.getindex((3))

        Chkresself_sprite.draw(screen)
        ChkresEn_sprite.draw(screen)

        #all_sprites.draw(screen)
        drawTowerUp() #The Error was ignored

        screen.blit(font.render(text, True, (0, 0, 0)), (12, 6))
        screen.blit(timeSC, (2, 2))

        #Draw Health Bar
        DHB_left.setHB(400)
        DHB_Right.setHB(500)
        DHB_Main.setHB(600)

        DHB_left_En.setHB(700)
        DHB_Right_En.setHB(300)
        DHB_Main_En.setHB(100)
        '''
        PRINCE
        '''

        #movement
        P.move()
        G.move()
        S.move()
        F.move()
        #---

        drawTowerDown()

        pygame.display.update()
if __name__ == '__main__':
    main()
#-_--__-_XXXXXXXXXXXXXXXXXXXXXXXXXXX-_#



class MoveTroops():
    def __init__(self, image, width, height, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.x1 = x
        self.y1 = y
        self.W = width
        self.H = height
        self.drag = False
        # self.image_m = image_m
        self.createimg = False
        self.getposition = (0, 0)
        self.counter = 0
        self.aliveimage = True
        self.control = False
        self.checkmouse = 0
        self.checker = False
        self.subexir = False

    def move(self):
        self.counter = 0

        if self.aliveimage:
            screen.blit(self.image, (self.x1, self.y1))

        if not self.control:
            self.counter = 0
            return None
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        if not self.createimg:
            if self.click[0] == 1 and self.x1 + self.W > self.mouse[0] > self.x1 and self.y1 + self.H > self.mouse[1] > self.y1:  # asking if i am within the boundaries of the image
                self.drag = True
                self.counter = 1
                self.checker = True

        if self.checker == True:
            if self.click[0] == 0:
                self.drag = False
                self.counter = 2

        if self.counter != 0:
            self.createimg = True
            self.aliveimage = False

        if self.drag == True:
            self.x = self.mouse[0] - (self.W / 2)
            self.y = self.mouse[1] - (self.H / 2)

            # screen.blit(self.image_m, (self.x, self.y))

        self.getposition = (self.x, self.y)

    def getpostion(self):
        return self.getposition


def loadtowerimage():
    cannon = pygame.image.load("Assets\\Towers\\cannon.png")
    cannon_scaled = pygame.transform.scale(cannon, (165, 151))
    cannon_scaled_left = pygame.transform.scale(cannon, (125, 111))
    cannon_scaled_right = pygame.transform.scale(cannon, (125, 111))


    en_cannon = pygame.image.load("Assets\\Towers\\En_cannon.png")
    en_cannon_scaled = pygame.transform.scale(en_cannon, (165, 151))
    cannon_dir = pygame.image.load("Assets\\Towers\\1_cannon.png")
    en_cannon_dir = pygame.image.load("Assets\\Towers\\18_cannon.png")

    screen.blit(cannon_scaled, (153, 440))
    screen.blit(cannon_scaled_left, (39, 390))
    screen.blit(cannon_scaled_right, (307, 390))
    screen.blit(en_cannon_scaled, (153, 0))
    # screen.blit(cannon_dir, (250, 500))
    # screen.blit(en_cannon_dir, (250, 100))


# --------------------------------------------------------------------


pri_ui = pygame.image.load("Assets\\EXir\\prince.png")
pri_ui = pygame.transform.scale(pri_ui, (73, 93))
giant_ui = pygame.image.load("Assets\\EXir\\giant.png")
giant_ui = pygame.transform.scale(giant_ui, (73, 93))
goblins_ui = pygame.image.load("Assets\\EXir\\goblins.png")
goblins_ui = pygame.transform.scale(goblins_ui, (73, 93))
barbar_ui = pygame.image.load("Assets\\EXir\\barbarians.png")
barbar_ui = pygame.transform.scale(barbar_ui, (73, 93))
knight_ui = pygame.image.load("Assets\\EXir\\knight.png")
knight_ui = pygame.transform.scale(knight_ui, (73, 93))
mini_PEKKA = pygame.image.load("Assets\\EXir\\mini_PEKKA.png")
mini_PEKKA = pygame.transform.scale(mini_PEKKA, (73, 93))
hog_rider = pygame.image.load("Assets\\EXir\\hog_rider.png")
hog_rider = pygame.transform.scale(hog_rider, (73, 93))
screen.blit(pri_ui, (182, 610))
screen.blit(giant_ui, (257, 610))
screen.blit(mini_PEKKA, (332, 610))
screen.blit(hog_rider, (406, 610))


# ------------------------------------------------------------------------

def main():
    # --------------------------------------------------------------------
    global prince
    global giant_ui
    global goblins_ui
    global knight_ui
    global mini_PEKKA
    global hog_rider

    randlist = [(182, 610), (257, 610), (332, 610), (406, 610)]
    choose = random.randint(0, len(randlist) - 1)

    dAd_prince = MoveTroops(pri_ui, 73, 93, randlist[choose][0], randlist[choose][1])
    randlist.remove(randlist[choose])

    choose_1 = random.randint(0, len(randlist) - 1)

    dAd_giant = MoveTroops(giant_ui, 73, 93, randlist[choose_1][0], randlist[choose_1][1])
    randlist.remove(randlist[choose_1])

    choose_2 = random.randint(0, len(randlist) - 1)
    dad_PEKKA = MoveTroops(mini_PEKKA, 73, 93, randlist[choose_2][0], randlist[choose_2][1])
    randlist.remove(randlist[choose_2])

    choose_3 = random.randint(0, len(randlist) - 1)
    dad_knight = MoveTroops(knight_ui, 73, 93, randlist[choose_3][0], randlist[choose_3][1])
    randlist.remove(randlist[choose_3])

    # --------------------------------------------------------------------

    UITab = pygame.image.load("Assets\\EXir\\UITab.p"
                              "ng")

    # create counter for end the game :)
    counter = 180
    text = '180'.rjust(2)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consloas', 30)

    # --------------------------------------------------------------------

    # create object


    cannon_sp_main_self = cannon.AnimatedSprite((173, 385), cannon.load_images(130), 130)
    up_cannon_sp_main_self = pygame.sprite.Group(cannon_sp_main_self)

    cannon_sp_left_self = cannon.AnimatedSprite((55, 349), cannon.load_images(100), 100)
    up_cannon_sp_left_self = pygame.sprite.Group(cannon_sp_left_self)

    cannon_sp_right_self = cannon.AnimatedSprite((320, 349), cannon.load_images(100), 100)
    up_cannon_sp_right_self = pygame.sprite.Group(cannon_sp_right_self)

    # --------------------------------------------------------------------

    # Draw Health Bar
    DHB_left = Healthbar(ELH=1000, Sc=17.5, x=87, y=440)
    DHB_Right = Healthbar(ELH=1000, Sc=17.5, x=355, y=441)
    DHB_Main = Healthbar(ELH=2000, Sc=35, x=223, y=501)
    DHB_left_En = Healthbar(ELH=1000, Sc=17.5, x=87, y=70)
    DHB_Right_En = Healthbar(ELH=1000, Sc=17.5, x=356, y=70)
    DHB_Main_En = Healthbar(ELH=1000, Sc=17.5, x=223, y=0)

    running = True
    temper = pygame.image.load("Assets\\Map\\map.png")
    temper = pygame.transform.scale(temper, (500, 600))

    # draw result of game in instant
    load_image_self = loadimageself()
    load_image_En = loadimageEn()
    Chkresself = Checkwin((430, 320), load_image_self)
    Chkresself_sprite = pygame.sprite.Group(Chkresself)

    ChkresEn = Checkwin((430, 220), load_image_En)
    ChkresEn_sprite = pygame.sprite.Group(ChkresEn)

    # draw excir bar
    exirbar = Exirbar(position=(170, 690))
    exirbar_sprite = pygame.sprite.Group(exirbar)
    C_pr = True

    timeSC = pygame.image.load('Assets\\EXir\\ui_sprite_476.png')
    timeSC = pygame.transform.scale(timeSC, (55, 25))

    while running:
        screen.fill((0, 0, 0))
        screen.blit(temper, (0, 0))
        screen.blit(UITab, (155, 600))

        dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop.
        # pygame.draw.rect(screen, (255, 255, 255), (0, 0, 480, 480))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                #  ----------------------------------------------------
            if event.type == pygame.USEREVENT and counter != 0:
                counter -= 1
                text = str(counter).rjust(3)

        screen.blit(font.render(text, True, (0, 0, 0)), (12, 6))
        screen.blit(timeSC, (2, 2))

        #  -----------------------------------------------------------------

        # DrawBg()    #blue background


        exirbar_sprite.update(dt)
        exirbar_sprite.draw(screen)

        # get the favorite index
        Chkresself.getindex(2)
        ChkresEn.getindex((3))

        Chkresself_sprite.draw(screen)
        ChkresEn_sprite.draw(screen)

        # all_sprites.draw(screen)
        drawTower()  # The Error was ignored
        loadtowerimage()

        # drawTower()
        # --------------------------------------------------------------------

        #  Draw Health Bar
        DHB_left.setHB(400)
        DHB_Right.setHB(500)
        DHB_Main.setHB(600)

        DHB_left_En.setHB(700)
        DHB_Right_En.setHB(300)
        DHB_Main_En.setHB(100)

        # --------------------------------------------------------------------
        #  prince
        if exirbar.getindex() >= 3:
            dAd_prince.control = True
        else:
            dAd_prince.control = False

        if dAd_prince.createimg:  # چک میکنه میبینه اگر موس فشرده شده بود اسپرایت پرینس رو ایجاد میکنه
            up_prince.update(dt, dAd_prince.getposition)
            up_prince.draw(screen)

        if exirbar.getindex() >= 3:
            if dAd_prince.counter == 2:
                exirbar.setindex(exirbar.getindex() - 3)
                dAd_prince.checker = False

        dAd_prince.move()  # enable to move troops

        # --------------------------------------------------------------------
        #  giant
        if exirbar.getindex() >= 5:
            dAd_giant.control = True
        else:
            dAd_giant.control = False

        if dAd_giant.createimg:
            up_giant.update(dt, dAd_giant.getposition)
            up_giant.draw(screen)

        if exirbar.getindex() >= 5:
            if dAd_giant.counter == 2:
                exirbar.setindex(exirbar.getindex() - 5)
                dAd_giant.checker = False

        dAd_giant.move()

        # --------------------------------------------------------------------
        #  pekka
        if exirbar.getindex() >= 3:
            dad_PEKKA.control = True
        else:
            dad_PEKKA.control = False

        if dad_PEKKA.createimg:
            up_pekka.update(dt, dad_PEKKA.getposition)
            up_pekka.draw(screen)

        if exirbar.getindex() >= 3:
            if dad_PEKKA.counter == 2:
                exirbar.setindex(exirbar.getindex() - 3)
                dad_PEKKA.checker = False

        dad_PEKKA.move()

        # --------------------------------------------------------------------

        if exirbar.getindex() >= 3:
            dad_knight.control = True
        else:
            dad_knight.control = False

        if dad_knight.createimg:
            up_knight.update(dt, dad_knight.getposition)
            up_knight.draw(screen)

        if exirbar.getindex() >= 3:
            if dad_knight.counter == 2:
                exirbar.setindex(exirbar.getindex() - 3)
                dad_knight.checker = False

        dad_knight.move()

        # --------------------------------------------------------------------


        up_cannon_sp_main_self.update(dt)
        up_cannon_sp_main_self.draw(screen)


        up_cannon_sp_left_self.update(dt)
        up_cannon_sp_left_self.draw(screen)


        up_cannon_sp_right_self.update(dt)
        up_cannon_sp_right_self.draw(screen)

        cannon_sp_right_self.x = 50
        cannon_sp_right_self.y = 300

        cannon_sp_main_self.x = 50
        cannon_sp_main_self.y = 300

        cannon_sp_left_self.x = 50
        cannon_sp_left_self.y = 300

        pygame.draw.rect(screen, (255, 255, 255), (50, 300, 40, 50))
        print(cannon_sp_main_self.degree)
        print(cannon_sp_left_self.degree)

        pygame.display.update()


if __name__ == '__main__':
    main()
