import pygame
from pygame.sprite import Group
from ship import Ship
from bullet import Bullet
from alien import Alien
import game_function as gf
from settings import Settings
from game_stats import Gamestats
from button import Button


def run_game():	
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#创建一个用于储存游戏统计信息的实例
	stats =Gamestats(ai_settings)

	#创建一艘飞船
	ship = Ship(ai_settings, screen)

	#创建一个用于存储子弹的编组
	bullets = pygame.sprite.Group()

	#创建一个外星人的编组
	aliens = Group()
	#创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#创建Play按钮
	play_button = Button(ai_settings, screen, "Play")

	#开始游戏的主循环
	while True:
		gf.check_events(ai_settings, screen, stats, play_button, ship,
			aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
			play_button)
		
		
	
run_game()
