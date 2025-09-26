import random, pygame, sys
from pygame.locals import *
pygame.init()

pygame.display.set_caption("MathDerr")

"""ขนาดจอเกม"""
SCREEN_W = 1000
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

"""COLOR"""
MAIN_RED = (158, 27, 20)

"""Image window 1"""
"""LOGO Mathder"""
LOGO_1 = pygame.image.load("IMAGE/logogo.png")
LOGO_1 = pygame.transform.scale(LOGO_1, (850,650))
LOGO1_rect = LOGO_1.get_rect()
LOGO1_rect.center = (SCREEN_W // 2, (SCREEN_H // 2) + 20)
"""component"""
shape_1 = pygame.image.load("IMAGE/Component 1.png")
shape_1 = pygame.transform.scale(shape_1 , (180,60))
shape_1_rect = shape_1.get_rect()
shape_1_rect.center = (SCREEN_W // 2, (SCREEN_H // 2) + 200)
"""start"""
start = pygame.image.load("IMAGE/start.png")
start = pygame.transform.scale(start , (80,20))
start_rect = start.get_rect()
start_rect.center = ((SCREEN_W // 2) - 15, (SCREEN_H // 2) + 202)
"""Arrow"""
arrow_1 = pygame.image.load("IMAGE/arrow.png")
arrow_1 = pygame.transform.scale(arrow_1 , (30,30))
arrow_1_rect = arrow_1.get_rect()
arrow_1_rect.center = (551, 502)

"==========================================================================="

"""Image window 2"""
"""LOGO Mathder"""
LOGO_2 = pygame.image.load("IMAGE/logogo.png")
LOGO_2 = pygame.transform.scale(LOGO_2, (550,350))
LOGO2_rect = LOGO_2.get_rect()
LOGO2_rect.center = (SCREEN_W // 2, (SCREEN_H // 2) - 120)
"""component"""
pink_com = pygame.image.load("IMAGE_2/1pink.png")
pink_com = pygame.transform.scale(pink_com , (180,55))
pink_com_rect = pink_com.get_rect()
pink_com_rect.center = (SCREEN_W // 2, (SCREEN_H // 2) - 30)

lbrown = pygame.image.load("IMAGE_2/2lbrown.png")
lbrown = pygame.transform.scale(lbrown , (180,55))
lbrown_rect = lbrown.get_rect()
lbrown_rect.center = (SCREEN_W // 2, (SCREEN_H // 2) + 50)

dbrown = pygame.image.load("IMAGE_2/3dbrown.png")
dbrown = pygame.transform.scale(dbrown , (180,55))
dbrown_rect = dbrown.get_rect()
dbrown_rect.center = (SCREEN_W // 2, (SCREEN_H // 2) + 125)

"""Mode"""
arrow_2 = pygame.image.load("IMAGE_2/arrow.png")
arrow_2 = pygame.transform.scale(arrow_2 , (20,20))
arrow_21_rect = arrow_2.get_rect()
arrow_22_rect = arrow_2.get_rect()
arrow_23_rect = arrow_2.get_rect()

EASY = pygame.image.load("IMAGE_2/EASY.png")
EASY = pygame.transform.scale(EASY , (65,19))
EASY_rect = EASY.get_rect()
EASY_rect.center = ((SCREEN_W // 2) - 5, (SCREEN_H // 2) - 26)
arrow_21_rect.center = ((SCREEN_W // 2) + 53, (SCREEN_H // 2) - 26)

MEDIUM = pygame.image.load("IMAGE_2/MEDIUM.png")
MEDIUM = pygame.transform.scale(MEDIUM , (100,18))
MEDIUM_rect = MEDIUM.get_rect()
MEDIUM_rect.center = ((SCREEN_W // 2) - 10, (SCREEN_H // 2) + 53)
arrow_22_rect.center = ((SCREEN_W // 2) + 62, (SCREEN_H // 2) + 53)

HARD = pygame.image.load("IMAGE_2/HARD.png")
HARD = pygame.transform.scale(HARD , (65,18))
HARD_rect = HARD.get_rect()
HARD_rect.center = ((SCREEN_W // 2) - 8, (SCREEN_H // 2) + 130)
arrow_23_rect.center = ((SCREEN_W // 2) + 50, (SCREEN_H // 2) + 130)

"""Back"""
BACK = pygame.image.load("IMAGE_2/back.png")
BACK = pygame.transform.scale(BACK, (65,40))
BACK_rect = BACK.get_rect()
BACK_rect.center = ((SCREEN_W // 2) + 10, (SCREEN_H // 2) + 200)

BACKARROW = pygame.image.load("IMAGE_2/backarrow.png")
BACKARROW = pygame.transform.scale(BACKARROW, (50,40))
BACKARROW_rect = BACKARROW.get_rect()
BACKARROW_rect.center = ((SCREEN_W // 2) - 50, (SCREEN_H // 2) + 200)

"""Interface of window 1"""
def window_1():
    """การทำงานของแอพ"""
    RUNNING = True
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos) or arrow_1_rect.collidepoint(event.pos):
                    window_2()
        screen.fill(MAIN_RED)
        screen.blit(LOGO_1, LOGO1_rect)
        screen.blit(shape_1, shape_1_rect)
        screen.blit(start, start_rect)
        screen.blit(arrow_1, arrow_1_rect)
        """แสดงภาพ"""
        pygame.display.update()
    pygame.quit()

"""Interface of window 2"""
def window_2():
    """การทำงานของเกม"""
    RUNNING = True
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_rect.collidepoint(event.pos) or BACKARROW_rect.collidepoint(event.pos):
                    window_1()
                elif EASY_rect.collidepoint(event.pos):
                    level = "easy"
                    return level
                elif MEDIUM_rect.collidepoint(event.pos):
                    level = "medium"
                    return level
                elif HARD_rect.collidepoint(event.pos):
                    level = "hard"
                    return level

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
        """แสดงภาพ"""
        pygame.display.update()

    pygame.quit()

window_1()

# 🎨 Colors
white = (255,255,255)
yellow = (255,255,102)
grey = (211, 211, 211)
black = (0,0,0)
green=(0,255,0)
lightGreen=(153,255,204)
red = (255, 0, 0)
MAIN_RED = (158, 27, 20)


# 🎨 Fonts
font = pygame.font.SysFont("Helvetica neue", 40)
bigFont = pygame.font.SysFont("Helvetica neue", 80)

youWin = bigFont.render("You Win!",       True, lightGreen)
youLose = bigFont.render("You Lose!",     True, lightGreen)
playAgain = bigFont.render("Play Again?", True, lightGreen)
incorrectAnswer = bigFont.render("Sum is incorrect, Press ENTER", True, red)


# 🔹 สร้างสมการสุ่ม
def generate_equation(level):
    digits = "0123456789"
    operators_easy = "+-"
    operators_easy = ["+", "-", "*", "/"]
    operators_hard = ["+", "-", "*", "/"]

    if level == "easy":
        length, n_ops, ops = 8, 1, operators_easy
    elif level == "medium":
        length, n_ops, ops = 8, 1, operators_easy
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
            left_val = eval(left)
            right_val = eval(right)
            if left_val == right_val and right_val != 0:
                if level == "hard" and "**" not in left:
                    continue
                return "".join(eq)
        except Exception:
            continue


# 🔹 ฟังก์ชันตรวจคำตอบ
def checkGuess(turns, nerdleSum, userGuess, window):
    spacing = 0
    renderList = []
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


# 🔹 Main game loop
def main():
    while True:  # loop เพื่อ restart เกม
        nerdleSum = generate_equation("easy")  # 👈 เปลี่ยน level ได้
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

        # 🔄 loop เล่นเกม
        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == K_BACKSPACE:
                        guess = guess[:-1]
                    elif event.key == K_RETURN:
                        if win or turns == 6:
                            playing = False  # ออก loop → restart
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

            # 🔹 แสดง guess ปัจจุบัน
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
