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
    knight_ui = pygame.transform.scale(knight_ui, (73, 93))
    mini_PEKKA = pygame.image.load("Assets\\EXir\\mini_PEKKA.png")
    mini_PEKKA = pygame.transform.scale(mini_PEKKA, (73, 93))
    hog_rider = pygame.image.load("Assets\\EXir\\hog_rider.png")
    hog_rider = pygame.transform.scale(hog_rider, (73, 93))
    screen.blit(UITab, (155, 600))
    screen.blit(pri_ui, (182, 610))
    screen.blit(giant_ui, (257, 610))
    screen.blit(mini_PEKKA, (332, 610))
<<<<<<< HEAD
    screen.blit(hog_rider, (406, 610))


Units_list = [[], []]

=======
    screen.blit(hog_rider , (406, 610))
Units_Animations_list=[[], []]
<<<<<<< HEAD
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
=======
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9

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

<<<<<<< HEAD
<<<<<<< HEAD
    def place_in_deck(self):
        self.deploy_state = 'inDeck'

    def deploy(self):
        self.life_state = 'Aliv   e'
        self.deploy_state = 'Deployed'

    def get_damage(self, value):
        self.hp = self.hitpoint
        self.hp -= value
        if self.hp == 0:
            self.kill()

    def re_assign_hp(self):
        self.hp = self.hitpoint

    def kill(self):
        self.life_state = 'Dead'
        self.deploy_state = 'notinDeck'
        self.re_assign_hp()

    def wethertomove(self):
        global Units_list
        self.wethertomove_counter = True
        if self.target_type == 'Any':
            if self.side == 'Down':
                for i in Units_list[0]:
                    if (abs(self.Animation.rect.center[0] - i.rect.center[0]) ** 2 + abs(
                                self.Animation.rect.center[1] - i.rect.center[1]) ** 2) ** 0.5 <= self.range:
                        self.wethertomove_counter = False
            if self.side == 'Up':
                for i in Units_list[1]:
                    if (abs(self.Animation.rect.center[0] - i.rect.center[0]) ** 2 + abs(
                                self.Animation.rect.center[1] - i.rect.center[1]) ** 2) ** 0.5 <= self.range:
                        self.wethertomove_counter = False
=======
    def wethertomove(self):
=======
    def wethertomove(self):
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
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
<<<<<<< HEAD
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
=======
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
        return self.wethertomove_counter

    def move(self):
        # Hit
        dt = 0.03
        self.HitGroup.update(dt)
