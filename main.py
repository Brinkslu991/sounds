import pygame, random, sys, time



WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
TITLE = 'THIS IS A TITLE'
TEXT_FONT = 'DejaVuSans.ttf'
FAVICON = 'favicon-32x32.png'
SOUND_1 = 'doom-death-sound-effect.ogg'
SOUND_2 = 'atomic-cat.ogg'
SOUND_3 = 'roblox-death-sound.ogg'
BGMUSIC = 'Malcom Todd - Chest Pains (I love) [Full Jakeneutron Cover] [TubeRipper.com].mp3'
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
FIRESKY = (230, 69, 29)
GOLDBRICK = (181, 101, 29)
SAPPHIRE = (15, 82, 186)

def init_game ():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(TITLE)
    return screen

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            
def draw_text(screen, text, font, text_color, y):
    img = font.render(text, False, text_color)
    screen.blit(img, (90, y))

def main():
    screen = init_game()
    #clock = pygame.time.Clock()
    text_font = pygame.font.Font(TEXT_FONT, 30)
    text_color = FIRESKY

    sound1 = pygame.mixer.Sound(SOUND_1)
    sound2 = pygame.mixer.Sound(SOUND_2)
    sound3 = pygame.mixer.Sound(SOUND_3)
    bgmusic = pygame.mixer.Sound(BGMUSIC)

    instructions = ["Press 'a' to play Sound Effect #1","Press 's' to play Sound Effect #2","Press 'd' to play Sound Effect #3","Press 'm' to play the Background music","Press 'p' to pause the Background Music"]

    base_y = 40
    line_height = 40
    running = True
    while running:
        screen.fill(WHITE) # Use color from config

        for i in range(len(instructions)):
            draw_text(screen, instructions[i], text_font, text_color, base_y + i * line_height)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            sound1.play()
        if keys[pygame.K_a]:
            sound2.play()
        if keys[pygame.K_d]:
            sound3.play()
        if keys[pygame.K_m]:
            bgmusic.play()
        if keys[pygame.K_p]:
            bgmusic.stop()

        pygame.display.flip()
        
        # Limit the frame rate to the specified frames per second (FPS)
        #clock.tick(FPS) # Use the clock to control the frame rate

        

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()