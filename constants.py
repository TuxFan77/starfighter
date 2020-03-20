# Global constants
# Screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Scaling
SPRITE_SCALING = 0.5
PLAYER_SHIP_SCALING = SPRITE_SCALING
ENEMY_SHIP_SCALING = SPRITE_SCALING

# Player ship motion properties
PLAYER_SHIP_THRUST = 0.3
PLAYER_SHIP_DRAG = 0.1
PLAYER_LASER_SPEED = 10

# Spritesheet properites
EXPLOSION_SPRITESHEET_COLUMNS = 4
EXPLOSION_SPRITESHEET_COUNT = 26
EXPLOSION_SPRITESHEET_WIDTH = 222
EXPLOSION_SPRITESHEET_HEIGHT = 222

# File paths
IMAGES_DIR = 'assets/images'
PLAYER_SPRITES_DIR = f'{IMAGES_DIR}/player_sprites'
ENEMY_SPRITES_DIR = f'{IMAGES_DIR}/enemy_sprites'
LASER_SPRITES_DIR = f'{IMAGES_DIR}/laser_sprites'
SPRITESHEETS_DIR = f'{IMAGES_DIR}/spritesheets'
PLAYER_SHIP_FILENAME = f'{PLAYER_SPRITES_DIR}/player_ship.png'
PLAYER_LASER_FILENAME = f'{LASER_SPRITES_DIR}/laserRed01.png'
ENEMY_LASER_FILENAME = f'{LASER_SPRITES_DIR}/laserBlue01.png'
EXPLOSION_FILENAME = f'{SPRITESHEETS_DIR}/explosion.png'
