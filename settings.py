class Settings():
	def __init__(self):
		#设置屏幕
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		#船的属性
		self.ship_speed_factor = 1
		self.ship_limit = 3

		#外星人的属性
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction为1表示向右移动，为-1表示向左移动
		self.fleet_direction = 1
		
		#子弹的属性
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60 ,60
		self.bullets_allow = 5
