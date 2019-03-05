import pygame
screen_height = 1080
screen_width = 1920
Running = True






def main():

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.get_caption("Mars Invaders")

    while Running:

