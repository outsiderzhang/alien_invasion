import pygame

class Ship():
	"""docstring for Ship"""
	def __init__(self, screen, ai_setting):

		# 是否在移动
		self.moving_right = False
		self.moving_left = False

		# 移动速度
		self.ai_setting = ai_setting

		# 屏幕初始设置
		self.screen = screen
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# 飞船在底部中间
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# 飞船属性center中存储小数值
		self.center = float(self.rect.centerx)

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""根据移动调整飞船位置"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_setting.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_setting.ship_speed_factor
		self.rect.centerx = self.center
		print("x:" + str(self.rect.centerx))





