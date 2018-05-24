import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
	# 初始化pygame,设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(screen, ai_settings)

	# 创建一个用于存储子弹的编组
	bullets = Group();
	#开始游戏的主循环	
	while True:

		# 监视键盘和鼠标事件
		gf.check_events(screen, ai_settings, ship, bullets)
		# 更新飞船位置
		gf.update_ship(ship)
		# 更新飞船位置, 并删除消失的子弹
		gf.update_bullets(bullets)
		# 更新后重绘屏幕
		gf.update_screen(screen, ai_settings, ship, bullets)

		
run_game()

		