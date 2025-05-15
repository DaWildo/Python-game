import pygame, sys #загрузка библиотек
pygame.init() #инициализация pygame
x_window, y_window = 800, 800 #размер экрана x*y
main_screen = pygame.display.set_mode([x_window, y_window]) #создание поверхности экрана
#фоны игры 1-5
background = pygame.image.load("C:/Users/79835/Documents/TimelessIdle/images/bg_fon.png") 
background2 = pygame.image.load("C:/Users/79835/Documents/TimelessIdle/images/upgrade_bg.png")
background3 = pygame.image.load("C:/Users/79835/Documents/TimelessIdle/images/dust.png")
background4 = pygame.image.load("C:/Users/79835/Documents/TimelessIdle/images/blackhole.png")
background5 = pygame.image.load("C:/Users/79835/Documents/TimelessIdle/images/rpupgrade_bg.png")
#фоны игры 1-5 под размер экрана игры
bg = pygame.transform.scale(background, (800, 800))
up_bg = pygame.transform.scale(background2, (800, 800)) 
res_bg = pygame.transform.scale(background3, (800, 800))
bh_bg = pygame.transform.scale(background4, (800, 800)) 
rp_up_bg = pygame.transform.scale(background5, (800, 800)) 
fps = pygame.time.Clock() #частота обновления
pygame.display.set_caption("TimelessIdle") #название игры
logo = pygame.image.load("C:/Users/79835/Documents/TimelessIdle/images/icon.jpg") #изображение иконки игры
pygame.display.set_icon(logo) #иконка игры
#переменные и константы
clicks = 0 #счетчик кликов
clicks_power = 1 #параметр улучшения колва кликов за раз
up1cost = 1 #цена улучшения 1
constant1 = 1.15**3 #цена улучшений 1-3
up2cost = 100
constant2 = 1.25**3
up3cost = 5000
constant3 = 1.10**3 
up4cost = 100000
constant4 = 1.2**2 #цена улучшения 4
constant5 = 1.05**5 #начальная цена рестарта игры
rps = 0 #колво очков reality 
rpsmp = 1 #колво RP за 1 reality
#цена улучшений RP 1-3
rp1upcost = 1 
rp2upcost = 10
rp3upcost = 25
bhs = 0 #нач колво финальной валюты (на данный момент)
restart_cost = 10**6 #restart_cost*=constant5
#класс который инициализирует кнопку по заданным параметрам
class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
    #обновление кнопки класса button
	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)     
    #проверка на условия кнопки класса button
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False
    #изменение цвета кнопки button при наведении на ее область
	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
#делает число коротким для удобства (10000 = 10K и тд)
def shorten_number(num: int | float):
    suffixes = ['K', 'M', 'B']
    if num < 1000:
        return str(num)
    num = float(num)
    for suffix in suffixes:
        num /= 1000
        if num < 1000:
            return '{:.1f}{}'.format(num, suffix)
    return '{:.1f}{}'.format(num, 'T')
#функции получения шрифтов нужного размера для удобства
def get_font_arial(size): 
    return pygame.font.SysFont("arial", size)
def get_font_mono(size):
    return pygame.font.SysFont("monospace", size)
