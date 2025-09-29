import pygame
pygame.init()
pygame.display.set_caption("MathDerr")

# ==============================
# ขนาดหน้าจอ
# ==============================
SCREEN_W = 1500
SCREEN_H = 800
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

# ==============================
# สีที่ใช้ในเกม
# ==============================
MAIN_RED = (158, 27, 20)

# ==============================
# หน้าต่างที่ 1 (Window 1)
# ==============================

# LOGO
LOGO_1 = pygame.image.load("logogo.png")
LOGO_1 = pygame.transform.scale(LOGO_1, (850, 650))
LOGO1_rect = LOGO_1.get_rect(center=(SCREEN_W // 2, (SCREEN_H // 2) + 20))

# Shape component
shape_1 = pygame.image.load("Component 1.png")
shape_1 = pygame.transform.scale(shape_1, (180, 60))
shape_1_rect = shape_1.get_rect(center=(SCREEN_W // 2, (SCREEN_H // 2) + 200))


# ปุ่ม Start
start = pygame.image.load("start.png")
start = pygame.transform.scale(start, (80, 20))
start_rect = start.get_rect(center=((SCREEN_W // 2) - 15, (SCREEN_H // 2) + 202))

# ลูกศร (Arrow)
arrow_1 = pygame.image.load("arrow.png")
arrow_1 = pygame.transform.scale(arrow_1, (30, 30))
arrow_1_rect = arrow_1.get_rect(center=(551, 502))


# ==============================
# หน้าต่างที่ 2 (Window 2)
# ==============================

# LOGO
LOGO_2 = pygame.image.load("logogo.png")
LOGO_2 = pygame.transform.scale(LOGO_2, (550, 350))
LOGO2_rect = LOGO_2.get_rect(center=(SCREEN_W // 2, (SCREEN_H // 2) - 120))

# ปุ่มเลือกโหมด (สีพื้นหลัง)
pink_com = pygame.image.load("1pink.png")
pink_com = pygame.transform.scale(pink_com, (180, 55))
pink_com_rect = pink_com.get_rect(center=(SCREEN_W // 2, (SCREEN_H // 2) - 30))

lbrown = pygame.image.load("2lbrown.png")
lbrown = pygame.transform.scale(lbrown, (180, 55))
lbrown_rect = lbrown.get_rect(center=(SCREEN_W // 2, (SCREEN_H // 2) + 50))

dbrown = pygame.image.load("3dbrown.png")
dbrown = pygame.transform.scale(dbrown, (180, 55))
dbrown_rect = dbrown.get_rect(center=(SCREEN_W // 2, (SCREEN_H // 2) + 125))

# ปุ่มโหมด Easy
EASY = pygame.image.load("EASY.png")
EASY = pygame.transform.scale(EASY, (65, 19))
EASY_rect = EASY.get_rect(center=((SCREEN_W // 2) - 5, (SCREEN_H // 2) - 26))

# ปุ่มโหมด Medium
MEDIUM = pygame.image.load("MEDIUM.png")
MEDIUM = pygame.transform.scale(MEDIUM, (100, 18))
MEDIUM_rect = MEDIUM.get_rect(center=((SCREEN_W // 2) - 10, (SCREEN_H // 2) + 53))

# ปุ่มโหมด Hard
HARD = pygame.image.load("HARD.png")
HARD = pygame.transform.scale(HARD, (65, 18))
HARD_rect = HARD.get_rect(center=((SCREEN_W // 2) - 8, (SCREEN_H // 2) + 130))

# ลูกศรสำหรับโหมด
arrow_2 = pygame.image.load("arrow.png")
arrow_2 = pygame.transform.scale(arrow_2, (20, 20))
arrow_21_rect = arrow_2.get_rect(center=((SCREEN_W // 2) + 53, (SCREEN_H // 2) - 26))
arrow_22_rect = arrow_2.get_rect(center=((SCREEN_W // 2) + 62, (SCREEN_H // 2) + 53))
arrow_23_rect = arrow_2.get_rect(center=((SCREEN_W // 2) + 50, (SCREEN_H // 2) + 130))

# ปุ่ม Back
BACK = pygame.image.load("back.png")
BACK = pygame.transform.scale(BACK, (65, 40))
BACK_rect = BACK.get_rect(center=((SCREEN_W // 2) + 10, (SCREEN_H // 2) + 200))

# ลูกศร Back
BACKARROW = pygame.image.load("backarrow.png")
BACKARROW = pygame.transform.scale(BACKARROW, (50, 40))
BACKARROW_rect = BACKARROW.get_rect(center=((SCREEN_W // 2) - 50, (SCREEN_H // 2) + 200))


# ==============================
# ฟังก์ชันแสดงหน้าต่าง
# ==============================

def window_1():
    """หน้าจอแรก: LOGO + ปุ่ม Start"""
    RUNNING = True
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # ถ้ากดปุ่ม Start หรือ Arrow → ไปหน้าต่าง 2
                if start_rect.collidepoint(event.pos) or arrow_1_rect.collidepoint(event.pos):
                    window_2()

        # วาดองค์ประกอบ
        screen.fill(MAIN_RED)
        screen.blit(LOGO_1, LOGO1_rect)
        screen.blit(shape_1, shape_1_rect)
        screen.blit(start, start_rect)
        screen.blit(arrow_1, arrow_1_rect)

        pygame.display.update()
    pygame.quit()


def window_2():
    """หน้าจอเลือกโหมดเกม (Easy/Medium/Hard + Back)"""
    RUNNING = True
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # ปุ่ม Back → กลับไปหน้าแรก
                if BACK_rect.collidepoint(event.pos) or BACKARROW_rect.collidepoint(event.pos):
                    window_1()
                # ตรงนี้สามารถเพิ่ม event handler ของ Easy/Medium/Hard ได้
                ###รอมาเชื่อม##
                if EASY_rect.collidepoint(event.pos):
                    import system as MS
                    MS.start_game("easy")
                if MEDIUM_rect.collidepoint(event.pos):
                    import system as MS
                    MS.start_game("medium")
                if HARD_rect.collidepoint(event.pos):
                    import system as MS
                    MS.start_game("hard")
        # วาดองค์ประกอบ
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


# ==============================
# เริ่มเกม
# ==============================
window_1()