<<<<<<< HEAD
<<<<<<< HEAD
        # waghti ke rah miran
        if self.wethertomove() == True:
            dt = 0.03
            self.Group.update(dt)
            if self.wetheranimate_counter == True:
                self.Group.draw(screen)
            if self.side == 'Down':
                if 0 <= self.x <= 225:
                    if self.Animation.rect.center != (130, 282) and self.leftmovecounter != 1:
                        self.xmovefactor = 130 - self.Animation.rect.center[0]
                        self.ymovefactor = 282 - self.Animation.rect.center[1]
                        if self.ymovefactor != 0:
                            self.Angle = math.atan2(self.ymovefactor, self.xmovefactor)
                            self.dx = math.cos(self.Angle) * 2
                            self.dy = math.sin(self.Angle) * 2
                            # should consider wether princess tower is destroyed or not
                            self.Animation.rect.move_ip(self.dx, self.dy)
                            self.HitAnimation.rect.move_ip(self.dx, self.dy)
                    else:
                        if self.Animation.rect.center != (130, 402):
                            self.xmovefactor = 130 - self.Animation.rect.center[0]
                            self.ymovefactor = 402 - self.Animation.rect.center[1]
                            if self.ymovefactor != 0:
                                self.Angle = math.atan2(self.ymovefactor, self.xmovefactor)
                                self.dx = math.cos(self.Angle) * 1.5
                                self.dy = math.sin(self.Angle) * 1.5
                                # should consider wether princess tower is destroyed or not
                                self.Animation.rect.move_ip(self.dx, self.dy)
                                self.HitAnimation.rect.move_ip(self.dx, self.dy)
                                self.leftmovecounter = 1
                                # self.Group.
                elif 225 < self.x <= 500:
                    if self.Animation.rect.center != (408, 282) and self.rightmovecounter != 1:
                        self.xmovefactor = abs(408 - self.Animation.rect.center[0])
                        self.ymovefactor = abs(282 - self.Animation.rect.center[1])
                        if self.ymovefactor != 0:
                            self.Angle = math.atan2(self.ymovefactor, self.xmovefactor)
                            self.dx = math.cos(self.Angle) * 2
                            self.dy = math.sin(self.Angle) * 2
                            # should consider wether princess tower is destroyed or not
                            self.Animation.rect.move_ip(self.dx, self.dy)
                            self.HitAnimation.rect.move_ip(self.dx, self.dy)
                    else:
                        if self.Animation.rect.center != (408, 402):
                            self.xmovefactor = 408 - self.Animation.rect.center[0]
                            self.ymovefactor = 402 - self.Animation.rect.center[1]
                            if self.ymovefactor != 0:
                                self.Angle = math.atan2(self.ymovefactor, self.xmovefactor)
                                self.dx = math.cos(self.Angle) * 1.5
                                self.dy = math.sin(self.Angle) * 1.5
                                # should consider wether princess tower is destroyed or not
                                self.Animation.rect.move_ip(self.dx, self.dy)
                                self.HitAnimation.rect.move_ip(self.dx, self.dy)
                                self.rightmovecounter = 1
            elif self.side == 'Up':
                if 0 <= self.x <= 225:
                    if self.Animation.rect.center != (130, 340) and self.leftmovecounter != 1:
                        self.xmovefactor = 130 - self.Animation.rect.center[0]
                        self.ymovefactor = 340 - self.Animation.rect.center[1]
                        if self.ymovefactor != 0:
                            self.Angle = math.atan2(self.ymovefactor, self.xmovefactor)
                            self.dx = math.cos(self.Angle) * 2
                            self.dy = math.sin(self.Angle) * 2
                            # should consider wether princess tower is destroyed or not
                            self.Animation.rect.move_ip(self.dx, self.dy)
                            self.HitAnimation.rect.move_ip(self.dx, self.dy)
                    else:
                        if self.Animation.rect.center != (130, 210):
                            self.xmovefactor = 130 - self.Animation.rect.center[0]
                            self.ymovefactor = 210 - self.Animation.rect.center[1]
                            if self.ymovefactor != 0:
                                self.Angle = math.atan2(self.ymovefactor, self.xmovefactor)
                                self.dx = math.cos(self.Angle) * 1.5
                                self.dy = math.sin(self.Angle) * 1.5
                                # should consider wether princess tower is destroyed or not
                                self.Animation.rect.move_ip(self.dx, self.dy)
                                self.HitAnimation.rect.move_ip(self.dx, self.dy)
                                self.leftmovecounter = 1
                elif 225 < self.x <= 500:
                    if self.Animation.rect.center != (408, 340) and self.rightmovecounter != 1:
                        self.xmovefactor = abs(408 - self.Animation.rect.center[0])
                        self.ymovefactor = -abs(340 - self.Animation.rect.center[1])
                        if self.ymovefactor != 0:
                            self.Angle = math.atan2(self.ymovefactor, self.xmovefactor)
                            self.dx = math.cos(self.Angle) * 2
                            self.dy = math.sin(self.Angle) * 2
                            # should consider wether princess tower is destroyed or not
                            self.Animation.rect.move_ip(self.dx, self.dy)
                            self.HitAnimation.rect.move_ip(self.dx, self.dy)
                    else:
                        if self.Animation.rect.center != (408, 210):
                            self.xmovefactor = 408 - self.Animation.rect.center[0]
                            self.ymovefactor = 210 - self.Animation.rect.center[1]
                            if self.ymovefactor != 0:
                                self.Angle = math.atan2(self.ymovefactor, self.xmovefactor)
                                self.dx = math.cos(self.Angle) * 1.5
                                self.dy = math.sin(self.Angle) * 1.5
                                # should consider wether princess tower is destroyed or not
                                self.Animation.rect.move_ip(self.dx, self.dy)
                                self.HitAnimation.rect.move_ip(self.dx, self.dy)
                                self.rightmovecounter = 1
        # hit
        # waghti ba ye sarbaze dige dargir mishan
        else:
            self.HitGroup.draw(screen)
        # waghti be tower miresan
        if self.side == 'Down':
            # towere payin chap
            if 0 <= self.x <= 225:
                if self.Animation.rect.center == (130, 402):
                    self.wetheranimate_counter = False
                    self.HitGroup.draw(screen)
            # towere payin rast
            else:
                if self.Animation.rect.center == (408, 402):
                    self.wetheranimate_counter = False
                    self.HitGroup.draw(screen)
        else:
            # towere bala chap
            if 0 <= self.x <= 225:
                if self.Animation.rect.center == (130, 210):
                    self.wetheranimate_counter = False
                    self.HitGroup.draw(screen)
            # towere bala rast
            else:
                if self.Animation.rect.center == (408, 210):
                    self.wetheranimate_counter = False
                    self.HitGroup.draw(screen)


