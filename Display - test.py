
import os
import pygame
import sys, random, math
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import time

pygame.init()

SIZE = WIDTH, HEIGHT = 500, 750
FPS = 60

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

pygame.display.set_caption('Clash Royale !')



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
class Units(pygame.sprite.Sprite):
    '''
    def __init__(self):
        self.movement_types=['Fly','Walk']
        self.movement_type='X'
        self.shoot_types=['Air','Ground','Both']
        self.shoot_type='X'
        self.target_types=['Building','Any']
        self.target_type=  'X'
        self.rarity_types = ['Common','Rare','Epic','Legendary']
        self.rarity_type = 'X'
        self.movement_speeds = ['Slow','Normal','Fast']
        self.movement_speed = 'X'
        self.elixir_costs = [1,2,3,4,5,6,7,8,9,10]
        self.elixir_cost = 'X'
        self.counts = [i for i in range(1,15)]
        self.count = 'X'
        self.hitpoints = [i for i in range(10,3000)]
        self.hp='X'
        self.damages=[i for i in range(10,1000)]
        self.damage='X'
        self.life_states=['Dead','Alive']
        self.life_state='X'
        self.deploy_states=['Deployed','inDeck','notinDeck']
        self.deploy_state = 'notinDeck'
        self.attack_types = ['Melee','Ranged']
        self.attack_type = 'X'
    '''

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


class Goblin(Units):
    def __init__(self):
        # attributes
        self.movement_type = 'Walk'
        self.shoot_type = 'Ground'
        self.target_type = 'Any'
        self.rarity_type = 'Common'
        self.movement_speed = ['Fast']
        self.elixir_cost = 2
        self.hitpoint = 60
        self.damage = 50
        self.count = 3
        self.attack_type = 'Melee'


class Prince(Units):
    def __init__(self,x,y):
        # attributes
        self.movement_type = 'Walk'
        self.shoot_type = 'Ground'
        self.target_type = 'Any'
        self.rarity_type = 'Common'
        self.movement_speed = ['Fast']
        self.elixir_cost = 2
        self.hitpoint = 60
        self.damage = 50
        self.count = 3
        self.attack_type = 'Melee'
        # load image
        self.x=x
        self.y=y
        self.images = []
        self.img = pygame.image.load("Assets\\chr_prince_out\\1_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\2_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\3_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\4_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\5_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\6_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\7_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\8_Down.png")
        self.img.get_rect()
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\9_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\10_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.prince = AnimatedSprite((self.x, self.y), self.images)
        self.up_prince = pygame.sprite.Group(self.prince)
        self.prince = AnimatedSprite((self.x, self.y), self.images)
        self.up_prince = pygame.sprite.Group(self.prince)
    def show(self):
        self.prince = AnimatedSprite((self.x, self.y), self.images)
        self.up_prince = pygame.sprite.Group(self.prince)







def drawTower():
    self_tower = pygame.image.load("Assets\\Towers\\Self_town_main.png")
    self_tower = pygame.transform.scale(self_tower, (100,118))
    self_small_tower = pygame.image.load("Assets\\Towers\\Self_town - Copy.png")
    self_small_tower = pygame.transform.scale(self_small_tower, (70, 90))
    self_small_tower_2 = pygame.image.load("Assets\\Towers\\Self_town.png")
    self_small_tower_2 = pygame.transform.scale(self_small_tower_2, (70, 90))

    Enm_tower = pygame.image.load("Assets\\Towers\\Enm_town_main.png")
    Enm_tower = pygame.transform.scale(Enm_tower, (100, 115))
    Enm_small_tower = pygame.image.load("Assets\\Towers\\Enm_town - Copy.png")
    Enm_small_tower = pygame.transform.scale(Enm_small_tower, (70, 90))
    Enm_small_tower_2 = pygame.image.load("Assets\\Towers\\Enm_town.png")
    Enm_small_tower_2 = pygame.transform.scale(Enm_small_tower_2, (70, 90))

    screen.blit(self_tower, (200, 445))
    screen.blit(self_small_tower, (78, 395))
    screen.blit(self_small_tower_2, (347, 395))
    screen.blit(Enm_tower, (200, 1))
    screen.blit(Enm_small_tower, (78, 80))
    screen.blit(Enm_small_tower_2, (347, 80))




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



class Helathbar:
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






#just starting from scratch! )





def main():
    # create counter for end the game :)
    counter = 120
    text = '120'.rjust(2)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consloas', 30)

    DrawBg()
    drawTower()

    '''
    PRINCE'''
    P=Prince(200,100)


    #Draw Health Bar
    DHB_left = Helathbar(ELH= 1000,Sc= 17.5,x= 87,y= 440)
    DHB_Right = Helathbar(ELH= 1000,Sc= 17.5,x= 355,y= 441)
    DHB_Main = Helathbar(ELH= 2000,Sc= 35 ,x= 223,y= 501)
    DHB_left_En = Helathbar(ELH= 1000,Sc= 17.5,x= 87,y= 70)
    DHB_Right_En = Helathbar(ELH= 1000,Sc= 17.5,x= 356,y= 70)
    DHB_Main_En = Helathbar(ELH= 1000,Sc= 17.5,x= 223,y= 0)




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

        '''
        PRINCE
        P.show ro comment konid yebaram nakonid
        '''

        P.y+=1
        P.show()
        P.up_prince.update(dt)
        P.up_prince.draw(screen)


        #get the favorite index
        Chkresself.getindex(2)
        ChkresEn.getindex((3))

        Chkresself_sprite.draw(screen)
        ChkresEn_sprite.draw(screen)

        #all_sprites.draw(screen)
        drawTower() #The Error was ignored

        screen.blit(font.render(text, True, (0, 0, 0)), (12, 6))
        screen.blit(timeSC, (2, 2))


        #Draw Health Bar
        DHB_left.setHB(400)
        DHB_Right.setHB(500)
        DHB_Main.setHB(600)

        DHB_left_En.setHB(700)
        DHB_Right_En.setHB(300)
        DHB_Main_En.setHB(100)


        pygame.display.update()


if __name__ == '__main__':
    main()

