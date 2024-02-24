from sys import exit
from swordsman import *
from worker import *
from archer import *
from random import randint as r
from building import *
from arrows import *
import pygame

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
menu_screen = pygame.transform.scale(pygame.image.load('images/background/aquila.jpg'), (1000, 250))
pygame.display.set_caption('CastleWars')

# font
title_font = pygame.font.Font('images/font/Pixeltype.ttf', 75)
screen_font = pygame.font.Font('images/font/Pixeltype.ttf', 40)
small_test_font = pygame.font.Font('images/font/Pixeltype.ttf', 25)

clock = pygame.time.Clock()

# background and ground
background = pygame.transform.scale(pygame.image.load('images/background/aquila.jpg'), (1000, 250))
ground = pygame.transform.scale(pygame.image.load('images/background/good_ground.png'), (1000, 250))
ground_below = pygame.image.load('images/background/good_ground.png')

# Groups
red_swordsmen_army = pygame.sprite.Group()
blue_swordsmen_army = pygame.sprite.Group()
red_archers_army = pygame.sprite.Group()
blue_archers_army = pygame.sprite.Group()
red_workers_army = pygame.sprite.Group()
blue_workers_army = pygame.sprite.Group()

red_archer_arrows = pygame.sprite.Group()
blue_archer_arrows = pygame.sprite.Group()
red_tower_arrows = pygame.sprite.Group()
blue_tower_arrows = pygame.sprite.Group()

# Adding buildings
red_mine = Building(pygame.image.load('images/player1/building/mine.png'), MINE_POS, SCREEN_HEIGHT - GROUND_HEIGHT)
blue_mine = Building(pygame.image.load('images/player2/building/mine.png'), 1000 - MINE_POS,
                     SCREEN_HEIGHT - GROUND_HEIGHT)
red_barracks = Building(pygame.image.load('images/player1/building/barracks.png'), BARRACKS_POS,
                        SCREEN_HEIGHT - GROUND_HEIGHT)
blue_barracks = Building(pygame.image.load('images/player2/building/barracks.png'), 1000 - BARRACKS_POS,
                         SCREEN_HEIGHT - GROUND_HEIGHT)
red_tower = Building(pygame.image.load('images/player1/building/tower.png'), WALL_POS, SCREEN_HEIGHT - GROUND_HEIGHT)
red_wall = Building(pygame.image.load('images/player1/building/wall.png'), WALL_POS, SCREEN_HEIGHT - GROUND_HEIGHT)

blue_tower = Building(pygame.image.load('images/player2/building/tower.png'), 1000 - WALL_POS,
                      SCREEN_HEIGHT - GROUND_HEIGHT)
blue_wall = Building(pygame.image.load('images/player2/building/wall.png'), 1000 - WALL_POS,
                     SCREEN_HEIGHT - GROUND_HEIGHT)


def menu_display():
    game_title_surf = title_font.render('CastleWars', False, 'Black')
    game_title_rect = game_title_surf.get_rect(center=(500, 50))
    screen.blit(game_title_surf, game_title_rect)

    start_surf = screen_font.render('To start the game press "enter" ...', False, 'Black')
    start_rect = start_surf.get_rect(center=(500, 200))
    screen.blit(start_surf, start_rect)


def group_display_update():
    # display the buildings for player 2
    blue_mine.draw(screen)
    blue_barracks.draw(screen)
    blue_tower.draw(screen)
    blue_wall.draw(screen)

    # display the arrows for player 2
    red_archer_arrows.update()
    red_archer_arrows.draw(screen)
    red_tower_arrows.update()
    red_tower_arrows.draw(screen)

    # display the armies for player 2
    red_swordsmen_army.update()
    red_swordsmen_army.draw(screen)
    red_archers_army.update()
    red_archers_army.draw(screen)
    red_workers_army.update()
    red_workers_army.draw(screen)


    # display the buildings for player 1
    red_mine.draw(screen)
    red_barracks.draw(screen)
    red_tower.draw(screen)
    red_wall.draw(screen)

    # display the armies for player 1
    blue_swordsmen_army.update()
    blue_swordsmen_army.draw(screen)
    blue_archers_army.update()
    blue_archers_army.draw(screen)
    blue_workers_army.update()
    blue_workers_army.draw(screen)

    # display the arrows for player 1
    blue_archer_arrows.update()
    blue_archer_arrows.draw(screen)
    blue_tower_arrows.update()
    blue_tower_arrows.draw(screen)



