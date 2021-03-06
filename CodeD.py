import pygame

def game(conn):

    pygame.init()

    WIDTH = 2000
    HEIGHT = 1000

    vars = {
        "counter": 0,
        "speed": 30,
        "backgroundSpeed": 20,
        "personMovement": 10,
        "running": False,
        "stopped": False
    }

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Skateboard Daredevil")

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
        nonlocal personRect
        personRect.topleft = (x, y)

    def background(x):
        screen.blit(backgroundImg, (x, 0))

    def car(x, y):
        screen.blit(carImg, (x, y))
        nonlocal carRect
        carRect.topleft = (x, y)

    def car2(x, y):
        screen.blit(car2Img, (x, y))
        nonlocal car2Rect
        car2Rect.topleft = (x, y)

    personX = 0
    personY = (HEIGHT/2)

    carX = WIDTH-500
    carY = (HEIGHT/2)+150

    backgroundX = 0
    maxBackgroundX = -WIDTH

    currentCar = car
    currentCarRect = carRect

    font = pygame.font.SysFont("", 60, 1)
    font2 = pygame.font.Font("SomethingStrange.ttf", 120)
    you_lose = font2.render("You Lose!", 1, (255, 0, 0))
    you_loseX = WIDTH/2-(you_lose.get_width()/2)
    you_loseY = 0
    text = font.render("Press enter to play again; Q to quit", 1, (0, 0, 0))
    textX = WIDTH/2-(text.get_width()/2)
    textY = HEIGHT/2-40
    creditsFont = pygame.font.SysFont("", 30)
    creditsText = creditsFont.render("Credits to David Fesliyan for music; publicdomainvectors.org for art", 1, (0, 0, 0))
    creditsX = WIDTH/2-(creditsText.get_width()/2)
    creditsY = HEIGHT-40

    titleFont = pygame.font.Font("SomethingStrange.ttf", 120)
    title = titleFont.render("Skateboard Daredevil", 1, (255, 0, 0))
    titleX = (WIDTH/2)-(title.get_width()/2)
    titleY = 200

    lost = False
    rounding = True

    up = False
    down = True

    car_deltas = []

    while not vars["running"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()
                    raise SystemExit()
                if event.key == pygame.K_s:
                    vars["running"] = True

        screen.fill((255, 255, 255))
        start_text = font.render("Press S to start, Q to quit, Spacebar to pause", 1, (0,0,0))
        screen.blit(start_text, (WIDTH/2-(start_text.get_width()/2), HEIGHT/2+100))
        screen.blit(title, (titleX, titleY))
        pygame.display.flip()

    vars["running"] = True
    vars["personMovement"] = 10

    pygame.mixer.music.load("music_final.mp3")
    pygame.mixer.music.play(-1)
    pygame.key.set_repeat(300, 50)

    def lose():
        nonlocal lost, personY, carX, carY, up, down, vars
        lost = False
        vars["counter"] = 0
        personY = HEIGHT/2
        carX = WIDTH-500
        carY = (HEIGHT/2)+150
        personY = HEIGHT/2
        up = False
        down = True
        vars["speed"] = 20

    def left_key():
        nonlocal personX, vars
        if lost or vars["stopped"]:
            return
        personX -= vars["personMovement"]
        personX = max(personX, 0)

    def right_key():
        nonlocal personX, vars
        if lost or vars["stopped"]:
            return
        personX += vars["personMovement"]
        personX = min(personX, WIDTH-personWidth)

    def up_key():
        nonlocal up, down, personY, vars
        if lost or up or vars["stopped"]:
            return
        up = True
        down = False
        car_deltas.append(-200)
        personY -= 200

    def down_key():
        nonlocal up, down, personY, vars
        if lost or down or vars["stopped"]:
            return
        up = False
        down = True
        car_deltas.append(200)
        personY += 200


    def losing_page():
        screen.fill((255, 255, 255))
        screen.blit(you_lose, (you_loseX, you_loseY))
        screen.blit(text, (textX, textY))
        screen.blit(creditsText, (creditsX, creditsY))
        score = font.render("Your score was " + str(vars["counter"]), 1, (0,0,0))
        screen.blit(score, (textX, textY+40))
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(1000)
        lost = True


    def current_car():
        nonlocal carX, carY, currentCar, currentCarRect, car_deltas, vars
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
        vars["counter"] += 1

    vars["stopped"] = False


    def stop():
        nonlocal vars
        if lost:
            return
        vars["stopped"] = not vars["stopped"]

    while vars["running"]:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vars["running"] = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    lose()
                if event.key == pygame.K_SPACE:
                    stop()
                if event.key == pygame.K_UP:
                    up_key()
                if event.key == pygame.K_DOWN:
                    down_key()
                if event.key == pygame.K_q:
                    vars["running"] = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_key()
                if event.key == pygame.K_RIGHT:
                    right_key()
            if event.type == pygame.VIDEORESIZE:
                w, h = event.w, event.h
                screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
        if conn.poll():
            obj = conn.recv()
            if obj["type"] == "set_var":
                print(repr(obj["value"]))
                vars[obj["name"]] = obj["value"]
            elif obj["type"] == "get_var":
                conn.send(vars[obj["name"]])
            elif obj["type"] == "command":
                locals()[obj["cmd"]]()



        screen.fill((255, 255, 255))
        background(backgroundX)
        background(backgroundX+WIDTH)
        currentCar(carX, carY)
        person(personX, personY)

        if vars["stopped"]:
            pygame.display.flip()
            continue

        if (not (personRect.colliderect(currentCarRect) and personY-25 <= carY)):
            carX -= vars["speed"]
            backgroundX -= vars["backgroundSpeed"]
        else:
            losing_page()

        counterText = font.render("Score: " + str((vars["counter"])), 1, (0,0,0))
        screen.blit(counterText, (0,0))

        pygame.display.flip()
        if backgroundX <= maxBackgroundX:
            backgroundX = 0


        if carX < -carWidth:
            current_car()

        vars["speed"] += 0.2

    pygame.quit()