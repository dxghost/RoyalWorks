import os
import pygame
import sys, random, math
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import time
import chr_giant_out as Giant
import chr_mini_PEKKA_out as PEKKA
import chr_knight_out as KNIGHT
import cannon
import bullet as BULLET

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


def loadimgprince():
    images = []
    a = pygame.image.load("Assets\\chr_prince_out\\1_Down.png")
    a = pygame.transform.scale(a, (90, 90))
    images.append(a)
    a = pygame.image.load("Assets\\chr_prince_out\\2_Down.png")
    a = pygame.transform.scale(a, (90, 90))
    images.append(a)
    a = pygame.image.load("Assets\\chr_prince_out\\3_Down.png")
    a = pygame.transform.scale(a, (90, 90))
    images.append(a)
    a = pygame.image.load("Assets\\chr_prince_out\\4_Down.png")
    a = pygame.transform.scale(a, (90, 90))
    images.append(a)
    a = pygame.image.load("Assets\\chr_prince_out\\5_Down.png")
    a = pygame.transform.scale(a, (90, 90))
    images.append(a)
    a = pygame.image.load("Assets\\chr_prince_out\\6_Down.png")
    a = pygame.transform.scale(a, (90, 90))
    images.append(a)
    a = pygame.image.load("Assets\\chr_prince_out\\7_Down.png")
    a = pygame.transform.scale(a, (90, 90))
    images.append(a)
    a = pygame.image.load("Assets\\chr_prince_out\\8_Down.png")
    a = pygame.transform.scale(a, (90, 90))
    images.append(a)
    a = pygame.image.load("Assets\\chr_prince_out\\9_Down.png")
    a = pygame.transform.scale(a, (90, 90))
    images.append(a)
    a = pygame.image.load("Assets\\chr_prince_out\\10_Down.png")
    a = pygame.transform.scale(a, (90, 90))
    images.append(a)

    return images


def drawTower():
    self_tower = pygame.image.load("Assets\\Towers\\Self_town_main.png")
    self_tower = pygame.transform.scale(self_tower, (100, 118))
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

    def update(self, dt, position):
        size = (96, 144)
        self.rect = pygame.Rect(position, size)
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

    def getindex(self):
        return self.index

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
    screen.blit(cannon_scaled_left, (39, 78))
    screen.blit(cannon_scaled_right, (307, 78))



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

    UITab = pygame.image.load("Assets\\EXir\\UITab.png")

    # create counter for end the game :)
    counter = 180
    text = '180'.rjust(2)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consloas', 30)

    # --------------------------------------------------------------------

    # create object
    a = loadimgprince()
    prince = AnimatedSprite(dAd_prince.getposition, a)
    up_prince = pygame.sprite.Group(prince)

    giant = Giant.AnimatedSprite(dAd_giant.getposition, Giant.load_images())
    up_giant = pygame.sprite.Group(giant)

    pekka = PEKKA.AnimatedSprite(dad_PEKKA.getposition, PEKKA.load_images())
    up_pekka = pygame.sprite.Group(pekka)

    knight = KNIGHT.AnimatedSprite(dad_knight.getposition, KNIGHT.load_images())
    up_knight = pygame.sprite.Group(knight)

    cannon_sp_main_self = cannon.AnimatedSprite((173, 385), cannon.load_images(130), 130, False)
    up_cannon_sp_main_self = pygame.sprite.Group(cannon_sp_main_self)

    cannon_sp_left_self = cannon.AnimatedSprite((55, 349), cannon.load_images(100), 100, False)
    up_cannon_sp_left_self = pygame.sprite.Group(cannon_sp_left_self)

    cannon_sp_right_self = cannon.AnimatedSprite((320, 349), cannon.load_images(100), 100, False)
    up_cannon_sp_right_self = pygame.sprite.Group(cannon_sp_right_self)

    cannon_sp_main_enemy = cannon.AnimatedSprite((173, -32), cannon.load_images(130), 130, True)
    up_cannon_sp_main_enemy = pygame.sprite.Group(cannon_sp_main_enemy)

    cannon_sp_left_enemy = cannon.AnimatedSprite((55, 35), cannon.load_images(100), 100, True)
    up_cannon_sp_left_enemy = pygame.sprite.Group(cannon_sp_left_enemy)

    cannon_sp_right_enemy = cannon.AnimatedSprite((318, 35), cannon.load_images(100), 100, True)
    up_cannon_sp_right_enemy = pygame.sprite.Group(cannon_sp_right_enemy)

    # --------------------------------------------------------------------

    bullet_right = BULLET.Bullet((380, 409))
    bullet_left = BULLET.Bullet((115, 409))
    bullet_main = BULLET.Bullet((246, 467))

    bullet_left_enemy = BULLET.Bullet((112, 87))
    bullet_main_enemy = BULLET.Bullet((255, 40))
    bullet_right_enemy = BULLET.Bullet((380, 92))




    # --------------------------------------------------------------------

    # Draw Health Bar
    DHB_left = Helathbar(ELH=1000, Sc=17.5, x=87, y=440)
    DHB_Right = Helathbar(ELH=1000, Sc=17.5, x=355, y=441)
    DHB_Main = Helathbar(ELH=2000, Sc=35, x=223, y=501)
    DHB_left_En = Helathbar(ELH=1000, Sc=17.5, x=87, y=70)
    DHB_Right_En = Helathbar(ELH=1000, Sc=17.5, x=356, y=70)
    DHB_Main_En = Helathbar(ELH=1000, Sc=17.5, x=223, y=0)

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

    z = 50

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

        bullet_right.movebullet(z, 300)
        bullet_left.movebullet(z, 300)
        bullet_main.movebullet(z, 300)

        bullet_right_enemy.movebulletenemy(z, 300)
        bullet_left_enemy.movebulletenemy(z, 300)
        bullet_main_enemy.movebulletenemy(z, 300)

        up_cannon_sp_main_self.update(dt)
        up_cannon_sp_main_self.draw(screen)

        up_cannon_sp_left_self.update(dt)
        up_cannon_sp_left_self.draw(screen)

        up_cannon_sp_right_self.update(dt)
        up_cannon_sp_right_self.draw(screen)

        up_cannon_sp_main_enemy.update(dt)
        up_cannon_sp_main_enemy.draw(screen)

        up_cannon_sp_left_enemy.update(dt)
        up_cannon_sp_left_enemy.draw(screen)

        up_cannon_sp_right_enemy.update(dt)
        up_cannon_sp_right_enemy.draw(screen)


        cannon_sp_right_self.x = z
        cannon_sp_right_self.y = 300

        cannon_sp_main_self.x = z
        cannon_sp_main_self.y = 300

        cannon_sp_left_self.x = z
        cannon_sp_left_self.y = 300

        #

        cannon_sp_right_enemy.x = z
        cannon_sp_right_enemy.y = 300

        cannon_sp_main_enemy.x = z
        cannon_sp_main_enemy.y = 300

        cannon_sp_left_enemy.x = z
        cannon_sp_left_enemy.y = 300

        pygame.draw.rect(screen, (255, 255, 255), (246, 467, 5, 5))
        pygame.draw.rect(screen, (255, 0  , 255), (115, 409, 5, 5))
        pygame.draw.rect(screen, (255, 255, 255), (380, 409, 5, 5))

        pygame.draw.rect(screen, (255, 255, 255), (z, 300, 20, 20))

        z += 1
        pygame.display.update()


if __name__ == '__main__':
    main()