class Dragon(Units):
    def attr(self):
        self.movement_type = 'Fly'
        self.shoot_type = 'Both'
        self.target_type = 'Any'
        self.rarity_type = 'Rare'
        self.movement_speed = ['Normal']
        self.elixir_cost = 4
        self.hitpoint = 600
        self.damage = 100
        self.count = 1
        self.attack_type = 'Ranged'

=======
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
=======
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
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
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
<<<<<<< HEAD
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
=======
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9

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
<<<<<<< HEAD
<<<<<<< HEAD

        self.range = 30
        self.shoot_type = 'Ground'
        self.target_type = 'Building'
=======
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
=======
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
        self.elixir_cost = 4
        self.target_type = 'Building'


<<<<<<< HEAD
        # load image
        self.x = x
        self.y = y
        self.Goimages = []
        self.Hitimages = []
        self.wetheranimate_counter = True
        if self.side == 'Down':
            for i in range(1, 17):
                self.img = pygame.image.load("Assets\\chr_giant_out\\%s_%s.png" % (i, self.side))
                self.img = pygame.transform.scale(self.img, (90, 90))
                self.Goimages.append(self.img)
            for i in range(1, 11):
                self.img2 = pygame.image.load("Assets\\chr_giant_out\\%s_Hit_%s.png" % (i, self.side))
                self.img2 = pygame.transform.scale(self.img2, (90, 90))
                self.Hitimages.append(self.img2)
        if self.side == 'Up':
            for i in range(1, 17):
                self.img = pygame.image.load("Assets\\chr_giant_out\\%s_%s.png" % (i, self.side))
                self.img = pygame.transform.scale(self.img, (90, 90))
                self.Goimages.append(self.img)
            for i in range(1, 11):
                self.img2 = pygame.image.load("Assets\\chr_giant_out\\%s_Hit_%s.png" % (i, self.side))
                self.img2 = pygame.transform.scale(self.img2, (90, 90))
                self.Hitimages.append(self.img2)
        self.Animation = AnimatedSprite((self.x, self.y), self.Goimages)
        self.HitAnimation = AnimatedSprite((self.Animation.rect.center[0] - 50, self.Animation.rect.center[1] - 80),
                                           self.Hitimages)
        self.HitGroup = pygame.sprite.Group(self.HitAnimation)

        self.Group = pygame.sprite.Group(self.Animation)
<<<<<<< HEAD
        if self.side == 'Down':
            Units_list[1].append(self.Animation)
        if self.side == 'Up':
            Units_list[0].append(self.Animation)


class Prince(Units):
    def __init__(self, x, y, side):
        global Units_list
        # needed for all troops classes
        # attributes
=======
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


=======
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
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
<<<<<<< HEAD
=======
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
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
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
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
        self.side = side
        # for movement
        self.leftmovecounter = 0
        self.rightmovecounter = 0
<<<<<<< HEAD
<<<<<<< HEAD
        #
        self.range = 30
=======
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
        self.target_type = 'Any'
        self.elixir_cost = 3
        # load image
        self.x = x
        self.y = y
        self.Goimages = []
        self.Hitimages = []

        self.wetheranimate_counter = True
        if self.side == 'Down':
            for i in range(1, 11):
                self.img = pygame.image.load("Assets\\chr_prince_out\\%s_%s.png" % (i, self.side))
                self.img = pygame.transform.scale(self.img, (90, 90))
                self.Goimages.append(self.img)
                self.img2 = pygame.image.load("Assets\\chr_prince_out\\%s_Hit.png" % (i))
                self.img2 = pygame.transform.scale(self.img2, (90, 90))
                self.Hitimages.append(self.img2)
        if self.side == 'Up':
            for i in range(1, 11):
                self.img = pygame.image.load("Assets\\chr_prince_out\\%s_%s.png" % (i, self.side))
                self.img = pygame.transform.scale(self.img, (90, 90))
                self.Goimages.append(self.img)
                self.img2 = pygame.image.load("Assets\\chr_prince_out\\%s_Hit_%s.png" % (i, self.side))
                self.img2 = pygame.transform.scale(self.img2, (90, 90))
                self.Hitimages.append(self.img2)
        self.Animation = AnimatedSprite((self.x, self.y), self.Goimages)
        self.HitAnimation = AnimatedSprite((self.Animation.rect.center[0] - 40, self.Animation.rect.center[1] - 80),
                                           self.Hitimages)
        self.HitGroup = pygame.sprite.Group(self.HitAnimation)

        self.Group = pygame.sprite.Group(self.Animation)

