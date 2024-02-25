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
menu_screen = pygame.transform.scale(pygame.image.load('images/background/aquila.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT))
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

# adding buildings for player 1
red_mine = Building(pygame.image.load('images/player1/building/mine.png'), MINE_POS, SCREEN_HEIGHT - GROUND_HEIGHT)
red_barracks = Building(pygame.image.load('images/player1/building/barracks.png'), BARRACKS_POS,
                        SCREEN_HEIGHT - GROUND_HEIGHT)
red_tower = Building(pygame.image.load('images/player1/building/tower.png'), WALL_POS, SCREEN_HEIGHT - GROUND_HEIGHT)
red_wall = Building(pygame.image.load('images/player1/building/wall.png'), WALL_POS, SCREEN_HEIGHT - GROUND_HEIGHT)

# adding buildings for player 2
blue_barracks = Building(pygame.image.load('images/player2/building/barracks.png'), 1000 - BARRACKS_POS,
                         SCREEN_HEIGHT - GROUND_HEIGHT)
blue_mine = Building(pygame.image.load('images/player2/building/mine.png'), 1000 - MINE_POS,
                     SCREEN_HEIGHT - GROUND_HEIGHT)
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

    # display the arrows for player 1
    red_archer_arrows.update()
    red_archer_arrows.draw(screen)
    red_tower_arrows.update()
    red_tower_arrows.draw(screen)

    # display the buildings for player 1
    red_mine.draw(screen)
    red_barracks.draw(screen)
    red_tower.draw(screen)
    red_wall.draw(screen)

    # display the armies for player 1
    red_swordsmen_army.update()
    red_swordsmen_army.draw(screen)
    red_archers_army.update()
    red_archers_army.draw(screen)
    red_workers_army.update()
    red_workers_army.draw(screen)

    # display the arrows for player 2
    blue_archer_arrows.update()
    blue_archer_arrows.draw(screen)
    blue_tower_arrows.update()
    blue_tower_arrows.draw(screen)

    # display the armies for player 2
    blue_swordsmen_army.update()
    blue_swordsmen_army.draw(screen)
    blue_archers_army.update()
    blue_archers_army.draw(screen)
    blue_workers_army.update()
    blue_workers_army.draw(screen)


def text(data, swordsmen1_army, swordsman2_text, worker1_army, worker2_army, archer1_army, archer2_army):
    swordsman1_text = small_test_font.render('Swordsmen: ' + str(len(swordsmen1_army)), False, 'WHITE')
    swordsman1_rect = swordsman1_text.get_rect(topleft=(10, 10))

    swordsman2_text = small_test_font.render('Swordsmen: ' + str(len(swordsman2_text)), False, 'WHITE')
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
    play_again_surf = screen_font.render('To resume the game press "space" ...', False, 'Black')
    play_again_rect = play_again_surf.get_rect(center=(500, 125))
    screen.blit(play_again_surf, play_again_rect)
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

    # Check collision between workers and mine
    for worker in workers:
        if pygame.sprite.collide_rect(mine, worker):
            # Worker starts digging
            worker.dig = True
            # Increase player resources based on player number
            if player == 1:
                data['p1_resources'] += WORKER_PROD / 20
            elif player == 2:
                data['p2_resources'] += WORKER_PROD / 20

    # Check collision between workers and wall
    for worker in workers:
        if pygame.sprite.collide_rect(worker, wall):
            # Worker starts repairing the wall
            worker.repair = True
            # Increase wall health based on player number
            if player == 1:
                data['p1_wallhealth'] += WORKER_REPAIR / 100
            elif player == 2:
                data['p2_wallhealth'] += WORKER_PROD / 100


# swordsmen collision
def swordsmen_collision(friendly_swordsmen, enemy_swordsmen, enemy_walls, enemy_archers, player):
    global data

    # Loop through each friendly swordsman
    for swordsman in friendly_swordsmen:
        # Check for collision with enemy swordsman
        colliding_sword = pygame.sprite.spritecollideany(swordsman, enemy_swordsmen)
        if colliding_sword:
            swordsman.attacking = True
            swordsman.unleash = False
            # If swordsman is index is 3 (able to attack)
            if swordsman.index == 3:
                # Decrease enemy swordsman health
                colliding_sword.health -= SWORD_HIT

        # Check for collision with enemy archer
        colliding_arch = pygame.sprite.spritecollideany(swordsman, enemy_archers)
        if colliding_arch:
            swordsman.attacking = True
            swordsman.unleash = False
            # If swordsman index is 3 (able to attack)
            if swordsman.index == 3:
                # Decrease enemy archer health
                colliding_arch.health -= SWORD_HIT

        # Check for collision with enemy wall
        colliding_wall = pygame.sprite.collide_rect(swordsman, enemy_walls)
        if colliding_wall:
            swordsman.attacking = True
            swordsman.unleash = False
            # If swordsman index is 3 (able to attack)
            if swordsman.index == 3:
                # Decrease enemy wall health based on player
                if player == 1:
                    data['p1_wallhealth'] -= SWORD_HIT
                else:
                    data['p2_wallhealth'] -= SWORD_HIT

        # Restrictions for movement
        if not (colliding_sword or colliding_arch or colliding_wall) and (
                swordsman.rect.x >= WALL_POS and swordsman.rect.x <= 1000 - WALL_POS):
            swordsman.attack = False
            swordsman.unleash = True


# archer collision

# Initialize the archer shoot cooldown
archer_shoot_cooldown = 0


def archer_collision(archers, enemy_archers, enemy_swordsmen, enemy_walls, archer_arrows, a_arrow, player):
    global archer_shoot_cooldown
    # Check if archer can shoot
    if archer_shoot_cooldown <= 0:
        # Iterate over archers
        for archer in archers:
            # archer attacking enemy soldiers
            for enemy_soldier in enemy_swordsmen:
                archer_range1 = abs(enemy_soldier.rect.x - archer.rect.x)
                if archer_range1 <= ARCHER_RANGE:
                    archer.shoot = True
                    archer.unleash = False
                    if archer.index >= 1:
                        archer_arrows.add(Archer_Arrow(a_arrow1, archer.rect.x, player))
                        # Set shoot cooldown
                        archer_shoot_cooldown = ARCHER_REST
                    break
                # If enemy archer is dead or archer has no one in range, allow the archer to move forward
                if enemy_soldier.health <= 0 or archer_range1 > ARCHER_RANGE:
                    archer.unleash = True
                    archer.shoot = False

            # archer attacking enemy archers
            for enemy_archer in enemy_archers:
                archer_range2 = abs(enemy_archer.rect.x - archer.rect.x)
                if archer_range2 <= ARCHER_RANGE:
                    archer.unleash = False
                    archer.shoot = True
                    # Check if index is 1 (able to shoot)
                    if archer.index >= 1:
                        # Create a new arrow
                        archer_arrows.add(Archer_Arrow(a_arrow1, archer.rect.x, player))
                        # Set shoot cooldown
                        archer_shoot_cooldown = ARCHER_REST
                    break
                # If enemy archer is dead or archer has no one in range, allow the archer to move forward
                if enemy_archer.health <= 0 or archer_range2 > ARCHER_RANGE:
                    archer.unleash = True
                    archer.shoot = False

            # Check if archer can shoot at walls
            archer_range3 = abs(enemy_walls.rect.x + 40 - archer.rect.x)
            if archer_range3 <= ARCHER_RANGE and not archer.shoot:
                archer.shoot = True
                archer.unleash = False
                # Check if index is 2 (able to shoot)
                if archer.index >= 1:
                    # Create a new arrow
                    archer_arrows.add(Archer_Arrow(a_arrow1, archer.rect.x, player))
                    # Set shoot cooldown
                    archer_shoot_cooldown = ARCHER_REST
                # Set shoot cooldown
                archer_shoot_cooldown = ARCHER_REST
                break  # Exit the loop if shooting is done

    # Decrease archer shoot cooldown
    if archer_shoot_cooldown > 0:
        archer_shoot_cooldown -= 1

    # Handle collisions of archer arrows with enemies
    for arrow in archer_arrows:
        enemy_swordsman_collision = pygame.sprite.spritecollideany(arrow, enemy_swordsmen)
        if enemy_swordsman_collision:
            enemy_swordsman_collision.health -= ARCHER_HIT
            arrow.kill()
        enemy_wall_collision = pygame.sprite.collide_rect(arrow, enemy_walls)
        if enemy_wall_collision:
            # Decrease wall health if hit by an arrow
            if player == 1:
                data['p2_wallhealth'] -= ARCHER_HIT
                arrow.kill()
            else:
                data['p1_wallhealth'] -= ARCHER_HIT
                arrow.kill()
        enemy_archer_collision = pygame.sprite.spritecollideany(arrow, enemy_archers)
        if enemy_archer_collision:
            enemy_archer_collision.health -= ARCHER_HIT
            arrow.kill()


# tower shooting
# Initialize the tower shoot cooldown
tower_shoot_cooldown = 0


def tower_shooting(arrow, tower_x_position, tower_arrows, enemy_swordsmen, enemy_archers, player):
    global tower_shoot_cooldown
    # Check if tower can shoot
    if tower_shoot_cooldown <= 0:
        # Find the nearest enemy to the tower
        nearest_enemy = None
        min_distance = float('inf')
        # Check for nearest enemy archer
        for enemy_archer in enemy_archers:
            tower_range1 = abs(tower_x_position - enemy_archer.rect.x)
            if tower_range1 <= TOWER_RANGE and tower_range1 < min_distance:
                nearest_enemy = enemy_archer
                min_distance = tower_range1
        # Check for nearest enemy swordsman
        for enemy_swordsman in enemy_swordsmen:
            tower_range2 = abs(tower_x_position - enemy_swordsman.rect.x)
            if tower_range2 <= TOWER_RANGE and tower_range2 < min_distance:
                nearest_enemy = enemy_swordsman
                min_distance = tower_range2

        # If there is a nearest enemy, shoot at it
        if nearest_enemy:
            dx = abs(nearest_enemy.rect.x - tower_x_position)
            dy = abs(nearest_enemy.rect.y - (SCREEN_HEIGHT - TOWER_HEIGHT))
            distance = max(abs(dx), abs(dy))
            arrow_speed_x = (dx / distance) * ARROW_SPEED
            arrow_speed_y = (dy / distance) * ARROW_SPEED

            # Create a new arrow aimed at the nearest enemy
            new_arrow = Tower_Arrow(arrow, tower_x_position, SCREEN_HEIGHT - TOWER_HEIGHT, arrow_speed_x, arrow_speed_y,
                                    player)
            tower_arrows.add(new_arrow)
            tower_shoot_cooldown = TOWER_REST

    # Reduce tower cooldown
    if tower_shoot_cooldown > 0:
        tower_shoot_cooldown -= 1

    # Check for collisions between tower arrows and enemy units
    for tower_arrow in tower_arrows:
        # Handle collisions with enemy archers
        enemy_archer_collision = pygame.sprite.spritecollideany(tower_arrow, enemy_archers)
        if enemy_archer_collision:
            enemy_archer_collision.health -= TOWER_HIT
            tower_arrow.kill()
            # Check if arrow has hit the ground and kill it
            if tower_arrow.rect.y <= SCREEN_HEIGHT - GROUND_HEIGHT:
                tower_arrow.kill()

        # Handle collisions with enemy swordsmen
        enemy_swordsmen_collision = pygame.sprite.spritecollideany(tower_arrow, enemy_swordsmen)
        if enemy_swordsmen_collision:
            enemy_swordsmen_collision.health -= TOWER_HIT
            tower_arrow.kill()
            # Check if arrow has hit the ground and kill it
            if tower_arrow.rect.y <= SCREEN_HEIGHT - GROUND_HEIGHT:
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
                if event.key == pygame.K_w and data['p1_resources'] >= SWORD_COST and len(red_swordsmen_army) < 50:
                    red_swordsman = Swordsman(swordsman1_ready, swordsman1_run, swordsman1_attack, swordsmasn1_dead,
                                              r(55, 157), 1)
                    red_swordsmen_army.add(red_swordsman)
                    data['p1_resources'] -= SWORD_COST
                if event.key == pygame.K_e and data['p1_resources'] >= ARCHER_COST and len(red_archers_army) < 50:
                    red_archer = Archer(archer1_ready, archer1_run, archer1_shoot, archer1_dead, r(65, 167), 1)
                    red_archers_army.add(red_archer)
                    data['p1_resources'] -= ARCHER_COST
                if event.key == pygame.K_q and data['p1_resources'] >= WORKER_COST:
                    red_worker = Worker(worker1_ready, worker1_run_left, worker1_run_right, worker1_dig, worker1_repair,
                                        r(75, 130))
                    red_workers_army.add(red_worker)
                    data['p1_resources'] -= WORKER_COST
                # Unleash P1 Units separately
                if event.key == pygame.K_d:
                    for swordsman in red_swordsmen_army:
                        if swordsman.rect.x < WALL_POS:
                            swordsman.unleash = True
                            break
                if event.key == pygame.K_f:
                    for archer in red_archers_army:
                        if archer.rect.x < WALL_POS:
                            archer.unleash = True
                            break
                # Unleash P1 Units together
                if event.key == pygame.K_z:
                    for swordsman in red_swordsmen_army:
                        if swordsman.rect.x < WALL_POS:
                            swordsman.unleash = True
                    for archer in red_archers_army:
                        if archer.rect.x < WALL_POS:
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
                if event.key == pygame.K_o and data['p2_resources'] >= SWORD_COST and len(blue_swordsmen_army) < 50:
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
                if event.key == pygame.K_i and data['p2_resources'] >= ARCHER_COST and len(blue_archers_army) < 50:
                    blue_archer = Archer(archer2_ready, archer2_run, archer2_shoot, archer2_dead,
                                         1000 - randint(65, 167), 2)
                    blue_archers_army.add(blue_archer)
                    data['p2_resources'] -= ARCHER_COST
                # Unleash P2 Units separately
                if event.key == pygame.K_j:
                    for swordsman in blue_swordsmen_army:
                        if swordsman.rect.x > SCREEN_WIDTH - WALL_POS:
                            swordsman.unleash = True
                            break
                if event.key == pygame.K_h:
                    for archer in blue_archers_army:
                        if archer.rect.x > SCREEN_WIDTH - WALL_POS:
                            archer.unleash = True
                            break
                # Unleash P2 Units together
                if event.key == pygame.K_m:
                    for swordsman in blue_swordsmen_army:
                        if swordsman.rect.x > SCREEN_WIDTH - WALL_POS:
                            swordsman.unleash = True
                    for archer in blue_archers_army:
                        if archer.rect.x > SCREEN_WIDTH - WALL_POS:
                            archer.unleash = True
                # Worker P2 movement
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

        # stabilize max resources
        if data['p1_resources'] >= 200:
            data['p1_resources'] = 200

        if data['p2_resources'] >= 200:
            data['p2_resources'] = 200

        if data['p1_wallhealth'] <= 0 or data['p2_wallhealth'] <= 0:
            game_active = False

        # collisions for player 1
        swordsmen_collision(red_swordsmen_army, blue_swordsmen_army, blue_wall, blue_archers_army, 2)
        archer_collision(red_archers_army, blue_archers_army, blue_swordsmen_army, blue_wall, red_archer_arrows,
                         a_arrow1, 1)
        workers_collision(red_workers_army, red_mine, red_wall, 1)
        tower_shooting(t_arrow1, WALL_POS, red_tower_arrows, blue_swordsmen_army, blue_archers_army, 1)

        # collisions for player 2
        swordsmen_collision(blue_swordsmen_army, red_swordsmen_army, red_wall, red_archers_army, 1)
        archer_collision(blue_archers_army, red_archers_army, red_swordsmen_army, red_wall, blue_archer_arrows,
                         a_arrow2, 2)
        workers_collision(blue_workers_army, blue_mine, blue_wall, 2)
        tower_shooting(t_arrow2, 1000 - WALL_POS, blue_tower_arrows, red_swordsmen_army, red_archers_army, 2)

        # Background
        screen.fill("BLACK")
        screen.blit(background, (0, 0))
        screen.blit(ground, (0, 250 - GROUND_HEIGHT))
        screen.blit(ground_below, (0, 250 - GROUND_HEIGHT))
        text(data, red_swordsmen_army, blue_swordsmen_army, red_workers_army, blue_workers_army, red_archers_army,
             blue_archers_army)

        # Groups draw and update
        group_display_update()

    # restarting the game
    elif game_active == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_active = True
                    # resetting everything
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
