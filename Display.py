
import os
import pygame
import sys, random, math
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME


pygame.init()

SIZE = WIDTH, HEIGHT = 500, 750
FPS = 60

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

pygame.display.set_caption('Clash Royale !')

previousMousePosition = [0,0]
mousePoisiton = None
mouseDown = False

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




UICoordinates = [{"name" : "pri_ui", "coordinates" : (182,610)},
                 {"name" : "giant_ui", "coordinates" : (257, 610)},
                 {"name" : "goblins_ui", "coordinates" : (0, 0)},
                 {"name" : "skeletons_ui", "coordinates" : (0, 0)},
                 {"name" : "knight_ui", "coordinates" : (0,0)},
                 {"name" : "mini_PEKKA", "coordinates" : (332, 610)},
                 {"name" : "hog_rider", "coordinates" : (406, 610)}]

Troops_img = {
    "pri_ui" : pri_ui,
    'giant_ui' : giant_ui,
    'goblins_ui' : goblins_ui,
    'skeletons_ui' : skeletons_ui,
    'knight_ui' : knight_ui,
    'mini_PEKKA' : mini_PEKKA,
    'hog_rider' : hog_rider

}


Troops = [{
	"name" : "pri_ui",
	"velocity" : [0,0],
	"position" : [0,0]
},
{
    "name": "giant_ui",
    "velocity": [0, 0],
    "position": [0, 0]
},
{
    "name": "goblins_ui",
    "velocity": [0, 0],
    "position": [0, 0]
},
{
    "name": "skeletons_ui",
    "velocity": [0, 0],
    "position": [0, 0]
},
{
    "name": "knight_ui",
    "velocity": [0, 0],
    "position": [0, 0]
},
{
    "name": "mini_PEKKA",
    "velocity": [0, 0],
    "position": [0, 0]
},
{
    "name": "hog_rider",
    "velocity": [0, 0],
    "position": [0, 0]
}]
currentTroop = []
celesticalBodeis = []

def drawUI():
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
def load_images():
    """
    Loads all images in directory. The directory must only contain images.

    Args:
        path: The relative or absolute path to the directory to load images from.

    Returns:
        List of images.
    """
    images = []
    temper = pygame.image.load("Assets\\Map\\map.png")
    temper = pygame.transform.scale(temper, (500, 600))
    images.append(temper)

    return images



class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, position, images):
        """
        Animated sprite object.

        Args:
            position: x, y coordinate on the screen to place the AnimatedSprite.
            images: Images to use in the animation.
        """
        super(AnimatedSprite, self).__init__()

        size = (936, 1200)  # This should match the size of the images.

        self.rect = pygame.Rect(position, size)
        self.images = images
        self.images_right = images
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the animation.



def main():
    drawTower()
    images = load_images()  # Make sure to provide the relative or full path to the images directory.
    player = AnimatedSprite(position=(0, 0), images=images)
    all_sprites = pygame.sprite.Group(player)  # Creates a sprite group and adds 'player' to it.
    running = True
    drawUI()

    while running:

        dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop.
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 480, 480))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        all_sprites.update(dt)  # Calls the 'update' method on all sprites in the list (currently just the player).

        all_sprites.draw(screen)
        drawTower() #The Error was ignored
        pygame.display.update()


if __name__ == '__main__':
    main()

