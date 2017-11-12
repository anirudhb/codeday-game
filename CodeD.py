import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 1000

counter = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Platform")
running = False

personWidth = 200

personImg = pygame.image.load("person_final2.png").convert_alpha()
personImg = pygame.transform.scale(personImg, (personWidth, 300))
personRect = personImg.get_rect()

backgroundImg = pygame.image.load("background.jpg")
backgroundImg = pygame.transform.scale(backgroundImg, (WIDTH, HEIGHT))
backgroundRect = backgroundImg.get_rect()

carWidth = 400
car2Width = 400

carImg = pygame.image.load("car.png")
carImg = pygame.transform.scale(carImg, (carWidth, 200))
carRect = carImg.get_rect()

car2Img = pygame.image.load("car2.png")
car2Img = pygame.transform.scale(car2Img, (car2Width, 200))
car2Rect = car2Img.get_rect()

def person(x, y):
    screen.blit(personImg, (x, y))
    global personRect
    personRect.topleft = (x, y)

def background(x):
    screen.blit(backgroundImg, (x, 0))

def car(x, y):
    screen.blit(carImg, (x, y))
    global carRect
    carRect.topleft = (x, y)

def car2(x, y):
    screen.blit(car2Img, (x, y))
    global car2Rect
    car2Rect.topleft = (x, y)

personX = 0
personY = (HEIGHT/2)

carX = WIDTH-500
carY = (HEIGHT/2)+150

car2X = WIDTH+carWidth
car2Y = (HEIGHT/2)+150

backgroundX = 0
maxBackgroundX = -WIDTH

currentCar = car
currentCarRect = carRect

currentCar2 = car2
currentCarRect2 = car2Rect

font = pygame.font.SysFont("", 60, 1)
text = font.render("You lose! Press any key to play again!", 1, (0, 0, 0))
textX = WIDTH/2-450
textY = HEIGHT/2-40

lost = False
rounding = True

up = False
down = True

car_deltas = []

speed = 20

while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                pygame.quit()
                raise SystemExit()
            if event.key == pygame.K_s:
                running = True

    screen.fill((255, 255, 255))
    start_text = font.render("Press S to start, Q to quit", 1, (0,0,0))
    screen.blit(start_text, (WIDTH/2-400, HEIGHT/2))
    pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if lost:
                lost = False
                counter = 0
                personY = HEIGHT/2
                carX = WIDTH-500
                carY = (HEIGHT/2)+150
                personY = HEIGHT/2
                up = False
                down = True
                speed = 20
            if event.key == pygame.K_UP and not up:
                up = True
                down = False
                car_deltas.append(-200)
                personY -= 200
            if event.key == pygame.K_DOWN and not down:
                up = False
                down = True
                car_deltas.append(200)
                personY += 200
            if event.key == pygame.K_q:
                running = False


    screen.fill((255, 255, 255))
    background(backgroundX)
    background(backgroundX+WIDTH)
    currentCar(carX, carY)
    person(personX, personY)


    if (not (personRect.colliderect(currentCarRect) and personY-25 <= carY)):
        carX -= speed
        backgroundX -= 10
    else:
        screen.fill((255, 255, 255))
        screen.blit(text, (textX, textY))
        score = font.render("Your score was " + str(counter), 1, (0,0,0))
        screen.blit(score, (textX, textY+40))
        lost = True

    counterText = font.render(str((counter)), 1, (0,0,0))
    screen.blit(counterText, (0,0))

    pygame.display.flip()
    if backgroundX <= maxBackgroundX:
        backgroundX = 0


    if carX < -carWidth:
        carX = WIDTH+carWidth
        if currentCar == car:
            currentCar = car2
        else:
            currentCar = car
        if currentCarRect == carRect:
            currentCarRect = car2Rect
        else:
            currentCarRect = carRect
        for d in car_deltas:
            carY += d
        car_deltas = []
        counter += 1

    speed += 0.2

print(counter)
pygame.quit()