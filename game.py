import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

screen.fill((255, 255, 255))
color = (0, 0, 0)
running = True
s_mouse = 0
k_mouse = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #rockY += 5

    mouse = pygame.mouse.get_pos()

    if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_r:
            pygame.draw.circle(screen, (255, 0, 0), (mouse[0], mouse[1]), 10, 0)
    if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_b:
            pygame.draw.circle(screen, (0, 0, 255), (mouse[0], mouse[1]), 10, 0)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_g:
            pygame.draw.circle(screen, (0, 255, 0), (mouse[0], mouse[1]), 10, 0)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
            pygame.draw.circle(screen, (255, 0, 255), (mouse[0], mouse[1]), 10, 0)
    elif pygame.mouse.get_pressed()[0]:
        pygame.draw.circle(screen, color, (mouse[0], mouse[1]), 10, 0)
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_e:
            pygame.draw.circle(screen, (255, 255, 255), (mouse[0], mouse[1]), 25, 0)

    pygame.display.update()

clock.tick(400)


pygame.quit()