# castles_war_constants.py
"""
Collection of the main constants defined for the
"Castles war" project.

Values can be modified according to the sprites used or the
game dynamics rule designed.

---
v 1.00
Stefano Ferrari
2022-01-26
"""

### Game constants

INIT_RESOURCES = 10  # initial amount of resources

# geometry
SCREEN_WIDTH = 1000  # width of the game window
SCREEN_HEIGHT = 250  # height of the game window
WALL_POS = 180  # horizontal coordinate of the center of the wall
WALL_WIDTH = 62  # width of the wall
WALL_HEIGHT = 80  # height of the wall
MINE_POS = 40  # horizontal coordinate of the center of the mine
MINE_WIDTH = 58  # width of the mine
MINE_HEIGHT = 37  # height of the mine
BARRACKS_POS = 106  # horizontal coordinate of the center of the barracks
BARRACKS_WIDTH = 62  # width of the barracks
BARRACKS_HEIGHT = 50  # height of the mine
TOWER_HEIGHT = 160  # height of the tower
GROUND_HEIGHT = 14  # height of the ground

BORDER = 10  # minimum distance of the buildings from the border
BUILDING_SEP = 5  # minimum distance between the buildings

### Units constants

# Worker
WORKER_COST = 5  # amount of resources to train a new worker
WORKER_TRAIN = 10  # amount of turns to train a new worker
WORKER_SPEED = 2  # distance covered in one turn by a running worker
WORKER_PROD = 1  # amount of resources per turn mined by a worker in mine
WORKER_REPAIR = 2  # amount of HP restored per turn by a worker in wall

# Swordsman
SWORD_COST = 20  # amount of resources to train a new swordsman
SWORD_TRAIN = 20  # amount of turns to train a new swordsman
SWORD_SPEED = 2  # distance covered in one turn by a running swordsman
SWORD_RANGE = 10  # maximum distance at which a swordsman can hit an unit
SWORD_HIT = 1  # damage caused by of a swordsman per turn
SWORD_REST = 10  # amount of turns of inactivity of a swordman after an attack
SWORD_HEALTH = 40  # initial amount of HP of a swordsman

# Archer
ARCHER_COST = 25  # amount of resources to train a new archer
ARCHER_TRAIN = 20  # amount of turns to train a new archer
ARCHER_SPEED = 2  # distance covered in one turn by a running archer
ARCHER_RANGE = 200  # maximum distance at which an archer can send an arrow
ARCHER_REST = 30  # amount of turns of inactivity of an archer after shooting
ARCHER_HEALTH = 100  # initial amount of HP of an archer
ARCHER_HIT = 10  # damage caused by of an arrow shoot by an archer
ARCHER_POS = BARRACKS_POS
# Arrow
ARROW_SPEED = 3  # distance covered in one turn by an arrow

### Buildings constants

# Wall
WALL_HEALTH = 1000  # maximum amount of HP af the wall

# Tower
TOWER_RANGE = 220  # maximum distance at which the tower can send an arrow
TOWER_HIT = 5  # damage caused by of an arrow shoot by the tower
TOWER_REST = 30  # amount of turns of inactivity of the tower after shooting


# Keybord commands
PL1_WORKER_TRAIN = 'q'
PL1_SWORD_TRAIN = 'w'
PL1_ARCHER_TRAIN = 'e'
PL1_TO_MINE = 'a'
PL1_TO_WALL = 's'
PL1_SWORD_ATTACK = 'd'
PL1_ARCHER = 'f'
PL1_UNLEASH = 'z'

PL2_WORKER_TRAIN = 'p'
PL2_SWORD_TRAIN = 'o'
PL2_ARCHER_TRAIN = 'i'
PL2_TO_MINE = 'l'
PL2_TO_WALL = 'k'
PL2_SWORD_ATTACK = 'j'
PL2_ARCHER = 'h'
PL2_UNLEASH = 'm'

PAUSE = ' '
SAVE = 'V'
LOAD = 'B'
