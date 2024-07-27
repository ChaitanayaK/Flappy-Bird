import pygame
import random
import time
import keyboard as kb
import cv2

# Load the pre-trained upper body classifier
body_cascade = cv2.CascadeClassifier(
    'C:/Users/Admin/OneDrive/Documents/Pythoncodes/eyes_casscade.xml')

# Capture the video from the webcam
cap = cv2.VideoCapture(0)

pygame.init()

s_width, s_height = 500, 650

win = pygame.display.set_mode((s_width, s_height))

bird_surf = pygame.image.load(
    'C:/Users/Admin/OneDrive/Documents/Pythoncodes/PROJECTS/Project_Flappy_Bird/Bird1.png')
pygame.display.set_icon(bird_surf)

pygame.display.set_caption('Flappy Bird Game')

clock = pygame.time.Clock()

minecraft = 'C:/Users/Admin/OneDrive/Documents/Pythoncodes/PROJECTS/Project_Flappy_Bird/Minecraft.ttf'

text_color = (76, 42, 58)

bird_jump_file = 'C:/Users/Admin/OneDrive/Documents/Pythoncodes/PROJECTS/Project_Flappy_Bird/bird_jump.wav'

bird_crash_file = 'C:/Users/Admin/OneDrive/Documents/Pythoncodes/PROJECTS/Project_Flappy_Bird/bird_crash.wav'

bird_surf = pygame.image.load(
    'C:/Users/Admin/OneDrive/Documents/Pythoncodes/PROJECTS/Project_Flappy_Bird/Bird1.png')
bird_surf = pygame.transform.scale(bird_surf, (50, 40)).convert_alpha()
initial_bird_pos = (100, 280)
bird_rect = bird_surf.get_rect(topleft=initial_bird_pos)

bird_loss = pygame.transform.scale(bird_surf, (150, 120)).convert_alpha()

bird2_surf = pygame.image.load(
    'C:/Users/Admin/OneDrive/Documents/Pythoncodes/PROJECTS/Project_Flappy_Bird/Bird2.png')
bird2_surf = pygame.transform.scale(bird2_surf, (50, 40)).convert_alpha()

cloud = pygame.image.load(
    'C:/Users/Admin/OneDrive/Documents/Pythoncodes/PROJECTS/Project_Flappy_Bird/cloud.png')
cloud = pygame.transform.scale(cloud, (250, 200)).convert_alpha()
cloud_rect = cloud.get_rect(topleft=(s_width, 30))
cloud1_rect = cloud.get_rect(topleft=(s_width+700, 120))

Font = pygame.font.Font(minecraft, 60)
loss = Font.render('You Lost', False, (76, 42, 58))

F1 = pygame.font.Font(minecraft, 50)

F2 = pygame.font.Font(minecraft, 35)


# Background
background_file = 'C:/Users/Admin/OneDrive/Documents/Pythoncodes/PROJECTS/Project_Flappy_Bird/background.jpg'
background_night_file = 'C:/Users/Admin/OneDrive/Documents/Pythoncodes/PROJECTS/Project_Flappy_Bird/background_night.jpg'
background = pygame.image.load(background_file)
background = pygame.transform.scale(
    background, (s_width, s_height)).convert_alpha()
background_rect1 = background.get_rect(topleft=(0, 0))
background_rect2 = background.get_rect(topleft=(s_width, 0))

pillar_file = 'C:/Users/Admin/OneDrive/Documents/Pythoncodes/PROJECTS/Project_Flappy_Bird/pillar.png'
pillar = pygame.image.load(pillar_file)
pillar2 = pygame.transform.scale(pillar, (110, 500))
pillar1 = pygame.transform.rotate(pillar2, 180)

rod_up_rect = pillar1.get_rect(bottomleft=(s_width, 250))
rod_down_rect = pillar2.get_rect(topleft=(s_width, 550))

flappy_bird_text_file = 'C:/Users/Admin/OneDrive/Documents/Pythoncodes/PROJECTS/Project_Flappy_Bird/flappybird_text.png'
logo_text = pygame.image.load(flappy_bird_text_file)
logo_text = pygame.transform.scale(logo_text, (450, 112))


gravity_bird = 0
gravity = 1
vel = 6
play = False
lost = False
gap = 300
score_int = 0

counter = 0


def Background():
    background_rect1.left -= 1
    win.blit(background, background_rect1)
    background_rect2.left -= 1
    win.blit(background, background_rect2)

    if background_rect1.right == 0:
        background_rect1.x = s_width

    if background_rect2.right == 0:
        background_rect2.left = s_width


def move():
    global gravity, gravity_bird
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        #bird_jump = pygame.mixer.Sound(bird_jump_file)
        # bird_jump.play()
        gravity_bird = -12
        win.blit(bird2_surf, (bird_rect.x, bird_rect.y))
    else:
        win.blit(bird_surf, bird_rect)

    gravity_bird += gravity
    bird_rect.y += gravity_bird

    if bird_rect.bottom >= 650:
        bird_rect.bottom = 650


