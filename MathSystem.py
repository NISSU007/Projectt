import random
import pygame
import sys
from pygame.locals import *

# 🟢 เริ่มต้นใช้งาน pygame
pygame.init()

# 🎨 กำหนดสี (RGB)
WHITE      = (255, 255, 255)
YELLOW     = (255, 255, 102)
GREY       = (211, 211, 211)
BLACK      = (0, 0, 0)
GREEN      = (0, 255, 0)
LIGHT_GREEN= (153, 255, 204)
RED        = (255, 0, 0)
MAIN_RED   = (158, 27, 20)

# 🎨 ฟอนต์
font    = pygame.font.SysFont("Helvetica neue", 40)
bigFont = pygame.font.SysFont("Helvetica neue", 80)

# 📝 ข้อความแสดงผล
youWin           = bigFont.render("You Win!",       True, LIGHT_GREEN)
youLose          = bigFont.render("You Lose!",      True, LIGHT_GREEN)
playAgain        = bigFont.render("Play Again?",    True, LIGHT_GREEN)
incorrectAnswer  = bigFont.render("Sum is incorrect, Press ENTER", True, RED)


# 🔹 ฟังก์ชันสร้างสมการแบบสุ่มตามระดับความยาก
def generate_equation(level):
    '''สร้างสมการแบบสุ่มตามระดับความยาก'''
    digits          = "0123456789"
    operators_easy  = "+-*/"
    operators_hard  = ["+", "-", "*", "/", "**"]

    # 🔧 กำหนดค่าตามระดับ
    if level == "easy":
        length, n_ops, ops = 8, 1, operators_easy
    elif level == "medium":
        length, n_ops, ops = 10, 2, operators_easy
    elif level == "hard":
        length, n_ops, ops = 12, 2, operators_hard
    else:
        raise ValueError("Level must be easy, medium, or hard")

    # 🔄 สุ่มสมการจนกว่าจะ valid
    while True:
        # สุ่มตำแหน่งของเครื่องหมาย "="
        eq_pos = random.randint(3, length - 3)
        eq = [""] * length
        eq[eq_pos] = "="

        # สุ่มตำแหน่ง operator
        possible_positions = [i for i in range(1, eq_pos)]
        op_positions = random.sample(possible_positions, n_ops)
        for pos in op_positions:
            eq[pos] = random.choice(ops)

        # เติมช่องที่เหลือด้วยตัวเลข
        for i in range(length):
            if eq[i] == "":
                eq[i] = random.choice(digits)

        # แยกซ้าย-ขวาของ "="
        left  = "".join(eq[:eq_pos])
        right = "".join(eq[eq_pos + 1:])

        try:
            left_val  = eval(left)
            right_val = eval(right)

            # ✅ ถ้าเป็นสมการที่ถูกต้อง
            if left_val == right_val and right_val != 0:
                # hard mode ต้องมี ** อยู่บ้าง
                if level == "hard" and "**" not in left:
                    continue
                return "".join(eq)
        except Exception:
            continue


# 🔹 ฟังก์ชันตรวจคำตอบ
def checkGuess(turns, nerdleSum, userGuess, window):
    '''ตรวจคำตอบและแสดงผลลัพธ์'''
    spacing = 0
    guessColourCode = [GREY] * len(nerdleSum)

    # เช็คว่าแต่ละตัวอักษรถูกต้องแค่ไหน
    for i, ch in enumerate(userGuess):
        if ch in nerdleSum:
            guessColourCode[i] = YELLOW
        if nerdleSum[i] == ch:
            guessColourCode[i] = GREEN

    # วาดกล่องคำตอบ
    for i, ch in enumerate(userGuess):
        text = font.render(ch, True, BLACK)
        pygame.draw.rect(window, guessColourCode[i],
                         pygame.Rect(60 + spacing, 50 + (turns*80), 50, 50))
        window.blit(text, (70 + spacing, 50 + (turns*80)))
        spacing += 80

    # ถ้าตัวอักษรทั้งหมดเป็นสีเขียว → ชนะ
    return all(c == GREEN for c in guessColourCode)


# 🔹 ฟังก์ชันหลักของเกม
def start_game(level):
    '''ฟังก์ชันหลักของเกม'''
    while True:  # loop สำหรับ restart เกม
        nerdleSum = generate_equation(level)  # 👈 เปลี่ยน level ได้
        grid_size = len(nerdleSum)

        print("Target:", nerdleSum)  # debug ดูคำตอบ

        # ตั้งค่า window
        height, width = 600, 800
        FPS = 30
        clock = pygame.time.Clock()
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Nerdle!")

        window.fill(MAIN_RED)

        # วาด grid
        for x in range(grid_size):
            for y in range(6):
                pygame.draw.rect(window, GREY,
                                 pygame.Rect(60+(x*80), 50+(y*80), 50, 50), 2)

        # ตัวแปรควบคุมเกม
        guess = ""
        turns = 0
        win   = False
        playing = True

        # 🔄 loop เล่นเกม
        while playing:
            for event in pygame.event.get():
                if event.type == QUIT:  # ออกจากเกม
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == K_BACKSPACE:  # ลบตัวอักษร
                        guess = guess[:-1]

                    elif event.key == K_RETURN:  # กด Enter
                        if win or turns == 6:
                            playing = False  # ออก loop → restart

                        elif len(guess) == grid_size and "=" in guess:
                            try:
                                # split และ eval สมการ
                                userGuess = guess.split("=")
                                if eval(userGuess[0]) == float(userGuess[1]):
                                    win = checkGuess(turns, nerdleSum, guess, window)
                                    turns += 1
                                    guess = ""
                                    window.fill(BLACK, (0, 500, 800, 200))
                                else:
                                    window.blit(incorrectAnswer, (60, 450))
                            except Exception:
                                window.blit(incorrectAnswer, (60, 450))

                    else:  # พิมพ์ตัวอักษร
                        if event.unicode.isprintable() and len(guess) < grid_size:
                            guess += event.unicode.upper()

            # 🖥️ แสดง guess ปัจจุบันด้านล่าง
            window.fill(BLACK, (0, 500, 800, 200))
            renderGuess = font.render(guess, True, GREY)
            window.blit(renderGuess, (180, 530))

            # 🏆 สถานะชนะ/แพ้
            if win:
                window.blit(youWin, (90, 200))
                window.blit(playAgain, (60, 300))

            if turns == 6 and not win:
                window.blit(youLose, (90, 200))
                window.blit(playAgain, (60, 300))

            # อัพเดทจอ
            pygame.display.update()
            clock.tick(FPS)
