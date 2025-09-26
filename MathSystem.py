import random, pygame, sys
from pygame.locals import *
pygame.init()

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
def generate_equation(level="easy"):
    digits = "0123456789"
    operators_easy = "+-*/"
    operators_hard = ["+", "-", "*", "/", "**"]

    if level == "easy":
        length, n_ops, ops = 8, 1, operators_easy
    elif level == "medium":
        length, n_ops, ops = 10, 2, operators_easy
    elif level == "hard":
        length, n_ops, ops = 12, 2, operators_hard
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