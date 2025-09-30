import random
import pygame
import sys
from pygame.locals import *
pygame.init()

# ==============================
# ขนาดหน้าจอ
# ==============================
SCREEN_W = 1500
SCREEN_H = 800
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

# ==============================
# สีที่ใช้ในเกม
# ==============================
WHITE      = (255, 255, 255)
YELLOW     = (255, 255, 102)
GREY       = (211, 211, 211)
BLACK      = (0, 0, 0)
GREEN      = (0, 255, 0)
LIGHT_GREEN= (150, 255, 210)
RED        = (255, 0, 0)
MAIN_RED   = (158, 27, 20)
CREAM      = (243, 229, 171)

# ปุ่ม Back
BACK = pygame.image.load("backarrow.png")
BACK = pygame.transform.scale(BACK, (80, 80))
BACK_rect = BACK.get_rect(center=(150, 100))

# ==============================
# ฟอนต์
# ==============================
font    = pygame.font.SysFont("Helvetica neue", 80)
fontinbox    = pygame.font.SysFont("Helvetica neue", 40)
bigFont = pygame.font.SysFont("Helvetica neue", 80)

# ==============================
# ข้อความแสดงผล
# ==============================
youWin           = bigFont.render("You Win! Play again?",       True, LIGHT_GREEN)
youLose          = bigFont.render("You Lose! Try again?",      True, WHITE)
incorrectAnswer  = bigFont.render("Sum is incorrect", True, WHITE)

# ==============================
# ฟังก์ชันอ่านสมการจากไฟล์ (โหมด Hard)
# ==============================
# 🔹 ฟังก์ชันอ่านสมการจากไฟล์ (โหมด Hard)
def generate_equation_from_file(filename="Equation.txt"):
    '''อ่านสมการจากไฟล์ แล้วสุ่มเลือก 1 สมการ'''
    try:
        with open(filename, "r", encoding="utf-8") as f:
            equations = [line.strip() for line in f if line.strip()]
        if not equations:
            raise ValueError("ไฟล์ว่าง ไม่มีสมการ")
        return random.choice(equations)  # เลือกสมการแบบสุ่ม
    except FileNotFoundError:
        raise FileNotFoundError(f"ไม่พบไฟล์ {filename}, กรุณาสร้างไฟล์นี้")

# ==============================
# ฟังก์ชันสร้างสมการแบบสุ่มตามระดับความยาก
# ==============================
def generate_equation(level):
    '''สร้างสมการแบบสุ่มตามระดับความยาก'''
    digits          = "0123456789"
    operators_easy  = "+-"
    operators_medium = "*/"

    # กำหนดค่าตามระดับ
    if level == "easy":
        length, n_ops, ops = 8, 1, operators_easy
    elif level == "medium":
        length, n_ops, ops = 10, 2, operators_medium
    else:
        raise ValueError("Level must be easy, medium, or hard")

    # สุ่มสมการจนกว่าจะ valid
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
                return "".join(eq)
        except Exception:
            continue

# ==============================
# ฟังก์ชันตรวจคำตอบ
# ==============================
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
        text = fontinbox.render(ch, True, BLACK)
        pygame.draw.rect(window, guessColourCode[i],
                         pygame.Rect(SCREEN_W//2 - 325 + spacing, 50 + (turns*80), 50, 50))
        window.blit(text, (SCREEN_W//2 - 310 + spacing, 60 + (turns*80)))
        spacing += 80

    # ถ้าตัวอักษรทั้งหมดเป็นสีเขียว → ชนะ
    return all(c == GREEN for c in guessColourCode)

# ==============================
# ฟังก์ชันหลักของเกม
# ==============================
def start_game(level):
    '''ฟังก์ชันหลักของเกม'''
    while True:  # loop สำหรับ restart เกม
        if level == "hard":
            nerdleSum = generate_equation_from_file("Equation.txt") # ใช้ไฟล์แทน
        else:
            nerdleSum = generate_equation(level) # easy / medium
        grid_size = len(nerdleSum)

        print("Tatget:", nerdleSum) # debug ดูคำตอบ
        
        # ตั้งค่าหน้าจอ
        FPS = 60 
        clock = pygame.time.Clock()
        screen.fill(MAIN_RED)

        # วาด grid
        for x in range(grid_size):
            for y in range(6):
                pygame.draw.rect(screen, GREY,
                pygame.Rect(((x*80)+(SCREEN_W//2 - 325)), (y*80)+50, 50, 50), 2)

        # ตัวแปรควบคุมเกม
        guess = ""
        turns = 0
        win   = False
        playing = True
        showincorrect = False

        # loop เล่นเกม
        while playing:
            for event in pygame.event.get():
                if event.type == QUIT:  # ออกจากเกม
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK_rect.collidepoint(event.pos):
                        import interface as SY
                        SY.window_2()


                if event.type == pygame.KEYDOWN:
                    if event.key == K_BACKSPACE:  # ลบตัวอักษร
                        guess = guess[:-1]

                    elif event.key == K_RETURN:  # กด Enter
                        if win or turns == 6:
                            playing = False  # ออก loop → restart

                        elif len(guess) == grid_size and "=" in guess:
                            try:
                                # split และ eval สมการ
                                userGuess = guess.split("=") #ถูก
                                if eval(userGuess[0]) == float(userGuess[1]):
                                    win = checkGuess(turns, nerdleSum, guess, screen)
                                    turns += 1
                                    guess = ""
                                    showincorrect = False
                                    screen.fill(MAIN_RED, (0, 700, 2000, 500))
                                else: # ผิด
                                    guess = ""
                                    showincorrect = True
                            except Exception: # ผิด
                                showincorrect = True
                                guess = ""
                    else:  # พิมพ์ตัวอักษร
                        if event.unicode.isprintable() and len(guess) < grid_size:
                            guess += event.unicode.upper()
                            showincorrect = False

            # แสดง guess ปัจจุบันด้านล่าง
            pygame.draw.rect(screen, CREAM, ((x*40), (y*110), 900, 150))
            renderGuess = font.render(guess, True, BLACK)
            screen.blit(renderGuess, (600, 600))


            # แสดงข้อความ error ถ้ามี
            screen.fill(MAIN_RED, (70, 700, 1000, 100))
            if showincorrect:
                screen.blit(incorrectAnswer, (500, 715))

            # 🏆 สถานะชนะ/แพ้
            if win:
                screen.blit(youWin, (500, 715))

            if turns == 6 and not win:
                screen.blit(youLose, (500, 715))
            # วาดปุ่ม Back
            screen.blit(BACK, BACK_rect)
            # อัพเดทจอ
            pygame.display.update()
            clock.tick(FPS)