def text(data, swordsmen1_army, swordsman2_text, worker1_army, worker2_army, archer1_army, archer2_army):
    swordsman1_text = small_test_font.render('Swordsmen: ' + str(len(swordsmen1_army)), False, 'WHITE')
    swordsman1_rect = swordsman1_text.get_rect(topleft=(10, 10))

    swordsman2_text = small_test_font.render('Swordsmen: ' + str(len(blue_swordsmen_army)), False, 'WHITE')
    swordsman2_rect = swordsman1_text.get_rect(topright=(960, 10))

    archer1_text = small_test_font.render('Archers: ' + str(len(archer1_army)), False, 'WHITE')
    archer1_rect = archer1_text.get_rect(topleft=(10, 25))

    archer2_text = small_test_font.render('Archers: ' + str(len(archer2_army)), False, 'WHITE')
    archer2_rect = archer2_text.get_rect(topright=(960, 25))

    worker1_text = small_test_font.render('Workers: ' + str(len(worker1_army)), False, 'WHITE')
    worker1_rect = worker1_text.get_rect(topleft=(10, 40))

    worker2_text = small_test_font.render('Workers: ' + str(len(worker2_army)), False, 'WHITE')
    worker2_rect = worker2_text.get_rect(topright=(960, 40))

    wall1_text = small_test_font.render(f'WALL HEALTH: {int(data["p1_wallhealth"])}', False, 'WHITE')
    wall1_rect = wall1_text.get_rect(topleft=(10, 55))

    wall2_text = small_test_font.render(f'WALL HEALTH: {int(data["p2_wallhealth"])}', False, 'WHITE')
    wall2_rect = wall2_text.get_rect(topright=(960, 55))

    p1_resource_text = small_test_font.render(f'RESOURCES: {int(data["p1_resources"])}', False, 'Pink')
    p1_resource_rect = p1_resource_text.get_rect(topleft=(10, 70))

    p2_resource_text = small_test_font.render(f'RESOURCES: {int(data["p2_resources"])}', False, 'Pink')
    p2_resource_rect = p2_resource_text.get_rect(topright=(960, 70))

    screen.blit(swordsman1_text, swordsman1_rect)
    screen.blit(swordsman2_text, swordsman2_rect)

    screen.blit(archer1_text, archer1_rect)
    screen.blit(archer2_text, archer2_rect)

    screen.blit(worker1_text, worker1_rect)
    screen.blit(worker2_text, worker2_rect)

    screen.blit(wall1_text, wall1_rect)
    screen.blit(wall2_text, wall2_rect)

    screen.blit(p1_resource_text, p1_resource_rect)
    screen.blit(p2_resource_text, p2_resource_rect)


def resume():
    playagain_surf = screen_font.render('To resume the game press "space" ...', False, 'Black')
    playagain_rect = playagain_surf.get_rect(center=(500, 125))
    screen.blit(playagain_surf, playagain_rect)
    pygame.display.update()

    resume = True
    while resume:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    resume = False
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


# worker collision
def workers_collision(workers, mine, wall, player):
    global data
    for worker in workers:
        # worker collision to mine
        if pygame.sprite.collide_rect(mine, worker):
            worker.dig = True
            if player == 1:
                data['p1_resources'] += WORKER_PROD / 20
                if data['p1_resources'] >= 200:
                    data['p1_resources'] = 200
                    return data['p1_resources']
            elif player == 2:
                data['p2_resources'] += WORKER_PROD / 20
                if data['p2_resources'] >= 200:
                    data['p2_resources'] = 200
                    return data['p2_resources']

    for worker in workers:
        # worker collision to wall
        if pygame.sprite.collide_rect(worker, wall):
            worker.repair = True
            if player == 1:
                data['p1_wallhealth'] += WORKER_REPAIR / 100

            elif player == 2:
                data['p2_wallhealth'] += WORKER_PROD / 100


