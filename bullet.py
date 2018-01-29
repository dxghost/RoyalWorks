import os
import pygame
import math
import time


SIZE = WIDTH, HEIGHT = 500, 750

screen = pygame.display.set_mode(SIZE)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position):

        super(Bullet, self).__init__()

        self.image = pygame.image.load("Assets\\Towers\\bullet.png")
        self.image = pygame.transform.scale(self.image, (10, 10))
        size = (10, 10)
        self.rect = pygame.Rect(position, size)
        self.velocity = pygame.math.Vector2(0, 0)
        self.x_origin = position[0]
        self.y_origin = position[1]
        self.x_target = 0
        self.y_target = 0
        self.l_x = 0
        self.l_y = 0
        self.m = 0
        self.move_in_x = position[0]
        self.move_in_y = position[1]
        self.clock = pygame.time.Clock()
        self.counter = 0
        self.control = False
        self.dis = 0
        self.W = 500
        self.H = 750

    def movebulletenemy(self, x, y):

        self.x_target = x
        self.y_target = y
        self.l_x = abs(self.x_origin - self.x_target)
        self.l_y = abs(self.y_origin - self.y_target)

        self.dis = math.sqrt(self.l_x ** 2 + self.l_y ** 2)

        if self.x_target > self.x_origin and self.y_target > self.y_origin:
            self.velocity.x = (self.l_x / self.dis) * 15
            self.velocity.y = +(self.l_y / self.dis) * 15

        if self.x_target < self.x_origin and self.y_target > self.y_origin:
            self.velocity.x = -(self.l_x / self.dis) * 15
            self.velocity.y = +(self.l_y / self.dis) * 15

        self.move_in_x += self.velocity.x
        self.move_in_y += self.velocity.y

        screen.blit(self.image, (self.move_in_x, self.move_in_y))

        if self.x_target > self.x_origin and self.y_target > self.y_origin:

            if self.move_in_x >= self.x_target and self.move_in_y >= self.y_target:
                self.move_in_x = self.x_origin
                self.move_in_y = self.y_origin

        if self.x_target < self.x_origin and self.y_target > self.y_origin:

            if self.move_in_x <= self.x_target and self.move_in_y >= self.y_target:
                self.move_in_x = self.x_origin
                self.move_in_y = self.y_origin

    def movebullet(self, x, y):

        self.x_target = x
        self.y_target = y
        self.l_x = abs(self.x_origin - self.x_target)
        self.l_y = abs(self.y_origin - self.y_target)

        self.dis = math.sqrt(self.l_x ** 2 + self.l_y ** 2)

        if self.x_target > self.x_origin and self.y_target < self.y_origin:
            self.velocity.x = (self.l_x / self.dis) * 15
            self.velocity.y = -(self.l_y / self.dis) * 15

        if self.x_target < self.x_origin and self.y_target < self.y_origin:
            self.velocity.x = -(self.l_x / self.dis) * 15
            self.velocity.y = -(self.l_y / self.dis) * 15

        self.move_in_x += self.velocity.x
        self.move_in_y += self.velocity.y

        screen.blit(self.image, (self.move_in_x, self.move_in_y))

        if self.x_target > self.x_origin and self.y_target < self.y_origin:

            if self.move_in_x >= self.x_target and self.move_in_y <= self.y_target:
                self.move_in_x = self.x_origin
                self.move_in_y = self.y_origin

        if self.x_target < self.x_origin and self.y_target < self.y_origin:

            if self.move_in_x <= self.x_target and self.move_in_y <= self.y_target:
                self.move_in_x = self.x_origin
                self.move_in_y = self.y_origin