import sys
import pygame
from bullet import Bullet
def check_keydown_events(event, screen, ai_settings, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(screen, ai_settings, ship, bullets)

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def fire_bullet(screen, ai_settings, ship, bullets):
	"""如果还没到达限制, 就发射一颗子弹"""

	# 限制判断后, 创建新子弹并加入到编组bullets中
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(screen, ai_settings, ship)
		bullets.add(new_bullet)

def check_events(screen, ai_settings, ship, bullets):
	"""响应键盘和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			print(event.key)
			check_keydown_events(event, screen, ai_settings, ship, bullets)
		elif event.type == pygame.KEYUP:
			print(event.key)
			check_keyup_events(event, ship)

def update_ship(ship):
	"""更新飞船位置"""

	# 更新位置
	ship.update()

def update_bullets(bullets):
	"""更新子弹位置, 并删除消失的子弹"""

	# 更新子弹位置
	bullets.update()

	# 更新后删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def update_screen(screen, ai_settings, ship, bullets):
	"""更新屏幕上的图像,并切换到新屏幕"""
	# 每次循环都重绘屏幕
	screen.fill(ai_settings.bg_color)

	# 将更新位置后的飞船绘制都屏幕上
	ship.blitme()

	# 将更新位置后的子弹绘制到屏幕
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	# 让最近绘制的屏幕可见
	pygame.display.flip()


