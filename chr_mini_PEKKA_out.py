import pygame
def load_images():
    """
    Loads all images in directory. The directory must only contain images.

    Args:
        path: The relative or absolute path to the directory to load images from.

    Returns:
        List of images.
    """
    images = []
    a = pygame.image.load("Assets\\chr_mini_PEKKA_out\\1_Up.png")
    a = pygame.transform.scale(a, (100, 100))
    images.append(a)
    a = pygame.image.load("Assets\\chr_mini_PEKKA_out\\2_Up.png")
    a = pygame.transform.scale(a, (100, 100))
    images.append(a)
    a = pygame.image.load("Assets\\chr_mini_PEKKA_out\\3_Up.png")
    a = pygame.transform.scale(a, (100, 100))
    images.append(a)
    a = pygame.image.load("Assets\\chr_mini_PEKKA_out\\4_Up.png")
    a = pygame.transform.scale(a, (100, 100))
    images.append(a)
    a = pygame.image.load("Assets\\chr_mini_PEKKA_out\\5_Up.png")
    a = pygame.transform.scale(a, (100, 100))
    images.append(a)
    a = pygame.image.load("Assets\\chr_mini_PEKKA_out\\6_Up.png")
    a = pygame.transform.scale(a, (100, 100))
    images.append(a)
    a = pygame.image.load("Assets\\chr_mini_PEKKA_out\\7_Up.png")
    a = pygame.transform.scale(a, (100, 100))
    images.append(a)
    a = pygame.image.load("Assets\\chr_mini_PEKKA_out\\8_Up.png")
    a = pygame.transform.scale(a, (100, 100))
    images.append(a)
    a = pygame.image.load("Assets\\chr_mini_PEKKA_out\\9_Up.png")
    a = pygame.transform.scale(a, (100, 100))
    images.append(a)
    a = pygame.image.load("Assets\\chr_mini_PEKKA_out\\10_Up.png")
    a = pygame.transform.scale(a, (100, 100))
    images.append(a)
    a = pygame.image.load("Assets\\chr_mini_PEKKA_out\\11_Up.png")
    a = pygame.transform.scale(a, (100, 100))
    images.append(a)
    a = pygame.image.load("Assets\\chr_mini_PEKKA_out\\12_Up.png")
    a = pygame.transform.scale(a, (100, 100))
    images.append(a)


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

        self.animation_time = 0.045
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

    def update(self, dt, position):
        size = (96, 144)
        self.rect = pygame.Rect(position, size)
        self.update_time_dependent(dt)



