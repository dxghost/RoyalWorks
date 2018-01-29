import math
import pygame


def load_images(x):
    """
    Loads all images in directory. The directory must only contain images.

    Args:
        path: The relative or absolute path to the directory to load images from.

    Returns:
        List of images.
    """
    images = []
    images.append(pygame.image.load("Assets\\Towers\\0_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\1_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\2_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\3_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\4_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\5_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\6_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\7_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\8_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\9_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\10_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\11_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\12_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\13_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\14_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\15_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\16_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\17_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\18_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\20_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\21_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\22_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\23_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\24_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\25_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\26_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\27_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\28_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\29_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\30_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\31_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\32_cannon.png"))
    images.append(pygame.image.load("Assets\\Towers\\33_cannon.png"))


    main_images = [pygame.transform.scale(image, (x, x)) for image in images]

    return main_images


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, position, images, scale, enemy):
        """
        Animated sprite object.

        Args:
            position: x, y coordinate on the screen to place the AnimatedSprite.
            images: Images to use in the animation.
        """
        super(AnimatedSprite, self).__init__()

        size = (130, 130)  # This should match the size of the images.
        self.position = position
        self.rect = pygame.Rect(position, size)
        self.images = images
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the animation.

        self.scale = scale

        self.animation_time = 0.01
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0

        self.corner_X = 0
        self.corner_Y = 0

        self.enemy = enemy

        self.l_x = 0
        self.l_y = 0
        self.count = 0
        self.degree = 0

        self.x = 0
        self.y = 0

        self.x_1 = 0
        self.y_1 = 0

    def update_frame_dependent(self):
        """
        Updates the image of Sprite approximately every 0.1 second.

        Args:
            dt: Time elapsed between each frame.
        """

        if self.scale == 130:
            self.x_1 = 73
            self.y_1 = 82
        if self.scale == 100:
            self.x_1 = 60
            self.y_1 = 60

        self.corner_X = self.position[0] + self.x_1
        self.corner_Y = self.position[1] + self.y_1

        self.l_x = abs(self.corner_X - self.x)
        self.l_y = abs(self.corner_Y - self.y)

        self.degree = abs(int(math.degrees(math.atan2(self.l_y, self.l_x))))

        if not self.enemy:
            if self.x < self.corner_X and self.y < self.corner_Y:

                self.degree = 90 - self.degree

                if self.degree == 90:
                    self.count = 25
                if 90 > self.degree >= 84:
                    self.count = 26

                if 84 > self.degree >= 72:
                    self.count = 27

                if 72 > self.degree >= 60:
                    self.count = 28

                if self.degree == 45:
                    self.count = 29

                if 60 > self.degree >= 48:
                    self.count = 29

                if 48 > self.degree >= 36:
                    self.count = 30

                if 36 > self.degree >= 24:
                    self.count = 31

                if 24 > self.degree >= 12:
                    self.count = 32

                if 12 > self.degree > 0:
                    self.count = 32

                if self.degree == 0:
                    self.count = 0

            if self.x > self.corner_X and self.y < self.corner_Y:

                self.degree = self.degree

                if self.degree == 90:
                    self.count = 0

                if 90 > self.degree >= 84:
                    self.count = 1

                if 84 > self.degree >= 72:
                    self.count = 2

                if 72 > self.degree >= 60:
                    self.count = 3

                if self.degree == 45:
                    self.count = 4

                if 60 > self.degree >= 48:
                    self.count = 4

                if 48 > self.degree >= 36:
                    self.count = 5

                if 36 > self.degree >= 24:
                    self.count = 6

                if 24 > self.degree >= 12:
                    self.count = 7

                if 12 > self.degree > 0:
                    self.count = 8

                if self.degree == 0:
                    self.count = 9

        if self.enemy:

            if self.x < self.corner_X and self.y > self.corner_Y:

                self.degree = 90 - self.degree

                if self.degree == 90:
                    self.count = 25

                if 90 > self.degree >= 84:
                    self.count = 24

                if 84 > self.degree >= 72:
                    self.count = 23

                if 72 > self.degree >= 60:
                    self.count = 22

                if self.degree == 45:
                    self.count = 21

                if 60 > self.degree >= 48:
                    self.count = 21

                if 48 > self.degree >= 36:
                    self.count = 20

                if 36 > self.degree >= 24:
                    self.count = 19

                if 24 > self.degree >= 12:
                    self.count = 18

                if 12 > self.degree > 0:
                    self.count = 17

                if self.degree == 0:
                    self.count = 17

            if self.x > self.corner_X and self.y > self.corner_Y:

                self.degree = self.degree

                if self.degree == 90:
                    self.count = 17

                if 90 > self.degree >= 84:
                    self.count = 16

                if 84 > self.degree >= 72:
                    self.count = 15

                if 72 > self.degree >= 60:
                    self.count = 14

                if self.degree == 45:
                    self.count = 14

                if 60 > self.degree >= 48:
                    self.count = 13

                if 48 > self.degree >= 36:
                    self.count = 12

                if 36 > self.degree >= 24:
                    self.count = 11

                if 24 > self.degree >= 12:
                    self.count = 10

                if 12 > self.degree > 0:
                    self.count = 9

                if self.degree == 0:
                    self.count = 9


        self.index = self.count
        self.image = self.images[self.index]

    def update(self, dt):
        self.update_frame_dependent()