# swordsmen collision
def swordsmen_collision(friendly_swordsmen, enemy_swordsmen, enemy_walls, enemy_archers, player):
    global data
    for swordsman in friendly_swordsmen:
        # swordsman attacking enemy swordsman
        colliding_sword = pygame.sprite.spritecollideany(swordsman, enemy_swordsmen)
        if colliding_sword:
            swordsman.attacking = True
            swordsman.unleash = False
            if swordsman.index == 3:
                colliding_sword.health -= SWORD_HIT
        # swordsman attacking enemy archer
        colliding_arch = pygame.sprite.spritecollideany(swordsman, enemy_archers)
        if colliding_arch:
            swordsman.attacking = True
            swordsman.unleash = False
            if swordsman.index == 3:
                colliding_arch.health -= SWORD_HIT
        # swordsman attacking enemy wall
        colliding_wall = pygame.sprite.collide_rect(swordsman, enemy_walls)
        if colliding_wall:
            swordsman.attacking = True
            swordsman.unleash = False
            if swordsman.index == 3:
                if player == 1:
                    data['p1_wallhealth'] -= SWORD_HIT
                    return data['p1_wallhealth']
                else:
                    data['p2_wallhealth'] -= SWORD_HIT
                    return data['p2_wallhealth']

        # restrictions for running
        if not (colliding_sword or colliding_arch or colliding_wall) and (
                swordsman.rect.x >= WALL_POS and swordsman.rect.x <= 1000 - WALL_POS):
            swordsman.attack = False
            swordsman.unleash = True


# archer collision
def archer_collision(archers, enemy_archers, enemy_swordsmen, enemy_walls, archer_arrows, a_arrow, player):
    global data
    # archer attacking enemy armies
    for archer in archers:
        # archer attacking enemy soldiers
        for enemy_soldier in enemy_swordsmen:
            archer_range1 = abs(enemy_soldier.rect.x - archer.rect.x)
            if archer_range1 <= ARCHER_RANGE:
                archer.shoot = True
                archer.unleash = False
                if archer.index == 3:
                    archer_arrows.add(Archer_Arrow(a_arrow1, archer.rect.x, player))
                break
            elif enemy_soldier.health <= 0:
                archer.unleash = True
                archer.shoot = False

        # archer attacking enemy archers
        for enemy_archer in enemy_archers:
            archer_range2 = abs(enemy_archer.rect.x - archer.rect.x)
            if archer_range2 <= ARCHER_RANGE:
                archer.shoot = True
                archer.unleash = False
                if archer.index == 1:
                    archer_arrows.add(Archer_Arrow(a_arrow, archer.rect.x, player))
                break
            elif enemy_archer.health <= 0:
                archer.unleash = True
                archer.shoot = False

    for arrow in archer_arrows:
        # arrow damaging enemy swordsmen
        enemy_swordsman_collision = pygame.sprite.spritecollideany(arrow, enemy_swordsmen)
        if enemy_swordsman_collision:
            enemy_swordsman_collision.health -= ARCHER_HIT
            arrow.kill()
        # arrow damaging enemy wall
        enemy_wall_collision = pygame.sprite.spritecollideany(arrow, enemy_walls)
        if enemy_wall_collision:
            if player == 1:
                data['p2_wallhealth'] -= ARCHER_HIT
                arrow.kill()
                return data['p2_wallhealth']
            else:
                data['p1_wallhealth'] -= ARCHER_HIT
                arrow.kill()
                return data['p1_wallhealth']

        # arrow damaging enemy archers
        enemy_archer_collision = pygame.sprite.spritecollideany(arrow, enemy_archers)
        if enemy_archer_collision:
            enemy_archer_collision.health -= ARCHER_HIT
            arrow.kill()


