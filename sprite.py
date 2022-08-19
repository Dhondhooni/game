import pygame
pygame.init()
#pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

player = pygame.sprite.Sprite() 
img = pygame.image.load (r"Doll.png")
#x = y = 0
#clicks = 0

#Doll = pygame.image.load(r'Doll.png')
#Doll = pygame.transform.scale(Doll, (20, 20))

#Necessary definitions
player.image = img
player.rect = img.get_rect()
#Player position
player.rect.x = 0
player.rect.y = 0

#Sprite group
group = pygame.sprite.Group()
group.add(player)

screen = pygame.display.set_mode((600, 500))
running = True

fpsClock = pygame.time.Clock()
fps = 60

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
            print(event.key, event.type)
            
            keys=pygame.key.get_pressed()
            
            if keys [pygame.K_s]:
               player.rect.y += 5
            if keys [pygame.K_w]:
               player.rect.y -= 5
            if keys [pygame.K_d]:
               player.rect.x  +=5
            if keys [pygame.K_a]:
               player.rect.x -= 5    
                
            if player.rect .x < 0: player . rect  .x = 0
            if player.rect .y < 0: player . rect  .y = 0
                        
            #if x < 0: X = 0    
            #if y < 0: y = 0    
                
    screen.fill((255, 255, 255))
    #screen.blit(player, (x, y))
    group .update () #Update all the sprites in the group
    group .draw(screen) #Draw the sprites on to the screen

    pygame.display.flip()
    fpsClock.tick(fps)
    
    pygame .quit ()

