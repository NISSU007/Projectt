import random
import pygame
import sys

pygame.init()
pygame.display.set_caption("MathDerr")

# ==============================
# Screen Settings
# ==============================
SCREEN_W = 1000
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

# ==============================
# Colors
# ==============================
MAIN_RED = (158, 27, 20)

# ==============================
# Window 1 Assets
# ==============================
LOGO_1 = pygame.image.load("IMAGE/logogo.png")
LOGO_1 = pygame.transform.scale(LOGO_1, (850, 650))
LOGO1_rect = LOGO_1.get_rect(center=(SCREEN_W // 2, (SCREEN_H // 2) + 20))

shape_1 = pygame.image.load("IMAGE/Component 1.png")
shape_1 = pygame.transform.scale(shape_1, (180, 60))
shape_1_rect = shape_1.get_rect(center=(SCREEN_W // 2, (SCREEN_H // 2) + 200))

start = pygame.image.load("IMAGE/start.png")
start = pygame.transform.scale(start, (80, 20))
start_rect = start.get_rect(center=((SCREEN_W // 2) - 15, (SCREEN_H // 2) + 202))

arrow_1 = pygame.image.load("IMAGE/arrow.png")
arrow_1 = pygame.transform.scale(arrow_1, (30, 30))
arrow_1_rect = arrow_1.get_rect(center=(551, 502))

# ==============================
# Window 2 Assets
# ==============================
LOGO_2 = pygame.image.load("IMAGE/logogo.png")
LOGO_2 = pygame.transform.scale(LOGO_2, (550, 350))
LOGO2_rect = LOGO_2.get_rect(center=(SCREEN_W // 2, (SCREEN_H // 2) - 120))

pink_com = pygame.image.load("IMAGE_2/1pink.png")
pink_com = pygame.transform.scale(pink_com, (180, 55))
pink_com_rect = pink_com.get_rect(center=(SCREEN_W // 2, (SCREEN_H // 2) - 30))

lbrown = pygame.image.load("IMAGE_2/2lbrown.png")
lbrown = pygame.transform.scale(lbrown, (180, 55))
lbrown_rect = lbrown.get_rect(center=(SCREEN_W // 2, (SCREEN_H // 2) + 50))

dbrown = pygame.image.load("IMAGE_2/3dbrown.png")
dbrown = pygame.transform.scale(dbrown, (180, 55))
dbrown_rect = dbrown.get_rect(center=(SCREEN_W // 2, (SCREEN_H // 2) + 125))

arrow_2 = pygame.image.load("IMAGE_2/arrow.png")
arrow_2 = pygame.transform.scale(arrow_2, (20, 20))
arrow_21_rect = arrow_2.get_rect(center=((SCREEN_W // 2) + 53, (SCREEN_H // 2) - 26))
arrow_22_rect = arrow_2.get_rect(center=((SCREEN_W // 2) + 62, (SCREEN_H // 2) + 53))
arrow_23_rect = arrow_2.get_rect(center=((SCREEN_W // 2) + 50, (SCREEN_H // 2) + 130))

EASY = pygame.image.load("IMAGE_2/EASY.png")
EASY = pygame.transform.scale(EASY, (65, 19))
EASY_rect = EASY.get_rect(center=((SCREEN_W // 2) - 5, (SCREEN_H // 2) - 26))

MEDIUM = pygame.image.load("IMAGE_2/MEDIUM.png")
MEDIUM = pygame.transform.scale(MEDIUM, (100, 18))
MEDIUM_rect = MEDIUM.get_rect(center=((SCREEN_W // 2) - 10, (SCREEN_H // 2) + 53))

HARD = pygame.image.load("IMAGE_2/HARD.png")
HARD = pygame.transform.scale(HARD, (65, 18))
HARD_rect = HARD.get_rect(center=((SCREEN_W // 2) - 8, (SCREEN_H // 2) + 130))

BACK = pygame.image.load("IMAGE_2/back.png")
BACK = pygame.transform.scale(BACK, (65, 40))
BACK_rect = BACK.get_rect(center=((SCREEN_W // 2) + 10, (SCREEN_H // 2) + 200))

BACKARROW = pygame.image.load("IMAGE_2/backarrow.png")
BACKARROW = pygame.transform.scale(BACKARROW, (50, 40))
BACKARROW_rect = BACKARROW.get_rect(center=((SCREEN_W // 2) - 50, (SCREEN_H // 2) + 200))

# ==============================
# Window Functions
# ==============================
def window_1():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos) or arrow_1_rect.collidepoint(event.pos):
                    window_2()

        screen.fill(MAIN_RED)
        screen.blit(LOGO_1, LOGO1_rect)
        screen.blit(shape_1, shape_1_rect)
        screen.blit(start, start_rect)
        screen.blit(arrow_1, arrow_1_rect)

        pygame.display.update()
    pygame.quit()

def window_2():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_rect.collidepoint(event.pos) or BACKARROW_rect.collidepoint(event.pos):
                    window_1()
                elif EASY_rect.collidepoint(event.pos):
                    return "easy"
                elif MEDIUM_rect.collidepoint(event.pos):
                    return "medium"
                elif HARD_rect.collidepoint(event.pos):
                    return "hard"

        screen.fill(MAIN_RED)
        screen.blit(LOGO_2, LOGO2_rect)
        screen.blit(pink_com, pink_com_rect)
        screen.blit(lbrown, lbrown_rect)
        screen.blit(dbrown, dbrown_rect)
        screen.blit(EASY, EASY_rect)
        screen.blit(arrow_2, arrow_21_rect)
        screen.blit(arrow_2, arrow_22_rect)
        screen.blit(arrow_2, arrow_23_rect)
        screen.blit(MEDIUM, MEDIUM_rect)
        screen.blit(HARD, HARD_rect)
        screen.blit(BACK, BACK_rect)
        screen.blit(BACKARROW, BACKARROW_rect)

        pygame.display.update()
    pygame.quit()

window_1()

# ==============================
# Fonts and Messages
# ==============================
white = (255,255,255)
yellow = (255,255,102)
grey = (211, 211, 211)
black = (0,0,0)
green=(0,255,0)
lightGreen=(153,255,204)
red = (255, 0, 0)
MAIN_RED = (158, 27, 20)

font = pygame.font.SysFont("Helvetica neue", 40)
bigFont = pygame.font.SysFont("Helvetica neue", 80)

youWin = bigFont.render("You Win!", True, lightGreen)
youLose = bigFont.render("You Lose!", True, lightGreen)
playAgain = bigFont.render("Play Again?", True, lightGreen)
incorrectAnswer = bigFont.render("Sum is incorrect, Press ENTER", True, red)

# ==============================
# Generate Equation
# ==============================
def generate_equation(level):
    digits = "0123456789"
    operators_easy = ["+", "-"]
    operators_medium = ["+", "-", "*", "/"]
    operators_hard = ["+", "-", "*", "/"]

    if level == "easy":
        length, n_ops, ops = 8, 1, operators_easy
    elif level == "medium":
        length, n_ops, ops = 8, 1, operators_medium
    elif level == "hard":
        length, n_ops, ops = 8, 2, operators_hard
    else:
        raise ValueError("Level must be easy, medium, or hard")

    while True:
        eq_pos = random.randint(3, length - 3)
        eq = [""] * length
        eq[eq_pos] = "="

        possible_positions = [i for i in range(1, eq_pos)]
        op_positions = random.sample(possible_positions, n_ops)
        for pos in op_positions:
            eq[pos] = random.choice(ops)

        for i in range(length):
            if eq[i] == "":
                eq[i] = random.choice(digits)

        left = "".join(eq[:eq_pos])
        right = "".join(eq[eq_pos + 1:])

        try:
            if eval(left) == eval(right) and eval(right) != 0:
                return "".join(eq)
        except Exception:
            continue

# ==============================
# Check Guess
# ==============================
def checkGuess(turns, nerdleSum, userGuess, window):
    spacing = 0
    guessColourCode = [grey] * len(nerdleSum)

    for i, ch in enumerate(userGuess):
        if ch in nerdleSum:
            guessColourCode[i] = yellow
        if nerdleSum[i] == ch:
            guessColourCode[i] = green

    for i, ch in enumerate(userGuess):
        text = font.render(ch, True, black)
        pygame.draw.rect(window, guessColourCode[i], pygame.Rect(60 + spacing, 50 + (turns*80), 50, 50))
        window.blit(text, (70 + spacing, 50 + (turns*80)))
        spacing += 80

    return all(c == green for c in guessColourCode)

# ==============================
# Main Game Loop
# ==============================
def main():
    while True:
        nerdleSum = generate_equation("easy")
        grid_size = len(nerdleSum)
        print("Target:", nerdleSum)

        height, width = 600, 800
        FPS = 30
        clock = pygame.time.Clock()
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Nerdle!")

        window.fill(MAIN_RED)

        for x in range(grid_size):
            for y in range(6):
                pygame.draw.rect(window, grey, pygame.Rect(60+(x*80), 50+(y*80), 50, 50), 2)

        guess = ""
        turns = 0
        win = False
        playing = True

        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        guess = guess[:-1]
                    elif event.key == pygame.K_RETURN:
                        if win or turns == 6:
                            playing = False
                        elif len(guess) == grid_size and "=" in guess:
                            try:
                                userGuess = guess.split("=")
                                if eval(userGuess[0]) == float(userGuess[1]):
                                    win = checkGuess(turns, nerdleSum, guess, window)
                                    turns += 1
                                    guess = ""
                                    window.fill(black, (0,500, 800, 200))
                                else:
                                    window.blit(incorrectAnswer,(60,450))
                            except Exception:
                                window.blit(incorrectAnswer,(60,450))
                    else:
                        if event.unicode.isprintable() and len(guess) < grid_size:
                            guess += event.unicode.upper()

            window.fill(black, (0,500, 800, 200))
            renderGuess = font.render(guess, True, grey)
            window.blit(renderGuess, (180, 530))

            if win:
                window.blit(youWin,(90,200))
                window.blit(playAgain,(60,300))
            if turns == 6 and not win:
                window.blit(youLose,(90,200))
                window.blit(playAgain,(60,300))

            pygame.display.update()
            clock.tick(FPS)

main()

