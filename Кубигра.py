import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
# смерть
died = pygame.font.Font(None, 50)
text = died.render("вы умерли", False, "Red")
text_rect = text.get_rect(center=(400, 30))
show_death_text = False
#счёт
schet = 0
total = pygame.font.Font(None, 50)
text2 = total.render("Ваш счёт: " + str(schet), False, "DarkGreen")

#настройки
colors = {
    1: "LightBlue",
    2: "Yellow",
    3: "Red",
    4: "DarkGreen",
    5: "Purple"
}
current_color = 3  # начальный цвет - Red
color_name = colors[current_color]
set4 = pygame.font.Font(None, 50)
set5 = total.render(f"Текущий цвет: {color_name}", False, "DarkGreen")

setting_active = False
set3_text = "Настройки: Нажмите кнопку Назад или R-сменить цвет"
set3 = total.render(set3_text, False, "DarkGreen")

# игрок
s = pygame.Surface((70, 70))
s.fill(colors[current_color])
player_rect = s.get_rect(center=(400, 550))
# движение игрока
speed = 8
player_x = 400

# поле часть 1
pole = pygame.Surface((10, 600))
pole.fill("Blue")
# поле часть 2
pole1 = pygame.Surface((800, 10))
pole1.fill("Blue")

# Враг 1
killer = pygame.Surface((70, 70))
killer.fill("Blue")
killer_rect = killer.get_rect(center=(random.randint(50, 750), 0))
speedvrag = 4

# Враг 2
killer2 = pygame.Surface((70, 70))
killer2.fill("Green")
killer2_rect = killer2.get_rect(center=(random.randint(50, 750), -200))
speedvrag2 = 6

# Кнопки для телефона (игровые)
button_left = pygame.Rect(50, 500, 100, 50)
button_right = pygame.Rect(650, 500, 100, 50)
button_font = pygame.font.Font(None, 30)
button_left_text = button_font.render("Влево", True, "Black")
button_right_text = button_font.render("Вправо", True, "Black")

# Кнопки меню
button_start = pygame.Rect(300, 200, 200, 60)
button_settings = pygame.Rect(300, 300, 200, 60)
button_back = pygame.Rect(300, 400, 200, 60)
button_color = pygame.Rect(300, 300, 200, 60)  # В настройках

menu_font = pygame.font.Font(None, 40)
start_text = menu_font.render("Старт игры", True, "Black")
settings_text = menu_font.render("Настройки", True, "Black")
back_text = menu_font.render("Назад", True, "Black")
color_text = menu_font.render("Сменить цвет", True, "Black")

clock = pygame.time.Clock()
running = True
game_active = False

while running:
    screen.fill("Black")
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()[0]
    
    if game_active:
        # Вывод счёта
        text2 = total.render("Ваш счёт: " + str(schet), False, "DarkGreen")
        screen.blit(text2, (10, 10))
        
        # Перемещение врагов
        killer_rect.y += speedvrag
        if killer_rect.top > 600:
            killer_rect = killer.get_rect(center=(random.randint(50, 750), -50))
            schet += 50
        
        killer2_rect.y += speedvrag2
        if killer2_rect.top > 600:
            killer2_rect = killer2.get_rect(center=(random.randint(50, 750), -100))
            schet += 100
        
        # Управление игроком
        if ((pygame.key.get_pressed()[pygame.K_LEFT] or 
             (mouse_clicked and button_left.collidepoint(mouse_pos))) and 
            player_x > 10):
            player_x -= speed
        if ((pygame.key.get_pressed()[pygame.K_RIGHT] or 
             (mouse_clicked and button_right.collidepoint(mouse_pos))) and 
            player_x < 720): 
            player_x += speed
        player_rect.x = player_x
        
        # Проверка столкновений
        if player_rect.colliderect(killer_rect) or player_rect.colliderect(killer2_rect):
            show_death_text = True
            game_active = False
        
        screen.blit(s, player_rect)
        if show_death_text:
            screen.blit(text, text_rect)
        
        screen.blit(killer, killer_rect)
        screen.blit(killer2, killer2_rect)
        
        # Кнопки управления для телефона
        pygame.draw.rect(screen, "Gray", button_left)
        pygame.draw.rect(screen, "Gray", button_right)
        screen.blit(button_left_text, (button_left.x + 20, button_left.y + 15))
        screen.blit(button_right_text, (button_right.x + 10, button_right.y + 15))
        
        # Увеличение скорости врагов
        if schet >= 3000:
            speedvrag = 10
            speedvrag2 = 13
        elif schet >= 10000:
            speedvrag = 15
            speedvrag2 = 20
        elif schet >= 1000:
            speedvrag = 8
            speedvrag2 = 10
        if schet <= 1000:
            speedvrag = 4
            speedvrag2 = 6
        
        # Границы
        screen.blit(pole, (0, 0))
        screen.blit(pole, (790, 0))
        screen.blit(pole1, (0, 0))
        screen.blit(pole1, (0, 590))
    
    elif setting_active:
        # Экран настроек
        screen.blit(set3, (50, 150))
        set5 = total.render(f"Текущий цвет: {color_name}", False, "DarkGreen")
        screen.blit(set5, (50, 200))
        
        # Кнопка смены цвета
        pygame.draw.rect(screen, "Gray", button_color)
        screen.blit(color_text, (button_color.x + 20, button_color.y + 15))
        
        # Кнопка назад
        pygame.draw.rect(screen, "Gray", button_back)
        screen.blit(back_text, (button_back.x + 60, button_back.y + 15))
        
        if (mouse_clicked and button_color.collidepoint(mouse_pos)) or pygame.key.get_pressed()[pygame.K_r]:
            current_color = random.randint(1, 5)
            color_name = colors[current_color]
            s.fill(colors[current_color])
            pygame.time.delay(200)
        
        if (mouse_clicked and button_back.collidepoint(mouse_pos)) or pygame.key.get_pressed()[pygame.K_s]:
            setting_active = False
            pygame.time.delay(200)
    
    else:  # Главное меню
        # Кнопка старта
        pygame.draw.rect(screen, "Gray", button_start)
        screen.blit(start_text, (button_start.x + 30, button_start.y + 15))
        
        # Кнопка настроек
        pygame.draw.rect(screen, "Gray", button_settings)
        screen.blit(settings_text, (button_settings.x + 40, button_settings.y + 15))
        
        if (mouse_clicked and button_start.collidepoint(mouse_pos)) or pygame.key.get_pressed()[pygame.K_q]:
            game_active = True
            show_death_text = False
            schet = 0
            killer_rect.y = 0
            killer2_rect.y = -200
            player_x = 400
            player_rect.x = player_x
            pygame.time.delay(200)
        
        if (mouse_clicked and button_settings.collidepoint(mouse_pos)) or pygame.key.get_pressed()[pygame.K_s]:
            setting_active = True
            pygame.time.delay(200)
    
    pygame.display.update()
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