UPGRADE_ONE_TEXT = get_font_arial(45).render(("Cost:{}".format(shorten_number(round(up1cost)))), True, ("White"))
#цикл экрана улучшений с кнопками улучшений и возвращения назад в основной цикл
def upgrademenu():
    while True:
        global clicks, clicks_power, up1cost, up2cost, up3cost, up4cost
        UPMENU_MOUSE_POS = pygame.mouse.get_pos()

        main_screen.blit(up_bg, (0, 0))

        UPMENU_TEXT = get_font_arial(45).render("Up menu", True, "White")
        UPMENU_RECT = UPMENU_TEXT.get_rect(center=(400, 75))
        main_screen.blit(UPMENU_TEXT, UPMENU_RECT)
        CLICK_TEXT = get_font_arial(36).render((("{}".format(shorten_number(round(clicks))))), True, (255, 255, 255))
        main_screen.blit(CLICK_TEXT, (390, 25))
        UPMENU_BACK = Button(image=None, pos=(400, 150),
                             text_input="Back", font=get_font_arial(45), base_color ="White", hovering_color="Blue")
        UPMENU_BACK.changeColor(UPMENU_MOUSE_POS)
        UPMENU_BACK.update(main_screen)
        
        UPGRADE_ONE_TEXT = get_font_arial(36).render("Upgrade level 1", True, ("White"))
        UPGRADE_ONE_RECT = UPGRADE_ONE_TEXT.get_rect(center=(225, 275))
        up1_rect = pygame.rect.Rect(100, 250, 255, 100)
        up2_rect = pygame.rect.Rect(450, 250, 255, 100)
        up3_rect = pygame.rect.Rect(100, 400, 255, 100)
        up4_rect = pygame.rect.Rect(450, 400, 255, 100)
        pygame.draw.rect(main_screen, (26, 26, 26), up1_rect)
        pygame.draw.rect(main_screen, (26, 26, 26), up2_rect)
        pygame.draw.rect(main_screen, (26, 26, 26), up3_rect)
        pygame.draw.rect(main_screen, (26, 26, 26), up4_rect)
        main_screen.blit(UPGRADE_ONE_TEXT, UPGRADE_ONE_RECT)
        UPGRADE_TWO_TEXT = get_font_arial(36).render("Upgrade level 2", True, ("White"))
        UPGRADE_TWO_RECT = UPGRADE_TWO_TEXT.get_rect(center=(575, 275))
        main_screen.blit(UPGRADE_TWO_TEXT, UPGRADE_TWO_RECT)
        UPGRADE_THREE_TEXT = get_font_arial(36).render("Upgrade level 3", True, ("White"))
        UPGRADE_THREE_RECT = UPGRADE_TWO_TEXT.get_rect(center=(225, 425))
        main_screen.blit(UPGRADE_THREE_TEXT, UPGRADE_THREE_RECT)
        UPGRADE_FOUR_TEXT = get_font_arial(36).render("Upgrade level 4", True, ("White"))
        UPGRADE_FOUR_RECT = UPGRADE_FOUR_TEXT.get_rect(center=(575, 425))
        main_screen.blit(UPGRADE_FOUR_TEXT, UPGRADE_FOUR_RECT)
        

        
        UPGRADE_ONE = Button(image=None, pos=(225, 325),
                            text_input="Cost: {}".format(shorten_number(round(up1cost)), True, "White"), font=get_font_arial(36), base_color=("White"), hovering_color="White")
        UPGRADE_ONE.changeColor(UPMENU_MOUSE_POS)
        UPGRADE_ONE.update(main_screen)

        UPGRADE_TWO = Button(image=None, pos=(575, 325),
                            text_input="Cost: {}".format(shorten_number(round(up2cost)), True, "White"), font=get_font_arial(36), base_color=("White"), hovering_color="White")
        UPGRADE_TWO.changeColor(UPMENU_MOUSE_POS)
        UPGRADE_TWO.update(main_screen)
        
        UPGRADE_THREE = Button(image=None, pos=(225, 475),
                            text_input="Cost: {}".format(shorten_number(round(up3cost)), True, "White"), font=get_font_arial(36), base_color=("White"), hovering_color="White")
        UPGRADE_THREE.changeColor(UPMENU_MOUSE_POS)
        UPGRADE_THREE.update(main_screen)

        UPGRADE_FOUR = Button(image=None, pos=(575, 475),
                            text_input="Cost: {}".format(shorten_number(round(up4cost)), True, "White"), font=get_font_arial(36), base_color=("White"), hovering_color="White")
        UPGRADE_FOUR.changeColor(UPMENU_MOUSE_POS)
        UPGRADE_FOUR.update(main_screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #если нажата кнопка назад то перебросит в основной цикл
                if UPMENU_BACK.checkForInput(UPMENU_MOUSE_POS):
                    game()
            #функционал кнопок улучшений клика 1-4 от клика по ним а также на клавиши 1-4
            if event.type == pygame.MOUSEBUTTONDOWN and up1_rect.collidepoint(event.pos):
                if event.button == pygame.BUTTON_LEFT and clicks>=up1cost:
                    clicks_power += 1
                    clicks-=up1cost
                    up1cost*=constant1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and clicks>=up1cost:
                    clicks_power += 1
                    clicks-=up1cost
                    up1cost*=constant1
            if event.type == pygame.MOUSEBUTTONDOWN and up2_rect.collidepoint(event.pos):
                if event.button == pygame.BUTTON_LEFT and clicks>=up2cost:
                      clicks_power += 10
                      clicks-=up2cost
                      up2cost*=constant1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2 and clicks>=up2cost:
                      clicks_power += 10
                      clicks-=up2cost
                      up2cost*=constant1
            if event.type == pygame.MOUSEBUTTONDOWN and up3_rect.collidepoint(event.pos):
                if event.button == pygame.BUTTON_LEFT and clicks>=up3cost:
                      clicks_power += 1000
                      clicks-=up3cost
                      up3cost*=constant1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3 and clicks>=up3cost:
                      clicks_power += 1000
                      clicks-=up3cost
                      up3cost*=constant1
            if event.type == pygame.MOUSEBUTTONDOWN and up4_rect.collidepoint(event.pos):
                if event.button == pygame.BUTTON_LEFT and clicks>=up4cost:
                      clicks_power += 10000
                      clicks-=up4cost
                      up4cost*=constant4
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4 and clicks>=up4cost:
                      clicks_power += 10000
                      clicks-=up4cost
                      up4cost*=constant4
                
        pygame.display.update()
#цикл меню улучшений колва RP/reality с двумя функциональными кнопками и кнопкой назад в меню простоя
def rp_upg_menu():
    while True:
        global rps, rpsmp, rp1upcost, rp2upcost, rp3upcost
        main_screen.blit(rp_up_bg, (0, 0))
        RP_UPG_MOUSE_POS = pygame.mouse.get_pos()
        RP_BACK = Button(image=None, pos=(400, 125),
                             text_input="Back to timeless menu", font=get_font_arial(45), base_color ="White", hovering_color="Blue")
        RP_BACK.changeColor(RP_UPG_MOUSE_POS)
        RP_BACK.update(main_screen)
        RPOINTS = get_font_arial(36).render("{} RP".format(rps), True, ("Blue"))
        main_screen.blit(RPOINTS, (350,50))
        RP_UPGRADE_ONE_RECT = pygame.rect.Rect(93, 290, 255, 100)
        pygame.draw.rect(main_screen, (26, 26, 26), RP_UPGRADE_ONE_RECT)
        RP_UPGRADE_ONE_TEXT = get_font_mono(27).render("Reality booster", True, ("White"))
        RP_UPGRADE_ONE_TEXT2 = get_font_mono(27).render("(+1 rp/rlt)", True, ("White"))
        main_screen.blit(RP_UPGRADE_ONE_TEXT, (100, 300))
        main_screen.blit(RP_UPGRADE_ONE_TEXT2, (125, 328))
        RP_UPGRADE_ONE_COST = get_font_mono(27).render("{} RP ".format(round(rp1upcost)), True, ("White"))
        main_screen.blit(RP_UPGRADE_ONE_COST, (185, 360))
        RP_UPGRADE_TWO_RECT = pygame.rect.Rect(455, 290, 255, 100)
        pygame.draw.rect(main_screen, (26, 26, 26), RP_UPGRADE_TWO_RECT)
        RP_UPGRADE_TWO_TEXT = get_font_mono(22).render("Reality accelerator", True, ("White"))
        RP_UPGRADE_TWO_TEXT2 = get_font_mono(27).render("(+5 rp/rlt)", True, ("White"))
        main_screen.blit(RP_UPGRADE_TWO_TEXT, (462, 300))
        main_screen.blit(RP_UPGRADE_TWO_TEXT2, (492, 328))
        RP_UPGRADE_TWO_COST = get_font_mono(27).render("{} RP ".format(round(rp2upcost)), True, ("White"))
        main_screen.blit(RP_UPGRADE_TWO_COST, (542, 360))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #если кнопка назад нажата то перебрасывает в меню простоя 
                if RP_BACK.checkForInput(RP_UPG_MOUSE_POS):
                    restart()
            if event.type == pygame.MOUSEBUTTONDOWN and RP_UPGRADE_ONE_RECT.collidepoint(event.pos) and rps>=rp1upcost:
                if event.button == pygame.BUTTON_LEFT:
                    rps-=rp1upcost
                    rpsmp += 1
                    rp1upcost += 1
            if event.type == pygame.MOUSEBUTTONDOWN and RP_UPGRADE_TWO_RECT.collidepoint(event.pos) and rps>=rp2upcost:
                if event.button == pygame.BUTTON_LEFT:
                    rps-=rp2upcost
                    rpsmp += 5
                    rp2upcost += 5
        pygame.display.update()
#цикл меню простоя-обнуления игры с 2 кнопками разных видов обнуления а также кнопкой переброса на экран меню улучшений rp/reality
def restart():
    while True:
        global clicks, clicks_power, up1cost, up2cost, up3cost, up4cost, rp1upcost, rp2upcost, rps, rpsmp, restart_cost, bhs
        main_screen.blit(res_bg, (0, 0))
        RESTART_MOUSE_POS = pygame.mouse.get_pos()
        RPOINTS = get_font_arial(36).render("{} RP".format(rps), True, ("Blue"))
        main_screen.blit(RPOINTS, (350, 50))
        RESTART_BUTTON = Button(image=None, pos=(400,150),
                                text_input=("ABSORB REALITY (+{}RP)".format(rpsmp)), font=get_font_mono(36), base_color=("White"), hovering_color="Blue")
        RESTART_BUTTON.changeColor(RESTART_MOUSE_POS)
        RESTART_BUTTON.update(main_screen)
        BLACKHOLE_BUTTON = Button(image=None, pos=(400,350),
                                  text_input="CREATE BLACKHOLE (100RP)", font=get_font_mono(36), base_color=("White"), hovering_color=(0, 50, 255))
        BLACKHOLE_BUTTON.changeColor(RESTART_MOUSE_POS)
        BLACKHOLE_BUTTON.update(main_screen)

        RP_UPGRADE_RECT = pygame.rect.Rect(272, 200, 255, 100)
        pygame.draw.rect(main_screen, (26, 26, 26), RP_UPGRADE_RECT)
        RP_UPGRADE_TEXT = get_font_mono(27).render("Reality upgrades", True, ("White"))
        main_screen.blit(RP_UPGRADE_TEXT, (272, 232))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #частичное обнуление (reality), сброс параметров и добавление валюты RP к счетчику а также повышение цены на новое обнуление
                if RESTART_BUTTON.checkForInput(RESTART_MOUSE_POS):
                    rps+=rpsmp
                    restart_cost*=constant5
                    clicks=0
                    clicks_power=1
                    up1cost=1
                    up2cost=100
                    up3cost=5000
                    up4cost=100000
                    game()
            if event.type == pygame.MOUSEBUTTONDOWN and rps>=100: #полное обнуление (blackholes) (будет в следующих обновлениях), пока нет функционала, вызывает финальный экран
                if BLACKHOLE_BUTTON.checkForInput(RESTART_MOUSE_POS):
                    bhs+=1
                    clicks=0
                    rps=0
                    clicks_power=1
                    rpsmp=1
                    up1cost=1
                    up2cost=100
                    up3cost=5000
                    up4cost=100000
                    rp1upcost=1
                    rp2upcost=10
                    end_game()
            if event.type == pygame.MOUSEBUTTONDOWN: #вызов экрана меню улучшений RP/reality
                if event.button == pygame.BUTTON_LEFT and RP_UPGRADE_RECT.collidepoint(event.pos):
                    rp_upg_menu()        
        pygame.display.update()
#функция квестов в игре        
def current_goal():
    goal1 = "click 1 time"
    if clicks==0 and rps==0:
        return goal1
    goal2 = "score 1000 clicks"
    if clicks<1000 and rps==0:
        return goal2
    goal3 = "reach reality"
    if rps<=99:
        return goal3
    goal4 = "create ???"
    if rps<=100 and rps>=1:
        return goal4
    goal5 = "Witness what you did"
    if rps>100:
        return goal5
gamename = get_font_mono(45).render("TimelessIdle", True, (0, 0, 255)) #название игры в текстовом виде
#функция финального экрана
def titles():
    while True:
        TITLE_MOUSE_POS = pygame.mouse.get_pos()
        main_screen.fill((0, 0, 0))
        TITLE1 = get_font_arial(45).render("Thanks for playing                                 alpha", True, ("White"))
        clicklol = Button(image=None, pos=(750, 775),
                          text_input="click", font=get_font_mono(25), base_color=(20, 20, 20), hovering_color="Black")
        clicklol.changeColor(TITLE_MOUSE_POS)
        clicklol.update(main_screen)
        main_screen.blit(TITLE1, (50, 250))
        main_screen.blit(gamename, (355, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if pygame.MOUSEBUTTONDOWN: #пасхалко       
            if clicklol.checkForInput(TITLE_MOUSE_POS):
                main_screen.fill((255, 0, 0))
                lol = get_font_arial(45).render("click the close lol", True, "Black")
                main_screen.blit(lol, (275, 300))
                pygame.display.flip()
                main_screen.fill((0, 255, 0))
                main_screen.blit(lol, (275, 300))
                pygame.display.flip()
                main_screen.fill((0, 0, 255))
                main_screen.blit(lol, (275, 300))
                pygame.display.flip()    
                main_screen.fill((255, 255, 255))
                pygame.display.flip()
                    
        pygame.display.update()
#экран конца игры                            
def end_game():
    while True:
        main_screen.fill((0, 0, 0))
        main_screen.blit(bh_bg, (0, 0))
        END_MOUSE_POS = pygame.mouse.get_pos()
        END_TEXT = get_font_arial(55).render("And it consumes everything...", True, "White")
        main_screen.blit(END_TEXT, (100,250))
        END = Button(image=None, pos=(375, 400),
                text_input="The End.", font=get_font_arial(36), base_color="White", hovering_color="Blue")
        END.changeColor(END_MOUSE_POS)
        END.update(main_screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if END.checkForInput(END_MOUSE_POS):
                    titles()   
        pygame.display.update()

#функция обновления колва RP и restart_cost
def rpupdate():
    RPOINTS = get_font_arial(36).render("{} RP".format(rps), True, ("Blue"))
    main_screen.blit(RPOINTS, (700, 25))
    RESTART_COST = get_font_arial(36).render("{} clicks ".format(shorten_number(round(restart_cost))), True, ("White"))
    main_screen.blit(RESTART_COST, (20, 75))
    pygame.display.update()
#основной цикл игры на котором кнопка-кликер, кнопка перехода в экран улучшений и отображение некоторых параметров на экране
def game():
    while True:
        global clicks, goal, rps
        main_screen.blit(bg, (0, 0))
        goal = get_font_arial(36).render("{}".format(current_goal()), True, ("White"))
        main_screen.blit(goal, (15, 25))
        GAME_MOUSE_POS = pygame.mouse.get_pos()
        CLICK_TEXT = get_font_arial(36).render((("{}".format(shorten_number(round(clicks))))), True, (255, 255, 255))
        main_screen.blit(CLICK_TEXT, (390, 25))

        button = pygame.image.load('C:/Users/79835/Documents/TimelessIdle/images/hourglass.png')
        button = pygame.transform.scale(button, (325, 350))
        main_screen.blit(button, (235, 125))

        UPMENU_BUTTON = Button(image=pygame.image.load("C:/Users/79835/Documents/TimelessIdle/images/Quit Rect.png"), pos=(400, 600), 
                               text_input="Up menu", font=get_font_mono(45), base_color=("Black"), hovering_color="Blue") #кнопка перехода на экран улучшений клика
        CLICKS_ADDER = pygame.Rect(310, 125, 175, 350) #кнопка-кликер
        #цикл обновления цвета и кнопки из списка
        for buttons in [UPMENU_BUTTON]:
            buttons.changeColor(GAME_MOUSE_POS)
            buttons.update(main_screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #переход на экран улучшений клика
                if UPMENU_BUTTON.checkForInput(GAME_MOUSE_POS):
                    upgrademenu()
            if event.type == pygame.MOUSEBUTTONDOWN and CLICKS_ADDER.collidepoint(event.pos): #работа кнопки-кликера
                if event.button == pygame.BUTTON_LEFT:
                     clicks+=clicks_power
            if clicks>=restart_cost: #переход в меню простоя если колво кликов больше цены обнуления (возможно будет в виде кнопки в будущем)
                restart()
        if rps>=1: #обновление RPs и цены на Reality если RP>1
            rpupdate()
        pygame.display.update() 
game()
end_game()
