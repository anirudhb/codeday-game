import pygame

pygame.init()

W = 500
H = 500

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
arrowImg = pygame.image.load("arrow.png")
arrowImg = pygame.transform.scale(arrowImg, (75, 50))
screen.fill((255, 255, 205))

circle_Y = 200
arrow_W = 425
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    pygame.draw.circle(screen, (255, 0, 0), (13, circle_Y), 10, 10)
    #circle_Y += 1
    if circle_Y >= H - 5:
        circle_Y = -circle_Y

    screen.blit(arrowImg, (arrow_W, 400))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            pygame.transform.rotate(screen, 90)
            arrow_W += 1
        if event.key == pygame.K_LEFT:
            arrow_W -= 1
    pygame.display.flip()
    screen.fill((255, 255, 205))
pygame.quit()