# tower shooting
def tower_shooting(tower, tower_range, arrow, x, tower_arrows, enemy_swordsmen, enemy_archers, player):
    # Tower1 Archer2
    for enemy_archer in enemy_archers:
        if enemy_archer.rect.x in tower_range:
            tower_arrows.add(Tower_Arrow(arrow, x, TOWER_HEIGHT, ARROW_SPEED, ARROW_SPEED, player))
            break

    for enemy_swordsman in enemy_swordsmen:
        if enemy_swordsman.rect.x in tower_range:
            tower_arrows.add(Tower_Arrow(arrow, x, TOWER_HEIGHT, ARROW_SPEED, ARROW_SPEED, player))
            break


    for tower_arrow in tower_arrows:
        enemy_archer_collision = pygame.sprite.spritecollideany(tower_arrow, enemy_archers)
        if enemy_archer_collision or tower_arrow.rect.x <= GROUND_HEIGHT:
            enemy_archer_collision.health -= TOWER_HIT
            tower_arrow.kill()
        enemy_swordsmen_collision = pygame.sprite.spritecollideany(tower_arrow, enemy_swordsmen)
        if enemy_swordsmen_collision or tower_arrow.rect.x <= GROUND_HEIGHT:
            enemy_swordsmen_collision.health -= TOWER_HIT
            tower_arrow.kill()


# data
data = {'p1_resources': INIT_RESOURCES, 'p2_resources': INIT_RESOURCES, 'p1_wallhealth': WALL_HEALTH,
        'p2_wallhealth': WALL_HEALTH}

# Main loop
game_active = False

