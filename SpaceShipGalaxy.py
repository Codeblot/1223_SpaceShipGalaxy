import pygame, sys, random

#Describe classes to be used and their base properties
#Spaceship that is controlled by mouse movement (pos)
class SpaceShip(pygame.sprite.Sprite):
        def __init__(self,path,x_pos,y_pos):
                super().__init__()
                self.image = pygame.image.load('assets/spaceship.png')
                self.rect = self.image.get_rect(center = (x_pos,y_pos))
                self.shield_surface = pygame.image.load('assets/shield.png')
                self.health = 5

        def update(self):
                self.rect.center = pygame.mouse.get_pos()
                pygame.mouse.set_visible(False)
                self.screen_constrain()
                self.display_health()

        def screen_constrain(self):
                if self.rect.right >= 1280:
                        self.rect.right = 1280
                if self.rect.left <= 0:
                        self.rect.left = 0
                if self.rect.top <= 0:
                        self.rect.top = 0
                if self.rect.bottom >= 720:
                        self.rect.bottom = 720

        def display_health(self):
                for index,shield in enumerate(range(self.health)):
                        screen.blit(self.shield_surface,(10 + index * 40,10))

        def get_damage(self,damage_amount):
                self.health -= damage_amount

#Meteor Shower that spawns on load
class Meteor(pygame.sprite.Sprite):
        def __init__(self,path,x_pos,y_pos,x_speed,y_speed):
                super().__init__()
                self.image = pygame.image.load(path)
                self.rect = self.image.get_rect(center = (x_pos,y_pos))
                self.x_speed = x_speed
                self.y_speed = y_speed

        def update(self):
                self.rect.centerx += self.x_speed
                self.rect.centery += self.y_speed

                if self.rect.centery >= 800:
                        self.kill()

#Laser for to be drawn on mouse button down
class Laser(pygame.sprite.Sprite):
        def __init__(self,path,pos,speed):
                super().__init__()
                self.image = pygame.image.load('assets/Laser.png')
                self.rect = self.image.get_rect(center = pos)
                self.speed = speed

        def update(self):
                self.rect.centery -= self.speed
                if self.rect.centery <-50:
                        self.kill()

pygame.init() # Initiate pygame
screen = pygame.display.set_mode((1280,720)) # Create display surface
clock = pygame.time.Clock() # Create clock object (frames per second max)


spaceship = SpaceShip('assets/spaceship.png',640,500) #Sprite Spaceship Group
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)


meteor_group = pygame.sprite.Group() #Sprite Meteor Group
METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT,100)

laser_group = pygame.sprite.Group()

while True: # Game loop
        for event in pygame.event.get(): # Check for events / Player input
                if event.type == pygame.QUIT: # Close the game
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == METEOR_EVENT:
                        meteor_path = random.choice((['assets/Meteor1.png','assets/Meteor2.png','assets/Meteor3.png']))
                        random_x_pos = random.randrange(0,1280)
                        random_y_pos = random.randrange(-500,-50)
                        random_x_speed = random.randrange(-1,1)
                        random_y_speed = random.randrange(4,10)
                        meteor = Meteor(meteor_path,random_x_pos,random_y_pos,random_x_speed,random_y_speed)
                        meteor_group.add(meteor)
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                        new_laser = Laser('assets/Laser.png', event.pos, 10)
                        laser_group.add(new_laser)

        screen.fill((42,45,51))
        
        laser_group.draw(screen)
        spaceship_group.draw(screen)
        meteor_group.draw(screen)

        laser_group.update()
        spaceship_group.update()
        meteor_group.update()
        
        # Collision Detections
        if pygame.sprite.spritecollide(spaceship_group.sprite,meteor_group,True):
                spaceship_group.sprite.get_damage(1)

        pygame.display.update() # Draw frame
        clock.tick(120) # Control framerate
