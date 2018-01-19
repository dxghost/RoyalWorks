
import os
import pygame
pygame.init()
screen = pygame.display.set_mode((700, 700))
background = pygame.draw.rect(screen, (0, 0, 0), (0, 0, 700, 700))

SIZE = WIDTH, HEIGHT = 720, 480
BACKGROUND_COLOR = pygame.Color('black')
FPS = 60

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


def load_images():
    """
    Loads all images in directory. The directory must only contain images.

    Args:
        path: The relative or absolute path to the directory to load images from.

    Returns:
        List of images.
    """
    images = []
    images.append(pygame.image.load("Assets\\chr_prince_out\\1_Down.png"))
    images.append(pygame.image.load("Assets\\chr_prince_out\\2_Down.png"))
    images.append(pygame.image.load("Assets\\chr_prince_out\\3_Down.png"))
    images.append(pygame.image.load("Assets\\chr_prince_out\\4_Down.png"))
    images.append(pygame.image.load("Assets\\chr_prince_out\\5_Down.png"))
    images.append(pygame.image.load("Assets\\chr_prince_out\\6_Down.png"))
    images.append(pygame.image.load("Assets\\chr_prince_out\\7_Down.png"))
    images.append(pygame.image.load("Assets\\chr_prince_out\\8_Down.png"))
    images.append(pygame.image.load("Assets\\chr_prince_out\\9_Down.png"))
    images.append(pygame.image.load("Assets\\chr_prince_out\\10_Down.png"))


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

        size = (96, 144)  # This should match the size of the images.

        self.rect = pygame.Rect(position, size)
        self.images = images
        self.images_right = images
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]  # Flipping every image.
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the animation.

        self.velocity = pygame.math.Vector2(0, 0)

        self.animation_time = 0.1
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0

    def update_time_dependent(self, dt):
        """
        Updates the image of Sprite approximately every 0.1 second.

        Args:
            dt: Time elapsed between each frame.
        """
        if self.velocity.x > 0:  # Use the right images if sprite is moving right.
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def update_frame_dependent(self):
        """
        Updates the image of Sprite every 6 frame (approximately every 0.1 second if frame rate is 60).
        """
        if self.velocity.x > 0:  # Use the right images if sprite is moving right.
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def update(self, dt):
        self.update_time_dependent(dt)


def main():
    images = load_images()  # Make sure to provide the relative or full path to the images directory.
    player = AnimatedSprite(position=(200, 200), images=images)
    all_sprites = pygame.sprite.Group(player)  # Creates a sprite group and adds 'player' to it.
    running = True
    while running:

        dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop.
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 480, 480))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update(dt)  # Calls the 'update' method on all sprites in the list (currently just the player).
        screen.fill(BACKGROUND_COLOR)
        all_sprites.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()

