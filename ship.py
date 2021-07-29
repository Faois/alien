import pygame

class Ship():
	def __init__(self, ai_setting, screen):
		self.screen = screen
		self.ai_settings = ai_setting
		
		#加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#将每艘新飞船放在屏幕底部正中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#在飞船属性center中存储小数
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		self.bottom = float(self.rect.bottom)

		#移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def center_ship(self):
		"""让飞船在屏幕上居中"""
		self.centerx = self.screen_rect.centerx
		self.centery = self.screen_rect.bottom - int(self.rect.height)/2

	def update(self):
		if (self.moving_right 
			and self.rect.right < self.screen_rect.right):
			self.centerx += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_settings.ship_speed_factor
		self.rect.centerx = self.centerx
		
		if self.moving_up and self.rect.top > 0:
			self.centery -= self.ai_settings.ship_speed_factor
		if (self.moving_down
			and self.rect.bottom < self.screen_rect.bottom):
			self.centery += self.ai_settings.ship_speed_factor
		self.rect.centery = self.centery
	

	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
