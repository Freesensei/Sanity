import pygame, sys, time

WHITE= (255, 255, 255)

    #background = pygame.image.load()

class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    width = 100
    height = 150
    left = False
    right = False
    walkCount = 0

    directon = "R"

    #char = pygame.image.load()
    #walkRight = [pygame.image.load("TheGuy.png")]
    #walkLeft = [pygame.image.load("TheGuy2.png")]

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface([70, 70])
        self.image.fill(WHITE)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6    
        
        self.image = pygame.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def draw(self):
        pass

    def go_Right(self):
        self.change_x = 6

    def go_Left(self):
        self.change_x = -6

    def go_Up(self):
        self.change_y = -6

    def go_Down(self):
        self.change_y = 6
    
    def update(self):
        self.rect.x += self.change_x
        pos = self.rect.x 

def main():
    screenwidth = 1920
    screenheight = 1080
    pygame.init()
    screen = pygame.display.set_mode((screenwidth, screenheight))

    pygame.display.set_mode((1920, 1080))

    pygame.display.set_caption("")
    
    boy = Player(50, 50, )

    running = True
    while running:
        
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False

            if event.type == pygame.K_d:
                boy.go_Right()

            if event.type == pygame.K_a:
                boy.go_Left()
            
            if event.type == pygame.K_w:
                boy.go_Up()
            
            if event.type == pygame.K_s:
                boy.go_Down()
            
        Player.draw()
        pygame.display.flip()

    pygame.quit()
main()
