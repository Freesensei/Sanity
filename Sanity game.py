import pygame, sys, time

WHITE= (255, 255, 255)

    #background = pygame.image.load()
"""
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
    walkRight = [pygame.image.load("TheGuy.png")]
    walkLeft = [pygame.image.load("TheGuy2.png")]

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.walkRight
        #self.image.fill(WHITE)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6    
        
        self.rect = self.image.get_rect()
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
"""
class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    walking_frames_l = []
    walking_frames_r = []

    direction = "R"

    level = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        image = pygame.image.load("TheGuy.png")
        self.walking_frames_r.append(image)
        image = pygame.image.load("TheGuy2.png")
        self.walking_frames_r.append(image)

        image = pygame.image.load("TheGuy.png")
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.image.load("TheGuy2.png")
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        self.image = self.walking_frames_r[0]

        self.rect = self.image.get_rect()

    def update(self):
        self.calc_grav()

        self.rect.x += self.change_x
        pos = self.rect.x #+ self.level.world_shift

        if self.change_x != 0 and self.change_y != 0 and self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]

        elif self.change_x != 0 and self.direction == "L":
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
    
        elif self.change_y != 0 and self.direction == "R" or self.change_x == 0 and self.direction == "R":
            self.image = self.walking_frames_r[1]
        
        elif self.change_x == 0 and self.direction == "L":
            self.image = self.walking_frames_l[1]
        
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left

            elif self.change_x < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y


        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top

            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0

            #if isinstance(block, MovingPlatform):
            #    self.rect.x += block.change_x

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .50

        if self.rect.y >= base_heigt - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = base_heigt - self.rect.height

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= base_heigt:
            self.change_y = -16

    def go_left(self):
        self.change_x = -9
        self.direction = "L"

    def go_right(self):
        self.change_x = 9
        self.direction = "R"

    def stop(self):
        self.change_x = 0

def main():
    screenwidth = 1920
    screenheight = 1080
    pygame.init()
    screen = pygame.display.set_mode((screenwidth, screenheight))

    pygame.display.set_mode((1920, 1080))

    pygame.display.set_caption("")
    
    boy = Player()

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