<<<<<<< HEAD
        if self.side == 'Down':
            Units_list[1].append(self.Animation)
        if self.side == 'Up':
            Units_list[0].append(self.Animation)


=======
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
=======
        self.target_type = 'Any'
        self.elixir_cost = 3
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
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
<<<<<<< HEAD
=======
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
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
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
<<<<<<< HEAD
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
=======
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
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
    self_tower = pygame.transform.scale(self_tower, (100, 118))
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
    def __init__(self, ELH, Sc, x, y):
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
<<<<<<< HEAD
<<<<<<< HEAD
    P = Prince(210, 100, 'Down')
    G = Giant(235, 120, 'Down')
    S = Giant(215, 320, 'Up')
    F = Prince(230, 350, 'Up')
    # Draw Health Bar
    DHB_left = Healthbar(ELH=1000, Sc=17.5, x=87, y=440)
    DHB_Right = Healthbar(ELH=1000, Sc=17.5, x=355, y=441)
    DHB_Main = Healthbar(ELH=2000, Sc=35, x=223, y=501)
    DHB_left_En = Healthbar(ELH=1000, Sc=17.5, x=87, y=70)
    DHB_Right_En = Healthbar(ELH=1000, Sc=17.5, x=356, y=70)
    DHB_Main_En = Healthbar(ELH=1000, Sc=17.5, x=223, y=0)
=======
=======
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
    P=Minipekka(210,100,'Down')
    G=Giant(235,120,'Down')
    S=Hogrider(215,320,'Up')
    F=Minipekka(230,350,'Up')
    #Draw Health Bar
    DHB_left = Healthbar(ELH= 1000, Sc= 17.5, x= 87, y= 440)
    DHB_Right = Healthbar(ELH= 1000, Sc= 17.5, x= 355, y= 441)
    DHB_Main = Healthbar(ELH= 2000, Sc= 35, x= 223, y= 501)
    DHB_left_En = Healthbar(ELH= 1000, Sc= 17.5, x= 87, y= 70)
    DHB_Right_En = Healthbar(ELH= 1000, Sc= 17.5, x= 356, y= 70)
    DHB_Main_En = Healthbar(ELH= 1000, Sc= 17.5, x= 223, y= 0)
>>>>>>> 8bb8e1e6bbd96ee22e7747391b86155d1f29b2d9
    running = True
    drawUI()
    temper = pygame.image.load("Assets\\Map\\map.png")
    temper = pygame.transform.scale(temper, (500, 600))
    # draw result of game in instant
    load_image_self = loadimageself()
    load_image_En = loadimageEn()
    Chkresself = Checkwin((430, 320), load_image_self)
    Chkresself_sprite = pygame.sprite.Group(Chkresself)
    ChkresEn = Checkwin((430, 220), load_image_En)
    ChkresEn_sprite = pygame.sprite.Group(ChkresEn)
    # create a glow gif when a exir bar is complete

    # draw exir bar
    exirbar = Exirbar(position=(170, 690))
    exirbar_sprite = pygame.sprite.Group(exirbar)
    C_pr = True

    timeSC = pygame.image.load('Assets\\EXir\\ui_sprite_476.png')
    timeSC = pygame.transform.scale(timeSC, (55, 25))

    while running:
        dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop.
        # pygame.draw.rect(screen, (255, 255, 255), (0, 0, 480, 480))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.USEREVENT and counter != 0:
                counter -= 1
                text = str(counter).rjust(3)

        if C_pr == True:
            if exirbar.getindex() >= 5:
                exirbar.setindex(exirbar.getindex() - 4)
                C_pr = False

        screen.blit(temper, (0, 0))

        exirbar_sprite.update(dt)
        exirbar_sprite.draw(screen)

        # get the favorite index
        Chkresself.getindex(2)
        ChkresEn.getindex((3))

        Chkresself_sprite.draw(screen)
        ChkresEn_sprite.draw(screen)

        # all_sprites.draw(screen)
        drawTowerUp()  # The Error was ignored

        screen.blit(font.render(text, True, (0, 0, 0)), (12, 6))
        screen.blit(timeSC, (2, 2))

        # Draw Health Bar
        DHB_left.setHB(400)
        DHB_Right.setHB(500)
        DHB_Main.setHB(600)

        DHB_left_En.setHB(700)
        DHB_Right_En.setHB(300)
        DHB_Main_En.setHB(100)
        '''
        PRINCE
        '''

        # movement
        P.move()
        G.move()
        S.move()
        F.move()
        # ---

        drawTowerDown()

        pygame.display.update()


if __name__ == '__main__':
    main()
