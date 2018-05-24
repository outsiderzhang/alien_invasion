import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
	"""一个对飞船发射的子弹管理的类"""
	def __init__(self, screen, ai_settings, ship):
		super(Bullet, self).__init__()
		
		# 屏幕
		self.screen = screen

		# 在(0, 0)处创建一个表示子弹的矩形, 在设置正确的位置
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# 存储小数表示子弹的位置
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed = ai_settings.bullet_speed_factor

	def update(self):
		"""向上移动子弹"""
		# 更新表示子弹位置的小数值
		self.y -= self.speed
		# 更新表示子弹的rect小数值
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)




		