def rods():
    global score_int, gap
    rod_up_rect.x -= vel
    rod_down_rect.x -= vel

    win.blit(pillar1, rod_up_rect)
    win.blit(pillar2, rod_down_rect)

    if score_int < 11:
        gap = 300
    elif 11 < score_int < 21:
        gap = 250
    elif 21 < score_int < 31:
        gap = 200
    elif 31 < score_int < 41:
        gap = 175
    elif 41 < score_int < 51:
        gap = 150
    elif 51 < score_int < 61:
        gap = 120

    if rod_down_rect.right < 0 and rod_up_rect.right < 0:
        rod_up_rect.left, rod_down_rect.left = s_width, s_width

        rod_up_rect.bottom = random.randint(50, (s_height-50-gap))
        rod_down_rect.top = rod_up_rect.bottom + gap


def Clouds():
    win.blit(cloud, cloud_rect)

    cloud_rect.x -= 1
    if cloud_rect.right <= -10:
        cloud_rect.left = s_width

    #win.blit(cloud, cloud1_rect)

    cloud1_rect.x -= 1
    if cloud1_rect.right <= -10:
        cloud1_rect.left = s_width+700


def Score():
    global counter, score_list, score_int, background_file, background_night_file
    counter += 1
    score_int = int(counter/60)
    score = str(score_int).zfill(3)
    score_text = F2.render(score, False, text_color)
    win.blit(score_text, (220, 20))
    score_list = []
    score_list.append(score)

    highscore_list.append(score)


def Highscore():
    file = open(
        "C:/Users/Admin/OneDrive/Documents/Pythoncodes/PROJECTS/Project_Flappy_Bird/highscore_txt.txt", "r")
    if int(max(score_list)) > int(file.read()):
        file = open(
            "C:/Users/Admin/OneDrive/Documents/Pythoncodes/PROJECTS/Project_Flappy_Bird/highscore_txt.txt", "r")
        file.write(str(max(score_list)))
    file.close()

    file = open(
        "C:/Users/Admin/OneDrive/Documents/Pythoncodes/PROJECTS/Project_Flappy_Bird/highscore_txt.txt", "r")

    your_score = 'Your Score: ' + max(score_list)

    your_score_text = F1.render(your_score, False, text_color)
    win.blit(your_score_text, (50, 50))

    HIGHSCORE_text = F1.render('HIGH SCORE', False, text_color)
    win.blit(HIGHSCORE_text, (90, 300))

    high_score_int = file.read()
    high_score_int_text = Font.render(high_score_int, False, text_color)
    win.blit(high_score_int_text, (190, 380))


def Blinking_Space():
    global i
    if i < 30:
        Press_SPACE = F1.render('Press SPACE', False, (76, 42, 58))
        win.blit(Press_SPACE, (90, 480))

    elif i > 60:
        i = 0


def collision():
    global play, lost
    if bird_rect.colliderect(rod_up_rect) or bird_rect.colliderect(rod_down_rect) or bird_rect.top <= 0 or bird_rect.bottom >= s_height:
        play = False
        lost = True


i = 0
highscore_list = []
while True:
    # Read the frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    i += 1
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            # For playing
            if event.key == pygame.K_SPACE:
                play = True
                lost = False
            # For entering the start window
            if event.key == pygame.K_ESCAPE:
                if play == False and lost == False:
                    pygame.quit()
                else:
                    play, lost = False, False

    #win.fill((202, 225, 255))
    win.fill((0, 0, 0))
    Background()

    # Detect the upper bodies in the frame
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw rectangles around the upper bodies
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Display the frame with the rectangles around the upper bodies
    cv2.imshow('Full Body Detection', frame)


    # Start Screen
    if play == False and lost == False:
        if len(bodies) == 0:
            kb.press('space')

        elif len(bodies) > 0:
            kb.release('space')

        win.blit(logo_text, (25, 75))
        win.blit(bird_loss, (160, 250))

        Blinking_Space()

    # For Playing The Game
    elif lost == False and play == True:

        if len(bodies) == 0:
            kb.press('space')

        elif len(bodies) > 0:
            kb.release('space')

        # Clouds()
        rods()
        Score()
        move()

        # For Collision
        collision()

    # After Collision
    elif play == False and lost == True:
        #win.fill((202, 225, 255))
        #win.fill((71, 199, 236))
        counter = 0
        #win.blit(your_score_text, (50, 250))
        win.blit(bird_loss, (160, 120))
        lost = True

        bird_rect.x, bird_rect.y = initial_bird_pos[0], initial_bird_pos[1]
        rod_up_rect.x, rod_down_rect.x = s_width, s_width

        Blinking_Space()

        Highscore()

    pygame.display.update()