while True:
    if game_active == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                # Stop and resume
                if event.key == pygame.K_SPACE:
                    resume()
                # Spawning P1 Units
                if event.key == pygame.K_w and data['p1_resources'] >= SWORD_COST and len(red_swordsmen_army) < 30:
                    red_swordsman = Swordsman(swordsman1_ready, swordsman1_run, swordsman1_attack, swordsmasn1_dead,
                                              r(55, 157), 1)
                    red_swordsmen_army.add(red_swordsman)
                    data['p1_resources'] -= SWORD_COST
                if event.key == pygame.K_q and data['p1_resources'] >= WORKER_COST:
                    red_worker = Worker(worker1_ready, worker1_run_left, worker1_run_right, worker1_dig, worker1_repair,
                                        r(75, 130))
                    red_workers_army.add(red_worker)
                    data['p1_resources'] -= WORKER_COST
                if event.key == pygame.K_e and data['p1_resources'] >= ARCHER_COST and len(red_archers_army) < 30:
                    red_archer = Archer(archer1_ready, archer1_run, archer1_shoot, archer1_dead, r(65, 167), 1)
                    red_archers_army.add(red_archer)
                    data['p1_resources'] -= ARCHER_COST
                # Unleash P1 Units separately
                if event.key == pygame.K_d:
                    for swordsman in red_swordsmen_army:
                        swordsman.unleash = True
                if event.key == pygame.K_f:
                    for archer in red_archers_army:
                        archer.unleash = True
                # Unleash P1 Units together
                if event.key == pygame.K_z:
                    for swordsman in red_swordsmen_army:
                        swordsman.unleash = True
                    for archer in red_archers_army:
                        archer.unleash = True
                # Worker movement
                if event.key == pygame.K_a:
                    for red_worker in red_workers_army:
                        if not red_worker.run_right:
                            red_worker.run_left = True

                if event.key == pygame.K_s:
                    for red_worker in red_workers_army:
                        if not red_worker.run_left:
                            red_worker.run_right = True

                # Spawning P2 Units
                if event.key == pygame.K_o and data['p2_resources'] >= SWORD_COST and len(blue_swordsmen_army) < 30:
                    blue_swordsman = Swordsman(swordsman2_ready, swordsman2_run, swordsman2_attack, swordsman2_dead,
                                               1000 - r(55, 157), 2)
                    blue_swordsmen_army.add(blue_swordsman)
                    data['p2_resources'] -= SWORD_COST
                if event.key == pygame.K_p and data['p2_resources'] >= WORKER_COST:
                    blue_worker = Worker(worker2_ready, worker2_run_left, worker2_run_right, worker2_dig,
                                         worker2_repair,
                                         1000 - randint(75, 130))
                    blue_workers_army.add(blue_worker)
                    data['p2_resources'] -= WORKER_COST
                if event.key == pygame.K_i and data['p2_resources'] >= ARCHER_COST and len(blue_archers_army) < 30:
                    blue_archer = Archer(archer2_ready, archer2_run, archer2_shoot, archer2_dead,
                                         1000 - randint(65, 167), 2)
                    blue_archers_army.add(blue_archer)
                    data['p2_resources'] -= ARCHER_COST
                # Unleash P1 Units separately
                if event.key == pygame.K_j:
                    for swordsman in blue_swordsmen_army:
                        swordsman.unleash = True
                if event.key == pygame.K_h:
                    for archer in blue_archers_army:
                        archer.unleash = True
                # Unleash P1 Units together
                if event.key == pygame.K_m:
                    for swordsman in blue_swordsmen_army:
                        swordsman.unleash = True
                    for archer in blue_archers_army:
                        archer.unleash = True
                # Worker movement
                if event.key == pygame.K_k:
                    for blue_worker in blue_workers_army:
                        if not blue_worker.run_right:
                            blue_worker.run_left = True
                if event.key == pygame.K_l:
                    for blue_worker in blue_workers_army:
                        if not blue_worker.run_left:
                            blue_worker.run_right = True

        # stabilize max wall health
        if data['p1_wallhealth'] >= 1000:
            data['p1_wallhealth'] = 1000

        if data['p2_wallhealth'] >= 1000:
            data['p2_wallhealth'] = 1000

        if data['p1_wallhealth'] <= 0 or data['p2_wallhealth'] <= 0:
            game_active = False

        swordsmen_collision(red_swordsmen_army, blue_swordsmen_army, blue_wall, blue_archers_army, 2)
        swordsmen_collision(blue_swordsmen_army, red_swordsmen_army, red_wall, red_archers_army, 1)

        archer_collision(red_archers_army, blue_archers_army, blue_swordsmen_army, blue_wall, red_archer_arrows,
                         a_arrow1, 1)
        archer_collision(blue_archers_army, red_archers_army, red_swordsmen_army, red_wall, blue_archer_arrows,
                         a_arrow2, 2)

        workers_collision(red_workers_army, red_mine, red_wall, 1)
        workers_collision(blue_workers_army, blue_mine, blue_mine, 2)

        tower_shooting(red_tower, range(WALL_POS+50, WALL_POS+TOWER_RANGE), t_arrow1, WALL_POS, red_tower_arrows, blue_swordsmen_army,
                       blue_archers_army, 1)

        # Background
        screen.fill("BLACK")
        screen.blit(background, (0, 0))
        screen.blit(ground, (0, 250 - GROUND_HEIGHT))
        screen.blit(ground_below, (0, 250 - GROUND_HEIGHT))
        text(data, red_swordsmen_army, blue_swordsmen_army, red_workers_army, blue_workers_army, red_archers_army,
             blue_archers_army)
        # Groups draw and update
        group_display_update()


    elif game_active == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_active = True
                    data = {'p1_resources': INIT_RESOURCES, 'p2_resources': INIT_RESOURCES,
                            'p1_wallhealth': WALL_HEALTH, 'p2_wallhealth': WALL_HEALTH}
                    red_workers_army.empty()
                    blue_workers_army.empty()
                    red_archers_army.empty()
                    blue_archers_army.empty()
                    red_swordsmen_army.empty()
                    blue_swordsmen_army.empty()
                    red_archer_arrows.empty()
                    blue_archer_arrows.empty()
                    red_tower_arrows.empty()
                    blue_tower_arrows.empty()
        screen.blit(menu_screen, (0, 0))
        menu_display()
        if data["p1_wallhealth"] <= 0:
            blue_surf = screen_font.render("BLUE WINS!!!", False, "Blue")
            blue_rect = blue_surf.get_rect(center=(500, 125))
            screen.blit(blue_surf, blue_rect)
        if data["p2_wallhealth"] <= 0:
            red_surf = screen_font.render("RED WINS!!!", False, "Red")
            red_rect = red_surf.get_rect(center=(500, 125))
            screen.blit(red_surf, red_rect)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
